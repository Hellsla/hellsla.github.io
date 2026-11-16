VERDICT: PASS
CONTENT-HASH: 314e06f209dcea75

## Blocking
(none)

## Polish
- content/en/FY2/fy2-1/lesson.md:98 — the caption reads "potential energy of water turns into kinetic energy in the turbine". The more exact chain is potential energy of the water → kinetic energy of the water → rotational kinetic energy of the turbine → electrical energy in the generator. At FY2 level this is a fair simplification (C), and it matches the Finnish caption word for word. If you change it, the fix is "into kinetic energy of the water and the turbine", made in the Finnish caption too.

## Checked
- Delta only. The hash was 314e06f209dcea75 (`--lang en`) at the start and at the end.
- sim.js: the diff changes only where the 0 and 1 000 tick labels sit on the E axis and whether their tick mark is drawn (textSize, textWidth, line, lab). It changes no model value, simState, adapter or control, so the model values I passed earlier stand.
- Seven-forms table: each row says the same physics as the list it replaces. Potential energy depends on position and mass, kinetic energy on motion and mass (none at rest), thermal energy on particle motion and interactions. Chemical energy is in bonds and released in combustion and metabolism. Radiant energy also travels through a vacuum. Electrical energy is transferred by a current. Nuclear energy is released in nuclear reactions (power plant, Sun). The examples are correct, and the terms follow the glossary and FY2 scope.
- The paragraph moved below the table still keeps thermal energy apart from temperature, defines heat as energy in transfer and says the net transfer runs from warmer to colder (guardrails "Heat is energy in transfer", "Net transfer").
- Photo hydropower-plant-aerial.webp (1600×1067): I looked at it. It shows a river, a car park, transformers and transmission towers, as its alt text says. It is used as a photo, not a measured or to-scale figure, and it claims no data.
- The English caption and alt text match the Finnish version.
