VERDICT: PASS
CONTENT-HASH: fe26daef07ff0e1c

## Blocking

## Polish
- sim.js:296 — the label box width comes from `p.textWidth` of the TeX source (for example `$\textcolor{#93…}{Q_1}$`), not the typeset width, so the overlap assertions on `simState.labels` no longer measure what the student sees. This does not affect the physics. Measure the KaTeX box in the overlay, or have the overlap test read rendered boxes.
- lesson.md:6 — the prose has "matkan $s$", but figure 1 uses $\Delta s$. Write $\Delta s$ (carried).
- lesson.md:54 — the heat-engine arrows are energies per cycle ($Q_1$, $W$, $Q_2$), but the legend says "kuvaa tehoa". Say "energiaa (tai tehoa)" (carried).
- lesson.md:39 — "lämpötilaero … kuuman lähteen lämpötilaan nähden" holds only for absolute temperatures. Add "(kelvineinä)" (carried).
- solutions.md:22 — Vastaus is 37 %, but the key and the Sijoitus give 37,2 %. Give 37,2 % (carried; `\textsf{l}` vs `\text{l}` also still mixed).

## Checked
- Diff since the passed version (46aa00b): sim.js changes only the label and readout strings (plain text to `$…$`, `fi` to `tx`, `labSub` to one `lab`). `phaseAt`, `advance`, `geometry`, `areas`, the bars and `simState` are unchanged. `Math.round(eta)` gives the same value as `fi(eta,0)`.
- Test changes: both readout assertions (Q = 750 J gives ΔV = 1,50 l and ΔU = 450 J; cycle B gives Q₁ 650, Q₂ 550, W 100 J, η 15 %) still check the same numbers, now in TeX. `!t.includes('W_')` still keeps W_k out of the readout. The replaced Lisätietoja assertion checked text, not physics. Its content (ideal gas, model values) now sits in inquiry.json `model`. No physics check was lost.
- inquiry.json howto/model/calc: ΔU = (3/2)Δ(pV), ΔV = 2Q/(5p₁), Q = (5/2)p₁ΔV, W = (p₁ − p₂)ΔV = the raised weight's energy, and Q₁ − Q₂ = W are all correct and match the code. Every assumption from the old Lisätietoja box survives (frictionless, massless piston, vacuum above, plate and water temperatures, latch).
- I recomputed all 12 exercise answers independently. They match answers.py (171,7 → 172; 21,67 → 21,7; 12,04 → 12,0 are inside tolerance).
- Inquiry recomputed: kertaus 250 J; pred-1 300 J (Q = 750 J); exp-1 ΔV = 2,00 l, W_k = 400 J, ΔU = 600 J; exp-2 path A W = 0, Q₂ = 500 J; path B Q₁ 650, Q₂ 550, W 100, η 15 %; virhe 360 J; suunnittele 2000/1250/800 MW, pump 60 MW, 120 MW from wastewater; siirto 22,5 MW; check-2 450 J; exit 100 J and 18/42 kW. Every mistake value and its feedback is right.
- Experiments: exp-1 varies only Qin (paluu locked) and measures dV and dU, both in simState. Exp-2 locks Qin and p2, varies paluu, and measures Q1, Q2, W and eta (eta only when the cycle is done).
- Worked example 38 % / 310 MW and 88 % / 60 MW. Every solution is symbolic first.
- Figures to scale: arrow widths 60 = 24 + 36 (engine) and 20 + 40 = 60 (pump).
- Sim range: the largest bar is 1240 J, under the 1250 J scale. V₂ ≤ 3 l fits the axis. Captures show the KaTeX labels rendered (390 px, 1280 px).
- Scope: cycles are qualitative only, as the slot says. The sign convention is tied to fy3-5.
