VERDICT: PASS
CONTENT-HASH: f15443b23434d757

## Blocking
(none left)

## Fixed
- Long strings that were byte-identical to the Finnish rewritten in plainer form (tasks.json: s1 b, c and criteria, s2 b and equation/calculation details, s3 a, c, e criteria, source notes; solutions.md: Kysytty/Annettu lines, Sijoitus and Kaava lead-ins, Hyväksytään myös and Yleisiä virheitä bullets), formulas unchanged.
- s2 d model answer: run-on sentence ("…massaan, $F = k\,mg$, energiayhtälö olisi…") split; s1 first common mistake: doubled "Silloin" removed.
- figures.json: the two long alt texts split into shorter sentences; figures regenerated into solutions.md (practice.py figures --lang fi-easy).

## Polish
- none

## Checked
- Compared tasks.json, solutions.md and figures.json line by line with content/fi/FY4/sovella: every step, justification, number and acceptance kept, nothing added beyond plain-language glosses (e.g. "komponentti tarkoittaa painon osaa tiettyyn suuntaan").
- Physics unchanged: μ_A 0,030 / μ_B 0,045, 17,2 m/s, F_vast 29 N, 14 m/s (13,6 accepted), v' 7,86 m/s, v_B 13,6 m/s ≈ 49 km/h, F_ka 4455 N ≈ 6,7 × paino; directions of every assumption's effect kept. Decimal comma {,} throughout; formulas identical to the Finnish (check_i18n.formulas).
- practice.py check OK; check_i18n fi-easy 0 errors; check_latex OK; figures --check up to date; check_layout 345 and 360 px OK.
