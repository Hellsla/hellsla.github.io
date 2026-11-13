VERDICT: FAIL
CONTENT-HASH: 0d3e72c7832d3fcd
SCOPE: delta added-exercise from c716085d5bc703dc base 81db4a6fd727

## Blocking
- fy5-13/exercises/solutions.md (L1-09, Järkevyys) — **A** (wrong mechanism). The solution says: "Sävel nousee lähes kolminkertaiseksi … minkä vuoksi heliumia hengittänyt puhuu korkealla äänellä." The whistle's pitch does triple. The voice does not: the vocal folds' fundamental frequency barely changes, while the vocal tract's resonances (formants) rise, so the timbre changes. Also, a breathed mixture is not pure helium. Fix: keep the pipe statement and either delete the voice clause, or write "Heliumia hengittäneen ääni kuulostaa oudolta, koska ääniväylän resonanssitaajuudet nousevat; äänihuulten perustaajuus ei juuri muutu."
- fy5-13/exercises/exercises.json (L2-09) and solutions.md (L2-09, Vastaus) — **A** (significant figures against tolerance). The solution keeps 3 significant figures "kuten pituudessa 1,20 m", but the limiting datum is v = 75 m/s, which has 2. A student who rounds correctly answers 1,3·10² Hz. That is 4 % from 125 Hz and is rejected at tolerance 0,02. Fix: give the speed as 75,0 m/s in the task, or make the answer 130 Hz with 2 significant figures and a justification from 75 m/s.

## Polish
- fy5-13/exercises (L2-09 vs L2-04) — L2-09 is L2-04 inverted on the same figure: the same reading (L = 1,20 m, n = 4) and the same λ = 0,60 m, with f asked instead of v. It does not give L2-04's answer away (75 m/s ≠ 60 m/s), but it adds little. Consider asking something the figure offers that L2-04 does not, for example the frequency of the next mode, or the mass change needed for three loops.

## Checked
- MAFY values: helium 971 m/s and air (0 °C) 331,5 m/s are the VERIFIED rows fy5-13 in docs/mafy-arvot.tsv. The hint names only the section and the table.
- L1-09: f₁ = v/(2L) for a pipe open at both ends. Δf = (971 − 331,5)/1,00 m = 639,5 Hz (recomputed). Tolerance 4 % with 2 significant figures (640 Hz) is fine, and both gases are at 0 °C as stated.
- L2-09: figures.py draws sin(4πu), so there are 4 loops and 5 nodes. The ruler runs 0–1,20 m with ticks every 0,10 m. λ = 0,60 m and f = nv/(2L) = 125 Hz (recomputed). The alt text matches the drawing.
- answers.py agrees with exercises.json for both added tasks.
- The hash was the same at the start and at the end.
