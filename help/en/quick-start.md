# Quick start

About five minutes from installing the app to a working meeting.

---

## 1. Get one API key

Menu → **AI Settings** → paste a key into a provider's field → tap the diskette icon. The provider switches on by itself.

The fastest option is Google: [aistudio.google.com/apikey](https://aistudio.google.com/apikey) → *Create API key*. No card, no billing.

Full instructions for all three providers: [api-keys.md](api-keys.md)

Use the **Test** button to confirm the key works before going further.

---

## 2. Warm up with Haiduk

Before assembling a meeting, try **Haiduk** — a single chat with one model, no setup at all. It confirms the key works end to end and gets you used to the interface.

Haiduk can wear any role, so it is also the fastest way to test a new prompt.

---

## 3. Create a meeting

On the home screen, create a project of type **Meeting** and give it a name.

Open **Participants settings**. Six seats:

- Seats 1-4: participants — each gets a role and a model
- Seat 5: Orchestrator — runs the round and writes the summary
- Seat 6: Secretary — handles documents and the protocol

**The minimum is an Orchestrator plus one participant.** Start with two participants on different providers; you can always add more.

Tap **Save**.

---

## 4. Ask something

Type into the **Ask the Orchestrator** field. The question goes to every participant at once. Each answer appears in its own tab, and the Orchestrator gathers them into a summary.

Ask something that has more than one defensible answer. A question with a single correct answer will get the same reply four times, which tells you nothing. A question involving trade-offs will show you where the models disagree — and that is the whole point.

---

## 5. Optional: add documents

Add documents to the project and hand them to specific participants using the badge counter at the top of each tab. Only the participants you give them to will see them.

---

## 6. Save what matters

The three-dot menu in any tab exports that chat to a text file in `Download/Molfar_s-…`, with a header showing seat, role and model, and every answer signed.

The Secretary tab can compose a full meeting protocol — roster, chronology, conclusions — and save it as a file.

**Do this for meetings you care about.** Everything else lives inside the app, and uninstalling the app deletes it.

---

## Where to go next

- [api-keys.md](api-keys.md) — all three providers in detail
- [faq.md](faq.md) — roles, prompts, skills, documents, web search
- [troubleshooting.md](troubleshooting.md) — when something does not work
- [../../models/recommended.md](../../models/recommended.md) — which model belongs in which seat
- [../../roles/](../../roles/) — ready-made roles to copy
