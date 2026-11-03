**English** · [Українська](README.ua.md)

# Agency Campaign Launch: a multi-model planning meeting in Molfar

> **Exercise type:** multi-agent planning meeting on a real task
> **Date:** November 3, 2026
> **Agents:** 4 roles from [The Agency](https://github.com/msitarzewski/agency-agents) (scenario "Marketing Campaign Launch") + Molfar's own orchestrator and secretary
> **Models:** 6 different models from 5 companies, one per seat
> **Rounds:** round 1, two rounds of follow-up questions, a consolidated plan, the minutes
> **Tokens and cost:** about 0.9 million input and 0.08 million output tokens in the exported requests; about $1.5 in total
> **Device:** one Android phone
> **Video:** _link will be added_
> **Purpose:** show The Agency's roles working as one team in Molfar System, on different models, with an orchestrator that joins and checks their answers

Nothing here was edited after the meeting. The exports in [`meeting/`](meeting/) are exactly what the app saved, including the typo in the meeting title ("Campaing").

---

## Contents

1. [Why this exercise](#1-why-this-exercise)
2. [The task](#2-the-task)
3. [The team](#3-the-team)
4. [How the meeting ran](#4-how-the-meeting-ran)
5. [What each specialist delivered](#5-what-each-specialist-delivered)
6. [The result: one 4-week plan](#6-the-result-one-4-week-plan)
7. [What the orchestrator caught](#7-what-the-orchestrator-caught)
8. [What it found on our own website](#8-what-it-found-on-our-own-website)
9. [What did not go perfectly](#9-what-did-not-go-perfectly)
10. [How to repeat it](#10-how-to-repeat-it)
11. [Files](#11-files)
12. [Credits](#12-credits)

---

## 1. Why this exercise

The Agency's README lists real-world scenarios — teams of agents for a shared goal — and its [`examples/`](https://github.com/msitarzewski/agency-agents/tree/main/examples) folder shows one of them run in full. We wanted to see what happens when the same kind of team sits at a **meeting**: every agent on a **different model**, answering at the same time, with an orchestrator that merges the answers, asks follow-up questions and refuses claims the facts do not support.

Molfar System is a free Android app built for exactly this. It is made by a solo developer from Ukraine, working with Claude. The app is new and almost unknown: no ads, no accounts, no servers of its own; users bring their own API keys.

## 2. The task

A real one, not an exercise: **plan a 4-week launch campaign for Molfar System Kit** — this repository — with **zero budget**, about **4 hours a week** of one person's time, **on a phone**, and possible gaps of **1–2 weeks** without warning.

Every model got the same three documents and its own task file — see [`documents/`](documents/):

- [`01_mission_brief.md`](documents/01_mission_brief.md) — the goal, the constraints, who is behind the project;
- [`02_facts.md`](documents/02_facts.md) — the only allowed facts about Molfar and the Kit;
- [`03_channels.md`](documents/03_channels.md) — which channels exist and which do not (including a Reddit account that was shadowbanned earlier);
- `task_1…4_*.md` — one personal task per seat;
- [`round1_all.md`](documents/round1_all.md) — the opening message to everyone.

Web search was on for the four specialists, with one rule: every outside fact comes with a source link, and anything unconfirmed is marked "[unverified]".

## 3. The team

| Seat | Role | Source | Model | Web |
|---|---|---|---|---|
| 1 | Content Creator | The Agency, marketing | OpenAI GPT-6.1 Terra Pro | on |
| 2 | Twitter Engager | The Agency, marketing | DeepSeek V4.1 Flash | on |
| 3 | Reddit Community Builder | The Agency, marketing | Anthropic Claude Haiku 5.5 | on |
| 4 | Analytics Reporter | The Agency, support | SpaceXAI Grok 4.7 | on |
| 5 | Campaign Project Manager (orchestrator) | Molfar, built on its "Project Manager" role | Anthropic Claude Sonnet 5.5 | on, not used |
| 6 | Secretary | Molfar, built in | Google Gemini 2.5 Flash | off |

Seats 1–5 ran through OpenRouter, the secretary through Google directly. The scenario has a fifth agent, Instagram Curator; we left it out — Molfar seats four specialists, and the campaign has no visual channel.

The four Agency roles are used **unchanged**, as converted in [`external/agency-agents/`](../../external/agency-agents/) (each agent split into a prompt and a skill). The orchestrator is ours: Molfar's built-in "Project Manager" with three additions for a campaign — a capacity check against the owner's hours, a plan that survives a lost week, and a measure for every step. Its full text: [`pack/campaign-orchestrator.md`](pack/campaign-orchestrator.md).

## 4. How the meeting ran

1. **Round 1.** One message to everyone; the four specialists answered at the same time, each inside its own zone.
2. **Summary 1.** The orchestrator merged the answers into a week-by-week plan, listed the forks for the owner and built a queue of four follow-up questions — one per specialist.
3. **Two rounds of follow-up questions.** Each time the specialists answered their question and the orchestrator updated the plan.
4. **Consolidated plan.** On the owner's request, the orchestrator joined all three summaries into one document — [`consolidated_4-week_plan.md`](meeting/consolidated_4-week_plan.md).
5. **Minutes.** The secretary wrote the minutes in Ukrainian (the app's interface language) and, on request, in English — [`protokol_en.md`](meeting/protokol_en.md).

Tokens per seat, from the counters under each answer (input / output, all requests of that seat):

| Seat | Requests | Input | Output |
|---|---|---|---|
| Content Creator | 3 | 245,135 | 5,554 |
| Twitter Engager | 3 | 44,211 | 11,453 |
| Reddit Community Builder | 3 | 209,423 | 16,515 |
| Analytics Reporter | 3 | 310,303 | 19,958 |
| Orchestrator (3 summaries) | 3 | 73,476 | 17,005 |
| Secretary (minutes, twice) | 2 | 13,242 | 6,982 |

Web search is what makes the input large: the Analytics Reporter's first answer alone used about 240,000 input tokens. The consolidation request is not in these counters.

## 5. What each specialist delivered

- **Content Creator** — a one-sentence and a one-paragraph description of the Kit, three headlines with their audiences, a ready announcement, a five-question FAQ, a 4-week content calendar with minutes per piece, and a review of our website and the Kit's README as a newcomer would see them. Raw: [`…_Content-Creator.txt`](meeting/0002_Molfar_Launch_Campaing_Content-Creator.txt)
- **Twitter Engager** — a bio line, a 7-post launch thread ready to copy, a one-post-a-week rhythm where a missed week is dropped rather than caught up, and a warning that a search for "Molfar" returns an unrelated company. It found no usable sources on current X mechanics and marked everything it said about them "[unverified]". Raw: [`…_Twitter-Engager.txt`](meeting/0002_Molfar_Launch_Campaing_Twitter-Engager.txt)
- **Reddit Community Builder** — a straight answer: Reddit is not for these four weeks. It explained why a new account can look like ban evasion, how to check the old one and file one appeal, which communities might fit later, and the red lines. It then checked its own draft post against the facts and cut what they did not support. Raw: [`…_Reddit-Community-Builder.txt`](meeting/0002_Molfar_Launch_Campaing_Reddit-Community-Builder.txt)
- **Analytics Reporter** — the most practical part: GitHub keeps traffic for **14 days only**, so a snapshot after launch is the only safeguard; a day-1 baseline, six weekly metrics, a 15-minute weekly note, honest "worked / unclear / did not work" bands, and what cannot be measured (pack installs; raw-file downloads). Sources linked to GitHub, Google and Discord documentation. Raw: [`…_Analytics-Reporter.txt`](meeting/0002_Molfar_Launch_Campaing_Analytics-Reporter.txt)

## 6. The result: one 4-week plan

[`consolidated_4-week_plan.md`](meeting/consolidated_4-week_plan.md) — 16 steps in one table. Every step has an action, a specialist who owns it, the time it takes, a done test and a measure. Around it:

- the shared base — one message, one disclosure line, one campaign tag;
- a capacity check: week 1 is about 3.2 hours of the 4, weeks 2–4 about 1.3–1.8 hours;
- what to do if a week is lost, and why a 15-day gap erases GitHub traffic for good;
- what was cut — Reddit (on the specialists' own advice), Facebook and Hacker News (nobody proposed a step);
- open risks, and nine decisions left to the owner.

## 7. What the orchestrator caught

The orchestrator did not just join the answers. In its own words, it did no web search and says where a claim rests on one participant only. Among other things it:

- **refused claims the facts do not support** — from the Reddit draft ("we spent a few weeks", "harder to write than the roles") and from the X thread ("I built it solo, from a phone", which contradicted the brief's "we");
- **named gaps nobody owned** — "Nobody addressed who answers GitHub Discussions while the owner is offline", website fixes that no one estimated;
- **caught a conflict** — the Reddit specialist's 4–6-hour reply window against the brief's "no daily presence", which settled Reddit as "out";
- **kept its own numbers honest** — "This is my sum of their estimates, not a measured figure."

## 8. What it found on our own website

The Content Creator read the site as a newcomer. We checked each point:

| Finding | Check |
|---|---|
| The home page says a role holds up to 10,000 characters; the facts say 25,000 | **Correct** — outdated text since the limit was raised |
| No visible link to the Kit on the home page | **Correct** |
| "Screenshots coming soon" | **Misleading, but useful**: the gallery exists, but it is drawn by JavaScript, so a reader without JavaScript — a search engine, an AI search tool — sees only that placeholder |

Fixes are on our list. A planning meeting that finds real problems in its own project is the best test we could ask for.

## 9. What did not go perfectly

- **The campaign itself has not been run yet.** This is the planning meeting, not its results. We will add what happened after four weeks.
- **Web search did not help everyone.** The Twitter Engager found nothing usable about X and said so; the Reddit Community Builder could not open Reddit's own rule pages and relied on third-party guides, marked as such.
- **Search is expensive in tokens** — most of the 0.9 million input tokens came from search results.
- **The meeting does not end by itself.** After each summary the orchestrator offers a new queue of questions; the user decides when to stop. The plan stayed spread over three summaries until we asked for one consolidated document.
- **The minutes button writes in the interface language only** (Ukrainian here); the English minutes came from a direct request to the secretary. Choosing the language is planned for the next version of the app.
- **A typo in the meeting title** ("Campaing", with a stray quote) is in every file name. We left it as the app saved it.
- **The models were a mix**, from budget (DeepSeek V4.1 Flash, Claude Haiku 5.5) to strong (GPT-6.1 Terra Pro, Claude Sonnet 5.5, Grok 4.7). Stronger models at every seat would likely give a deeper result.

## 10. How to repeat it

You need Molfar System 2.0.5 or newer ([Google Play](https://play.google.com/store/apps/details?id=com.nova_hata.molfar)) and API keys of your own.

1. Install the roles — Settings → Data archive → **Install roles**:
   - [`external/agency-agents/packs/agency-marketing.zip`](../../external/agency-agents/packs/agency-marketing.zip) — Content Creator, Twitter Engager, Reddit Community Builder;
   - [`external/agency-agents/packs/agency-support.zip`](../../external/agency-agents/packs/agency-support.zip) — Analytics Reporter;
   - [`pack/molfar-campaign-orchestrator.zip`](pack/molfar-campaign-orchestrator.zip) — Campaign Project Manager.
2. Create a meeting and seat the roles: 1–4 the specialists, 5 the orchestrator, 6 the secretary. Seats 1–5 need five different models.
3. Add the documents from [`documents/`](documents/) to the meeting and **attach them to the seats**: each specialist gets `01`–`03` and its own task file, the orchestrator gets `01`–`03`. A seat sees only the documents attached to it.
4. Send [`round1_all.md`](documents/round1_all.md) to everyone, then run the queue of follow-up questions as long as it is useful.
5. Ask the orchestrator for one consolidated plan, and the secretary for the minutes.

For your own project, rewrite the three shared documents and keep the task files' structure.

## 11. Files

| Folder | What is inside |
|---|---|
| [`meeting/`](meeting/) | Exports from the app, unedited: each specialist's tab, the orchestrator's tab, the secretary's tab, the minutes (Ukrainian and English) and the consolidated plan |
| [`documents/`](documents/) | What the models received: the brief, the facts, the channels, four task files, the opening message |
| [`pack/`](pack/) | The orchestrator role as a pack, and its text |
| [`media/`](media/) | Screenshots from the phone |

## 12. Credits

- Roles at seats 1–4: [The Agency](https://github.com/msitarzewski/agency-agents) — MIT License, © AgentLand Contributors. Used unchanged, as converted in [`external/agency-agents/`](../../external/agency-agents/). Molfar System is not affiliated with The Agency.
- Everything in this folder is CC0 (public domain), like the rest of this repository outside `external/`. The model answers in `meeting/` are published as they were produced.
- Molfar System — https://molfar.nova-hata.com · not affiliated with any other company named Molfar.
