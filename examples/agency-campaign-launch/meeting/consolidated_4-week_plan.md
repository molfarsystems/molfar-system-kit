# Molfar System Kit: final consolidated 4-week plan

This is built from the three brief documents and the specialists' answers in rounds 1–3. I did no web search. The follow-up questions from round 3 have not been answered, so the points they cover use defaults, marked below. All times are the specialists' estimates, not timed trials. The capacity sums are mine.

## Goal

The owner sets the final numbers. The direction from the brief is:
- People find the Kit and install packs.
- A few outsiders react: a star, a comment, a question or a submitted role.
- Molfar gets new installs from the Kit.
- The owner ends with a routine that fits 4 hours a week and survives a lost week.

## Shared base

- **Message.** The Content Creator's one-sentence and one-paragraph descriptions, announcement text and 5-question FAQ are the single source. Every channel reuses them, and all facts trace to `02_facts.md`.
- **Voice.** Every post says the author made the project: "a solo developer from Ukraine, working with Claude". The text uses "we".
- **Tagging.** `utm_campaign=kit-launch`, `utm_medium=social`, and `utm_source` is one of `github`, `discord`, `telegram` or `x`. `utm_content` is `w1` to `w4` by week. The repository URL stays plain, because GitHub links cannot carry a UTM. The tagged links are the website link and the Play link.
- **Empty and lost cells.** Write "not yet" for Play and site UTM cells that are still empty. A blank GitHub cell after a long gap is "lost", never zero. A skipped post is recorded as skipped, not as zero.

## Plan

| # | Week | Action | Owner | Time | Done test | Measure |
|---|---|---|---|---|---|---|
| 1 | 1 | Fill the day-1 baseline: GitHub Traffic (phone browser), stars, Play acquisitions, GA sessions, Discord and Telegram counts. Open the Play link once to test UTM capture. | Analytics Reporter | 30 min (25–40) | Dated note saved **before the first post** | The baseline itself |
| 2 | 1 | Edit the README to add the FAQ and the pinned note, which says replies may be delayed. **Fallback** if the owner cannot edit or pin from the phone: put the 5 FAQ answers and the note in the Discussions announcement (step 3). | Content Creator | 20–30 min; the fallback adds 10–15 | README or fallback text is live | Questions about install steps (proxy) |
| 3 | 1 | Publish the announcement in GitHub Discussions, linking to the README FAQ. Pin it if possible. | Content Creator | ~60 min | Post is live, link saved | Unique visitors, outside replies |
| 4 | 1 | Post the same self-contained text in the Discord `feedback` forum. | Content Creator | not estimated | Post is live | Outside replies. The Discord count is context only. |
| 5 | 1 | Batch-write the X posts in a phone note, then publish the 7-post thread and pin it. Posts 1/–5/ and 7/ carry no link. Post 6/ carries the plain repository URL. A reply under 1/ carries the Play link (with `referrer`), the website link (`utm_source=x`) and the repository link. | Twitter Engager | ~60 min | Thread live and pinned; reply posted | Website sessions with `utm_source=x`. The `t.co` row only says that X sent people. |
| 6 | 1 | Take the GitHub Traffic launch snapshot at the end of the sitting, after steps 3–5 are live. | Analytics Reporter | 10 min | Snapshot saved with the time noted | Visitor and clone totals. A missing `t.co` row on launch day is not evidence. |
| 7 | 1 | Weekly check, copying the GitHub cells from the snapshot. | Analytics Reporter | 10 min | Note filled | The six weekly metrics |
| 8 | 2 | Post the short install walkthrough in Telegram. | Content Creator | ~45 min | Post live | Subscribers (context), unique visitors |
| 9 | 2 | Post "role of the week" on X. Repost the pinned reply with `utm_content=w2`. | Twitter Engager | 20 min plus refresh (refresh not estimated) | Posted | Impressions noted in a phone note. This is the Twitter Engager's own proposal and not one of the Analytics Reporter's metrics. |
| 10 | 2 | Weekly check. | Analytics Reporter | 15 min | Note filled | Six metrics |
| 11 | 3 | Post "prompt versus skill, and submit a role" in GitHub Discussions. | Content Creator | ~60 min | Post live | Outside replies, issues, submitted roles |
| 12 | 3 | Post the X install walkthrough, reusing step 8. Refresh the pinned reply (`w3`). | Twitter Engager | 20 min plus refresh | Posted | Sessions with `utm_source=x` |
| 13 | 3 | Weekly check. | Analytics Reporter | 15 min | Note filled | Six metrics |
| 14 | 4 | Post answers to the five newcomer questions in the Discord forum. | Content Creator | ~60 min | Post live | Outside replies |
| 15 | 4 | Post "submit a role without git" on X. Refresh the pinned reply (`w4`). | Twitter Engager | 20 min plus refresh | Posted | Submitted roles |
| 16 | 4 | Final check against day 1, then apply the bands below. | Analytics Reporter | 15 min (10–20) | Verdict noted | The bands below |

