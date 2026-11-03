VERDICT: PASS
CONTENT-HASH: e198735ef8b8ce03

Round 2 review. Every changed item was checked in full: Tutki, `ennusta-leikkaus`, `linearisointi`, `kulmakerroin-g`, `jaksonaika`, `mittausmatka`, `nollapiste` mistakes, `check-2`, `check-3`, s1 a/b, s2 a/d, s4 a, s5 d and s6 d. Unchanged items keep their round 1 pass.

## Round 1 Blocking
- s5 d) is fixed. The overflow can is no longer given the scale's resolution as its uncertainty. The solution and rubric now name about $0{,}5\,\text{cm}^3$ from water left in the spout and on the walls.

## Blocking
(none)

## Polish
1. **Tutki readings are too precise for the instrument.** `inquiry.json` `aineisto`: the readings are taken from a ruler next to the spring but written to $0{,}01\,\text{cm}$ ($2{,}99$, $10{,}79$), while the zero reading is $1{,}0\,\text{cm}$. A mm-scale ruler cannot give that precision. Write the readings to $0{,}1\,\text{cm}$ ($3{,}0$; $4{,}9$; $6{,}9$; $6{,}9$; $10{,}8$), or say the readings come from a scale with a vernier. The row values $k$ stay almost the same (16,4 … 22,7).
2. **Axis order differs from the linked chapter.** `aineisto` model answer and criterion 5: the answer says "$(F, x)$-kuvaaja … kulmakerroin on $\tfrac{1}{k}$". This is right for the unit's own (horizontal, vertical) convention. But *Jousivakion määrittäminen*, the chapter that Kertaa tarvittaessa links to, plots $F$ on the vertical axis, so its slope is $k$. Either add "tai $(x, F)$-kuvaaja, jonka kulmakerroin on $k$" to the model answer and criterion, or switch to $(x, F)$.
3. **One line in the `kulmakerroin-g` solution can be tied to the theory.** The solution explains the intercept $0{,}04\,\text{s}^2$ as the spring's own mass, which is right ($m_\text{eff} \approx 25\,\text{g}$). One more clause would link it to the theory section: "sama lisämassa jokaisessa pisteessä siirtää suoraa".

## Checked
One Python script recomputed every number with my own formulas, and everything agrees.
- **Tutki:**
  - $F$ per row and row $k$ = 16,4 / 20,0 / 21,3 / 28,6 / 22,7, mean 21,8.
  - A spring with $k = 25\,\text{N/m}$ gives true extensions of 1,96 … 9,81 cm. With the $+1{,}0\,\text{cm}$ offset these reproduce the table, so 8,85 → 6,85 is a believable misread.
  - Fit of $x(F)$ without row 4: $k = 25{,}1\,\text{N/m}$, intercept $1{,}02\,\text{cm}$.
  - Corrected rows: 24,6–25,2.
- **Sovella:**
  - cart: sum 28,40, mean 5,68, $\Delta t$ 0,13, $\varepsilon$ 2,29 % (mistakes 4,58 / 0,13 / 0,0229);
  - spring $(m, T^2)$: slope 1,6, $k$ 24,67 (mistake $1/k$ = 0,0405), $T(0{,}50\,\text{kg})$ = 0,894 s;
  - $\theta_0$ = −275,1 °C (−295,1 / −355,1 are $-p_1/k$ and $-p_2/k$, as the new feedback says);
  - walking: 10 s, 14 m (0,14 / 0,28 / 9,3 %);
  - `valine` 2 / 100 / 5 / 10 %.
- **check-2:** $\rho$ 7,94, $\rho_\text{max}$ 8,18, $\rho_\text{min}$ 7,70, $\Delta\rho$ 0,238 (mistakes 0,079 and 0,476). check-1: 1,7 g.
- **Long tasks:**
  - s2: 160 s;
  - s3: 9,695 ± 0,872;
  - s4: fit 4,020 / 0,1035, $g$ 9,82, drawn-line readings 4,013 → 9,839, $d$ 4,98 cm, row $g$ 8,87–9,60, ±0,1 slope gives 9,6–10,1;
  - s5: 2677 ± 78, 0,05 % / 2,9 %;
  - s6: origin fit 0,1205 → 4,15, $\mu_0$ 0,425, 1,1025, 3,78, 0,385.

Every tolerance accepts the rounded answer and rejects the listed mistakes. Each choice item has exactly one correct option, and every distractor's feedback is right. This includes the new `ennusta-leikkaus` (beaker mass = offset, slope = density) and `linearisointi` ($T \propto \sqrt{m}$, $m \propto T^2$, $\sqrt{T} \propto m^{1/4}$).

Round 1 polish is all applied:
- "todennäköisesti todellinen";
- "b poikkeaa selvästi nollasta";
- resoluutio/epävarmuus in `valine`;
- sisäenergia → lämpö in s2 a;
- s2 d alternatives;
- s6 d precision;
- "resoluutio 0,1°".

Law conditions are stated where the laws are used: small angle, rigid flask and thin gas, no change of state, start from rest, no air resistance, constant speed for $s = vt$. The physics stays inside FY1–FY5.

Build and Playwright at 390 and 1280: no page errors, no `.katex-error`, 31 details opened. The hash was the same at the start and the end.
