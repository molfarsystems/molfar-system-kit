**English** · [Українська](README.ua.md)

# Molfar System Kit

Roles for **Molfar System** — a free Android app where several AI models hold a meeting instead of one chatbot answering alone. Here you'll find ready-made role packs that go into the app as a single file, and individual roles to copy by hand.

- Website: [molfar.nova-hata.com](https://molfar.nova-hata.com)
- Google Play: [Molfar System](https://play.google.com/store/apps/details?id=com.nova_hata.molfar)
- App help: inside the app ("?" on every screen) and on the website — [FAQ](https://molfar.nova-hata.com/faq)

The app never contacts this repository on its own: you decide what to install.

---

## What a role is

A role is who the model will be in a conversation: the **prompt** (who it is and how it talks) and the **skill** (what it does and in what order), up to 25,000 characters each. Roles live in two catalogs in the app:

- **Experts** — specialists at the meeting table (seats 1–4) and in the expert chat;
- **Orchestrators** — run the meeting (seat 5): bring the answers together, look for disagreements, sum up.

The app already comes with 28 built-in roles. This repository holds the ones it doesn't have.

---

## Install a role pack (the easy way)

A pack is a `.zip` file the app adds to your catalog. You need Molfar **2.0.5** or newer.

1. Download a pack: from [`roles/packs/`](roles/packs/) (Molfar and community roles) or from [`external/`](external/) (selections from other open collections). On GitHub: open the file → **Download raw file**.
2. In Molfar: **Settings** → **Data archive** → **Install roles** → pick the file.
3. The app shows how many roles the pack holds — tap **Add**.

Nothing is deleted and nothing restarts:

- new roles appear in their categories;
- a role that is already there unchanged is skipped;
- a role with the same name but a different text opens the "Already exists" window: **Replace**, **Keep both** ("Name (2)" appears) or **Skip**.

A pack doesn't touch your API keys, chats or meetings — it holds roles only.

---

## Install a single role by hand

1. Open the role's folder, e.g. [`roles/en/devils-advocate/`](roles/en/devils-advocate/).
2. In the app: on the home screen, the **Roles** block → **Experts** (or **Orchestrators**) → **+** at the top → category, name, description → **Save**.
3. Tap the **Prompt** block → paste the text from `prompt-*.md` → save. The same with `skill-*.md` in the **Skill** block.

---

## Share your own roles

**Settings** → **Data archive** → **Create archive** → **Roles only — to share**. You get a `.zip` with your own and changed roles — send it to friends or colleagues: they install it exactly like a pack from here.

Want your role to be here? Open a **New issue** → the *Submit a role* form. No git needed: fill in the fields, submit, and the role appears here with a link to you.

---

## What's where

| Folder | What is inside |
|---|---|
| [`roles/packs/`](roles/packs/) | Ready-made `.zip` packs — installed via "Data archive" |
| [`roles/`](roles/README.md) | Individual Molfar and community roles: prompt, skill and description for each |
| [`roles/builtin-ua/`](roles/builtin-ua/README.md) | The 26 built-in roles in Ukrainian — texts and a pack |
| [`external/`](external/) | Selections from other open role collections — under their own licenses |
| [`external/agency-agents/`](external/agency-agents/) | 151 roles from The Agency (agency-agents), 12 packs by division — MIT |
| [`FORMAT.md`](FORMAT.md), [`tools/`](tools/) | The pack format and the scripts that build and check packs — make your own |

**Languages.** Roles are not mirrored: a role exists in the languages someone wrote it in. The language of a role doesn't set the language of the answer — the model answers in the language of the question.

**Models.** There are no model lists here: the app loads each provider's models itself over the API (**AI Settings** → provider card → **Models** → **Load from API**). The keys are yours; providers — Google Gemini, OpenAI, Anthropic Claude, OpenRouter, NVIDIA NIM or any OpenAI-compatible service.

---

## License

Everything in this repository **except the [`external/`](external/) folder** is **CC0 1.0**, public domain: take it, change it, publish it, use it commercially. Credit is not required, but appreciated.

The contents of `external/` are under their authors' licenses (each subfolder has its `LICENSE` and source).
