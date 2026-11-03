#!/usr/bin/env python3
"""逐条验证 sources.toml，写 verified.jsonl，并生成 ROUTER.md。

    python3 verify.py            # 全量验证 + 生成
    python3 verify.py --only hn  # 只验证指定 id（不重写 ROUTER.md）

有任何一条 fail 则退出码 1；ROUTER.md 照样生成，失败条目标 ❌，不静默删除。
只用标准库。GitHub 令牌取自 $GITHUB_TOKEN，或 `gh auth token`（不落盘、不进命令行）。
"""
from __future__ import annotations

import datetime as dt
import json
import os
import subprocess
import sys
import time
import tomllib
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent
UA = "open-data-router/0.1 (+https://github.com/; data source liveness check)"
STALE_DAYS = 540  # 非 frozen 源超过这么久没更新 → warn
CATS = ["社区信号", "人工清单", "学术", "百科知识", "书籍文化", "视频音频", "代码开发",
        "法律政府", "金融", "新闻事件", "网页语料", "消费兴趣", "生物医学", "物理AI",
        "AI交互评测", "数据平台"]
TODAY = dt.datetime.now(dt.timezone.utc)


def gh_token() -> str | None:
    if t := os.environ.get("GITHUB_TOKEN"):
        return t
    try:
        return subprocess.run(["gh", "auth", "token"], capture_output=True, text=True,
                              timeout=10).stdout.strip() or None
    except (OSError, subprocess.TimeoutExpired):
        return None


GH_TOKEN = gh_token()


def http(url: str, headers: dict | None = None, limit: int = 65536) -> tuple[int, bytes]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, **(headers or {})})
    for attempt in range(3):  # 429/5xx 退避重试；最终仍 429 由调用方记为 warn
        try:
            with urllib.request.urlopen(req, timeout=25) as r:
                return r.status, r.read(limit)
        except urllib.error.HTTPError as e:
            code, body = e.code, (e.read(limit) if e.fp else b"")
            if code != 429 and code < 500:
                return code, body
            time.sleep(3 * (attempt + 1))
    return code, body


def age_days(iso: str | None) -> int | None:
    if not iso:
        return None
    t = dt.datetime.fromisoformat(iso.replace("Z", "+00:00"))
    return (TODAY - t).days


def check_hf(s: dict) -> dict:
    fields = "&".join(f"expand[]={f}" for f in ("lastModified", "likes", "downloads", "cardData", "gated", "tags"))
    code, body = http(f"https://huggingface.co/api/datasets/{s['ref']}?{fields}", limit=4 << 20)
    if code != 200:
        return {"status": "fail", "detail": f"HF API {code}"}
    d = json.loads(body)
    lic = (d.get("cardData") or {}).get("license") or next(
        (t.split(":", 1)[1] for t in d.get("tags", []) if t.startswith("license:")), None)
    if isinstance(lic, list):
        lic = ",".join(lic)
    return {"updated": d.get("lastModified"), "license": lic, "popularity": d.get("likes"),
            "gated": bool(d.get("gated")), "detail": f"likes={d.get('likes')} dl30d={d.get('downloads')}"}


def check_gh(s: dict) -> dict:
    h = {"Accept": "application/vnd.github+json"}
    if GH_TOKEN:
        h["Authorization"] = f"Bearer {GH_TOKEN}"
    code, body = http(f"https://api.github.com/repos/{s['ref']}", h, limit=1 << 20)
    if code != 200:
        return {"status": "fail", "detail": f"GitHub API {code}"}
    d = json.loads(body)
    if d.get("full_name", "").lower() != s["ref"].lower():
        return {"status": "fail", "detail": f"重定向到 {d.get('full_name')}，请更新 ref"}
    out = {"updated": d.get("pushed_at"), "license": (d.get("license") or {}).get("spdx_id"),
           "popularity": d.get("stargazers_count"), "detail": f"stars={d.get('stargazers_count')}"}
    if d.get("archived"):
        out["status"], out["detail"] = "warn", out["detail"] + " 已归档"
    return out


def check_web(s: dict) -> dict:
    url = s["ref"]
    hdr = {"Range": "bytes=0-1023"} if url.endswith(".gz") else {}
    code, body = http(url, hdr)
    if code == 429:
        return {"status": "warn", "detail": "HTTP 429 限流（端点存在，数据未取到）"}
    if code not in (200, 206):
        return {"status": "fail", "detail": f"HTTP {code}"}
    exp = s.get("expect")
    if exp and exp.encode() not in body:
        return {"status": "fail", "detail": f"HTTP {code} 但响应不含 {exp!r}"}
    return {"detail": f"HTTP {code}" + (f" 含 {exp!r}" if exp else "")}


