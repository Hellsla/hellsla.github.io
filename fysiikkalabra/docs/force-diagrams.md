# Force diagrams (voimakuviot)

The standard for teaching, practising and assessing force diagrams (teacher 2026-10-29, "FY04 – Force Diagrams as a
Core Competency"). It applies to every lesson whose curriculum entry has an `"fbd"` plan (FY4 now; later courses
when forces are drawn). Writers, the science reviewer and the pedagogy reviewer of those lessons get this file in
their packet (`review_packet.py`). The goal: a student who finishes FY4 can draw a correct force diagram for an
unfamiliar situation without help, and can form Newton's second law from it.

## What the matriculation examination expects (verified 2026-10-29)

These are the official *Hyvän vastauksen piirteet* of five Finnish matriculation exams (ylioppilastutkinto,
tiedostot.ylioppilastutkinto.fi/kokeet/&lt;date&gt;_FY_fi/grading-instructions.html). The deductions differ from exam to
exam. **There is no universal YTL scheme: never write one.** Cite the exam when you state a deduction.

| Exam | Task | Points for the diagram | Stated deductions and requirements |
|---|---|---|---|
| Spring 2025 (2025-03-21) | 4.1 Heliumpallo katossa | 5 p | Missing, extra or wrongly directed forces −5. Velocity or acceleration drawn on the ball −5. Air resistance drawn or named −5. −2 for each type of error: net force not zero, a force at the wrong point, two forces with one symbol or name, a missing name. Weight $G$, the ceiling's normal force $N$ (pointing **down**) and buoyancy. |
| Autumn 2025 (2025-09-17) | 4.1 Jalkaprässi | 3 p | Missing, extra or wrongly directed forces −3. −1 for each type: a missing name or symbol, a net force clearly not zero, two forces with one name. −1 for drawing on a picture other than the one given. Typical error: the normal force is missing. |
| Spring 2024 (2024-03-27) | 4 Voimat (arrow, curling stone, towed buoy) | 2 p per diagram chosen + 1 p per force named right | Choose the right diagram out of four, then name each force. A sliding curling stone has only weight, the ice's normal force and friction: no forward force. Gravity is named as the Earth's force, not the object's "own gravity". |
| Spring 2022 (2022-03-30) | 10.1 Vierivä lieriö | 4 p | No points if one force is missing, if there are extra forces, if one direction is wrong, or if components cannot be told apart from the forces. −1 for forces at the wrong point or clearly wrong arrow lengths. Friction is parallel to the surface, and on a rolling cylinder its direction can reverse later. Typical errors: the normal force not perpendicular to the slope, the slope drawn horizontal. |
| Autumn 2021 (2021-09-15) | 4.2 Ilmapallo seinällä | 2 p diagram + 2 p names | No points for the diagram if a force is missing or extra. −1 if the arrow lengths are not in proportion. Typical error: forces that act on the wall drawn on the balloon. |

What recurs in all five: every force present, no invented force, each direction right, each force named without
ambiguity, arrows in physically meaningful proportion and place, and no velocity, acceleration or component mistaken
for a force. That recurring core, not one exam's point values, is what Fysiikkalabra teaches and assesses.

## The method the student learns ("Voimakuvion piirtäminen")

The guide is taught in full in the chapter *Voimakuvio ja voimien yhteisvaikutus*. Earlier chapters prepare it and
later chapters use it. Its steps:

1. **Valitse kappale.** Name the object or system. The diagram shows forces that act **on** it, never forces that it
   exerts on its surroundings.
2. **Etsi vuorovaikutukset.** List what interacts with the object: the Earth (weight), each surface it touches
   (normal force, friction), each rope (tension), a push or pull, the air or water (resistance, buoyancy). Every
   force has a cause outside the object. Motion alone causes no force.
3. **Piirrä voimat.** One arrow for each force, starting on the object.
   - Weight points vertically down. In a uniform field, it acts at the centre of mass.
   - A normal force is perpendicular to the contact surface and pushes away from it. It does not always point up: a
     ceiling pushes down and a wall pushes sideways.
   - Friction acts along the contact surface. Its direction comes from the sliding, or from the tendency to slide,
     *relative to that surface*. It is not always opposite to the object's velocity.
   - Tension acts along the rope and pulls the object towards the rope.
   - Air resistance is opposite to the object's velocity relative to the air. Draw it only when the situation and its
     assumptions call for it.
