VERDICT: PASS
CONTENT-HASH: fe414bd9a9a971c6

## Blocking
None.

## Polish
- All three new "Stop and think" boxes (cottage voltage, series power, terminal voltage) sit after a paragraph that already states their answer: "so the voltage across each is 12 V", "In series the larger resistance gets the larger power", "part of the emf is used inside the battery, so the terminal voltage is smaller". The student can copy the reply from the line above, so the box checks recall, not reasoning. In a review unit that is acceptable. A better placement is before the stating sentence, or a prompt that asks for something new (for example "What would the voltage be if the two were in series?"). If the Finnish unit has the same placement, change both together.
- Box 1 says "cooler" where the text, figure and aria-label say "cool box". Use "cool box".
- Box 2 gives the answer "the one with the greater resistance" but never says the current is the same before it uses that fact. That is fine, since the reason is in the answer. The same-current idea could be named in the question ("the same current flows through both").
- The new mokki, piiri and hero figures are pictures (webp) with unchanged LaTeX labels and aria-labels. The descriptions give the same data, so a reader who cannot see the figure loses nothing.

## Checked
- Scope: the three new `pysahdy` boxes in unit.md. Each is short, is placed beside the figure or paragraph it follows, and is on the right topic for the course's learning path (parallel voltage, series power, internal resistance). Each has a one-line model reply with a reason.
- Terms: "emf", "terminal voltage", "internal resistance" and "parallel" are used consistently. Number-and-unit LaTeX is correct in the boxes.
- The inquiry.json s7 model answer is only split into paragraphs. The content is the same, and each paragraph is under 120 words.
- Sovella set (8 tasks: heater, scooter, torch batteries, safety claims, Ohm test, water heater, filament lamp, three resistors): the titles name no model. Each task has 3–4 parts with rising points. The tasks are varied: calculation, data and graph, claim evaluation, and series and parallel circuits. Solutions and common-mistakes sections exist for every task. The deterministic check is OK, and the Finnish set already passed. I did not re-judge the task content and found nothing in the translation diff that touches it.
- I did not open captures. The page layout and figure legibility are for the visual reviewer.
