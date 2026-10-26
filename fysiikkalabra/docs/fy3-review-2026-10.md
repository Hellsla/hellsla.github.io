# FY3 Energia ja lämpö: pedagogical and scientific review (2026-10-26)

Scope: all 12 published FY3 lessons (`site/fy3-1.html` … `site/fy3-12.html`), read from source (`lesson.md`,
`inquiry.json`, `exercises.json`, `exit-ticket.json`, `sim.js`, `sim-spec.md`) and from the rendered pages
(Chromium, 360 px and 1280 px). Every lesson currently has science PASS and pedagogy PASS for its content hash, so
this review is not about errors the pipeline missed line by line. It is about what the pipeline cannot see: the
sequence as a whole, what the student actually does, and whether the evidence is real evidence.

## 0. Inventory

| # | Lesson | Sim | Experiments | Visible words (360 px) | Page height (360 px) |
|---|---|---|---|---|---|
| fy3-1 | Voima vuorovaikutuksen mittana ja paino G = mg | spring scale, 4 bodies | 2 | 1 790 | 16 300 px |
| fy3-2 | Työ ja energia | box pulled, (s,F) area | 2 | 1 770 | 16 100 px |
| fy3-3 | Termodynaaminen systeemi, tilanmuuttujat ja lämpötila | 80-particle box, pressure from counted hits | 2 | 1 830 | 17 100 px |
| fy3-4 | Paine ja hydrostaattinen paine | gauge in a pool, (h,p) line | 2 | 2 060 | 16 700 px |
| fy3-5 | Sisäenergia, lämpömäärä ja energian säilyminen | none | 0 (two tables) | 1 700 | 15 100 px |
| fy3-6 | Aineen lämpeneminen ja jäähtyminen: Q = cmΔT | calorimeter | 2 | 2 700 | 19 400 px |
| fy3-7 | Olomuodon muutokset | heating curve of water | 2 | 1 980 | 17 500 px |
| fy3-8 | Lämpölaajeneminen | lattice + rod, (T,ΔL) | 2 | 2 380 | 19 200 px |
| fy3-9 | Kaasujen tilanmuutokset ja Boylen laki | piston cylinder, 3 modes | 2 | 2 400 | 19 800 px |
| fy3-10 | Ideaalikaasun tilanyhtälö pV = nRT | N-particle box, pressure from impulses | 2 | 2 460 | 19 900 px |
| fy3-11 | Kaasun tekemä työ ja lämpövoimakone | Sankey energy flows | 2 | 2 450 | 19 600 px |
| fy3-12 | Lämmön siirtyminen, energiatasapaino ja ilmastonmuutos | none | 0 (two tables) | 2 010 | 18 000 px |

Every page uses the same six-stage template: hook → retrieval choice → 2–3 committed predictions → free sim →
two "lock everything but one" experiments → theory → reflection → staged example → error-spotting choice →
transfer numeric → 5/4/3 exercises → concept choice, numeric, explanation → 3-item exit ticket. That is about
25 activities and 20 problems per lesson, 20–25 phone screens.

## 1. Course-wide findings (the ones that matter most)

1. **Most experiments confirm the program's arithmetic, not the physics.** In fy3-1 (G = mg), fy3-2 (W = Fs),
   fy3-4 (p = p₀ + ρgh), fy3-6 (T from the balance equation), fy3-7 (durations `t = Q/P`, "näkyvät heti"),
   fy3-8 (ΔL = αL₀ΔT), fy3-9 (p from pV/T = vakio, sim.js line 6) and fy3-11 (MW arithmetic) the sim computes the
   very formula the prediction is about, and the feedback then says "Mallin arvot tukevat tätä". The student
   learns that the simulation agrees with itself. Only fy3-3 and fy3-10 produce a result that *emerges* (pressure
   from counted wall hits). Honest labelling ("mallin arvoja") is there; the epistemic problem is not.
