VERDICT: PASS
CONTENT-HASH: e2f7da247d6bbbda

Full review, round 1. The new YO-skill task (type 4, Virheen löytäminen) is L2-08. The rest of the set is unchanged from the version that passed (40177a99521db833).

## Blocking

## Polish
- exercises.json:295 (L2-08) — The stem says "Täsmälleen yhdellä rivillä on virhe", which rules out the last option "Laskussa ei ole virhettä" before the student checks anything. — Drop that sentence from the stem, or drop the option. The option is the type's convention, so dropping the sentence is better.
- solutions.md:195 (L3-05) — Carried over: the end-point speed 0,55 m/s equals k_max by construction, so it is no check. — Compare with the best line, about 0,51 m/s.
- solutions.md:189 (L3-05) — Carried over: "arvo on välin keskikohta" is stated as a rule. — Write "arvioidaan välin keskikohdaksi".
- solutions.md:194 (L3-05) — Carried over: the rounding reason "kuten pisteiden koordinaateissa" does not fit an uncertainty.
- solutions.md:183 (L3-04) — Carried over: the reason "kuten venymissä" should be the by-eye fit, and the extrapolation to the unloaded spring should be softened to "todennäköisesti".

## Checked
- L2-08: Δt = 10,0 − 2,0 = 8,0 min, so row 3 (12,0 min) is the only wrong row. The correct slope is 12,0 l / 8,0 min = 1,5 l/min, as the feedback and the Mallivastaus state.
- L2-08: rows 1, 2 and 4 are correct. Row 4's feedback rightly separates a correct formula from a wrong input. The check 1,5 · 8,0 = 12,0 l is a real check.
- L2-08: the slope is called the flow rate (virtaama) in l/min, and its unit is the y-unit over the x-unit. It stays within FY1's linear model, and the notation matches the lesson.
- All 18 numeric answers were recomputed with numpy polyfit, separately from answers.py. All agree within tolerance: L2-02 3,89 m, L2-05 0,0797, L2-06 0,829 m, L2-07 2,894, L3-04 0,0802, L3-05 15,8 %.
- answers.py prints the same values as exercises.json.
- The hash was the same at the start and the end.
