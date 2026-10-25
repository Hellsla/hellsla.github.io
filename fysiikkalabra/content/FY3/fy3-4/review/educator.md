VERDICT: PASS
CONTENT-HASH: e640982b5aa42904

## Blocking
(none)

## Polish
- exercises.json:72 (L2-04) — still the second half of the worked example (overpressure × area with a cm² conversion, lesson.md:53) with new numbers, plus bar and kN conversions: one rearrangement and three conversions, more than level 2 allows. This was not acted on in round 1; I keep it as polish because each step is shown in the lesson. — Make the student form the overpressure, e.g. "Mittari näyttää kattilan sisällä 186 kPa, ulkona ilmanpaine on 101 kPa. Kannen pinta-ala on 0,0380 m². Kuinka suuren voiman paine-ero kohdistaa kanteen?" (answer 3,2 kN, keep kN), and drop the bar.
- lesson.md:8 — "Se ei riipu astian muodosta eikä veden kokonaismäärästä" comes right after a derivation that needs a straight water column above the surface, so the claim does not yet follow from it. The reason only arrives in line 10 (otherwise the water would flow sideways), and the two are never connected. L3-02 and exit-ticket Q3 depend on this idea. — Add at the end of line 10: "Samasta syystä paine on sama kaikissa pisteissä, jotka ovat samalla syvyydellä, joten astian muoto tai veden määrä sivuilla ei muuta sitä."
- lesson.md:47 — "kun huoneessa on ilmaa normaalipaineessa": the lesson never defines "normaalipaine" (fy3-3:10 only uses it in passing), yet line 53 relies on the room pressure being exactly the surface air pressure. — Write "kun huoneen ilmanpaine on sama 101 kPa kuin veden pinnalla".

## Checked
- lint_lesson.py fy3-4: 0 errors, 0 warnings. Hash unchanged from start to finish.
- Round-1 fixes read as a student would read them. The dam hook is answered (lesson.md:14). The ρgh derivation now names V = Ah, m = ρV and G = mg (line 8). The sideways-pressure reason is given (line 10). Δp is named (line 27).
- Worked example (lines 49–53): rounds only at the end, explains why only the overpressure acts on the window, and explains why the diver is not crushed. Nothing it uses comes before its prerequisites.
- Prerequisites cover everything used: G = mg (fy3-1), Pa/kPa and the gas micro-model (fy3-3:6), density from FY1, restated in line 8.
- The linear-model link (h, p) ↔ y = kx + b (line 27) matches the skill goal in curriculum.json.
- Level 1: five single-formula tasks. L2-01–L2-03 each have one rearrangement or conversion.
- Level 3: G = mg with p = F/A, Pascal's barrel with a distractor, two liquid layers. All three combine ideas.
- answers.py output matches all 12 answers. The significant figures follow the data.
- The exit ticket tests force versus pressure, p₀ + ρgh, and independence from vessel shape. These are the core ideas, not details.
- All six meta glossary terms, including "ylipaine" and "tiheys", exist in glossary.json.
