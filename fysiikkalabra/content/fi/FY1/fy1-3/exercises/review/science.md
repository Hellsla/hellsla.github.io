VERDICT: FAIL
CONTENT-HASH: d9611902d296811e

Full review, round 1. The new YO-skill task (type 10, Mittausdata) is L2-08. The rest of the set is unchanged from the version that passed (b767859bee6529a5).

## Blocking
- content/fi/FY1/fy1-3/exercises/exercises.json:307 and solutions.md:201 (L2-08) — **A**. Option 4 says "Kevyen kuulan heilahdusaika on 14,300 s". 14,30 s is the time of ten swings; the period is about 1,43 s. The feedback (line 308) and the Mallivastaus fault the option only for its extra digits and offer "14,3 s ± 0,2 s" as the right form. That teaches a wrong quantity as if it were the period. — Write "Kevyen kuulan kymmenen heilahduksen aika on 14,300 s …", and in the Mallivastaus say "kymmenen heilahduksen aika 14,3 s ± 0,2 s" (heilahdusaika 1,43 s ± 0,02 s).

## Polish
- exercises.json:249, 254, 295, 298; solutions.md:198 (L2-08) — The text calls the hand-timing uncertainty 0,2 s "lukeman epävarmuus" and writes it Δx. The lesson keeps *lukeman epävarmuus* (half a scale step, d/2) apart from reaction-time uncertainty, which it says the display step does not show. — Write "käsin otetun ajan epävarmuus Δt = 0,2 s".
- exercises.json:249 (L2-08) — The stem gives the means as 14,30 s and 14,36 s, but option 4's feedback says the 0,2 s uncertainty allows only tenths. — Call them "laskimen keskiarvot" in the stem, or note in the feedback that unrounded means are kept so the two can be compared.
- exercises.json:254/298 (L2-08) — The text says "painon vaikuttavan" although the varied quantity is the mass. — Write "kuulan massan vaikuttavan". The stem also has the typo "heilurilanguan".
- solutions.md:140 (L1-08) — Carried over from the last review: "joten työntömitta on tarkempi väline" infers accuracy from resolution. — Limit the claim to reading uncertainty.
- solutions.md:163 (L2-06) — Carried over: "eli siinä on systemaattinen virhe" should say *todennäköisesti*, as line 164 does.

## Checked
- L2-08 data: means 71,5/5 = 14,30 s and 71,8/5 = 14,36 s; difference 0,06 s; half-ranges 0,20 s and 0,15 s, as the Mallivastaus states.
- L2-08 has exactly one correct option. "Ei osoita" is right: the intervals 14,30 ± 0,2 and 14,36 ± 0,2 overlap. Comparing the difference with a single result's 0,2 s is conservative but still right (C). Option 3 is correctly too strong (a difference that cannot be shown is not proof of equality), which matches the guardrail.
- Physics of L2-08: the period really does not depend on mass, and T ≈ 1,43 s gives L ≈ 0,51 m, which is realistic. The conclusion does not claim more than the data support.
- All 19 numeric answers were recomputed with my own formulas, separately from answers.py. All agree within tolerance: L2-01 4,83 %, L2-02 10,67 mm, L2-05 1,820 s, L2-07 14, L3-04 2,41 s (2,48 s with all eight), L3-05 0,04 g/cm³.
- answers.py prints the same values as exercises.json. The two multiple-choice tasks rightly have no number.
- The hash was the same at the start and the end.
