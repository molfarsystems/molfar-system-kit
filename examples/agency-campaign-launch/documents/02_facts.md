# Facts — Molfar System and Molfar System Kit (November 2026)

Use ONLY these facts. If something is not here or in the brief, do not write it — ask.

## Molfar System (the app)
- Name: **Molfar System** (short: Molfar). Developer: Nova Hata. Free, no ads, no in-app purchases, no accounts.
- Android only (Android 7.0 and newer). No iOS, no web version.
- Current version: **2.0.5** (Google Play, November 2026). Version 2.0 is a full rewrite in Kotlin of an earlier Python app.
- Interface and help in 5 languages: English, Ukrainian, German, French, Spanish.
- Google Play: https://play.google.com/store/apps/details?id=com.nova_hata.molfar
- Website and FAQ: https://molfar.nova-hata.com (FAQ: /faq, earlier demo meeting: /narada)
- Not affiliated with molfar.io or any other company named Molfar.
- Bring your own key: Google Gemini, OpenAI, Anthropic Claude, OpenRouter, NVIDIA NIM, or one OpenAI-compatible service. Keys are encrypted on the phone and sent only to their provider. No server of our own; requests go from the phone straight to the provider.
- **Gaiduk** — the built-in assistant: knows the app, talks about any topic, web search on models that support it, files in the chat.
- **Expert chat** — a chat with a model in a role.
- **Meetings** — up to 4 expert participants + an Orchestrator + a Secretary. Each seat has its own role and its own model, so one meeting is several different models. Round 1: all answer at the same time; the Orchestrator sums up and builds a queue of follow-up questions; the Secretary answers questions about the documents and writes the minutes. Shared document pool up to 50 MB.
- **Roles**: a prompt (who the model is and how it talks) and a skill (what it does and in what order), up to 25,000 characters each. 28 built-in roles; two catalogs: Experts and Orchestrators.
- Since 2.0.5: **Install roles** (Settings → Data archive) — accepts only a role pack (roles and nothing else); new roles are added, identical ones skipped, a changed one asks Replace / Keep both / Skip. Nothing is deleted.
- Also: chat access to a chosen storage folder (the model proposes file changes, the user confirms), text/Markdown editor with Mermaid, "Document" (PDF/DOCX/XLSX → one PDF and Markdown), image viewer, private file storage, AI usage statistics, data archive.
- Privacy: no own server, no accounts, no ads, no trackers or analytics in the app.

## Molfar System Kit (the repository)
- https://github.com/molfarsystems/molfar-system-kit — public, for users. License: **CC0** (public domain) for everything except `external/`.
- `roles/packs/` — role packs: English (4 roles), Ukrainian (6), German (1), French (1), Spanish (1), and `molfar-builtin-ua` — the 26 built-in roles in Ukrainian.
- `external/agency-agents/` — **151 roles from The Agency** (https://github.com/msitarzewski/agency-agents), MIT license, © AgentLand Contributors, **12 packs**: academic 6, design 10, finance 5, GIS 13, marketing 34, paid media 7, product 5, project management 6, research 1, sales 9, specialized 50, support 5. Each role keeps an attribution line; agents that drive tools (code, files, packages) were left out.
- Install: download a `.zip` → Molfar → Settings → Data archive → **Install roles** → Add. Needs Molfar 2.0.5 or newer.
- Contribute: **New issue → "Submit a role"** form; a bot turns it into a pull request. No git needed.
- `FORMAT.md` — the open pack format with a compatibility promise; `tools/` — Python scripts (standard library, CC0) to build and check packs.
- GitHub Discussions are open for questions and ideas.
- The Kit is new: very few people know about it yet.

## About this meeting
- The roles at seats 1–4 come from The Agency, unchanged except for the split into prompt and skill. The orchestrator and the secretary are Molfar's own.

## Do not
- Invent features, numbers, users, reviews or plans.
- Write personal details about the developer.
- Use hype words.
