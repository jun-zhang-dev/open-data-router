# open-data-router

**要找某类优质公开数据 → 看 [ROUTER.md](ROUTER.md)。**

这是一份路由表，不是数据目录：不镜像任何数据，每条只回答三件事——什么时候来这里、为什么算优质（信号从哪来）、现在还活着吗。

起点：Karpathy 的 [HackerTube](https://karpathy.bearblog.dev/hacker-tube/) 用 HF 上的 HN 全量评论筛出 6,454 个被反复推荐的视频。"社区存档 + LLM 过滤"这个配方可以换源复用，这里收的就是可复用的源。

## 为什么不做全量目录

全量目录已有人做得更好（[awesome-public-datasets](https://github.com/awesomedata/awesome-public-datasets)、HF Hub 搜索、Google Dataset Search），自己再做一份，主要成本是维护，且会静默腐烂。这里只补它们缺的两样：

1. **按需求路由**：一句"什么时候来这里"，而不是按数据类型罗列
2. **可重放的验证**：每条都有机器可判定的探针；"号称实时"的源超过阈值没更新会被标出来

长尾需求走 ROUTER.md 里的「人工清单」「数据平台」两类入口。

## 用法

```bash
python3 verify.py            # 验证全部 → 写 verified.jsonl + 重新生成 ROUTER.md；有 ❌ 时退出码 1
python3 verify.py --only hn  # 只验证某几条（不重写 ROUTER.md）
```

GitHub Actions 每周一自动重跑并提交刷新后的 ROUTER.md；有 ❌ 时该次运行标红。

只依赖 Python 3.11+ 标准库。GitHub 探针读 `$GITHUB_TOKEN`，没有则尝试 `gh auth token`，都没有就走匿名额度（60 次/小时，够用）。

## 加一条源

只改 `sources.toml`（字段说明在文件头），然后跑 `verify.py`。收录标准：

- 有一手来源或明确的筛选信号（投票、引用、人工策展、官方发布），不收二手合成/蒸馏集
- 探针必须是能返回数据的端点，web 类配 `expect` 子串，防止 200 的错误页蒙混过关
- 源头声称持续更新的填 `live_days`，有意冻结的快照填 `frozen = true`

## 文件

| 文件 | 作用 |
|---|---|
| `sources.toml` | 唯一真相：源清单 + 路由句 + 探针 |
| `verify.py` | 探针 + 生成器 |
| `verified.jsonl` | 最近一次验证的逐条证据（时间、更新日期、许可、热度） |
| `ROUTER.md` | 生成物，勿手改 |

## 许可

`sources.toml`、`ROUTER.md`、`verified.jsonl`、本 README：[CC0-1.0](LICENSE-CC0)。`verify.py`：[MIT](LICENSE-MIT)。各数据源遵循其自身许可，表中许可列为源头自报。
