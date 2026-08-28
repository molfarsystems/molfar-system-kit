# Troubleshooting

---

## A model does not answer, or shows an error

Check these in order — the first two cover most cases.

**1. The key.** AI Settings → the provider's **Test** button. If Test fails, the problem is the key, not the model. Re-copy it; a stray space at the start or end is the usual culprit.

**2. Rate limits.** Free tiers limit requests per minute and per day. Wait a minute and try again, or switch that seat to another provider. This is by far the most common cause when a seat worked earlier in the session and then stopped.

**3. Timeout** — *"did not respond in 220 s"*. A heavy question plus large documents plus a slow model. Simplify the request, detach some documents, or put a faster model in that seat.

**4. An error carrying the provider's own text.** Then the problem is on their side. Try a different model, or come back later.

---

## One seat fails, the others work

Almost always the model, not the app.

- Check whether that model is marked `$` on OpenRouter and your balance is empty
- Check whether the model still exists — providers deprecate models regularly, and a seat saved months ago may point at something that is gone
- Reopen the model picker for that seat and pick from the current list

---

## The round takes forever

A round finishes only when the **slowest** participant finishes. One reasoning model among four fast ones sets the pace for everyone.

If this bothers you, keep reasoning models to one seat, or use them in Haiduk where nothing waits on them.

---

## All four participants say the same thing

Usually means the seats share a model, or share a model family. Four Gemini variants are still one opinion.

Mix providers. See [../../models/recommended.md](../../models/recommended.md).

It can also mean the question genuinely has one answer — in which case a meeting is the wrong tool and Haiduk would have been faster.

---

## The globe icon is greyed out

That provider or model does not support web search. Not a fault. Switch the seat to a model that does, or accept an answer from the model's own knowledge.

---

## A role I created does not appear

Roles are saved per role list, not per project. Check the **Roles** section — if it is there, reopen Participants settings and pick it for a seat.

If the prompt was loaded from a file and the field looks empty, the file may not be plain text. The editor accepts `.txt` and `.md`. A `.docx` will not load.

---

## The prompt will not fit

The prompt limit is 5000 characters. Long prompts are usually long because they contain instructions that belong in the **skill** field instead. Split it.

---

## The app crashed

The crash screen has a copy button. Copy the report and send it through the website — it contains what is needed to find the cause.

---

## I uninstalled the app and lost everything

Unfortunately that is how it works: no server means no backup. Projects, roles, histories and keys were all in the app folder.

What may still be on the phone: anything exported to `Download/Molfar…`. Chat exports and protocols live outside the app and survive uninstalling.

**Before you next reinstall or change phones,** export the meetings that matter.

---

## Something else

Ask in [Discussions](https://github.com/molfarsystems/molfar-system-kit/discussions) — public questions get public answers, which helps whoever hits the same thing next.