2. **The answer key was guessable.** 58 of 75 choice items had the correct option second; in the
   competing-explanations items "Bea" was right in 11 of 12. A student who noticed this after two lessons
   needed no physics. **Fixed in this branch** (seeded shuffle at build time, section 6).
3. **On a phone the experiment and its controls were 1–2.5 screens apart.** The record button of Koe 2 sat
   600–1 900 px below the slider it depends on (measured: fy3-9 slider at y = 5 054, Koe 2 button at 6 946).
   Every measurement meant scrolling up and down. **Fixed in this branch** (the sim moves to the active
   experiment, section 6).
4. **One template, twelve times.** Every lesson asks for the same moves in the same order, every experiment
   varies exactly one pre-chosen variable with the others locked, and no activity ever asks the student to
   *choose* what to control, design a measurement, read a value off a graph, fit a line, or handle noise. The
   inquiry spec's own goal ("experiment, interpret evidence") is met formally but not cognitively. The exit
   ticket repeats the three Tarkista checks (six end-of-lesson checks).
5. **Length.** 1 700–2 700 visible words and ~20 phone screens per lesson, before exercises are opened. The
   theory appears twice in effect: the predictions' feedback already contains the explanation, then Selitä
   repeats it in full.
6. **The gas progression repeats one case and skipped another.** Isochoric heating (p ∝ T) is investigated in
   fy3-3 Koe 1, worked in the fy3-3 example (extrapolation to −270 °C) and again in fy3-9 Koe 2 with the same
   Celsius-ratio distractor as the fy3-3 error-spotting item (120 kPa, 20 → 40 °C). The isobaric case (V ∝ T) was
   stated in fy3-9 but never investigated anywhere, and the air γ = 3,4 · 10⁻³ 1/K of fy3-8 (which *is*
   1/293 K, i.e. Charles's law) was never connected to it. **fy3-9 Koe 2 is rewritten in this branch** to the
   isobaric case with exactly that connection.
7. **Two of the three MAOL key experiments are read, not done.** Absolute zero by extrapolation (fy3-3) and the
   specific latent heat of vaporisation (fy3-7) exist only as worked examples; the sims cannot produce the data
   (fy3-3 check-2 gives three perfect points; fy3-7's sim has no scale and shows `rm/P` directly). Only Boyle's law
   (fy3-9) is investigated.

### Symbols, terminology, conventions

- **W means five things.** fy3-2: work by a force. fy3-5: work done *on* the system. fy3-11 in one lesson: work
  done *by* the gas (W = pΔV), work on the gas in ΔU = Q + W (so −pΔV), engine work W = Q₁ − Q₂ and the heat
  pump's electrical energy. The text flags the clash, but a flagged clash is still a clash. Use `W_k` (kaasun
  tekemä työ) or write the first law with `−p\,ΔV` explicitly in fy3-11.
- **T is sometimes Celsius.** fy3-3 introduces θ for °C and T for kelvin; fy3-9 follows it. fy3-6 then writes
  `T_v = 20,0 °C`, `T = 24,5 °C`, and fy3-8 labels its axis and slider "T (°C)". Students who learnt "T is
  kelvin" in fy3-3 see the convention broken three lessons later. Use θ in fy3-6 and fy3-8, or say once why ΔT
  is safe.
- **fy3-3 says something false about the course.** "Paineen ja kelvinlämpötilan suoraa verrannollisuutta
  tutkitaan kunnolla *myöhemmillä kaasuja käsittelevillä kursseilla*" — it is fy3-9 of this module. One-line fix
  (delta review).
- "Liike-energia" is used qualitatively from fy3-3 on although E_k is FY4. Acceptable, but say once that it is
  the energy of motion and is quantified in FY4.
- fy3-9's sim breaks house rule 3: its model explanation is always visible under the canvas (not behind
  Lisätietoja), and it has its own "Tallenna mittaus" button and table beside the experiment's "Kirjaa mittaus"
  table, so a student sees two record buttons and two tables.

### Prerequisites not established

