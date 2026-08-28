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
| 3 | OpenRouter (free model) | A third opinion from a third vendor |
| 4 | Leave empty at first | Three participants is already plenty to read |

Start with two participants. Four answers plus an Orchestrator summary is a lot of text to read on a phone, and most questions do not need it.

---

## Seat 5 — Orchestrator

This one reads every answer and writes the summary. It needs the **largest context window** you can give it, because it processes everything the participants produced, plus the question, plus its own instructions.

Pick a model with a long context. A fast, small model here will truncate or lose track of the later answers.

This is the seat where paying a little makes the most difference, if you ever decide to.

---

## Seat 6 — Secretary

Handles project documents and writes the protocol on request. Also wants a long context, since documents go through it.

Speed matters less here — you are not waiting on it during a round.

---

## Practical notes

**Rate limits bite when seats share a provider.** Four Google models in one round is four simultaneous requests against the same per-minute quota. Spreading seats across providers avoids this entirely.

**Timeouts.** A long question plus attached documents plus a slow model equals a timeout. If a seat keeps failing, put a faster model there rather than shortening your question.

**Reasoning models are slow.** They produce better analysis but can take a minute or more. Fine for one seat, painful when all four do it — the round finishes only when the slowest participant does.

**Model names change often.** Trust the picker inside the app over any list, including this one.
