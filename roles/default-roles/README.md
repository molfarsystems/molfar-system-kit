# Default roles

The default roles of Molfar System, mirrored here for reference and for pulling
into app updates. Unlike `roles/`, this folder is not community content and its
roles are not listed in the top-level `roles/README.md` / `README.ua.md` tables.

26 roles: the 23 the app ships with today (`modules/roles_seed.py`), plus three
marked **new** below, which are queued for the next update and are not in the
shipped app yet.

Each role's `README.md` carries `code` / `name` / `description` / `seat` as
YAML front matter, matching the fields `roles_seed.py` needs — that's the
source of truth for re-generating the seed file from these folders.

Each role exists in Ukrainian (`ua/`) and English (`en/`). Ukrainian is the
original — the app ships in Ukrainian — and English is a translation of it,
kept structurally identical so the two stay in sync.

---

## Participants (seats 1-4)

| Code | Name | Description | Languages |
|---|---|---|---|
| `cto` | Chief Technology Officer | Chief Technology Officer. Technology strategy, architectural decisions, and management of technical teams. | [ua](participants/ua/cto/) · [en](participants/en/cto/) |
| `criminal_lawyer` | Criminal Defense Lawyer | Criminal defense lawyer specializing in criminal procedure law and human rights protection in criminal proceedings. | [ua](participants/ua/criminal_lawyer/) · [en](participants/en/criminal_lawyer/) |
| `it_lawyer` | IT Lawyer | Legal counsel in the field of information technology, digital products, and small business. | [ua](participants/ua/it_lawyer/) · [en](participants/en/it_lawyer/) |
| `marketer` | Marketer | Specialist in strategy, promotion, and development of products and brands. | [ua](participants/ua/marketer/) · [en](participants/en/marketer/) |
| `cybersecurity` | Cybersecurity | Cybersecurity specialist protecting information systems, databases, and network infrastructure. | [ua](participants/ua/cybersecurity/) · [en](participants/en/cybersecurity/) |
| `frontend_developer` | Frontend Developer | Client-side developer for web applications. | [ua](participants/ua/frontend_developer/) · [en](participants/en/frontend_developer/) |
| `mechanician` | Design Engineer | Design engineer. Designing products, mechanisms, prototypes, and Arduino-based systems. | [ua](participants/ua/mechanician/) · [en](participants/en/mechanician/) |
| `programmer` | Programmer | Generalist software developer. | [ua](participants/ua/programmer/) · [en](participants/en/programmer/) |
| `defense_attorney` | Defense Attorney | Defense attorney for the accused: the line of defense, challenging the prosecution's evidence, reasonable doubt. | [ua](participants/ua/defense_attorney/) · [en](participants/en/defense_attorney/) |
| `prosecutor` | Prosecutor | Prosecutor — state prosecution with objectivity: classification, evidence assessment, procedural documents, the charge. | [ua](participants/ua/prosecutor/) · [en](participants/en/prosecutor/) |
| `suspect` | Suspect | The accused (suspect): their own version of events, defense documents, exercising procedural rights. | [ua](participants/ua/suspect/) · [en](participants/en/suspect/) |
| `medical_expert` | Medical Expert | Forensic medical examiner: the nature and mechanism of injuries, degree of severity, cause of death, expert opinion. | [ua](participants/ua/medical_expert/) · [en](participants/en/medical_expert/) |
| `football_coach` | Football Coach | Football coach — tactical match analysis: form, lineups, schemes, key factors, and the most likely scenario. | [ua](participants/ua/football_coach/) · [en](participants/en/football_coach/) |
| `football_journalist` | Football Journalist | Football journalist — gathering and verifying match news: official statements, personnel, atmosphere; facts versus rumors. | [ua](participants/ua/football_journalist/) · [en](participants/en/football_journalist/) |
| `football_tactician` | Football Tactician | Football tactician — the on-pitch matchup: schemes, pressing, transitions, zones, duels; which tactic neutralizes which. | [ua](participants/ua/football_tactician/) · [en](participants/en/football_tactician/) |
| `football_psychologist` | Football Psychologist | Football psychologist — psychological factors of a match from open sources: motivation, pressure, resilience; no diagnoses. | [ua](participants/ua/football_psychologist/) · [en](participants/en/football_psychologist/) |
| `mathematic` | Analytical Mathematician | Analytical mathematician — statistics, probability and data models (xG, Poisson, Elo); results carry a confidence level. | [ua](participants/ua/mathematic/) · [en](participants/en/mathematic/) |
| `interviewer` | Interviewer **new** | Interviewer. Draws out the full picture of an idea through questions and returns a structured summary. Does not advise. | [ua](participants/ua/interviewer/) · [en](participants/en/interviewer/) |
| `tech_journalist` | Technology Journalist **new** | Technology journalist. Deep, accurate articles built from supplied material; fact kept apart from interpretation. | [ua](participants/ua/tech_journalist/) · [en](participants/en/tech_journalist/) |
| `architect_roles` | Role Architect **new** | Role architect. Turns the idea of a specialist you need into a finished Molfar pair of files: prompt and skill. | [ua](participants/ua/architect_roles/) · [en](participants/en/architect_roles/) |

---

## Orchestrators (seat 5)

| Code | Name | Description | Languages |
|---|---|---|---|
| `moderator` | Moderator | Reconciles the participants' answers into a single, balanced summary. | [ua](orchestrators/ua/moderator/) · [en](orchestrators/en/moderator/) |
| `referee` | Referee (for Debates) | Assesses the parties' arguments and delivers a well-reasoned verdict. | [ua](orchestrators/ua/referee/) · [en](orchestrators/en/referee/) |
| `analyst` | Analyst | In-depth analysis of the answers to uncover what's really being said. | [ua](orchestrators/ua/analyst/) · [en](orchestrators/en/analyst/) |
| `project_manager` | Project Manager | Turns the discussion into an action plan. | [ua](orchestrators/ua/project_manager/) · [en](orchestrators/en/project_manager/) |
| `criminal_judge` | Criminal Judge | Judge. | [ua](orchestrators/ua/criminal_judge/) · [en](orchestrators/en/criminal_judge/) |
| `bookmaker` | Bookmaker Analyst | Weighs the participants' specialist findings against the bookmaker market; checks doubtful claims online; no betting advice. | [ua](orchestrators/ua/bookmaker/) · [en](orchestrators/en/bookmaker/) |