def verify(s: dict) -> dict:
    try:
        r = {"hf": check_hf, "gh": check_gh, "web": check_web}[s["kind"]](s)
    except Exception as e:  # 网络/解析异常一律记为 fail，带原因
        r = {"status": "fail", "detail": f"{type(e).__name__}: {e}"[:200]}
    if "status" not in r:
        a = age_days(r.get("updated"))
        if a is not None and s.get("live_days") and a > s["live_days"]:
            r["status"], r["detail"] = "warn", f"声称持续更新，但已 {a} 天未更新"
        elif a is not None and a > STALE_DAYS and not s.get("frozen"):
            r["status"], r["detail"] = "warn", f"{a} 天未更新"
        else:
            r["status"] = "ok"
    return {"id": s["id"], "checked_at": TODAY.isoformat(timespec="seconds"), **r}


def link(s: dict) -> str:
    if s["kind"] == "hf":
        return f"[{s['ref']}](https://huggingface.co/datasets/{s['ref']})"
    if s["kind"] == "gh":
        return f"[{s['ref']}](https://github.com/{s['ref']})"
    host = s["ref"].split("/")[2]
    return f"[{host}]({s['ref']})"


ICON = {"ok": "✅", "warn": "⚠️", "fail": "❌"}


def render(sources: list[dict], res: dict[str, dict]) -> str:
    n = {k: sum(1 for r in res.values() if r["status"] == k) for k in ICON}
    L = [
        "# Open Data Router",
        "",
        "按需求找优质公开数据源的路由表。每一条都有可机判的探针，由 `verify.py` 验证后生成本文件。",
        "",
        f"- 最近验证：{TODAY:%Y-%m-%d %H:%M} UTC；共 {len(sources)} 条：✅ {n['ok']} · ⚠️ {n['warn']} · ❌ {n['fail']}",
        f"- ✅ 探针通过且近期有更新（或有意冻结的快照）；⚠️ 降级：超过 {STALE_DAYS} 天未更新 / 声称实时但已停更 / 仓库已归档 / 被限流；❌ 探针失败",
        "- 这里不追求全：长尾需求先去「人工清单」与「数据平台」两类入口",
        "- 「为什么优质」写的是信号来源（谁在筛、凭什么筛），不是对内容的担保；许可列为源头自报，使用前以源头为准",
        "- 改动只改 `sources.toml`，然后跑 `python3 verify.py` 重新生成",
        "",
    ]
    by = {c: [s for s in sources if s["cat"] == c] for c in CATS}
    L += ["## 目录", ""] + [f"- [{c}](#{c.lower()})（{len(v)}）" for c, v in by.items() if v] + [""]
    for c, items in by.items():
        if not items:
            continue
        L += [f"## {c}", "", "| 源 | 什么时候来这里 | 为什么优质 | 状态 | 最近更新 | 许可 |",
              "|---|---|---|---|---|---|"]
        for s in items:
            r = res.get(s["id"], {"status": "fail", "detail": "未验证"})
            upd = (r.get("updated") or "")[:10] or "—"
            tag = " 🔒" if r.get("gated") else ""
            tag += " 🧊" if s.get("frozen") else ""
            st = ICON[r["status"]] + ("" if r["status"] == "ok" else f" {r.get('detail', '')}")
            L.append(f"| {link(s)}{tag} | {s['use']} | {s['why']} | {st} | {upd} | {r.get('license') or '—'} |")
        L.append("")
    L += ["🔒 需申请访问　🧊 有意冻结的快照（不按久未更新降级）", "",
          "## 许可", "", "本文档与 `sources.toml` 以 CC0-1.0 发布；`verify.py` 以 MIT 发布。各数据源遵循其自身许可。", ""]
    return "\n".join(L)


def main() -> int:
    sources = tomllib.loads((ROOT / "sources.toml").read_text())["source"]
    ids = [s["id"] for s in sources]
    assert len(ids) == len(set(ids)), f"重复 id: {[i for i in ids if ids.count(i) > 1]}"
    bad = [s["id"] for s in sources if s["cat"] not in CATS or s["kind"] not in ("hf", "gh", "web")]
    assert not bad, f"cat/kind 非法: {bad}"
    only = sys.argv[sys.argv.index("--only") + 1:] if "--only" in sys.argv else None
    todo = [s for s in sources if not only or s["id"] in only]
    with ThreadPoolExecutor(8) as ex:
        results = list(ex.map(verify, todo))
    for r in results:
        print(f"{ICON[r['status']]} {r['id']:<26} {r.get('detail', '')}")
    if only:
        return int(any(r["status"] == "fail" for r in results))
    with open(ROOT / "verified.jsonl", "w") as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    (ROOT / "ROUTER.md").write_text(render(sources, {r["id"]: r for r in results}))
    fails = [r["id"] for r in results if r["status"] == "fail"]
    print(f"\n{len(results)} checked, fail={fails}")
    return int(bool(fails))


if __name__ == "__main__":
    sys.exit(main())
