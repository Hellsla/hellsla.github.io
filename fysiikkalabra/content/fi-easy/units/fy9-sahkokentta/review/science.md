VERDICT: PASS
CONTENT-HASH: 5d7c37ca8b9e6324

## Delta review

Delta review (2026-11-05). `git diff dcad1b122 -- content/fi-easy/units/fy9-sahkokentta lessons/units/fy9-sahkokentta` shows one change only: sovella/tasks.json s1 b, rubric criterion `calculation` (1 p). The long inline formula q = 0,080 m·sqrt(4,93·10^-4 N / 8,988·10^9 N·m²/C²) is now split into $F_\text{s} = 4{,}93 \cdot 10^{-4}\,\text{N}$ ja $k = 8{,}988 \cdot 10^{9}\,\text{N}\cdot\text{m}^2/\text{C}^2$, joten $q = 0{,}080\,\text{m} \cdot \sqrt{F_\text{s}/k} \approx 1{,}87 \cdot 10^{-8}\,\text{C}$ ja $n = q/e \approx 1{,}2 \cdot 10^{11}$. The text is identical to the Finnish source's criterion (check_i18n fi-easy 0 errors; the S2 formula-keeping rule holds).

Science: recomputed q = 0,080·sqrt(4,93e-4/8,988e9) = 1,874·10^-8 C, n = 1,17·10^11; values, units and the result are unchanged. F_s is the unit's own symbol for the electric force (same as in criterion 1, $q = r\sqrt{F_\text{s}/k}$), so the split names the given values and keeps the physics. Points (1 p, part b 4 p, task total) unchanged; practice.py check and units.py check OK. No new issue.

## Earlier review (still valid)

Science review of the Selkeä suomi translation of fy9-sahkokentta (source content/fi/units/fy9-sahkokentta/, passed).

Checks done: `check_i18n.py` (fi-easy 0 errors), `practice.py check` (OK, 6 tasks, 95 points), `units.py check` (ok).
I also compared every `$…$` / display formula and every number outside the maths between the source and the translation
in unit.md, inquiry.json, exit-ticket.json, teacher.md, sovella/tasks.json and sovella/solutions.md. The multisets are
identical, so no formula, value, unit or answer was changed, dropped or added. The correct flags, tolerances, mistake values
and criteria points match. I recomputed in one Python call: F = 0,493 mN, q = 18,7 nC (1,17·10^11 e), F' = 0,2465 mN,
r = 6,35 cm; C = 184,5 pF, Q = 0,830 µC, W = 1,868 mJ, E = 1,50 MV/m, U' = 803,6 V, W' = 0,3335 mJ; fit slope 353,7
pF·mm, intercept 22,2 pF, ε0 = 8,84·10^-12 F/m; 1,5 mV, 4 mm; panel P_max = 0,989 W, η = 16,5 %; v = 40,2 km/s,
F = 87,5 mN, Δv = 349 m/s, m_Xe = 5,64 kg, 1,76 kW; Tutki v = 7264 km/s (mistakes 9377, 5136, 169,5); 35,95 µN;
6,008 pN; 1690 V; 3,865 h; 0,1126 J; teacher's extra question d ≈ 0,71 mm. All agree.

The added explanations (kohdistaa, influenssi, homogeeninen, hylkivät, mitätön, polarisoituminen, kammiovärinä,
ajomassa, alaraja, marginaali …) are physically correct and keep the model conditions (point charges, wide plates,
disconnected vs. connected capacitor, only the electric force does work, phase-to-earth 12 kV).

## Blocking
None.

## Polish
1. unit.json `key_concepts`, *potentiaali*: "Kertoo varauksen potentiaalienergian yhtä varausyksikköä kohti, $E_\text{p} = qV$."
   The sentence defines V as energy per charge, but the formula shown is the energy. Clearer: "Potentiaali kertoo
   potentiaalienergian yhtä varausyksikköä kohti: $V = \tfrac{E_\text{p}}{q}$." (Not wrong, so not blocking.)
2. unit.json `key_concepts`, *sähkökenttä*: "Varauksen ympärillä oleva alue" is the usual school wording and agrees with
   FY6; optionally "alue, jossa toiseen varaukseen kohdistuu voima" to reuse the lesson's verb *kohdistua*.
