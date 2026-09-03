# Choosing models for seats

A meeting has six seats: four participants, an Orchestrator, and a Secretary. They need different things from a model.

---

## Seats 1-4 — participants

These answer your question independently. What you want here is **variety**, not raw quality.

A working default:

| Seat | Provider | Why |
|---|---|---|
| 1 | Google | Fast, reliable, good baseline |
| 2 | NVIDIA NIM | Different training, different blind spots |
| 3 | OpenRouter (a `:free` model) | A third opinion from a third vendor |
| 4 | Leave empty at first | Three participants is already plenty to read |

Start with two participants. Four answers plus an Orchestrator summary is a lot of text to read on a phone, and most questions do not need it.

---

## Seat 5 — Orchestrator

This one reads every answer and writes the summary. It needs the **largest context window** you can give it, because it processes everything the participants produced, plus the question, plus its own instructions.

Pick a model with a long context. A fast, small model here will truncate or lose track of the later answers.

Most of the models the app ships with have a 1M window, so this is easy — but not all of them. `GPT-OSS 20B` (131K) and `MiniMax M2.7` (197K) are the smallest, and belong in a participant seat rather than here. [`catalogue.md`](catalogue.md) lists the window for every model.

This is the seat where paying a little makes the most difference, if you ever decide to. Models with a `$` in front of their name bill against your OpenRouter balance; `$ GLM 5.3 Flash` is the cheapest of them and the sensible one to try first.

---

## Seat 6 — Secretary

Handles project documents and writes the protocol on request. Also wants a long context, since documents go through it.

Speed matters less here — you are not waiting on it during a round.

---

## Practical notes

**The same model on two providers is still one opinion.** `Laguna XS 2.1` ships twice — free through OpenRouter, direct through NVIDIA NIM. Useful when one of them is throttling, useless as two seats. [`catalogue.md`](catalogue.md) groups every default model by training family, so you can see which picks actually differ.

**Free OpenRouter models need a privacy setting.** Without it they all fail at once with a 404. One-time fix, explained in [`providers.md`](providers.md#free-models-return-404).

**Rate limits bite when seats share a provider.** Four Google models in one round is four simultaneous requests against the same per-minute quota. Spreading seats across providers avoids this entirely.

**Timeouts.** A long question plus attached documents plus a slow model equals a timeout. If a seat keeps failing, put a faster model there rather than shortening your question.

**Reasoning models are slow.** They produce better analysis but can take a minute or more. Fine for one seat, painful when all four do it — the round finishes only when the slowest participant does.

**Model names change often.** Trust the picker inside the app over any list, including this one.
