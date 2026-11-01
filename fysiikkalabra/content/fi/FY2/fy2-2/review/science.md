VERDICT: PASS
CONTENT-HASH: f2b127d4e8340cd8

## Blocking

## Polish
- inquiry.json ennuste-1 / koe-1: ruoan 10 MJ on ravintoarvo (elimistön hyödynnettävä energia), bensiinin 32 MJ lämpöarvo; yksi lause erosta koe-1:n intron sopisi guardrailin "Food and fuel" kanssa.
- inquiry.json siirto solution: "kaikki tiedot tunnetaan gigajoulen tarkkuudella" on oletus ($9\,\text{GJ}$ on yksinumeroinen); sano "oletetaan".
- lesson.md:466: tasaisella ajolla liike-energiaa muuttuu jatkuvasti lämmöksi ilmanvastuksessa ja vierimisessä, ei vain pysähtyessä; "ajaessa ja pysähtyessä" riittäisi.
- lesson.md:99 hero: kuvassa leipä, tekstissä kaurapuuro; sama ketju, yhtenäisyys olisi parempi.
- sim.js `byName`: an unknown value silently falls back to the photon (OBJ[0]).

## Checked
- Sim change: option value = FI name, label = page-language name, `byName` and `reset` use FI; physics (OBJ table, lg, powTex, prefTex, E_MJ, E_EJ) unchanged. Initial "päivän ruoka" and "Aurinko Maahan tunnissa" match FI.ruoka and FI.aurinko_h exactly; simState gives E_MJ 10 / 32 (koe-1) and E_EJ 620 / 620 (koe-2). The `values` maps are identity in fi, no physics.
- Test diff: one assertion added, none removed or loosened; test_sims PASS (fi, en, fi-easy, 42 assertions), test_inquiry 67/0.
- Recomputed in one script: 340 kJ, 32:10 = 3,2, Sun 1361 W/m² · πR² · 3600 s = 625 EJ vs 620 EJ (2023), 1000 a → ≈ 41 vrk, 600 kJ, 66 MJ (= 60 + 2 + 4), 51 GJ, 100 ruokaa, 2200:300 ≈ 7,3 and the 7333 distractor, exit ticket 9 kJ.
- Magnitudes: omena 0,1 kg · 9,81 · 1 m ≈ 0,98 J; OL3 1,6 GW · 1 vrk ≈ 138 TJ; tankki 50 l · 32 MJ/l = 1,6 GJ; 550 nm fotoni 3,6 · 10⁻¹⁹ J; M 9 ≈ 10^18,3 J; Suomen sähkö 2,9 · 10¹⁷ J/365 ≈ 7,9 · 10¹⁴ J; muscle 110/450 ≈ 24 %, plausible.
- Tikapuut figure to scale: 10 MJ at x 328, 1,6 GJ at 401, 140 TJ at 565 match a 33,2 px/decade axis.
- Säilyminen figure: 800 = 200 + 600, widths proportional (96 px = 24 + 72).
- Predictions and checks: exactly one correct option each; every distractor wrong and its feedback names the right reason (kilo ≠ sata, units before ratio, energy not lost).
- Experiments vary only `kohde`; nothing else to control in a lookup sim; values labelled model values / rounded orders of magnitude, estimates marked.
- Scope: no E_k/E_p, W = Fs, Q = cmΔT or chain efficiency product; conservation and prefixes only, FY2 central contents.
- Definitions consistent with fy2-1 and guardrails: heat leaves "lämpönä", lämpöenergia "ei enää helposti" usable.
