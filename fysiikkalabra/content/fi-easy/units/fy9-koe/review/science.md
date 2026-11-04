VERDICT: FAIL
CONTENT-HASH: b32f7a442b2e29c4

Science review of the Selkeä suomi translation of fy9-koe (source content/fi/units/fy9-koe/, reviewed). Checked:
`check_i18n.py` (fi-easy: 0 errors), `practice.py check` (fi-easy/units/fy9-koe: 4 tasks, 61 points), every LaTeX
expression of unit.md, teacher.md and sovella/solutions.md against the source (identical multisets, nothing lost or
added), every changed string of inquiry.json, exit-ticket.json and sovella/tasks.json side by side with the Finnish,
and the figures.json texts (numbers 1,02 m / 3,50 m / 0,62 m/s and 0,46 s² / 3,68 s² / 4,03 s²/m kept). Numbers,
answers, tolerances, correct flags and points are unchanged; the added explanations (verrannollinen, hidastuvuus,
normaali, vektori, homogeeninen, tiivistyminen, lämpöarvo) are physically correct.

## Blocking
1. **sovella/tasks.json, fy9-koe-s3, rubric criteria drop "net transfer" (physics-guardrails.md "Net transfer").**
   The source criteria say *nettomääräisesti* in two places; the translation drops it, so a grader's criterion now
   states a one-way transfer, while solutions.md (correctly) keeps *nettona*.
   - `tasks[2].parts[0].criteria[4].detail`: "Teestä siirtyy silti energiaa ympäristöön, mutta hitaasti." →
     "Teestä siirtyy silti nettona energiaa ympäristöön, mutta hitaasti."
   - `tasks[2].parts[3].criteria[0].text`: "Nyt energiaa siirtyy lämpimästä ympäristöstä kylmään veteen." →
     "Nyt energiaa siirtyy nettona lämpimästä ympäristöstä kylmään veteen."
   Optionally explain the word once where it first appears in solutions.md s3 a) Periaate: "nettona eli kun
   molempiin suuntiin siirtyvä energia lasketaan yhteen".

## Polish
2. inquiry.json `activities[30].choices[3].feedback`: "Silloin mittarin viisari liikkuu" assumes an analogue meter;
   the prompt has a (usually digital) yleismittari. Use "Silloin mittari näyttää jännitettä."
3. inquiry.json `activities[3].choices[0].text` and unit.md "Yleisiä virheitä": "kertautuvat" became "kasvavat";
   fine for S2, but "virhe kasvaa lopputulokseen" (unit.md) is unclear. Use "Silloin lopputulokseen tulee suurempi
   virhe."
4. unit.json key_concepts "kulmakerroin": "kahdesta kaukana olevasta pisteestä" → "kahdesta pisteestä, jotka ovat
   kaukana toisistaan" (as in unit.md), so the condition is not ambiguous.