4. **Nimeä voimat.** Use the course's notation. In FY4 vectors are bold: $\mathbf{G}$ is the weight, $\mathbf{N}$
   the normal force, $\mathbf{F}_\mu$ friction, $\mathbf{T}$ tension, $\mathbf{F}_\text{noste}$ buoyancy, and
   $\mathbf{F}_\text{v}$ the resistance of the air or water. Two forces of the same kind get distinct symbols
   ($\mathbf{T}_1$, $\mathbf{T}_2$). Other sources use other letters: what matters is that each force is named
   without ambiguity.
5. **Mieti suuruudet.** At rest and at constant velocity the net force is zero, so the arrows cancel. With
   acceleration, the net force points in the direction of the acceleration, which need not be the direction of the
   velocity. Do not invent precise sizes when the information does not fix them.
6. **Vain voimat.** Velocity, acceleration and displacement are not forces. If they help, draw them beside the body
   in their own style. The net force is not one more force. If a teaching figure shows it, it is labelled
   $\Sigma\mathbf{F}$ and drawn apart from the forces.
7. **Komponentit eivät ole uusia voimia.** Resolving a force gives two components that together *replace* the
   force in a calculation. On a slope, weight still points vertically down. Its components along and across the
   slope are drawn dashed, so they cannot be mistaken for forces.
8. **Liikeyhtälö.** Only now write $\Sigma\mathbf{F} = m\mathbf{a}$. Choose the axes, resolve the forces, and write
   the scalar equations $\Sigma F_x = ma_x$ and $\Sigma F_y = ma_y$ with signs from the diagram.

The order is the same in every worked solution: **valitse kappale → vuorovaikutukset → voimakuvio → akselit →
komponentit → liikeyhtälöt → ratkaisu**. A solution never writes $F = ma$ without first naming the forces and the
positive direction.

## Representations

- **Tilannekuva and voimakuvio are different figures.** A situation picture shows the objects, the surfaces and the
  motion. A force diagram shows the chosen object and the forces on it, nothing else. When the difference matters,
  draw the two separately, side by side or one under the other.
- **Physical-object diagram.** The object is drawn with its shape and contacts. Each force starts at its point of
  application: weight at the centre of mass, the normal force and friction at the contact surface, tension where the
  rope is attached.
- **Point-particle diagram.** When rotation does not matter, the object may be a point and every force starts at
  that point. This is correct too. Never teach that all forces must start at the centre of mass, or that a
  common-origin diagram is wrong. Follow the task's model.
- **Visual conventions** (`scripts/fbd.py`, every course):
  - a force is a solid red arrow with a filled head and a bold symbol;
  - a component is thinner, dashed and of the same colour, with an open head;
  - velocity and acceleration are thin blue arrows with an open head, drawn beside the body, never from it;
  - the net force is a hollow green arrow labelled $\Sigma\mathbf{F}$, away from the forces.
  
  Colour is never the only difference: the line style and the symbol carry the meaning too.
- **Lengths.** `fbd.py` draws every arrow at scale × force, so its length is right by construction. It refuses a
  diagram whose forces do not sum to $m\mathbf{a}$, or that breaks a direction rule. A deliberately wrong figure
  (a distractor, an error to find) says why with `wrong="…"`.

## Practice: four levels of independence

Each force chapter tags its tasks with `"fbd"` (inquiry activities, exercises, exit ticket). `coverage.py` reports
the tags and checks them against the chapter's plan in `curriculum.json`:

| tag | the student | form |
|---|---|---|
| `identify` | chooses which forces act on the object (and which do not) | `choice`, distractors such as a forward force "because it moves" or a force the object exerts |
| `select` | chooses the right diagram among several | `choice` with `"figure"` on each option (`layout: "figures"`); distractors each have **one** error: a missing force, an extra force, a wrong normal-force direction, a wrong friction direction, wrong relative lengths, velocity drawn as a force, or a reaction force on the wrong body |
| `error` | finds and corrects the error in a drawn diagram | `choice` or `explain` with a figure made `wrong="…"`; the title, labels and description must not give the error away |
| `draw` | draws the diagram without help, on paper | `explain` with `"draw": true` and `"model_figure"`: the page asks for the drawing, then shows the model diagram, why each force is there, the checklist and the equations |
| `equations` | writes $\Sigma F_x = ma_x$, $\Sigma F_y = ma_y$ from a diagram | `numeric` or exercise with a complete solution that starts from the diagram |