- fy3-3 uses pressure in Pa before fy3-4 defines it (acknowledged in the text; acceptable).
- fy3-10 relies on the mole "kuten kemiasta voi olla tuttua". Students in FY3 may not have met ainemäärä in
  chemistry yet; the jump from N particles in the sim to n = N/N_A is the steepest step in the module and gets
  one sentence.
- fy3-11 needs ΔU = Q + W *and* W = pΔV *and* the sign conventions of both at once; the retrieval item is the
  only bridge.

### Misconceptions insufficiently addressed

- Metal "feels colder" than wood at the same temperature (conduction rate vs temperature) — the classic FY3
  misconception, absent from fy3-5, fy3-6 and fy3-12.
- Objects in the same room are at the same temperature (thermal equilibrium) — never asked.
- Bubbles in boiling water are air; evaporation only happens at 100 °C; sweating cools "because water is cold"
  — fy3-7 treats boiling only, not evaporation below the boiling point.
- Energy is "used up" in an engine (fy3-11 pred-2 touches it) vs energy *quality* (no 2nd-law intuition beyond
  "osa on luovutettava").
- Particles in a gas "fill" the container / there is air between the particles — not addressed in fy3-3 or
  fy3-10 although both draw particles.
- fy3-4: pressure is a vector pointing down — check-1 addresses it well; fine.

### Formulas before phenomena

fy3-10 Kaava has five display formulas (pV = nRT, n = m/M, N = nN_A, p ∝ NT/V, combined law); fy3-11 has six;
fy3-6 has five, with the equilibrium-temperature algebra before the student has felt why a weighted mean
appears. In each of these the student meets the full formula set before any activity that needs more than
one of them.

### Curriculum coverage (LOPS 2019 / MAOL guide)

All eight central contents are covered and scope is respected (FY3 force only as interaction; no cycles).
Required experiments: Boyle — investigated; absolute zero by extrapolation — worked example only; latent heat
of vaporisation — worked example only; calorimetric measurement (fy3-6 Kokeellisesti) — example + sim.
Optional enrichment that is *not* required and could be trimmed if time is short: heat-pump COP and the CHP
numbers in fy3-11, U-value economics in fy3-12 L2/L3, Avogadro's number count in fy3-10 L3-01. The thematic
links (energiantuotanto, rakentaminen ja energia kotona, ilmastonmuutos) are well served.

### Opportunities to reuse simulations

One **gas-cylinder engine** — fy3-9's piston cylinder, with fy3-10's pressure-from-impulses instead of a formula
— could serve fy3-3 (heating at fixed V), fy3-5 (a piston pushed fast into the gas: particles bounce off the
moving piston faster, the "maila osuu palloon" sentence made visible; slow push with heat leaking out), fy3-9
(all three laws, measured rather than computed), fy3-10 (N slider) and fy3-11 (isobaric expansion with the
pΔV area filling under the (V,p) graph, the same visual language as fy3-2's (s,F) area). Five lessons, one
mental model, one set of controls to learn.

## 2. Lesson-by-lesson assessment

Each entry: what a student should understand; then the three highest-priority improvements.

**fy3-1 Voima ja paino.** Goal: weight is an interaction between object and celestial body; G = mg; mass is
invariant. Strengths: clean calibration-table activity (5,6 cm → 3,5 N), good Jupiter "no surface" distractor.
Weakness: both experiments ask the sim to multiply m by g. Improvements: (1) replace Koe 1 with *calibrating*
the spring yourself — hang 1, 2, 3 identical masses, read the stretch, mark the scale, then weigh an unknown
(the student builds the newton scale the text describes); (2) Koe 2: an unknown planet whose g the student
must determine from (m, G) readings — the current check-2 as an experiment; (3) add the bathroom-scale-on-the-Moon
paradox as the hook question (kg reading 1/6) rather than the misconception paragraph.

**fy3-2 Työ ja energia.** Goal: work = force × displacement along the force; area under (s,F); power as rate.
Strengths: Joule table, (s,F) area figure, P = Fv transfer. Weakness: the hook's real puzzle (carrying a
backpack is not work) is the one thing the sim cannot test; experiments confirm W = Fs. Improvements: (1) give
the sim a variable force mode (spring stretched, force grows linearly) and make Koe 1 "estimate the area" before
the sim fills it — 40 N × 0,20 m vs ½ · 40 N · 0,20 m is the misconception the lesson's virhe item targets;
(2) let the force direction rotate to vertical so the backpack case is investigated (W = 0 when the force is
perpendicular), without vectors or cos α — just "voima ylös, liike sivulle"; (3) cut pred-1 (doubling s doubles
W) — it is the formula, not a misconception.

