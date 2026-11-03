VERDICT: PASS
CONTENT-HASH: 049f2a19955600af

## Blocking

## Polish
- lesson.md:151 and lesson.md:259 — "Jos levossa olevaan kappaleeseen vaikuttava kokonaismomentti ei ole nolla, kappale alkaa kiertyä" right after "saman valitun kiertoakselin": for a free body a nonzero moment about an arbitrarily chosen point does not by itself start rotation (B-leaning, harmless in this chapter's fixed-axis context, but fy5-2 lets students choose the axis) — say "akselin ympäri kiertyvään kappaleeseen" or "kiinteän akselin ympäri", at least in the Tiivistelmä bullet.
- inquiry.json:321 (virhe, cos distractor feedback) — "Kosini antaa varren suuntaisen osan" is said of the length $d\cos 30^\circ$, which is the distance along the line of action, not a handle-parallel part; only $F\cos\alpha$ is a handle-parallel force component — reword, e.g. "$Fd\cos\alpha$ vastaisi voiman varren suuntaista komponenttia, joka ei kierrä mutteria".
- inquiry.json:276 (johtopäätös model) — "Kuvaajassa kaikki yritykset jakautuvat samalla rajalla": exp-1 (tight, 30 Nm) and exp-2 (rusty, 60 Nm) have different limits and the chart is cleared between them — "saman mutterin yritykset".
- inquiry.json:420 (check-2 Järkevyys) — "pyörä alkaa kääntyä vastapäivään" ignores the steering mechanism's resisting moment — "käsien voimat kiertävät pyörää vastapäivään".

## Checked
- Definitions of momentti, voiman varsi (perpendicular distance to the line of action), vaikutussuora, kiertoakseli agree across theory, glossary, summary, sim boxes, exit ticket.
- Figures recomputed from SVG coordinates: varsi (60°, r = 280·sin 60° px, foot correct), kulma (α ≈ 40° at P, r = d sin α, vertical angles right), suunta (CCW +, CW −), ovi; hero's downward push on the left handle turns the nut CCW (loosening).
- Worked example: 240·0,35·sin 65° = 76,1 Nm < 80; perpendicular 84 Nm; symbolic first; 2 s.f. justified.
- One script recomputed every lesson number with my own vector torque τ = r_x F_y − r_y F_x: kertaus 100 N, virhe 10/20/17,3 Nm, siirto 135,3 Nm (mistakes 176,6/113,5/270,5), check-2 1,9 (7,6, −1,9), exit ticket 20 vs 25 Nm and clockwise sign — all agree.
- sim.js implements r = d sin α, M = F r, opens at M ≥ M0 (30/60 Nm hidden); force at angle α CCW from the handle always turns CCW; α = 0°/180° gives r = 0.
- exp-1: minimum opening forces 300/200/150/120/100 N all on the 10 N slider grid within 0–300 N; float products pass the 1e-6 margin; pred-1 consistent.
- exp-2: rusty nut opens at 90°, 60° (69 Nm), not at 45° (57), 30° and 150° (40) — pred-2 and the choice question consistent; locked F, d, nut isolate α; simState carries F, r, M, tulos.
- Each choice item has exactly one correct option; distractor feedback correct (check-1 locked-door option included).
- Scope: no angular quantities or rotational dynamics; sim states the turning is a picture only.
