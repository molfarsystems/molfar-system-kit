# Tools

Python 3, standard library only. The pack format is in [`../FORMAT.md`](../FORMAT.md).

| Script | What it does |
|---|---|
| `build_pack.py <out.zip> <category> <role folder>...` | Builds a pack from role folders (README.md + prompt-*.md + skill-*.md) |
| `rebuild_packs.py` | Rebuilds `roles/packs/*.zip` (one per language + the built-in roles in Ukrainian) and their tables; touches only what changed — run by the bot after a role is merged |
| `check_pack.py <pack.zip>...` | Checks packs the way the app reads them; exit code 1 on a problem |
| `agency_convert.py <agent.md> <out dir> <category> [commit]` | One [agency-agents](https://github.com/msitarzewski/agency-agents) agent → a role folder |
| `agency_packs.py <agency-agents checkout> <out dir>` | All suitable agency-agents agents → one pack per division, `LICENSE`, `ROLES.md` |

Rebuild everything in this repository:

```bash
# Molfar roles (the bot does this on every merge into main)
python3 tools/rebuild_packs.py

# agency-agents (pin the commit you convert; it is written into every role)
git clone https://github.com/msitarzewski/agency-agents /tmp/agency-agents
python3 tools/agency_packs.py /tmp/agency-agents external/agency-agents

python3 tools/check_pack.py roles/packs/*.zip external/*/packs/*.zip
```

CC0 1.0.
