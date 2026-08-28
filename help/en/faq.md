# FAQ

---

## What is Molfar System?

An Android app that replaces the single chatbot with a **meeting**. Up to four AI participants from different providers answer the same question independently, each in its own role.

The **Orchestrator** runs the round, compares the answers and produces one summary. The **Secretary** handles project documents and writes the protocol when asked.

For quick questions there is **Haiduk** — a single chat that can wear any role.

---

## What does it cost?

The app is free. The provider keys are free too. Models marked `$` on OpenRouter are paid and draw from your OpenRouter balance — just do not pick those, and the running cost stays at zero.

There is no subscription, no premium tier, no ads.

---

## Why several models instead of one good one?

Because a single answer gives you no way to judge itself. A model that is confidently wrong looks exactly like a model that is right.

When four models answer separately, the places where they agree are probably solid, and the places where they diverge are the places worth checking. Disagreement is the signal.

This only works if the models are actually different. Four seats on the same model produce four versions of one opinion.

---

## What is a role?

A role is the AI's personality: a **prompt** (who I am) plus a **skill** (how I work).

The app ships with **23 built-in roles** — 17 specialists for participant seats and 6 leaders for the Orchestrator seat.

You can create your own in the **Roles** section, and it will appear in the lists next to the built-in ones. One role works both in meetings and in Haiduk.

---

## Prompt and skill — what is the difference?

The **prompt** is the system instruction defining who the role is: profession, character, answer style. *"You are an experienced lawyer, you answer formally and cite articles of law."*

The **skill** is the concrete rules and steps: checklists, templates, order of work, output format. If the prompt says who I am, the skill says how exactly I work.

The prompt limit is 5000 characters. Write it in the language you want the answers in.

**Orchestrator skills are special.** The round mechanics are built into the app, and an Orchestrator's skill stacks on top of them. So write only the leading style and the evaluation criteria there — repeating the mechanics just wastes context.

---

## Where do I get ready-made prompts and skills?

From this repository — see [`roles/`](../../roles/) — and from the website, [molfar.nova-hata.com](https://molfar.nova-hata.com).

To apply one: save the `.txt` or `.md` file to your phone, open the role, open the prompt or skill editor, tap the folder icon, pick the file. Or just copy and paste. The filename does not matter; the app stores it as `prompt.md` / `skill.md` internally.

---

## How do documents work?

Add documents to a project, then hand them to specific participants using the badge counter at the top of each tab.

Only the participants you gave them to will see them. This is deliberate: you can give the same question to one participant who has read the contract and one who has not, and compare.

---

## Who is the Secretary?

Seat six. It manages the project's documents and, on request, composes a **protocol** — the roster of participants, the chronology of the meeting and the conclusions — and saves it as a file.

---

## What is Haiduk?

A single chat with one model and no meeting structure. Use it for quick questions, and for testing a new role before putting it into a meeting.

---

## What does the globe icon do?

Enables web search. The model receives fresh results and cites its sources with title and address.

It is not available everywhere — not every provider and model supports it, and the icon stays inactive when they do not. On OpenRouter, web search is **paid**; the app warns you before turning it on.

With search off, the model answers from its own knowledge and will not claim to have searched.

---

## Where is my data?

All of it on your device: projects, chat histories, roles, documents and API keys live in the app's folder. Nothing goes to a Molfar server, because there is no Molfar server. Your keys travel only to the AI providers, at the moment a request is made.

The trade-off: **uninstalling the app deletes everything.** What survives are exported chats and protocols, saved in `Download/Molfar…`, which live outside the app.

Export the meetings that matter to you.

---

## What happens when I delete a project?

Its chats, its documents and its settings go with it. Exports already saved to `Download/` are not affected.

---

## Is it open source?

The app itself is not published as source. This kit — roles, help, model notes — is public domain under CC0.

---

## What Android version do I need?

Android 7.0 or newer.
