**English** · [Українська](README.ua.md)

# The Agency (agency-agents) for Molfar

Roles from [**The Agency**](https://github.com/msitarzewski/agency-agents) — an open collection of AI agent personalities — converted for Molfar System and packed by division.

- **Source:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) at commit `b37b5bb` (2026-10-24).
- **License:** MIT, © AgentLand Contributors — see [`LICENSE`](LICENSE). Each role keeps an attribution line at the end of its skill, and the full license text travels inside every pack (in its `manifest.json`). These roles are **not** CC0.
- Molfar is not affiliated with, endorsed by, or a partner of The Agency or AgentLand.
- **151 roles in 12 packs.** The full list with descriptions — [`ROLES.md`](ROLES.md).

## Install

Download a pack from [`packs/`](packs/) (**Download raw file**) → Molfar → **Settings** → **Data archive** → **Install roles** → **Add**. You need Molfar **2.0.5** or newer. The roles land in the **Experts** catalog, in categories **Agency — <division>**. Nothing is deleted; a role you already have unchanged is skipped.

| Pack | Roles | Pack | Roles |
|---|---|---|---|
| [`agency-academic`](packs/agency-academic.zip) | 6 | [`agency-paid-media`](packs/agency-paid-media.zip) | 7 |
| [`agency-design`](packs/agency-design.zip) | 10 | [`agency-product`](packs/agency-product.zip) | 5 |
| [`agency-finance`](packs/agency-finance.zip) | 5 | [`agency-project-management`](packs/agency-project-management.zip) | 6 |
| [`agency-gis`](packs/agency-gis.zip) | 13 | [`agency-research`](packs/agency-research.zip) | 1 |
| [`agency-marketing`](packs/agency-marketing.zip) | 34 | [`agency-sales`](packs/agency-sales.zip) | 9 |
| [`agency-specialized`](packs/agency-specialized.zip) | 50 | [`agency-support`](packs/agency-support.zip) | 5 |

## How they were converted

- The front matter gives the name and the description (cut to 128 characters at a word, the app's limit).
- **Prompt** — identity, mission, critical rules, communication style; **skill** — templates, workflow, frameworks, metrics. Emoji are removed from headings; the texts stay in English, as in the original.
- **Left out:** the "Learning & Memory" section (Molfar has no memory between chats); agents that drive tools (code bases, package managers, files, webhooks); the divisions engineering, game development, healthcare, security, spatial computing and testing. Everything else fits the app's 25,000-character limits whole.
- Script: [`../../tools/agency_packs.py`](../../tools/agency_packs.py). Rebuild — see [`../../tools/README.md`](../../tools/README.md).
