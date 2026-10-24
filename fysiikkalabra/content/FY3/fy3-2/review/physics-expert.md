VERDICT: PASS

Reviewer: physics-expert. Lesson fy3-2 (Työ ja energia), fresh review of the revised version. No real physics, number, unit or scope errors found. Every exercise answer was recomputed from the problem text alone and matches the stored answer within tolerance. The findings below are all minor, non-blocking wording or scope-borderline notes.

## Scope check against the source
Source: docs/lops2019/maol-fysiikan-tukimateriaali-lops2019.txt.
- FY3 clarification: "Työn laki W = Fs on tarkoituksenmukaista määritellä perustuen kokeeseen ... (ns. Joulen koe)". lesson.md lines 8 and 17-19 follow this. Graphical integration in (s,F) is in meta.json goals and is covered in lines 19 and 34-53.
- FY3: force is "vuorovaikutuksen voimakkuuden mittana", not the cause of changes in motion. The lesson never uses Newton's laws, vectors, E_k, E_p or the work-energy theorem. W = mgh is written as the work of lifting (a W = Fs special case with F = G), not as E_p. This is fine.
- FY2: energy forms are described without expressions. The lesson names no energy-form expression. P = W/t is consistent with FY2 P = ΔE/Δt. P = Fv is a direct consequence of W = Fs and v = s/t, and carries the "tasaisessa liikkeessä, voima liikkeen suuntainen" condition. This is not a scope breach.
- Conditions are present everywhere: "vakiovoima", "liikkeen suuntainen", "hitaasti" (lifting), "tasaisessa liikkeessä" (P = Fv).

## Formulas (lesson.md)
- Line 15, W = Fs: correct, with the condition stated. Units 1 J = 1 N·m are correct.
- Lines 19 and 51-53: area under the F(s) graph is correct. Triangle ½·40·0,20 = 4,0 J, and the average-force check 20 N · 0,20 m = 4,0 J is correct. The warning that 40·0,20 = 8,0 J would be double is correct. The SVG matches the text: triangle (0,0)-(0,20 m,0)-(0,20 m,40 N), and the ticks, labels and label position are consistent.
- Lines 21-25, W = Gh = mgh with g = 9,81: correct for slow (constant-velocity) lifting.
- Line 29, P = W/t = Fv: correct under the stated condition. 1 W = 1 J/s is correct.
- Lines 6, 56 and 60: a perpendicular force does no work, and holding or carrying horizontally at constant speed is not work done by the supporting force. Both are correct.
- Line 10: "Portaat ylös kävellen ja juosten teet saman työn" holds for the work against gravity, to good approximation. A 6 kW sauna heater giving 6000 J/s is correct.
- Joule's experiment (lines 8 and 61): the 1840s date is correct (paddle wheel 1843-1847). A falling weight turning a paddle in water, a measurable temperature rise, and heat proportional to the mechanical work done are all correct. The lesson uses "lämpö" loosely for "internal-energy increase"; this is acceptable at FY3 level.
- Friction and heat (lines 10 and 61): "kitkaa vastaan tehty työ lämmittää pintoja" and "kitkassa lämmöksi" are physically sound.

## Exercises recomputed (python3 -I, g = 9.81)
```
L1-01 2.0 kJ (stored 2.0)
L1-02 180.0 J (180)
L1-03 3.0 kW (3.0)
L1-04 210.0 J (210)
L1-05 60.0 W (60)
L2-01 30.0 m (30)
L2-02 360.0 kJ (360)
L2-03 250.155 kJ (250)
L2-04 100.0 J (100)   # 10*2.0 + 0.5*(10+30)*4.0
L3-01 W=60.0 J, F_avg = 30.0 N (30)   # 10 + 40 + 10 J over 2.0 m
L3-02 588.6 J (590)   # 20*2.0*9.81*1.5; deviation 0.2 %
L3-03 45.4167 min (45)   # 1000*9.81*50/180/60; deviation 0.9 %
```
All are within the 0.02 relative tolerance. Significant figures follow the data (2 s.f. for L3-02 and L3-03). Units and magnitudes are plausible: 3 kW lift motor, 250 kJ for 850 kg to 30 m, and a Joule-type run of 20 drops of a 2 kg weight from 1,5 m giving about 0,6 kJ. That is a realistic Joule-like scale, with a tiny temperature rise.

## solutions.md
All reasoning is correct, and the given / wanted / formula / substitution / answer / sanity structure is followed.
Sanity-check numbers were verified:
- L1-01: 2000 J = lifting 20 kg by about 10,2 m.
- L1-02: 150 N is about 15 kg.
- L2-02: 360 kJ equals lifting 1000 kg by about 36,7 m.
- L2-03: weight 8,34 kN; 30 m is roughly 10 storeys.
- L2-04: average force 100/6 ≈ 16,7 N lies between 10 and 30 N.
- L3-03: 0,490 MJ = 0,136 kWh, about 0,14 kWh.
Exit-ticket answers are also correct: 98,1 J ≈ 98 J, 1,0 J, same work and double power.

## sim.js
- Line 37: W = F·s exactly. Line 38: P = W/t (average power, which equals F·v with v = s/t because the box moves at constant speed). Line 40: Wdone = W·u, linear in distance for a constant force, which is correct. Line 69 fills the shaded area (xS−G.x)·u × (F height), which is the work done so far. Readout and simState are consistent. Slider ranges match sim-spec.md. Floor scale 20 m·13 px + 40 + half box stays left of x = 346.

## Findings (all minor and non-blocking)
1. sim.js:30 (and sim-spec.md) — "kitka ottaa vastaan vetovoiman tekemän työn" and "kitka pitää vauhdin vakiona" are loose. Friction does not "receive" work. Friction force equals the pull, so the net force and net work are zero and the speed stays constant. The work Fs done by the pull ends up as heat in the box and floor. Fix (optional): "Kitkavoima on yhtä suuri kuin vetovoima, joten vauhti ei muutu. Vetovoiman tekemä työ muuttuu kitkassa lämmöksi."
2. lesson.md:21 and exercises.json:L1-02 (line 14) — W = Gh needs the lift to be at constant speed, or at rest at the start and end. Line 21 says "hitaasti", which is fine. L1-02 text says only "nostetaan", so it is implicit. Fix (optional): "nostetaan hitaasti". L2-03 already says "hitaasti". Also note that "nostovoima = paino" is an equilibrium argument, which is borderline against FY3's "no force as cause of motion change". It is acceptable because the weight is measured, for example with a force meter, and no Newton law is named.
3. exercises.json:L3-01 (line 82) — "keskimääräinen suuruus koko 2,0 m:n matkalla" is an average over distance, not over time; the hint and solution resolve it. Fix (optional): "matkan suhteen keskimääräinen".
4. exercises.json:L3-02 (line 90) — "painon menettämä nostotyön suuruinen energia" is awkward. Fix (optional): "Oleta, että kunkin pudotuksen aikana painon menettämä energia m g h siirtyy kokonaan veden lämpömääräksi." Do not name E_p.
5. sim.js:62 and 63 — non-physics layout note. At F near 100 N and s near 20 m the force arrow (120 px) crosses into the graph panel at x ≥ 380. Defer to the web-designer. Optional fix: scale the arrow to a maximum of about 50 px.
6. solutions.md:7 — "Mopon työntäminen 25 m on raskasta" is subjective; 80 N is light for steady pushing. Optional fix: delete the sentence or write "Sopiva suuruusluokka."

No FAIL-level issues.
