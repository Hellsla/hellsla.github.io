VERDICT: FAIL
CONTENT-HASH: 18cb6ea9366ee3fa

## Blocking
- inquiry.json:321 (laske-r solution, Vastaus) — gives 8,30 with three figures and says n = 0,2075 mol has four. That n comes from m = 0,83 g, which has two figures, and line 101 keeps four digits only as an intermediate. The answer `8.3` and lesson.md:238 (≈ 8,3) agree on two figures. — Write "8,3 J/(mol·K), kaksi merkitsevää numeroa; rajoittaa heliumin massa 0,83 g".
- inquiry.json:421 (siirto, Sijoitus) — shows "= 2645 kg" and then rounds it to 2,64·10³ kg, a wrong rounding step: 2645 rounds to 2650. The true value is 91 200 · 0,0290 = 2644,8 kg. — Write 2644,8 kg.

## Polish
- inquiry.json:480 (check-2, Periaate) — "pV = NkT" uses a k the lesson never defines. — Write "p = nRT/V ja n ∝ N, joten p ∝ NT/V".
- solutions.md:118 (L3-03) — says M = 29 g/mol does not limit the answer. It has two figures, as Δp does, so it limits equally.
- solutions.md:119 (L3-03, Järkevyys) — the "30 % ylipaineesta … koska ilmanpaine ei vuoda" reasoning is muddled. The leaked share is 3,0/11,0 = 27 %, and the check assumes an atmospheric pressure of 1,0 bar without saying so.
- solutions.md:79 (L2-03) — "lämpötila nousee, kun kaasua puristetaan" is true only for this data, not for every compression.

## Checked
- One script recomputed all 12 answers independently and against answers.py. All agree, and every rounded answer is inside its tolerance.
- Inquiry numbers all match: m/M 0,2064–0,2076 (masses within ±0,02 g of n = 0,2072), R = 8,30 and 8,32, every mistake value, virhe 1,2 and 0,083 mol, siirto, check-2 3,0, exp-2 50, the pV/(NT) column, and the exit ticket 0,601 mol.
- Worked example: 0,2073 mol and 0,83 g. Two figures follows from 5,0 l and 4,0 g/mol, and the 24 l/mol check is independent.
- Every exercise solution states a principle that applies, solves in symbols first, and converts units correctly. Its reasonableness check uses an independent value.
- The rounding rule for differences is applied correctly: 10,0 − 7,0 bar and 40 − 29 g/mol each have two figures.
- Magnitudes are realistic: ball 57 kPa gauge pressure, oxygen cylinder 180 bar, diesel engine 555 °C, argon gap 11 mm.
- Figures: speed ratio 2,7 (√(29/4) = 2,69), √2 arrows in the 2T panel, V/2 piston, particle counts, molar-mass bars in proportion to M.
- sim.js: impulse per perimeter per time gives NkT/A exactly. The speeds scale as √T, a volume change keeps the speeds (stated), and there are no particle–particle collisions (stated).
- The experiments lock T and V and vary N. The check-2 and table states can be reached on the sliders.
- Every correct option and every feedback is physically right.
