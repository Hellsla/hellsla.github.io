VERDICT: PASS
CONTENT-HASH: 561ea006852fe64e

Pedagogy review of the Selkeä suomi (S2) translation of fy9-kokeellisuus, judged against NOTES.md §12.

The translation keeps the source's review design: the same activities, task counts, correct options, feedback per misconception, rubrics, points and 75-minute plan. `check_i18n.py` passes. The S2 rewriting is careful and natural:
- Long participial sentences are split into short sentences ("Toistot näyttävät hajonnan eli sen, kuinka paljon tulokset vaihtelevat").
- Difficult words are explained the first time, inside the sentence: virhelähde, vaimenee eli heikkenee, vakioidaan eli pidetään samana, taaraus, sovitetaan eli piirretään, hypoteesi eli oletus, riippuu, pito, syrjäyttää, lukkiutua, rajakulma, komponentti eli osa, särmä eli reuna.
- Multi-step instructions are numbered or split (activities.7 1)–3), activities.20, the exit ticket).
- Physics terms are kept and explained, never replaced.

Key concepts: there are 5 (muuttuja, mittausepävarmuus, satunnaisvirhe, systemaattinen virhe, kulmakerroin). They are the unit's central ideas, the glossary check passes, and the component renders after the opening with the fixed lead. teacher.md adds a sensible S2 note.

## Blocking
None.

## Polish
1. sovella/solutions.md: the "Yleisiä virheitä" and "Hyväksytään myös" lists of all six tasks are copied from the source word for word. So are s4 b) (Vastaus, Järkevyys), s5 a) Vastaus/Järkevyys, s5 b) and s6 b). These are the densest sentences on the page, e.g. "$T^2$ lasketaan kymmenen heilahduksen ajasta jakamatta ensin kymmenellä", "…kertomatta, mikä virhe on kyseessä…", "jolloin unohtuu, että…". Split them as the rest of the solutions are split, e.g. "$T^2$ lasketaan kymmenen heilahduksen ajasta. Aikaa ei ensin jaeta kymmenellä."
2. unit.json key_concepts "kulmakerroin": "kahdesta kaukana olevasta pisteestä" is ambiguous (far from what?). Write "kahdesta pisteestä, jotka ovat kaukana toisistaan", as unit.md does.
3. sovella/tasks.json tasks.4.parts.3.criteria.1: "Esimerkiksi kapeampi mittalasi, jonka asteikkoväli on pienempi. Tai ylivuotoastia, …" are verbless fragments. Write "Keino voi olla esimerkiksi kapeampi mittalasi … Toinen keino on ylivuotoastia, …".
4. unit.md "Yleisiä virheitä", item 3: "Mittaustapa tuo kuitenkin suuremman epävarmuuden, esimerkiksi reaktioaika." Here "esimerkiksi reaktioaika" attaches to the wrong noun. Write "Mittaustapa, esimerkiksi reaktioaika, tuo kuitenkin suuremman epävarmuuden."

## Shared issues
None.
