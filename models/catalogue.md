# Model catalogue

Every model the app ships with, in picker order, with the numbers that matter:
the exact ID, the context window, and what it costs.

English only, like the rest of this folder — it is mostly model IDs and numbers.

The list here is generated from [`app-defaults.md`](app-defaults.md), which is
the working file. If the two disagree, `app-defaults.md` is right.

---

## How to read this

Every entry shows the **model ID** in a code block. That is the string the app
needs. On GitHub, tap the code to copy it, then paste it into the model field
in **AI Settings**.

**Everything listed here is already in the app.** You do not have to type any of
it — these are the models in the picker before you add anything of your own.
The IDs are here for when you want to check what a seat is actually running, or
to re-enter one by hand.

**Free** means the model runs on the provider's free tier. **Paid** models show
the price as `input / output` per million tokens, and carry a `$` in front of
their name in the app so you can see at a glance what draws on your balance.

**Context** is the input window. That is what matters most for the Orchestrator,
which reads every participant's answer at once.

**Seat** is a suggestion derived from the context window alone, not from
testing: a model with a 1M window can hold a full round plus documents, so it
suits seat 5 or 6; a smaller window is fine for a participant, which only sees
your question.

**What is deliberately not here:** speed, answer quality, how well a model
writes Ukrainian. Those need testing on your own questions, and a number
invented for a table would be worse than no number. Try a model in Haiduk
first — one seat, immediate answer — and judge it there.

---

## OpenRouter

Free models carry `:free` in the ID. The other four bill against your balance.