**fy3-3 Systeemi, tilanmuuttujat, lämpötila.** Goal: kelvin scale from the micro model; p ∝ T at fixed V;
absolute zero. Strengths: genuinely emergent pressure; the speed (×1,41) vs pressure (×2) contrast. Weakness:
the MAOL experiment (extrapolate to absolute zero) is only a worked example; "myöhemmillä kursseilla" error.
Improvements: (1) make the extrapolation the experiment: measure the sim's p at 4–5 temperatures in °C (noisy,
from hits), plot, fit a line, read where it meets p = 0 — the student *finds* −273 °C; (2) fix the false
sentence about later courses; (3) drop pred-2 (volume halving) — it belongs to fy3-9 and is repeated there.

**fy3-4 Paine ja hydrostaattinen paine.** Goal: p = F/A; p = p₀ + ρgh, independent of vessel shape.
Strengths: the dam hook, mercury-barometer transfer, the hydrostatic paradox item. Weakness: the hydrostatic
paradox (pred-3) — the most surprising idea — has no evidence, only theory; experiments read off the formula.
Improvements: (1) add vessel shapes to the sim (narrow tube, wide basin, a flask) with the gauge at the same
depth — the paradox becomes observable; (2) let the student find the depth at which pressure doubles (≈ 10 m),
the number divers use, instead of recording 4 depths; (3) the p = F/A half of the lesson has no activity at all
— one short nail/ski comparison would do.

**fy3-5 Sisäenergia, lämpömäärä, ensimmäinen pääsääntö.** Goal: heat and work are two ways of transferring
energy; ΔU = Q + W; heat is not a property. Strengths: the pump hook and venttiili-viileä contrast are excellent;
pred-1 Aino/Bea/Cem are real competing models. Weakness: the most abstract lesson in the module has no sim;
the evidence is a table of model numbers, and the sign convention arrives as a rule. Improvements: see the
detailed redesign C1.

**fy3-6 Q = cmΔT.** Goal: specific heat; heat balance; weighted-mean equilibrium temperature. Strengths:
sand-vs-water hook, the 0,30 + 0,20 kg sand/water comparison, the bathtub transfer. Weakness: longest page
(2 700 words); five formulas incl. full algebra before the student has seen why the mean is weighted.
Improvements: (1) start with a qualitative puzzle — "pour 1 cup of 80 °C into 3 cups of 20 °C: where does it
end?" — and let the sim show it before any formula; (2) make the calorimetric experiment a real determination:
unknown metal, the student measures T and computes c, then identifies the metal from the table (now this is the
worked example); (3) use θ for Celsius temperatures as fy3-3 taught.

