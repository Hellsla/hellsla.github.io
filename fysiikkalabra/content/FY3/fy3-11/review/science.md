VERDICT: PASS
CONTENT-HASH: d1ddfcf862eff861

## Blocking

## Polish
- lesson.md:6 — the derivation says the piston moves "matkan $s$", but figure 1 and its formula use $\Delta s$ — write $\Delta s$ in the prose too.
- lesson.md:54 (heat-engine figure) — the arrows are labelled $Q_1$, $W$, $Q_2$ (energies per cycle), but the legend says "nuolen leveys kuvaa tehoa" — say "energiaa (tai tehoa)", or relabel.
- lesson.md:39 — "lämpötilaero kuuman lähteen lämpötilaan nähden" is right only for absolute temperatures — add "(kelvineinä)".
- solutions.md:22 — Vastaus $37\,\%$, while the answer key and the Sijoitus line give 37,2 % — give 37,2 % (it is within tolerance, but it is inconsistent).
- solutions.md (L1-02, L2-03, L3-03) — the litre is typeset as `\textsf{l}`, while inquiry and lesson use `\text{l}` — use one style.

## Checked
- All 12 exercise answers were recomputed independently and match answers.py and exercises.json. L1-02: 1 g of steam at 373 K and 101 kPa is 1,705 l, so the 1,70 l in the task is right. L2-03: 700 J = (7/2)pΔV for diatomic air, so the data are consistent.
- Worked example: 38 %, 310 MW, 88 %, 60 MW. It is symbolic before substitution, and its reasoning about lowering the condensing temperature in CHP is correct.
- Exp-1: model ΔV = 2Q/(5p₁). Q = 1000 J gives ΔV = 2,00 l, W_k = 400 J and ΔU = 600 J. The mistakes 400 000, 600 and 1000 are right. The pred-1 options and feedback (300 J, which needs Q = 750 J) are right.
- Exp-2 (Q = 500 J, p₂ = 100 kPa): A gives W = 0 and Q₂ = 500 J. B gives Q₁ = 650 J, Q₂ = 550 J, W = 100 J = (p₁ − p₂)ΔV, η = 15 %. The cycle closes (ΣΔU = 0). Varying only `paluu` with Qin and p2 locked isolates the variable, and simState carries Q1, Q2, W, eta, dV and dU.
- sim.js phaseAt: the heat and work in each phase match a monatomic ideal gas, and Q₁ − Q₂ = W. The limits (frictionless piston, monatomic gas, no losses) are stated in Lisätietoja and in the sim activity's text.
- Kertaus (250 J), virhe (360 J), siirto (22,5 MW; mistakes 31,5 and 2,57), check-2 (450 J; mistakes 450 000 and 750) and the exit ticket (100 J, 18 kW, 42 kW) are right.
- Suunnittele: P = (P_l + 3P_e)/1,75 = 800 MW; pump 60 MW, 180 MW of heat, 120 MW from the wastewater. Options 1 and 2 are 2000 MW and 1250 MW. The 941 and 667 distractors are right.
- Figures: the heat-engine arrow widths are 60/24/36 (η = 40 %) and the heat-pump widths are 20/40/60 (ε = 3). Both are to scale as stated. The (V, p) and piston figures are correct.
- Sign convention: ΔU = Q − W_k is tied explicitly to fy3-5's ΔU = Q + W with W = −W_k.
- Scope: cycles are only shown qualitatively, as the slot's note allows. Efficiencies (lauhde about 40 %, nuclear about 35 %, CHP 85–90 %, OL3 4300/1600 MW) are realistic.
