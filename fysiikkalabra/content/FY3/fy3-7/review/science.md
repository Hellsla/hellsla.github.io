VERDICT: FAIL
CONTENT-HASH: a6d789c47096713f

## Blocking
- inquiry.json:316 (check-2) — the data are physically impossible. With all 1500 W going into the water, the 4,0 min before the plateau give 360 kJ. That would warm the 0,597 kg that later boils away by 144 K, which liquid water cannot do. The mistake feedback at line 628 ("ensimmäiset 4,0 minuuttia vesi vasta lämpeni") states this impossible warm-up outright. — Move the plateau to 2,0–17,0 min: the duration stays 15,0 min and the answer stays 0,597 kg, and the warm-up becomes 180 kJ ≈ 72 K, starting from about 28 °C. Update hint 3 to match (line 323), and change the whole-time mistake value to 1500·1020/2,26e6 ≈ 0,677 with its feedback (17,0 min).

## Polish
- solutions.md:87 — "Muutama kauhallinen jäähdyttää kiviä kymmeniä kelvinejä": under the task's assumption one ladle alone already gives 27 K, so a few ladles would give about 80 K or more. Say that the real stove keeps heating the stones.
- solutions.md L1-03 — 45 kg/m² is about 5 cm of ice in one night, which is generous for a first frost night. 2–3 cm (about 25 kg/m²) would be more typical.

## Checked
- All 12 answers recomputed independently in one script. They match answers.py exactly and round within the 2 % tolerance.
- Worked example: r = Pt/Δm = 2,34 MJ/kg, solved symbolically first. The loss explanation is correct, with implied losses of about 36 W.
- Lesson numbers check out: r/s ≈ 6,8; r vs. heating 0→100 °C ≈ 5,4; melting ≈ heating 0→80 °C.
- Heating-curve SVG: plateau and segment lengths are proportional to s : cΔT : r (6,4 kJ/px throughout). Ice and steam slopes are about 2× the water slope, as the text says.
- sim.js: the stage energies, stateAt, the plateau lengths sm/P and rm/P, and the ice and water fractions are all correct. simState exposes tMelt and tBoil. The screenshot curve matches 167 s / 1130 s.
- exp-1 and exp-2: the locked and varied parameters isolate P and m. The values 0,25 kg and 2000 W can be reached on the slider steps. The feedback numbers (83,5 / 565 / 167 / 1130 s, ratio 6,8) match the model.
- pred-3 options and feedback are correct, including that the model has no losses or delay.
- pr-lampo, virhe, siirto (188 W) and the mistakes 27,8 W and 11 300 W are correct.
- check-3 model answer: 2260 + 264 J against 264 J, a ratio of about 9,6, correct.
- Exit ticket, glossary use and the pressure dependence of the boiling point are correct and in scope.
