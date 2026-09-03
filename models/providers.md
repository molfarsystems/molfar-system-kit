# Providers

Molfar System supports three providers. All three give out free API keys. You need at least one; two or more is where the app gets interesting, because participants can then run on genuinely different infrastructure.

Keys are stored on your device only. They are sent to the provider at request time and nowhere else.

---

## Google AI Studio

**Key:** [aistudio.google.com/apikey](https://aistudio.google.com/apikey) → Create API key

The easiest to start with. Sign in with a Google account, click once, done. No card, no billing setup.

Good for: fast general answers, long documents, anything where speed matters more than depth.

Watch out for: rate limits are per minute and per day. If you run four participants at once on Google models, you can hit the per-minute limit in a single round.

---

## NVIDIA NIM

**Key:** [build.nvidia.com](https://build.nvidia.com) → sign up → *Get API Key* on any model page

Hosts open-weight models — Llama, Qwen, Mistral, DeepSeek and others — on NVIDIA's own infrastructure.

Good for: a genuinely different opinion. These models were trained by different teams than Google's, so when they agree with a Gemini answer, that agreement carries real information.

Watch out for: the key is issued from a model page, which confuses people who go looking for a settings screen. Any model page will do — the key is account-wide.

---

## OpenRouter

**Key:** [openrouter.ai/keys](https://openrouter.ai/keys) → Create Key

A gateway to hundreds of models from many vendors through one key. Twelve of the app's twenty default models come from here.

Good for: filling seats with models the other two providers do not have, and for trying something new without creating another account.

Watch out for: **not everything on OpenRouter is free.** Models marked with `$` in the app draw from your OpenRouter balance. Free models there carry `:free` in their name. Web search through OpenRouter is billed separately — the app warns you before enabling it.

### Free models return 404

A fresh OpenRouter key often fails on every `:free` model with an empty answer and this error:

```
OpenRouter HTTP 404: 0 endpoints out of 1 requested are available
matching your guardrail restrictions and data policy. We removed them
for the following reasons: Free model training violation (account
settings): 1 endpoint excluded
```

Nothing is broken and the key is fine. Before routing a request, OpenRouter drops every endpoint that does not match your data policy; if that leaves none, you get a 404. **Most free endpoints train on the prompts they receive, or publish them**, so when those permissions are off there is nowhere left to route a free request — and since that is how nearly all free models are served, they fail as a group.

**The fix:** [openrouter.ai/settings/privacy](https://openrouter.ai/settings/privacy) → turn on both

- *Free endpoints that may train on request data*
- *Free endpoints that may publish prompts*

One is not enough. Either one left off is sufficient to cut out almost every free model.

**If it still fails,** the policy exists at three levels — account, organisation, and the individual API key — and the strictest one wins. Your account toggles can look right while a restriction on the key itself still filters free endpoints out. Check the settings of the key the app is using.

**Know what you are agreeing to.** Turning these on lets providers train on the content of your meetings, and some publish prompts and completions to public datasets. Fine for trying models out; not fine for anything confidential. That is the real price of the free tier — the paid models on OpenRouter and the other two providers' free tiers are not affected by these toggles.

---

## Which to pick if you only want one

Start with **Google AI Studio**. Shortest path from zero to a working meeting.

Add **NVIDIA NIM** second. That is the point where a meeting stops being an echo and starts being a comparison.
