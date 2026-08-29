# Default roles

The 23 roles Molfar System ships with out of the box (`modules/roles_seed.py`),
mirrored here for reference and for pulling into future app updates. Unlike
`roles/`, this folder is not community content and its roles are not listed in
the top-level `roles/README.md` / `README.ua.md` tables.

Each role's `README.md` carries `code` / `name` / `description` / `seat` as
YAML front matter, matching the fields `roles_seed.py` needs — that's the
source of truth for re-generating the seed file from these folders.

Currently Ukrainian only (`ua/`); English translations are a follow-up pass.

---

## Participants (seats 1-4)

| Code | Name | Description |
|---|---|---|
| [`cto`](participants/ua/cto/) | Технічний директор | Технічний директор. Стратегія розвитку технологій, архітектурні рішення та управління технічними командами. |
| [`criminal_lawyer`](participants/ua/criminal_lawyer/) | Адвокат криміналіст | Адвокат з кримінального процесуального права та захисту прав людини у кримінальному провадженні. |
| [`it_lawyer`](participants/ua/it_lawyer/) | ІТ Юрист | Юридичний консультант у сфері інформаційних технологій, цифрових продуктів та малого бізнесу. |
| [`marketer`](participants/ua/marketer/) | Маркетолог | Спеціаліст зі стратегії, просування та розвитку продуктів і брендів. |
| [`cybersecurity`](participants/ua/cybersecurity/) | Кібербезпека | Фахівець із кібербезпеки та захисту інформаційних систем, баз даних і мережевої інфраструктури. |
| [`frontend_developer`](participants/ua/frontend_developer/) | Фронтенд-розробник | Розробник клієнтської частини вебзастосунків. |
| [`mechanician`](participants/ua/mechanician/) | Конструктор | Інженер-конструктор. Проєктування виробів, механізмів, прототипів та систем на базі Arduino. |
| [`programmer`](participants/ua/programmer/) | Програміст | Універсальний розробник програмного забезпечення. |
| [`defense_attorney`](participants/ua/defense_attorney/) | Адвокат-захисник | Адвокат-захисник обвинуваченого у кримінальному провадженні: лінія захисту, оспорювання доказів обвинувачення, розумний сумнів. |
| [`prosecutor`](participants/ua/prosecutor/) | Прокурор | Прокурор — державне обвинувачення з об'єктивністю: кваліфікація, оцінка доказів, процесуальні документи, обвинувачення. |
| [`suspect`](participants/ua/suspect/) | Обвинувачений | Обвинувачений (підозрюваний): власна версія подій, документи на захист, реалізація процесуальних прав. |
| [`medical_expert`](participants/ua/medical_expert/) | Мед. Експерт | Судово-медичний експерт: характер і механізм ушкоджень, ступінь тяжкості, причина смерті, висновок експерта. |
| [`football_coach`](participants/ua/football_coach/) | Футбольний тренер | Футбольний тренер — тактичний аналіз матчу: форма, склади, схеми, ключові фактори та найімовірніший сценарій. |
| [`football_journalist`](participants/ua/football_journalist/) | Футбольний журналіст | Футбольний журналіст — збір і перевірка новин про команди й матч: офіційні заяви, кадри, атмосфера; факти проти чуток. |
| [`football_tactician`](participants/ua/football_tactician/) | Футбольний тактик | Футбольний тактик — розбір матчапу на полі: схеми, пресинг, переходи, зони, дуелі; яка тактика нейтралізує яку. |
| [`football_psychologist`](participants/ua/football_psychologist/) | Футбольний психолог | Футбольний психолог — психологічні фактори матчу за відкритими джерелами: мотивація, тиск, стійкість; без діагнозів. |
| [`mathematic`](participants/ua/mathematic/) | Математик-аналітик | Математик-аналітик — статистика, ймовірності й моделі на даних (зокрема xG, Poisson, Elo); результат із рівнем довіри. |

---

## Orchestrators (seat 5)

| Code | Name | Description |
|---|---|---|
| [`moderator`](orchestrators/ua/moderator/) | Модератор | Узгоджує відповіді учасників у єдиний підсумок. |
| [`referee`](orchestrators/ua/referee/) | Суддя (для дебатів) | Оцінює аргументи сторін і виносить обґрунтований вердикт. |
| [`analyst`](orchestrators/ua/analyst/) | Аналітик | Глибокий аналіз відповідей та виявлення суті. |
| [`project_manager`](orchestrators/ua/project_manager/) | Керівник проекту | Перетворює дискусію на план дій. |
| [`criminal_judge`](orchestrators/ua/criminal_judge/) | Суддя Криміналіст | Суддя. |
| [`bookmaker`](orchestrators/ua/bookmaker/) | Букмекер-аналітик | Слухає профільні висновки учасників і зважує їх проти букмекерського ринку; сумнівне перевіряє в мережі; не радить ставки. |
