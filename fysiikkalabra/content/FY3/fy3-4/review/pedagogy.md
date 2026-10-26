VERDICT: PASS
CONTENT-HASH: 706bdc1c984c1ed5

## Blocking
(none) Round-1 blocking finding is fixed: pred-3 feedback now sends the student to Teoriatiivistelmä, where the column weight is derived and A cancels; no answer is disclosed before commitment.

## Polish
- inquiry.json pred-3 — the only prediction with no experiment or reveal; the simulation cannot test narrow tube vs wide basin, so it is settled by derivation only. Consider a one-line note in the reflect prompt, or a "kaksi astiaa" mode later.
- simulation canvas and DOM readout ("Syvyys h = 5,0 m", "ρgh", "p = p₀ + ρgh") are plain interface text, not maths; per NOTES.md §1 this stays until the teacher decides. Visible mismatch with the maths-typeset Alkutila line and table headers next to it.
- simulation panel shows two separate boxes, "Mallin oletukset ja selitys" and "Mallin oletukset", with overlapping content; merge or rename so the student does not open both.
- pred-2 prompt at 390 px breaks the line after "(" before the inline maths ("vesi ( / 1000 kg/m³ )"); rephrase so the unit is not at a line start, e.g. "tavallinen vesi, tiheys $1000\,\text{kg/m}^3$,".
- exp-2 has no numeric question (exp-1 has); one such as "Kuinka monta prosenttia kokonaispaine kasvoi, kun tiheys kasvoi 24 %?" would make the refutation of "kokonaispaine kasvaa 24 %" explicit.

## Checked
- Hash unchanged at start and end; no lesson file edited.
- Opening question (muurin paksuus) is answered after the derivation, via ylipaine; the slot's goals (p = F/A, p = p₀ + ρgh as a line with constant term, scalar force) are covered, no more.
- pred-1 and pred-2 can be refuted by exp-1/exp-2 (min 2); wrong-option feedback repairs the misconception (constant p₀ term, buoyancy confusion).
- Experiments: locked and varied parameters, Alkutila line and table headers render symbols as maths; density slider visibly locked in exp-1 capture.
- 1280 px: simulation beside the experiments, readable; 390 px: ennusta, exp-1 not clipped.
- Worked example is staged one step per stage, differs from the exercises, ends with a sanity check.
- Exercises: three levels, L3 combines two ideas (snowshoe, tank cover, layered liquids); solutions in LaTeX with Järkevyys.
- Exit ticket tests the core idea (area, hydrostatic and total pressure, tube vs basin).
- Finnish reads correctly; "Teoriatiivistelmä" naming consistent.