Multiple choice alone is no evidence that a student can draw a diagram. Every force chapter has at least one `draw`
task. Nothing tries to grade a drawn image automatically.

## Self-assessment and marking

Shared criteria (`lang/<lang>.json` "criteria", `competencies.json`), used in `draw` tasks and in Sovella rubrics:

1. `fbd_object`: the object or system is clear, and only forces on it are drawn.
2. `fbd_forces`: every force is there, and there is no invented one.
3. `fbd_directions`: every force points the physically right way.
4. `fbd_representation`: arrows start at a meaningful point, and each force has its own unambiguous name.
5. `fbd_magnitudes`: relative lengths are right where they can be known, and forces are not mixed with components,
   velocity or acceleration.
6. `fbd_equations` (separate): the equations follow from the diagram, with the axes and signs stated.

Adapt them to the task: add a `detail`, and leave out what the task does not ask. The diagram and the equations are
judged separately, so a wrong diagram does not erase unrelated correct work. That is, unless a verified
exam-specific rule says otherwise in exam-style practice.

Tell students what the exam evidence above shows: *in some YTL tasks* a missing, extra or wrongly directed force
cancels all of the diagram's points. While learning, the feedback names each mistake on its own.

## Reviewer checklist (mechanics lessons with an `"fbd"` plan)

The science reviewer checks every force diagram, model diagram, option figure and solution:

- [ ] all relevant interactions are identified, and the diagram shows the chosen object;
- [ ] every force has a physical cause, and its direction is right (normal force, friction);
- [ ] each force is named unambiguously, and the names in the text match the figure;
- [ ] third-law pairs are not on one diagram;
- [ ] velocity or acceleration is not drawn as a force;
- [ ] the diagram agrees with the motion and the stated assumptions (the net force and the acceleration);
- [ ] components are not double-counted with their force;
- [ ] the equations match the diagram (axes, signs, trigonometry).

The pedagogy reviewer checks:

- [ ] the chapter's `fbd` plan is practised at the planned levels, with at least one `draw` task;
- [ ] distractor diagrams each carry one recognisable error, and their feedback names it;
- [ ] no figure, title or description reveals what the student must work out;
- [ ] each solution draws the diagram before any equation.

## Accessibility

A figure's description lists what a sighted student sees. When the task is to judge the directions of forces, the
description lists each arrow's direction as drawn ("nuoli $\mathbf{N}$ osoittaa alas"). It never says whether that
is right. A model diagram's description, shown after the student commits, may explain it.

## Example situations and where they go

| | Situation | Chapter (curriculum id) |
|---|---|---|
| A | object at rest on a horizontal surface: $G$ and $N$ equal | *Voimakuvio* (fy4-5), already in *Newtonin toinen laki* (fy4-4) |
| B | object sliding after release: $G$, $N$, kinetic friction, no forward force | fy4-5 |
| C | object pulled and accelerating: pull, friction, nonzero horizontal net force | fy4-5 (pull at an angle: components) |
| D | inclined plane: $G$ vertical, $N$ perpendicular, friction along; components separate | *Paino, kitka ja kalteva taso* (fy4-6) |
| E | lift or a load on a rope: constant velocity, accelerating up, accelerating down | fy4-4, fy4-5 |
| F | two connected bodies: a diagram for each body, the rope's force on each | *Liikeyhtälö kytketyille kappaleille* (fy4-13) |
| G | falling with air resistance: speeding up vs terminal velocity; thrown up | *Ilmanvastus ja putoaminen ilmassa* (fy4-14) |
| H | helium balloon under the ceiling: buoyancy up, weight down, ceiling's normal force down | fy4-5 (challenge) |
| I | curling stone after release: no forward force | fy4-3 (first law), fy4-5 |
| J | friction on a rolling wheel or a walking foot need not oppose the motion | fy4-6 (qualitative, no rotational dynamics) |
