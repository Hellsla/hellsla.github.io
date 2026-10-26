VERDICT: FAIL
CONTENT-HASH: fa37d70a3cebe951

## Blocking
- lesson.md:131-135, 210 (also figure 4 label $P_\text{h}$, solutions.md fy3-15-L2-04) — $P_\text{h}$ is defined at line 84 as the total waste power $P_0 - P_\text{hyöty}$ (flue gas + steam cycle + generator losses). It is then reused for the condenser heat alone, $P_\text{h} = c\,q_m\,\Delta T$. The lesson's own numbers show these differ: in the worked example $P_\text{h} = 372\,\text{MW}$, but the condenser takes 306 MW. A student can wrongly set $c\,q_m\,\Delta T = P_0 - P_\text{s}$. — Give the condenser heat its own symbol (e.g. $P_\text{l}$, "lauhduttimen lämpöteho"). Say it is the largest part of the waste heat, not all of it. Update figure 4, the summary line and the L2-04 solution to match.
- solutions.md (all 12 solutions) — Kaava/Sijoitus/Vastaus are in plain Unicode text (`η = 0,920 · 0,980 = 0,9016`), not LaTeX. This breaks the teacher's standing rule that calculations in solutions are in LaTeX. — Rewrite every formula, substitution and result as `$…$` / display LaTeX, with units in `\text{}` and thin spaces, as the worked example does.

## Polish
- lesson.md:31 — "edellisessä luvussa Kaasun tekemä työ ja lämpövoimakone" — that chapter is the prerequisite, not the previous lesson (this is lesson 15) — write "luvussa Kaasun tekemä työ ja lämpövoimakone".
- lesson.md:111,113,115 — figure 3 has three invisible leftover `<path … stroke="none"/>` elements — remove them.
- lesson.md:197 (Esimerkki, Järkevyys) — uses $P_2 = 240\,\text{MW}$, which no stage computes — add $P_1 = 546\,\text{MW}$ and $P_2 = 240\,\text{MW}$ in the Sijoitus stage.
- inquiry.json:323 — typo "polttoatehosta" → "polttoainetehosta".
- solutions.md fy3-15-L2-03 — the substitution goes through the rounded $P_0 = 416{,}7\,\text{MW}$; substitute straight into $m = P_\text{s}t/(\eta H)$ so the solution stays symbolic-first.

## Checked
- All 12 answers recomputed independently; they match answers.py and exercises.json, and tolerances cover rounding to the data's significant figures.
- Worked example: 228 MW, 0,380, 372 MW; losses 54 / 306 / 12 MW add up to 372 MW.
- Figure 1 Sankey checked to scale (40 px per 100 MW): 40 + 248 + 12 + 200 = 500 MW, and every band width is right.
- Figure 2 checked to scale: 160 → 120 MW electricity, 352 MW useful at $P_\text{k} = 232\,\text{MW}$, waste 240 → 48 MW.
- Figure 3 bar heights (500/460/212/200 MW) and loss boxes checked to scale. All figure labels are LaTeX `foreignObject`s and read well at 390 px.
- Inquiry: Q₂ = 520 MJ, chain 200 MW, CHP 130 MW, retrofit 8,64 MW, error spotting 342 MW, check-2 216 MW. All mistake values reproduce the stated wrong method, and every correct option is right.
- Pred-2 physics: a higher condensing temperature means less turbine work. A loss of 0,17 MW electricity per MW of district heat is a realistic figure.
- Typical efficiencies (condensing 38–42 %, CHP 85–90 %, hydro 90 %, wind 40–45 %, PV 20 %) are realistic, and the lesson says their denominators differ.
- Scope: power, efficiency, energy conservation and $Q = cm\Delta T$ are FY3 content; there are no FY4 formulas. The heat pump's COP (lämpökerroin) is treated in fy3-11/12.
- No lesson ids appear in visible student text (ids appear only in HTML attributes).
