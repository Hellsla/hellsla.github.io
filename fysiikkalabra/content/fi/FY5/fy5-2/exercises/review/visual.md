VERDICT: FAIL
CONTENT-HASH: d390f27b68875a74

## Blocking
- [Major] exercises.json fy5-2-L1-01 (sorkkarauta; open-exercises-1280-1) — the task was rewritten to ask for a force in newtons (answer 960), but the entry still has `"unit": "m"`, so the answer box shows "m" next to a force; solutions.md and the shown answer say $960\,\text{N}$ — a student is told to enter a force in metres, and an answer typed with the right unit may be refused — set `"unit": "N"` for L1-01 (lessons/FY5/fy5-2/answers.py already computes 960 N).

## Polish
- [Minor] new figure `hylly` (L2-03, L2-1280-3) — geometry is right: the plumb line passes through P and the centre of mass, $\alpha$ is marked, and the $\tfrac{d}{2}$ and $\tfrac{h}{2}$ legs are dimensioned. But $\tfrac{d}{2}$ is dimensioned on the floor below P, while the leg it names runs along the tilted base; a short dashed leg along the base would be clearer.
- [Minor] solutions.md L2-03 Kaava — one 100-word paragraph with four "koska/joten" steps is heavy to follow on a phone; split it into the construction and the tangent step.
- [Minor] new figure `kyltti` (L3-02, L3-1280-2) — a clear figure: the wire attaches above the hinge, the $30{,}0^\circ$ arc is correct, and the sign hangs from the rod end. It could mark $\overline{T}$ with an arrow, but the exercise does not need it.

## Checked
- Delta round 2 (exercises hash d390f27b68875a74): L1-01 with the Annettu, Kaava, Sijoitus, Vastaus and Järkevyys blocks (open-exercises-1280-1), the new `hylly` figure with the L2-03 task (L2-1280-3), and the new `kyltti` figure with the L3-02 task (L3-1280-2).
- Read from the diff: the L1-03 wording "vaakasuunnassa", the L2-04 joint-force sentence, the L3-01 Järkevyys rewritten with units, and the single Vastaus line in L2-02. No plain quantity appears outside maths.
- Solution rows align at "=", fractions read well, and units are upright.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 3
