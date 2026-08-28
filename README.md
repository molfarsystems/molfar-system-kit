**English** · [Українська](README.ua.md)

# Molfar System Kit

Roles, model lists and help files for **Molfar System** — a free Android app where several AI models hold a meeting instead of one chatbot answering alone.

Everything here is plain text. Copy what you need, paste it into the app, change it however you like.

- App website: [molfar.nova-hata.com](https://molfar.nova-hata.com)
- Google Play: `com.nova_hata.molfar`

---

## What is in this repository

| Folder | What is inside |
|---|---|
| [`help/`](help/) | Guides: getting started, API keys, FAQ, troubleshooting |
| [`roles/`](roles/) | Ready-made roles — prompt + skill for each |
| [`models/`](models/) | Which model to put in which seat, and where to get keys |

The app itself never connects to this repository. Nothing here is downloaded automatically — you copy what you want by hand.

---

## Quick start

New to the app? Read [help/en/quick-start.md](help/en/quick-start.md) first. It takes about five minutes and covers the whole setup.

No API key yet? [help/en/api-keys.md](help/en/api-keys.md) shows where to get free ones from all three supported providers.

Something not working? [help/en/troubleshooting.md](help/en/troubleshooting.md).

---

## How to use a role from this repository

1. Open the role folder, for example [`roles/en/devils-advocate/`](roles/en/devils-advocate/)
2. Open `prompt-*.md`, tap the copy button on the code block
3. In the app: **Roles** → create a new role → paste into the **Prompt** field
4. Do the same with `skill-*.md` into the **Skill** field
5. Save. The role now appears in the lists next to the built-in ones

You can also save the `.md` file to your phone and load it through the folder icon in the prompt editor — the app accepts `.txt` and `.md`.

The app already ships with 23 built-in roles, so this repository only holds roles that are **not** in the app.

---

## Contributing a role

Have a role that works well? Open a **New issue** and pick the *Submit a role* form. Fill in the fields, send it, and it will be added here with your name in the credit line.

You do not need to know git. The form is just a form.

---

## Language policy

- `help/` — translated strictly, the same files in every language
- `roles/` — **not** mirrored. A role exists in whatever languages someone wrote it in
- `models/` — English only, since it is mostly model names and numbers

---

## License

Everything in this repository is released under **CC0 1.0** — public domain. Take it, change it, publish it, use it commercially. No attribution required, though it is always welcome.
