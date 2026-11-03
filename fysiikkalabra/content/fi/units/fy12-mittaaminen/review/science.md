VERDICT: PASS
CONTENT-HASH: 9a4783083d3a7ff6

Science review of `fy12-mittaaminen`, round 2. The hash was the same at the start and at the end. I recomputed
every number again in one numpy script with my own formulas, least-squares fits and extreme-line search, and did not
use answers.py. Every published value agrees within its rounding. Tutki: fit 0,276 kPa/°C and 75,1 kPa, θ₀ = −272 °C.
kolikot: 2,70 %. jousi-suora: 79,0 N/m and L₀ = 0,135 m. kuula: 1,24 m/s². kattila: 10,0 min. Tarkista 2: 28 kg/m³.
s1: 7,29 ± 0,12 m/s. s2: 102 ± 2 µm, 79,8 g/m² and 783 kg/m³. s3: 0,918/0,919 g/cm³, 118,6 g, Δρ 0,012 g/cm³ and
1,38 kg. s4: k 1,0205 and 750 g. s5: 0,477 ± 0,014 m/s, with 0,634 m/s through the origin. s6: pV rises
monotonically by 8,1 %, V₀ 1,77 ml, C 2,603 J, n 1,06·10⁻³ mol, and p(V+V₀) = 2595–2608 kPa·ml. In the browser:
0 `.katex-error`, no raw `$` and no console errors.

## Blocking
None. The round 1 Blocking finding is fixed. In the browser, `kolikot` 0,27 now gets the "Δd divided by the stack
height" feedback, which is correct (0,05 : 18,5 = 0,27 %), and 0,027 gets the new "decimal, multiply by 100 %"
feedback. 2,7 and 3 are accepted.

## Polish
1. **A (rounding justification).** `sovella/solutions.md` s1 a) Vastaus says "nopeudessakin vasta sadasosat metriä
   sekunnissa ovat epävarmoja" and that b's 0,12 m/s "vahvistaa tämän". A 1,4 % time spread gives about 0,1 m/s, so
   the tenths are already uncertain. Three figures are kept because the uncertainty starts with 1. **Fix:** "aika
   tunnetaan noin $0{,}2\,\text{s}$:n eli noin prosentin tarkkuudella, joten nopeuden epävarmuus on noin
   $0{,}1\,\text{m/s}$; koska sen ensimmäinen numero on 1, nopeuteen jätetään kaksi desimaalia (b-kohta
   vahvistaa: $0{,}12\,\text{m/s}$)."
2. **Consistency.** `inquiry.json` › `jousi-suora`: the feedback for mistake 48.6 (17,0 N : 0,350 m) says "yhden
   pisteen". **Fix:** "toisen pisteen", which matches the 8 (first point) feedback.

## Checked, no finding
- **Changed items.** `lahto-4` (candle): the intercept is the length at t = 0 and the slope is −0,80 cm/h. Every
  distractor's feedback is right, including that forcing the line through the origin would claim a zero-length
  candle. `jousi-suora`: Hooke's law with total length, F = kL − kL₀. The slope is k and the ratio F : L is not.
  The 0,79, 48,6 and 8 mistakes are distinct from the 2 % tolerance. Hooke's law is FY4/FY5 content, within scope.
  `aika-kuvaaja`: t = s·(1/v) with slope s = 2,0 m, exactly one correct option, and every distractor's feedback is
  right.
- **Round 1 Polish.** s6 a) criterion, Periaate and Yleisiä virheitä now argue steady one-way growth, and pV does rise
  on every row. tarkista-2 says "lähes puolivälissä, kuten yleensä". The s3_fit description says eight points. The s3
  a) prompt now asks for a graph that gives the intercept. kattila and anatomia use θ for °C.
- **Guardrails.** The uncertainty is half the range. Outliers are rejected only for a stated reason. Extrapolation
  limits are given in Tutki, Ennusta 6, s3 e) and kattila. Overlapping intervals are not taken as proof of equality.
  Ideal gas uses T in kelvins.
- **Rubrics.** The 89 points add up, and every criterion asks only what its part asks.