**If a sitting runs out of time:** do the baseline first, then the snapshot, then the full weekly check. Posts come between the baseline and the snapshot.

## Capacity

- **Week 1:** about 3.2–3.3 h (steps 1, 2, 3, 5, 6, 7). With the README fallback it is about 3 h. The Discord post (step 4), replies and website fixes are not included, so week 1 is close to the 4-hour limit. **Cut if needed:** the website fixes, and step 4 can simply paste the step 3 text.
- **Weeks 2–4:** about 1.3 h, 1.6 h and 1.8 h. The weekly pinned-reply refresh and replies are not included.

## Result bands (the Analytics Reporter's proposal; the owner decides)

- **Worked:** at least 3 of these 4:
  - 14-day unique visitors of at least 30 and at least 3 times the day-1 figure.
  - At least 5 net new stars.
  - At least 3 outside replies.
  - Play acquisitions at least 5 above the prior 28 days, or at least 3 acquisitions carrying a campaign UTM.
- **Did not work:** only if all of these hold:
  - No 14-day window is more than 10 visitors above day 1.
  - Net stars are under 2.
  - There are no outside replies.
  - Play acquisitions are not above the prior 28 days.
- **Unclear:** everything else, including a lost GitHub window.

Installing a pack inside the app cannot be measured, because the app has no analytics and GitHub does not count raw-file downloads. The proxies are unique cloners, questions about install steps and submitted roles.

## If a week is lost

- **Week 2, 3 or 4 lost:** that week's posts move or are dropped, and a missed week is not repeated. The README, the pinned Discussion and the pinned thread keep working.
- **Lost before launch:** everything shifts, but step 1 still comes before the first post.
- **Offline 15 days or more after launch:** early GitHub days are gone for good, because GitHub keeps 14 days of traffic and cannot backfill ([GitHub Docs: viewing traffic](https://help.github.com/articles/viewing-traffic-to-a-repository/)). The launch snapshot is the safeguard. Mark those cells "lost".
- **Skipped pinned-reply refresh:** the weekly note must record that the week's X sessions are still tagged `w1`, so it is not read as a drop. The Analytics Reporter's wording for this has not been provided yet (see queue question 4).

## Cut or deferred

- **Reddit:** out for the 4 weeks (Branch A).
  - The Reddit Community Builder's own go/no-go test requires reading the current Reddit and subreddit rules, and most of their sources were not opened.
  - It also needs a 4–6 hour reply window, which conflicts with "no daily presence".
  - The only cheap item is checking the old account's profile while logged out (a few minutes). The Reddit Community Builder has not yet confirmed this, and it is not a plan step.
  - The Reddit draft post must not be used unless the owner checks every sentence.
- **Facebook and Hacker News:** no steps, because nobody proposed any.
- **Ukrainian wave:** pending the owner's answer.

## Open risks and gaps

- **Nobody answers Discussions while the owner is offline.** The pinned note and the README FAQ only set expectations.
- **Unverified X mechanics:** the character limit (the Twitter Engager's own count is about 250 for post 6/ and about 320 for the reply) and whether X lets you pin a reply. Paste the drafts into the composer and read the counter. If the reply is too long, split it in two.
- **Website fixes, not verified by me:** the Content Creator reports from the live site that screenshots say "coming soon", that the role limit reads 10,000 characters where `02_facts.md` says 25,000, and that no Kit link is obvious on the homepage. Nobody has estimated or owned these fixes.
- **GitHub app:** whether it shows Traffic is [unverified]. Use a phone browser.
- **Estimates:** they assume Play Console and Analytics are already logged in on the phone.

## Decisions needed from the owner

1. Can you edit the README, pin a Discussion, and post in Discord from the phone? If not, use the fallback in step 2.
2. Is a thread with no links in the body except one, plus a pinned reply, acceptable?
3. Do the website fixes and a screenshot get done, and which one fix is the minimum?
4. Do you keep "from a phone" in post 7/ and the mixed "we / a solo developer" voice?
5. Which pack is the walkthrough example?
6. Which single posting slot can you hold?
7. Are Play Console and Analytics already logged in on the phone?
8. Do you want a Ukrainian wave this month or later?
9. Reddit: stay out (default)? If you want one community tested, send the subreddit name and its rules text to the Reddit Community Builder.

## Follow-up queue (round 3 questions, still unanswered)

1. Content Creator — How many minutes do the Discord forum post and the three website fixes (screenshot, the 10,000 vs 25,000 character wording, a visible Kit link) take, and which one fix is the minimum worth doing?
2. Twitter Engager — If X does not allow pinning a reply, where should the Play and website links sit instead, and how many minutes does the weekly refresh of that link set take?
3. Reddit Community Builder — Since your 4–6 hour reply window conflicts with a possibly offline owner, do you withdraw Branch B and confirm that only the logged-out profile check of the old account remains for these 4 weeks?
4. Analytics Reporter — If the owner skips refreshing the link set in a week, how should the weekly note record that week's X sessions still tagged `utm_content=w1`, so it is not read as a drop?