**fy3-7 Olomuodon muutokset.** Goal: phase change at constant temperature; Q = sm, Q = rm; micro model of bonds.
Strengths: the heating-curve sim is the best single visual in the module; strong pred-3 alternatives ("lag in the
thermometer"). Weakness: the experiments record `t = Q/P` values the sim prints immediately, so the plateau the
student watches is not the data; the MAOL vaporisation experiment is an example only. Improvements: (1) the
student measures plateau lengths off the (t,T) graph (ruler-style cursor) and computes s and r themselves; (2) a
virtual open calorimeter on a scale: mass falls linearly at the boil, slope × P gives r — the MAOL experiment,
including the heat-loss bias the example discusses; (3) add evaporation below 100 °C (sweat, wet clothes) and the
"bubbles are air" misconception.

**fy3-8 Lämpölaajeneminen.** Goal: ΔL = αL₀ΔT; micro model (asymmetric potential); liquids and gases expand more.
Strengths: the Aino/Bea/Cem/Daniel micro-model item is one of the best in the module; the hole-grows idea.
Weakness: both experiments confirm proportionality in the formula; the asymmetry argument is told, not seen.
Improvements: (1) show the asymmetric bond in the micro view (a particle that swings further out than in, its
average position marked), so "helpompi loitota" is visible; (2) a bimetal or rail-gap design challenge (choose
the gap for −30…+30 °C) instead of a second one-variable experiment; (3) connect air's γ to fy3-9 (done from the
fy3-9 side in this branch).

**fy3-9 Kaasujen tilanmuutokset ja Boylen laki.** Goal: Boyle's law verified via the 1/V linearisation; V ∝ T and
p ∝ T in kelvin. Strengths: the syringe-table outlier (fast compression heats), the (1/V, p) linearisation, the
crisp-packet hook. Weaknesses: pressure is computed from pV/T, so "verifying" Boyle's law on the sim is circular;
isochoric repeated from fy3-3, isobaric never investigated (fixed); duplicate record UI; visible sim
explanation. Improvements: (1) **done:** Koe 2 is now isobaric, with a question tying the measured 0,171 ml/K to
fy3-8's γ = 1/293 K; (2) measure pressure from hits (fy3-10's code) so Boyle's law emerges; (3) remove the sim's
own table and move its explanation behind Lisätietoja.

**fy3-10 pV = nRT.** Goal: amount of substance; the ideal-gas equation unifies the laws; same n for any gas at the
same p, V, T. Strengths: the 1,41 × 1,41 = 2 argument; pV/(NT) table; hot-air-balloon transfer. Weakness:
formula overload; R and Avogadro's law are stated, not discovered; the sim is fy3-3's box again with an N slider.
Improvements: see C2.

**fy3-11 Kaasun työ ja lämpövoimakone.** Goal: W = pΔV as area; heat engine must reject heat; η; CHP; heat pump.
Strengths: Finnish energy context, CHP reasoning, the "pressurised bottle does no work" check. Weakness: the sim
is an arithmetic Sankey (vary η, read 1000 − η·1000); the hardest idea (why Q₂ > 0 always, and why ΔT matters)
has no evidence; five meanings of W. Improvements: see C3.

**fy3-12 Lämmön siirtyminen ja ilmastonmuutos.** Goal: conduction/convection/radiation; P = UAΔT; energy balance;
greenhouse effect as back-radiation. Strengths: the cleanest physics in the module (consistent 240/390/150/140
W/m² budget), the cloudy-night transfer, ethics link. Weakness: no sim; tables of model values; the three
transfer modes get no activity. Improvements: (1) a two-box energy-balance sim (surface + one atmospheric layer):
change absorbed fraction, watch the surface temperature relax to a new equilibrium — the second table as a live
graph, with the time lag from ocean heat capacity; (2) a "find the leak" house challenge with P = UAΔT (which
upgrade saves most per euro); (3) add the metal-feels-colder misconception to the conduction paragraph.

## 3. Audit table (A)

