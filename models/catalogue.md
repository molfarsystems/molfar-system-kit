# Model catalogue

Which models to put in the app, with the numbers that matter: context window,
price, and how a model behaves in a meeting.

English only, like the rest of this folder — it is mostly model IDs and numbers.

---

## How to use this

Every entry shows the **model ID** in a code block. That is the string the app
needs. On GitHub, tap the code to copy it, then paste it into the model field
in **AI Settings**.

Marks next to a name:

- **✓** — ships with the app by default, no typing needed
- **★** — we recommend it
- **?** — listed but not verified by us; check it works before relying on it

**Prices** are per million tokens, written `input / output`. Output is normally
several times more expensive than input, so one number would mislead. Free
models say `Free`.

**Context** is the input window. That is what matters for the Orchestrator,
which reads every participant's answer at once.

---

## Google AI Studio

Free tier: **10 requests/minute**, 250K tokens/minute. The daily cap is the
number that varies between sources — treat it as "a few hundred a day" and
watch for the error rather than counting.

### Gemini 2.5 Flash ✓

```
gemini-2.5-flash
```

Context 1M · Free tier · Fast · Ukrainian good
**Seat:** participant, orchestrator

The current default in the app. Solid all-rounder, wide context, quick enough
that four seats do not feel slow.

### Gemini 2.0 Flash ✓

```
gemini-2.0-flash
```

Context 1M · Free tier · Fast · Ukrainian good
**Seat:** participant

The older sibling, still in the app as a fallback. No reason to pick it over
2.5 unless 2.5 is rate-limited.

### Gemini 3 Flash ★ ?

```
gemini-3-flash-preview
```

Context 1M · $0.25 / $1.50 · Fast · Ukrainian good
**Seat:** orchestrator

Newer generation than what the app ships with. Worth testing as the
Orchestrator seat — that is where a better model pays off most.

---

## NVIDIA NIM

Free tier: **40 requests/minute**, and a credit budget rather than a token
count — roughly 1,000 credits to start. Small models cost a fraction of a
credit per call, large ones cost more.

### Nemotron 3 Ultra 550B ✓

```
nvidia/nemotron-3-ultra-550b-a55b
```

Context 1M · Free tier (credits) · Slow · Ukrainian good
**Seat:** orchestrator

Large model, large context. Being slow, it is a poor fit for a participant
seat — the round only finishes when the slowest one does.

### Gemma 4 31B ✓ ★

```
google/gemma-4-31b-it
```

Context 262K · Free tier (credits) · Medium · Ukrainian good
**Seat:** participant

Good balance for a working seat. Google-trained but served by NVIDIA, so it
still gives you infrastructure variety against a Gemini seat.

### Mistral Nemotron ✓

```
mistralai/mistral-nemotron
```

Context ? · Free tier (credits) · Medium · Ukrainian ?
**Seat:** participant

Already in the app. European training data — a genuinely different angle from
the Google and Meta families.

---

## OpenRouter

Free tier: about **20 requests/minute** and a low daily cap (tens of requests).
Buying $10 of credit once raises the daily cap substantially. Free models carry
`:free` in the ID.

### Nemotron 3 Super 120B ✓ ★

```
nvidia/nemotron-3-super-120b-a12b:free
```

Context ? · Free · Slow, reasoning · Ukrainian good
**Seat:** orchestrator

Reasoning model. Strong synthesis, but do not put it in more than one seat —
the wait adds up.

### Gemma 4 31B ✓

```
google/gemma-4-31b-it:free
```

Context 262K · Free · Medium · Ukrainian good
**Seat:** participant

Same model as the NVIDIA entry above, different provider. Useful when NVIDIA
credits run low.

### GPT-OSS 120B ✓

```
openai/gpt-oss-120b:free
```

Context ? · Free · Medium · Ukrainian ?
**Seat:** participant

Open-weight model from a fourth training lineage — good for breaking up an
echo between Google- and NVIDIA-family seats.

### Llama 3.3 70B ?

```
meta-llama/llama-3.3-70b-instruct:free
```

Context 131K · Free · Medium · Ukrainian acceptable
**Seat:** participant

Not in the app's defaults. Meta family, so a different set of blind spots
again. Smaller context than most here.

### MiniMax M3 ?

```
minimax/minimax-m3:free
```

Context 1M · Free · ? · Ukrainian ?
**Seat:** orchestrator

Listed with a full 1M window on the free tier, which is unusual. Worth a test
in the Orchestrator seat.

---

## Adding an entry

Copy this block, fill it in, drop it under the right provider:

```markdown
### <Short name>  <✓ if shipped>  <★ if recommended>  <? if unverified>

​```
<full model ID>
​```

Context <N>K · <Free | $in / $out> · <fast|medium|slow><, reasoning> · Ukrainian <good|acceptable|weak>
**Seat:** <participant | orchestrator | secretary>

<One line: a limit, a quirk, or why you would pick this over its neighbour.>
```

Keep the note to one line. Anything longer belongs in
[`recommended.md`](recommended.md), which covers strategy rather than
individual models.

---

## Freshness

Verified: **not yet** — entries marked **?** still need a pass through the app.

Providers rename, deprecate and replace models constantly, and prices move.
When something here stops working, the app's own model picker is the source of
truth: it pulls the live list from the provider.
