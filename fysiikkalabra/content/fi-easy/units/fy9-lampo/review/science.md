VERDICT: PASS
CONTENT-HASH: 75fc60790851a73b
SCOPE: full (fi-easy, since 689e602ef05c8a50): three new ```pysahdy boxes in unit.md judged first against fi; hero SVG to webp; inquiry explain model split into paragraphs; then unit texts and the Sovella task set.

## Blocking
(none)

## Polish
- s8 Yleisiä virheitä (a), solutions.md line 522: "lämpötilan muutokseksi otetaan 0 °C tai 16 °C". But 16 K is the right size of the change. The error meant is probably -16 °C or 0 °C used as ΔT. Carried from the last review; fi has the same line.

## Checked
- Pysähdy 1 (kahvikuppi): "Ei ole. Lämpö on energian siirtymistä lämpötilaeron takia ... vain siirtymisen aikana". This is the same physics as fi lines 13-17 and agrees with the Ydinajatus definition, the key_concepts "lämpö" and Yleisiä virheitä item 1. It has no "lämmöksi" wording.
- Pysähdy 2 (sulava jää): the energy raises the interaction energy, not the kinetic energy, so T stays the same. This matches fi lines 110-114 and the paragraph above it, which states the constant-pressure, pure-substance condition.
- Pysähdy 3 (jää + vesi): ice and water together means exactly 0 °C. This matches fi lines 197-201 and the comparison paragraph. The final state is equilibrium, and the pressure condition is stated earlier in the text (C, not a finding).
- The order of the boxes and their placement match fi. Each one follows the paragraph it checks.
- Hero: the webp (viewed) is the same scene as the aria-label and the Miksi question. It has no numbers or physics claims. fi uses the same file.
- Inquiry explain model: the split changes only the paragraphs; the text is the same. Recomputed: 334·0,050 = 16,7 ≈ 17 kJ, and 16,7 kJ/(4190·0,050) = 79,7 ≈ 80 K.
- Unit numbers: 2100·10 = 21 kJ; 334 kJ; 4190·100 = 419 kJ. The heating-curve breakpoints are 21, 355 and 774 kJ, plus 2260 kJ for boiling, which matches the aria-label. The formula conditions are stated (ΔU = Q + W with no change in Ek or Ep, Q = cmΔT with no phase change, expansion within about 100 K, P = UAΔT in a steady state).
- Task set (no change since the PASS at 689e602e): I recomputed every keyed answer in one script with my own formulas and numpy polyfit. s1 21,88 GJ, 17,37 h; s2 81,63 K, 1,667 kW, 35,8 %; s3 2,256 MJ/kg, 69,9 W from the read line (the least-squares fit gives 2,263 and 68,9, inside the tolerance); s5 370,8 and 333,0 kJ/kg; s6 31,48 K, 133,7 K, 40,2 %; s7 0,222 K/s, 900 J/(kg·K), 360 s; s8 2083 J/(kg·K), 333 kJ/kg, 270,2 kJ, 0,300 kg. All of them agree.
- The hash was 75fc60790851a73b at the start and at the end.
