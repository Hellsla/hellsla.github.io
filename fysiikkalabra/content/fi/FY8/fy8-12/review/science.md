VERDICT: PASS
CONTENT-HASH: c075a7b9a825b4cf

## Blocking

## Polish
- inquiry.json (ennuste-1, correct option's feedback): the feedback calls 9 alpha pulses behind aluminium "satunnaisvaihtelun rajoissa taustasäteilyn tasoa". With a background mean of 4, P(N ≥ 9) ≈ 2 %, and koe-1 gave 5 behind paper. Fix: call it an unusually high background reading, or use a seed that gives about 4.
- lesson.md (Ydinajatus, "kirkaskaan valo ei ionisoi vettä"): a fair simplification (C). Multiphoton ionisation by intense lasers is the only exception, so no change is needed.

## Checked
- Round 1 fixes: the `energia` band now runs from red at 1,7 eV to violet at 3,3 eV (fig-4-390). The HFIR caption says "varatut hiukkaset". The misconception is limited to conventional sterilisation, and the low-dose risk sentence says "arvioidaan".
- Own recompute: n_i = 1,61·10⁵, range 4,09 cm, visible light 1,77–3,26 eV, m_α/m_e ≈ 7290.
- Worked example: 23,77 mm, rounded to 24 mm, with a valid check between 4 and 5 half-value thicknesses. Siirto: 5,57 %; the mistake values 84,7, 94,4 and 12,0 recompute, and d½ = 0,12 mm matches XCOM for lead at 60 keV.
- Tarkistus-2 curve 800·(1/2)^(d/12): 400 at 12 mm, 200 at 24 mm, 50 at 48 mm.
- Half-value thickness table from XCOM at 662 keV: 5,5 / 12 / 34 / 39 / 81 mm. Concrete ≈ 7 × lead. μ = ln 2 / d½ is derived correctly. The `vaimeneminen` figure's markers and the aluminium value 0,60 at 25 mm are correct.
- Seeded model values: koe-1 5/5/550/577, koe-2 9/4/535, lead 590/332/175/89/57. Net ratios 0,56 and 0,29 give d½ ≈ 5,6 mm. Every value quoted in the predictions and the conclusion matches.
- Beta model: 6,6 cm²/g, with a 1,1 g/cm² cut-off (Katz–Penfold 1,10 for 2,28 MeV), which is about 4,1 mm of aluminium.
- Experiments: each varies only its own parameter and locks the rest, and simState gives `pulssit`. The model box states the sim's limits.
- Every choice item has exactly one correct option, and each distractor's feedback is right. The photon interaction ranges and the 1,022 MeV threshold are right.
- The GM tube description and the background subtraction agree across the theory, summary, tarkistus-3, the glossary and the exit ticket.