| Lesson | Current strengths | Main pedagogical weakness | Most valuable change | Priority |
|---|---|---|---|---|
| [fy3-1](https://hellsla.github.io/fysiikkalabra/site/fy3-1.html) | calibration table, mass ≠ weight distractors | experiments multiply m·g | student calibrates the spring and weighs an unknown | Medium |
| [fy3-2](https://hellsla.github.io/fysiikkalabra/site/fy3-2.html) | Joule table, (s,F) area figure | the hook (backpack) is untestable; sim confirms W = Fs | variable-force (spring) mode: estimate the area before the sim fills it | Medium |
| [fy3-3](https://hellsla.github.io/fysiikkalabra/site/fy3-3.html) | emergent pressure from hits | MAOL extrapolation is only an example; false sentence | extrapolate noisy sim data to absolute zero | High |
| [fy3-4](https://hellsla.github.io/fysiikkalabra/site/fy3-4.html) | dam hook, paradox item, barometer | hydrostatic paradox has no evidence | vessel shapes in the sim, same depth → same p | Medium |
| [fy3-5](https://hellsla.github.io/fysiikkalabra/site/fy3-5.html) | pump hook, competing models | no sim for the most abstract idea | piston-compression particle sim (C1) | High |
| [fy3-6](https://hellsla.github.io/fysiikkalabra/site/fy3-6.html) | sand/water, bathtub transfer | longest page; algebra before intuition | qualitative mixing puzzle first; unknown-metal determination | Medium |
| [fy3-7](https://hellsla.github.io/fysiikkalabra/site/fy3-7.html) | heating-curve sim | recorded values are printed formula outputs | read plateaus off the graph; virtual scale experiment for r | High |
| [fy3-8](https://hellsla.github.io/fysiikkalabra/site/fy3-8.html) | micro-model item, hole grows | asymmetric bond told, not shown | show the asymmetric vibration; rail-gap design task | Low |
| [fy3-9](https://hellsla.github.io/fysiikkalabra/site/fy3-9.html) | syringe outlier, 1/V linearisation | circular sim pressure; isobaric missing (fixed) | pressure from hits; one record UI | High (started) |
| [fy3-10](https://hellsla.github.io/fysiikkalabra/site/fy3-10.html) | 1,41 × 1,41 argument, pV/(NT) table | formula overload; R and Avogadro stated | weigh the balloons: discover equal n (C2) | High |
| [fy3-11](https://hellsla.github.io/fysiikkalabra/site/fy3-11.html) | Finnish energy context, CHP | arithmetic sim; five meanings of W | piston cylinder doing pΔV work; reservoir-ΔT engine (C3) | High |
| [fy3-12](https://hellsla.github.io/fysiikkalabra/site/fy3-12.html) | consistent energy budget, ethics | no sim; transfer modes have no activity | two-box energy-balance sim with time lag | Medium |

## 4. Course-wide plan (B): the five changes most likely to improve learning

| # | Change | Impact | Effort | Status |
|---|---|---|---|---|
| 1 | Shuffle answer options at build time (no content change, no review cost) | removes answer-position guessing from all 75 choice items | small | **done** |
| 2 | Bring the sim to the active experiment (template) | every measurement on one phone screen in 10 lessons | small | **done** |
| 3 | Replace formula-echo experiments with measurements that need interpretation: read off a graph, fit a line, extrapolate, deal with noise. Start with the MAOL experiments: fy3-3 extrapolation, fy3-7 latent heat on a scale, fy3-9 Boyle from hits | the core scientific skill FY3 names | medium per lesson | fy3-9 started |
| 4 | One gas-cylinder sim (pressure from impulses) reused in fy3-3, 5, 9, 10, 11 | one micro model carried through the whole thermodynamics strand; fy3-5 gets its missing sim | large once, small per lesson | proposal |
| 5 | Vary the template and cut length: per lesson one prediction that a real investigation can refute, one open challenge (student chooses what to hold constant), drop the exit ticket where Tarkista already has three checks, shorten prediction feedback so Selitä is not pre-empted | attention and agency; ~30 % less reading | medium | proposal |

Also queued (small, one delta review each): fy3-3 "myöhemmillä kursseilla" sentence; θ for Celsius in fy3-6/fy3-8;
fy3-9 sim Lisätietoja and duplicate table; distinct symbol for gas work in fy3-11.

## 5. Detailed redesigns (C)

### C1 fy3-5 — "Mistä pumpun ilma saa energiansa?"

*Approach: competing explanations tested in a particle simulation, then energy bookkeeping.*

1. **Herätä.** Keep the pump hook. Retrieval stays.
2. **Ennusta (one item).** Keep pred-1 (Aino: high pressure is hot / Bea: work transfers energy / Cem: heat is a
   substance squeezed together). Add `justify`.
3. **Tutki — new sim** (the shared gas cylinder): 40 particles, a piston the student pushes with a speed slider
   (hidas · nopea) and a wall-conductivity toggle (eristetty / johtava). Each particle that hits the moving piston
   rebounds faster (draw the speed-up as a brief longer trail). Readouts: W done by the piston (J, from force ×
   displacement, the fy3-2 idea), Q through the walls, ΔU, T.
   - *Koe 1:* insulated wall, push fast, then push the same distance slowly. Student predicts first: "Kumpi
     lämmittää enemmän?" Evidence: same W, same ΔT when insulated → speed of pushing is not the cause; work is.
     This refutes Aino (the pressure is the same at the end both ways) and Cem (no substance moved).
   - *Koe 2:* conducting wall, slow push: W > 0, ΔT ≈ 0, Q ≈ −W. The student fills a three-bar energy diagram
     (Q, W, ΔU) from the readouts — the sign convention is *built* from arrows into / out of the box before the
     formula is written.
   - *Koe 3 (open):* "Saa ilman lämpötila nousemaan 20 K niin, että seinien läpi siirtyy ulos vähintään 10 J."
     The student must choose the settings; feedback checks the logged Q, W.
4. **Selitä.** ΔU = Q + W now names what the bars already showed. Keep the "kappaleessa ei ole lämpöä" paragraph.
5. **Sovella.** Keep the venttiili-viileä question as the transfer: run the sim backwards (gas pushes the piston
   out) → particles leave slower → cools. Keep tulimäntä numeric.
6. **Tarkista.** Keep the three checks; drop the exit ticket.

Feedback rules: the speed-up at the piston is the *mechanism*; feedback for a wrong choice points to a specific
frame ("katso hiukkasta, joka osuu liikkuvaan mäntään").

### C2 fy3-10 — "Onko heliumpallossa vähemmän kaasua?"

*Approach: a virtual experiment with masses that leads to Avogadro's law, then the equation.*

1. **Herätä.** Keep the two balloons. Retrieval: Boyle (keep).
2. **Ennusta.** One item: "Kummassa pallossa on enemmän hiukkasia?" (enemmän ilmapallossa / yhtä monta /
   enemmän heliumpallossa / riippuu kaasun lämpötilasta). Keep justify.
3. **Tutki 1 — weigh it** (interpret, new): a table of *measured-looking* masses of 5,00 l of He, N₂, air, CO₂ at
   101 kPa, 20 °C (0,83 g, 5,80 g, 6,01 g, 9,12 g, with ±0,02 g scatter), and molar masses. The student computes
   m/M for each → all ≈ 0,207 mol. Question: "Mitä huomaat?" This is Avogadro's law discovered from data, not
   stated.
4. **Tutki 2 — the particle box** (current sim, one experiment, not two): vary N and T *together* so that the
   pressure stays the same (an open challenge: "pidä paine 1,00:ssa, kun T kaksinkertaistuu"). Students find
   that N must halve: pV ∝ NT, measured.
5. **Selitä.** Only now: n = N/N_A in one paragraph with a picture (a mole as a dozen-like count), then
   pV = nRT with R measured from step 3: R = pV/(nT) = 101 000 Pa · 0,005 m³ / (0,207 mol · 293 K) ≈ 8,3. The
   combined gas law moves to the summary as a consequence (one line), not a fifth display formula.
6. **Sovella.** Keep the hot-air balloon transfer; it now uses the idea the student found (n falls as T rises at
   fixed p, V).
7. **Tarkista.** Keep check-2 (p/p_ref) and check-3 (1,41 × 1,41).

### C3 fy3-11 — "Miksi voimala heittää puolet energiasta mereen?"

*Approach: from a piston doing work to an engine that must reject heat; one evidence chain, then the Finnish
energy system.*

1. **Herätä.** Keep the museum locomotive + 1000 MW / 400 MW hook.
2. **Ennusta 1.** "Kaasu laajenee vakiopaineessa 200 kPa:ssa 1,0 l → 2,5 l. Kuinka paljon työtä se tekee?" with
   distractors from pressure alone and from p·V₂.
3. **Tutki 1 — the gas cylinder again** (shared sim, isobaric mode): heat the gas, the weighted piston rises,
   the (V,p) graph fills the rectangle p·ΔV exactly as fy3-2's (s,F) area filled. The readout shows W_k (gas
   work), Q and ΔU, and the student checks Q = ΔU + W_k for three runs. One symbol per meaning: W_k for the
   gas's work; the first law written as ΔU = Q − W_k on this page.
4. **Ennusta 2.** "Voiko mäntäkone toistaa tämän niin, että kaikki lämpö muuttuu työksi?" (kyllä, jos kitka
   poistetaan / ei, mäntä on saatava takaisin / ei, koska energia häviää).
5. **Tutki 2 — make it a cycle** (same sim, a "palauta mäntä" button): to repeat, the piston must come back
   down. Pushing it down hot costs as much work as was gained; cooling the gas first (contact with a cold
   reservoir) makes the return cheaper — but that cooling *is* Q₂. Student logs W_net and Q₂ with a hot
   reservoir at 400 K and cold at 300 K, then cold at 350 K: smaller ΔT → smaller share of heat becomes work.
   Qualitative only (no Carnot formula; cycles are outside core content, the sim shows just enough to make
   "osa on luovutettava" a consequence, not a decree).
6. **Selitä.** W = Q₁ − Q₂, η = W/Q₁. Keep the energy-flow figure.
7. **Sovella.** Now the existing Sankey sim, but as a design task: "Kaupunki tarvitsee 300 MW sähköä ja 500 MW
   lämpöä. Vertaa lauhdevoimalaa + sähkölämmitystä, yhteistuotantoa ja yhteistuotantoa + lämpöpumppua:
   kuinka paljon polttoainetta kukin tarvitsee?" Students argue with numbers; the ethics link from LOPS sits
   here.
8. **Tarkista.** Keep the pressurised-bottle check and the "rakennetaan voimala ilman lauhdutinta" explanation.

## 6. What this branch changes

1. `scripts/inquiry.py`: every choice item's options are shown in a seeded order (sha256 of lesson and activity
   id), identical on every build; "Laskussa / Päättelyssä ei ole virhettä" stays last. The correct option is now
   in positions 1–4 at 26 / 17 / 22 / 10 items instead of 12 / 58 / 5 / 0. No lesson content changes, so all
   reviews stay current. `scripts/test_inquiry.py` checks determinism, completeness and spread, and the browser
   tests now pick wrong options by `data-correct` instead of by position.
2. `templates/inquiry.js`, `templates/site.css`: "Aseta alkutila" moves the page's simulation into that
   experiment, above its buttons and table, and leaves a link in its first place. Measured on fy3-9 at 360 px:
   slider-to-button distance 700–840 px instead of 1 200–1 900 px. Free exploration before any experiment is
   unchanged.
3. `content/FY3/fy3-9` (separate commit, a **draft** until both reviews pass): Koe 2 and Ennuste 2 now
   investigate the isobaric case (50 ml, 20 → 80 °C at 100 kPa → 60,2 ml; distractors 200 ml, 50 ml, 110 ml),
   and an evidence question connects the measured 0,171 ml/K to fy3-8's γ = 3,4 · 10⁻³ 1/K = 1/(293 K). `prior`
   now retrieves fy3-3's p ∝ T. The adapter exposes the gas volume in ml and V/T in ml/K so the table reads in the
   units of the slider. The isochoric law stays in the theory as a recap of fy3-3.