**Free models need a privacy setting turned on** — without it every `:free`
model returns a 404 and nothing works. See
[`providers.md`](providers.md#free-models-return-404) before you start.

### Nemotron 3 Ultra 550B

```
nvidia/nemotron-3-ultra-550b-a55b:free
```

Context 1M · Free · Seat: orchestrator, secretary

The largest model in the list, with the largest window. Also available direct
from NVIDIA NIM in a smaller variant.

### Nemotron 3 Super 120B

```
nvidia/nemotron-3-super-120b-a12b:free
```

Context 262K · Free · Seat: participant

The middle Nemotron. A quarter of Ultra's window, still comfortable for a
participant seat, which only reads your question.

### Nemotron 3 Nano Omni 30B

```
nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free
```

Context 256K · Free · Seat: participant

A reasoning variant — it thinks before answering, which costs time. Keep it to
one seat: a round ends only when its slowest participant does.

### Nemotron 3.5 Lightning

```
nvidia/nemotron-3.5-lightning:free
```

Context 1M · Free · Seat: participant, orchestrator

Newer generation than the Nemotron 3 pair above. Also on NVIDIA NIM as a
30B variant, if OpenRouter is rate-limiting you.

### Laguna XS 2.1

```
poolside/laguna-xs-2.1:free
```

Context 262K · Free · Seat: participant

The same model is available direct from NVIDIA NIM. Two routes to one model:
useful when one provider is throttling, useless as two separate seats — they
would give you one opinion twice.

### MiniMax M3

```
minimax/minimax-m3:free
```

Context 1M · Free · Seat: orchestrator, secretary

A full million-token window on a free tier, which is unusual. Worth trying in
the Orchestrator seat.

### Ling 3.0 Flash Fin

```
inclusionai/ling-3.0-flash-fin:free
```

Context 262K · Free · Seat: participant

A different training lineage from everything else in this list, which is the
whole point of filling seats from more than one family.

### MiniMax M2.7

```
minimax/minimax-m2.7:free
```

Context 197K · Free · Seat: participant

The previous MiniMax generation and the smallest window on OpenRouter. Reach
for M3 above unless it is rate-limited.

### $ Qwen 3.8 Flash

```
qwen/qwen3.8-flash
```

Context 1M · $0,15 / $0,47 per 1M · Seat: orchestrator, secretary

Paid. The most expensive output in this list — about three times what the
others charge — so watch it in a seat that writes long summaries.

### $ GLM 5.3 Flash

```
z-ai/glm-5.3-flash
```

Context 1M · $0,05 / $0,17 per 1M · Seat: orchestrator, secretary

Paid, and the cheapest of the four on both input and output. The one to try
first if you want to see whether paying changes anything for you.

### $ Muse Spark 1.2

```
meta/muse-spark-1.2-contributor
```

Context 1M · $0,10 / $0,20 per 1M · Seat: orchestrator, secretary

Paid. Meta lineage, so a different set of blind spots from the Nemotron and
Gemini seats.

### $ GPT 5.6 Luna

```
openai/gpt-5.6-luna
```

Context 1M · $0,10 / $0,20 per 1M · Seat: orchestrator, secretary

Paid. OpenAI lineage — a fourth family again, and the only OpenAI model here
that is not open-weight.

---

## Google AI Studio

### Gemini 2.5 Flash

```
gemini-2.5-flash
```

Context 1M · Free tier · Seat: participant, orchestrator, secretary

The one Google model in the defaults, and the shortest path from no API key to
a working meeting. A wide window and a free tier make it usable in any seat —
which is exactly why you should not put it in all of them.

---

## NVIDIA NIM

NVIDIA's free tier runs on credits rather than a token count, so a heavy model
spends the budget faster than a small one.

### Laguna XS 2.1

```
poolside/laguna-xs-2.1
```

Context 262K · Free tier (credits) · Seat: participant

Same model as the OpenRouter entry above, served direct. No `:free` suffix
here — on NVIDIA the free tier is the account, not the model ID.

### Kimi K3

```
moonshotai/kimi-k3
```

Context 1M · Free tier (credits) · Seat: orchestrator, secretary

Moonshot lineage, trained largely on Chinese and English data — a genuinely
different angle from the Western families in this list.

### DeepSeek V4 Flash

```
deepseek-ai/deepseek-v4-flash-0731
```

Context 1M · Free tier (credits) · Seat: participant, orchestrator

The lighter of the two DeepSeek builds here. The `0731` is the snapshot date,
so this ID stays pinned to one version rather than drifting under you.

### DiffusionGemma 26B

```
google/diffusiongemma-26b-a4b-it
```

Context 262K · Free tier (credits) · Seat: participant

Google-trained but served by NVIDIA. That still buys you infrastructure
variety against a Gemini seat, though not training variety — worth knowing
before you count it as an independent opinion.

### DeepSeek V4 Pro

```
deepseek-ai/deepseek-v4-pro-0813
```

Context 1M · Free tier (credits) · Seat: orchestrator, secretary

The heavier DeepSeek. Larger models spend NVIDIA credits faster, so it earns
its place better in one summarising seat than in four participant seats.

### Nemotron 3.5 Lightning 30B

```
nvidia/nemotron-3.5-lightning-30b-a3b
```

Context 1M · Free tier (credits) · Seat: participant, orchestrator

The 30B build of the Lightning model that also appears on OpenRouter. Same
family, different provider and size.

### GPT-OSS 20B

```
openai/gpt-oss-20b
```

Context 131K · Free tier (credits) · Seat: participant

Open-weight model from OpenAI, and the smallest window in the whole list.
Fine for a participant, too small to hold a full round in seat 5.

---

## Counting the families

Twenty entries, but fewer independent opinions than that. By training lineage:

- **NVIDIA / Nemotron** — 5 entries (3 Ultra/Super/Nano, 2 Lightning builds)
- **DeepSeek** — 2
- **MiniMax** — 2
- **Google** — 2 (Gemini, DiffusionGemma)
- **OpenAI** — 2 (GPT-OSS, GPT 5.6 Luna)
- **Poolside / Laguna** — 2 entries, one model on two providers
- **Moonshot, InclusionAI, Qwen, Z-AI, Meta** — 1 each

Two seats from the same row above will agree with each other more often than
the agreement deserves. Pick from different rows.

---

## Freshness

IDs, context windows and prices here were checked against each provider's own
model list. Behaviour was not — see the note above about what is deliberately
missing.

Providers rename, deprecate and replace models constantly, and prices move.
When something here stops working, the app's own model picker is the source of
truth: it pulls the live list from the provider.
