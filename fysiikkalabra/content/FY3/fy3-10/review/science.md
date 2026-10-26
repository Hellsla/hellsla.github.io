VERDICT: PASS
CONTENT-HASH: e56ebee5dbb1da71

## Blocking

## Polish
- lesson.md:366 — the piston changes V without doing work on the gas, so the temperature stays the same by construction. The sim's Lisätietoja says this, but the lesson paragraph does not — add "tilavuuden muutos ei muuta hiukkasten nopeuksia eli lämpötilaa" where the simulation is introduced.
- solutions.md:23 — "18 g, mikä on tavallisen patruunan koko": adult automatic life jackets mostly use 33 g cartridges — say "pienen patruunan koko" or drop the claim.
- sim.js:96 — right after "Aseta alkutila" the readout shows a one-step value (for example 1,43 with "keskiarvo 0,0 s:n ajalta"), as in the capture exp-1-390-1. The intro says to wait about 2 s, so nothing is wrong, but you could show "–" until tAvg ≥ 0,5 s.

## Checked
- Round-2 conversion: every number token in lesson.md, inquiry.json, exercises.json, exit-ticket.json and solutions.md is the same before the figure pass (ae4cffa) and now, once LaTeX `{,}`, `\,` and superscripts are normalised. The only changes are symbols wrapped as $…$, units written as \tfrac and powers written as 10^n. No formula or meaning changed, and the minus sign of −30 °C is kept.
- I recomputed all 12 exercise answers independently. They match answers.py and exercises.json (L1-05 9,659 → 9,7; L3-02 10,96 → 11; L2-03 555,3 °C).
- Inquiry: m/M is 0,2075 / 0,2064 / 0,2076 / 0,2068 and their mean 0,2071 gives R 8,32 (lesson "≈ 8,3"). laske-r is 8,302, with mistakes 121,7 / 8302 / 0,0083. siirto: n = 91 200 mol, 2645 kg, mistakes 9869 and 2,64, outside air 3,37 t. virhe: 1,22 → 0,083 mol. check-2 3,00 (2,25, 1,69). exp-2 N = 50. kertaus 200 kPa. Table column pV/(NT): 1,05 / 1,00 / 0,98 / 0,98 / 0,99.
- Worked example: n = 0,2073 mol, m = 0,83 g, air 6,0 g, molar volume 24,1 l; solved symbolically first. Exit ticket 0,601 mol; the other two exit answers are correct.
- Solutions' side claims are correct: 0,32 kg; 57 kPa gauge; O₂ 1,32 g and CO₂ 1,81 g; 2,7× ratio; 23,9 l and 17 %; 2,7·10²¹ O₂; 22 g / 16 g; 24,8 mol and initial 2,6 kg.
- Figures: helium-ilma has 12 + 12 particles and an arrow ratio of 32 : 12 = 2,67 ≈ √(29/4); mole-masses bars are 14 : 101,5 : 154 = 4 : 29 : 44 with 8 particles each; paine-ja-tekijat has 6/12/6/6 particles, 2T arrows 1,40× ≈ √2 longer, and the V/2 column is half the height. The labels match the text.
- Experiment captures: the table headers render $N$ and $p/p_\text{ref}$ correctly. exp-1 and exp-2 lock T and V and vary only N.
- sim.js is unchanged in physics. Impulse per perimeter gives p = NkT/A, and P_REF comes from the same model.
- Scope is within FY3 "ideaalikaasun tilanyhtälö".
- Hash e56ebee5dbb1da71 at start and end.
