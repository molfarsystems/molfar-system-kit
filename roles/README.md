# Roles

Ready-made roles for Molfar System. Each one is a **prompt** (who the role is) and a **skill** (how it works).

The app already ships with 23 built-in roles. This folder holds only roles that are **not** in the app.

---

## All roles

Roles are not mirrored across languages — each exists in whatever languages someone wrote it in. A missing language is an invitation to add it.

| Role | What it does | Seat | Languages |
|---|---|---|---|
| Ментор з IT-професій | Коли людина хоче увійти в IT, але не знає, з чого почати і який напрям їй пасує. Роль підбирає професію під сильні сторони людини, складає… | Participant | [ua](ua/it-mentor/) |
| Маркетолог-стратег | Практик просування малого бізнесу з обмеженими бюджетами. | Participant | [ua](ua/marketing-strateg/) |
| Архітектор ролей | Майстер, що робить майстрів: перетворює ідею «мені б у нараду юриста з митного права» на готовий промпт і скіл у форматі Molfar. | Participant | [ua](ua/architect-roles/) |
| Devil's Advocate | Attacks a plan to find where it breaks | Participant | [en](en/devils-advocate/) · [ua](ua/advokat-dyiavola/) |

---

## How to use a role

1. Open the role folder
2. Open `prompt-*.md` and tap the copy button on the code block
3. In the app: **Roles** → new role → paste into **Prompt**
4. Same with `skill-*.md` into **Skill**
5. Save

Or save the `.md` file to your phone and load it through the folder icon in the editor. The app accepts `.txt` and `.md`.

---

## Folder rules

```
roles/<language>/<role-name>/
  README.md
  prompt-<role-name>.md
  skill-<role-name>.md
```

- Folders and files: lowercase Latin, words separated by hyphens
- The suffix in `prompt-*.md` matches the folder name exactly
- No language code in the filename — the language is already in the path
- The folder name is in the role's own language: `ua/advokat-dyiavola/`, `de/anwalt/`

---

## Participant roles vs Orchestrator roles

**Participant roles** (seats 1-4) answer the question. Write them as a specialist with a point of view.

**Orchestrator roles** (seat 5) run the round. The round mechanics are built into the app, and an Orchestrator's skill stacks on top of the fixed rules of that seat. So an Orchestrator skill should describe only the **leading style and evaluation criteria** — not how rounds work. Repeating the mechanics wastes context and can conflict with the built-in rules.

---

## Writing a good role

**Give it a real opinion.** A role that agrees with everything adds nothing to a meeting. The useful roles are the ones that push back.

**Say what it should refuse to do.** "Do not soften the assessment to be polite" does more work than three sentences describing expertise.

**Keep the prompt under 5000 characters.** If it is longer, part of it belongs in the skill.

**Test it in Haiduk first.** One model, instant feedback, no meeting to set up.

**Write it in the language you want answers in.** The models follow the prompt's language by default.

---

## Contributing

Open a **New issue** → *Submit a role*. Fill in the form, send it. No git knowledge needed.

Everything here is CC0 — public domain. By submitting, you agree to release your text the same way.
