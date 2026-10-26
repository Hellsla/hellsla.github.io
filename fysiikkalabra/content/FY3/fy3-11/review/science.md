VERDICT: PASS
CONTENT-HASH: 35c7e28697874a1d

## Blocking

## Polish
- lesson.md:6 — the derivation says the piston moves "matkan $s$", but figure 1 and its formula use $\Delta s$ — write $\Delta s$ in the prose too (carried from round 1).
- lesson.md:54 (heat-engine figure) — the arrows are labelled $Q_1$, $W$, $Q_2$ (energies per cycle), but the legend says "nuolen leveys kuvaa tehoa" — say "energiaa (tai tehoa)", or relabel (carried).
- lesson.md:39 — "lämpötilaero kuuman lähteen lämpötilaan nähden" holds only for absolute temperatures — add "(kelvineinä)" (carried).
- solutions.md:22 — Vastaus $37\,\%$, while the key and the Sijoitus line give 37,2 % — give 37,2 % (carried).
- solutions.md:10, 90 (and L2-03) — the litre is `\textsf{l}`, but inquiry and lesson use `\text{l}` — use one style (carried).

## Checked
- The diff since the passed version (d1ddfcf, commit 0bbacb9) touches only exercises.json L2-01 and nine strings in inquiry.json. Every change wraps $(V, p)$, $(s, F)$, $V$-akseli or $1\,\text{TJ} = 10^{12}\,\text{J}$ in maths. No number, formula, option, `correct` flag or meaning changed.
- Experiment names and headers as rendered by `tex_name`: lämpö $Q$, paine $p_2$, männän paluu (plain), $\Delta V$ (l), $\Delta U$ (J), $Q_1$ (J), $Q_2$ (J), $W$ (J), $\eta$ (%). Every symbol and unit is the same as before, and no Finnish word was turned into maths. The exp-2 capture shows them as typeset.
- I recomputed all 12 exercise answers independently. They match answers.py and exercises.json: 12,0 kJ; 172 J; 37,2 %; 170 kJ; 21,7 %; 41,0 %; 9,0 %; 500 J; 720 kW; 120 MW; 9,6 MWh; 12,0 kW.
- Inquiry numbers are unchanged and recomputed: exp-1 at Q = 1000 J gives ΔV = 2,00 l, W_k = 400 J and ΔU = 600 J. In pred-1, Q = 750 J gives 1,0 → 2,5 l and 300 J. Exp-2 path B gives W = 100 J and η ≈ 15 %. Check-2 gives 450 J. The exit ticket gives 100 J, 18 kW and 42 kW.
- The exp-2 setup still isolates `paluu`: Qin and p2 are locked.
- lesson.md, solutions.md, answers.py, sim.js, figures and exit-ticket.json have not changed since the round-1 full review. The judgements in that review still stand: the formulas and their conditions, the sign convention tied to fy3-5, the to-scale figures, the sim's model and its stated limits, and the scope.
