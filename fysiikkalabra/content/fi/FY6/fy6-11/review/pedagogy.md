VERDICT: PASS
CONTENT-HASH: f9ea5baa5155e9c8

## Blocking
(none)

## Polish
- Slot goal "potentiaalin käsitteet" — the lesson uses only the voltage U between plates; potential is never named. Fine if the next lesson takes it, but then the lesson's `learn` list should not suggest it, and one line ("jännite = potentiaaliero, ks. seuraava luku") would help the student who meets the word in the LOPS goal.
- inquiry.json workload — three required experiments plus an optional fourth, two numeric questions inside experiments, three predictions-and-explain steps, Etsi virhe, siirto, two required checks, and a theory section with six topics (field, test charge, field lines, plates, E = U : d, particle motion). It fits a lesson only if the student does not do every item; consider making koe-3's numeric question or siirto optional.
- Sim at 1280 px (shot #52): the five sliders sit in a ragged 3 + 2 grid with labels at different heights (d, h); line them up in one row each.
- lesson.md "Ilmanpuhdistin" — the paragraph says the particles "saavat varauksen" in a first stage but never says why the plates are not simply charged by the same stage; one clause ("varaus on sama kuin kentässä, jonka voima sitä kuljettaa") is optional, not required.
- tarkistus-2 (figure abc): B sits near the positive plate with its label touching the plate; move the label so the letter is readable at 360 px.

## Checked
- Opening question (why dust goes to the plates; does the force depend on position) is answered by ennuste-1/koe-1 and the Ilmanpuhdistin text; hook and tarkistus-3 close the loop.
- Prerequisites (Coulomb, V = J/C, Newton II) are in `prior`; the E = U : d derivation from W = qEd = qU is one step per sentence and uses only those.
- Predictions 1 and 2 are refuted or supported by koe-1 and koe-3 with min 3; each wrong option's feedback repairs its misconception (Coulomb's r^-2 misapplied to plates, "more space more force") and cites model values.
- The sim computes the field from plate charges, so the homogeneity emerges rather than being typed in; koe-4 shows the end effects.
- Worked example (oil drop): eight stages, one step each, answer 3,0 e verified (4,8e-19 C).
- Etsi virhe (cm not converted) and siirto (inkjet, 1 333 m/s^2) verified; mistake values match real slips.
- Tarkista: concept check on electron direction has misconception distractors; figure check abc needs the figure and does not give the answer in its description.
- Figures: field-line and plate figures are recognisable, colours (green field, red force, blue velocity, orange acceleration) follow the house rules and are never the only cue.
- Exit ticket tests E = U : d and why lines do not cross, both in the lesson.
