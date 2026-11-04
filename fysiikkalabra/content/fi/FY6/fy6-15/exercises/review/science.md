VERDICT: PASS
CONTENT-HASH: ab5847925a41a7da

## Blocking

## Polish
- content/fi/FY6/fy6-15/exercises/solutions.md:138 (L2-07 Vastaus) — "sulake ei suojaa ihmistä" is stated flatly and the last sentence says the RCD protects "yhdessä suojamaadoituksen kanssa", which reverses the lesson's wording (the fuse protects people only together with protective earthing; the RCD cuts the small current through the body on its own) — write: "Sulake ei huomaa kehon läpi kulkevaa virtaa; ihmistä se suojaa vain yhdessä suojamaadoituksen kanssa. Kehon kautta kulkevan virran katkaisee vikavirtasuoja." (B, consistency with the brief's Yleinen virhekäsitys).
- content/fi/FY6/fy6-15/exercises/solutions.md:190 (L3-05 b) — "viikoilla 5 ja 7 virta on tuntokynnyksen yläpuolella" leaves out week 3 (1,9 mA > 0,5 mA) — write "viikoilla 3, 5 ja 7".
- content/fi/FY6/fy6-15/exercises/solutions.md:119 (L2-05 Järkevyys) — "satakertaisen vaaran vain muutamassa kymmenessä kilo-ohmissa" does not match the computed ratio of 61 — e.g. "Kosteus ja paljas iho kasvattavat samalla jännitteellä virran yli kuusikymmenkertaiseksi."
- content/fi/FY6/fy6-15/exercises/solutions.md:175 (L3-04 Periaate) — the origin line needs its physical reason (guardrails, Fits) — add: "Kun tehoa ei kehity, johto on ympäristön lämpötilassa, joten suora kulkee origon kautta."
- docs/exercise-bank/FY6.md (fy6-15 Taso 1) — the plan's third L1 item (largest power on a fuse) is existing L1-02, so the new L1-08 (U = E_max d) was added instead and is the mirror image of L2-03 — update the plan line, or give L1-08 a context other than an air gap.

## Checked
- All 20 answers recomputed in one script with my own formulas: answers.py, exercises.json and the solutions agree (L2-05 61,1; L2-06 9,57 A; L2-07 115 mA; L3-04 k = 0,297 K/W, 20,5 A; L3-05 6,17 kΩ).
- L2-05 currents 4,2 / 19,2 / 95,8 / 256 mA and their categories against the IEC 60479-1 type thresholds: correct.
- L2-06: all five pairs above 2300 W found; the best allowed pair is 1400 + 800 W.
- L3-04: ratios ΔT : P 0,33/0,30/0,30/0,30; ΔT at 16 A 30 K and at 25 A 74 K; the extrapolation is named. Linear cooling and constant R are an assumption that suits the level (C).
- L3-05: the series model R_e + R_k, the RCD seeing the leakage to earth, the currents 0,26–41,8 mA, and the threshold week 9.
- L1-06, L1-07: exactly one correct option each; every distractor and its feedback is right (class I/II/III, earthing carries no current in normal use).
- Significant figures and their stated reasons, units (kertaa, kΩ) and tolerances.
- Level fit 8/7/5. New tasks are not duplicates (L2-07 b repeats L1-03's U : R, but its error-analysis part carries the level).
- Notation (I_s, R, E_max, U : R) matches the brief. Everything is inside the FY6 safety content.
