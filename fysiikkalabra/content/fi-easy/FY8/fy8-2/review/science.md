VERDICT: PASS
CONTENT-HASH: 16ffb2c6d4454fc3

## Blocking

## Polish
- lesson.md (fig "spectra", aria 380–720 nm) vs inquiry.json simulaatio `calc` and sim.js (380–750 nm) — the visible band has two upper limits in one lesson — use one limit (the worked example's 1,7–3,3 eV matches 380–750 nm).
- inquiry.json siirto, hint 3 and solution "Periaate" — say "lämmöksi / lämpönä" where the prompt and answer say "sisäenergiaksi" (guardrail: a body has internal energy, heat is energy in transfer) — use sisäenergia throughout; same for lesson.md Fluoresenssi "luovuttaa osan energiasta lämpönä" vs Tiivistelmä "muuttuu sisäenergiaksi".
- lesson-answers.py `ex-J` comment 3,1037e-19 J vs worked example 3,1039e-19 J (from the rounded hc) — harmless (final 1,94 eV either way); align the comment.
- inquiry.json ennuste-1, last distractor feedback "Lähtötaso vaikuttaa siihen yhtä paljon kuin loppumistaso" — loose; "fotonin energia riippuu molemmista tasoista" is exact.

## Checked
- Recomputed in one script (h, c, e of the lesson): level table −13,6 … −0,38 eV; Balmer 656/486/434/410 nm, gaps 170/52/24 nm, 7→2 397 nm; Lyman 122/103/97/95/94 nm, 10,2 eV.
- Worked example: hc = 1,9865e-25 J m, 3,104e-19 J, 1,94 eV; symbolic first, conversion and 3 s.f. reason right, check against 656 nm (1,89 eV) real.
- inquiry numerics: kertaus 3,02 / 1,91 eV; virhe 1,05e-25 "m", 3,028e-19 J, 656 nm; siirto 3,062 − 2,340 = 0,722 eV, mistakes 9,92 / 3,06 / 2,34 / −0,722; tarkistus-2 2,27 eV, mistakes 3,64 and 0,44.
- Every choice item: exactly one correct option, distractors wrong, feedback physics right (ennuste-2: visible Balmer absorption needs atoms already at n = 2).
- Experiments: tila and n_a locked, n_y varied; adapter exposes tila, ny, na; simState gives dE and lam; n_y ≤ n_a disabled.
- sim.js: E_n = −13,6/n², λ = hc/ΔE with the lesson's constants; readout 656 nm, 1,89 eV (capture); limits (one atom, no intensities, hot gas for n_a > 1) stated in Mallin oletukset.
- Figures to scale: levels (22,0 px/eV), spectra (1 px/nm, lines at 410/434/486/656), fluorescence (365 nm 3,40 eV; 520 nm 2,38 eV).
- Lamp spectrum and table: Hg 405/436/546/577/579, He, Na, H lines agree with NIST values.
- Greenhouse box: 15 µm = 0,083 eV, vibration gaps 0,08–0,5 eV; mechanism (absorption, collisions, re-emission in all directions) correct; inside FY8 scope (optional box).
- Conditions stated: exact-energy rule with line width, transition strengths and the ionisation exception; exit ticket agrees with theory.
