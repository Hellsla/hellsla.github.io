VERDICT: PASS
CONTENT-HASH: cb88a832c037b5d1

## Blocking

## Polish
- lesson.md:215 — $mgh = \tfrac12 mv^2 + Q$ assumes the magnet starts from rest and air resistance is negligible; the worked example says the second, the Kaava section says neither — add "levosta" and "ilmanvastus on pieni" in a few words.
- lesson.md:213 — "$N$ on silmukan kierrosten lukumäärä" — "käämin kierrosten lukumäärä" (a loop has one turn), as fy7-5 names it.
- lesson.md:228 — "Sama kaava pätee jokaiseen pyörrevirtajarruun … liike-energia muuttuu sisäenergiaksi": for the falling magnet at constant speed it is potential energy that converts; "mekaaninen energia" would cover both cases.

## Checked
- Lenz directions in the ring figure, the tube figure (section × / • for both rings, top view anticlockwise, $\overline{B}_\text{ind}$ up below and down above the N-down magnet), sim.js ring arrows (below anticlockwise from above, above clockwise), both pysähdy answers, check-1, virhe and exit ticket 1: all correct; exactly one correct option in every choice item, each distractor's feedback right.
- Recomputed in one script with my own numerical ODE ($m\dot v = mg - kv$): fall times muovi 0,45 s, alumiini 4,24 s, kupari 6,68 s, rako 0,82 s; final speeds 4,43 / 0,24 / 0,15 / 1,49 m/s; Q 195,6 / 196,0 / 173,9 mJ; $mgh$ = 196,2 mJ: all inquiry feedback and the johtopäätös model answer match; slit/plastic ratio 1,8 ("noin kaksinkertainen") fair.
- sim.js: $F_\text{j} = Mgv/v_\text{t} = kv$, analytic $v(t)$, $y(t)$, Newton fall time, aluminium $k$ ratio 0,633 from σ 3,77/5,96·10⁷ S/m, slit $k/10$ ⇒ $v_\text{t}$ = 1,5 m/s; Q = ΔEp − Ek; simState gives aika, vLoppu, lampo after the run; model box states every limit (no air drag, no end effects, $k$ chosen, slit estimate, model values).
- koe-1/koe-2: kappale locked, putki varied, initial states right.
- Energy figure to scale (196,2 mJ → 206 px at 52,5 px per 50 mJ; copper Ek 0,225 mJ labelled 0,2 mJ).
- Worked example: v = 0,15 m/s, Q = 0,29402 J → 0,29 J (two s.f. from 25 g, 8,0 s), Ek share 0,096 %, ΔT ≈ 0,0025 K ≈ 0,003 K; symbolic first.
- pysähdy 0,059 W; siirto 21 kN and mistakes 25 / 9 / 42 kN, deceleration 8,75 m/s², 630 kJ; tarkistus-2 42 mW, mistakes 4,32 mW and 0,518.
- Energy-conservation argument for Lenz (lesson and tarkistus-3) correct; energy wording is "sisäenergiaksi" throughout, no "lämmöksi".
- Scope: induction, Lenz, eddy currents, laminated core; no self-induction or diamagnetism; induction hob frequency and lamination mechanism correct.
