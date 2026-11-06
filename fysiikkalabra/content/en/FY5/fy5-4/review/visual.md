VERDICT: PASS
CONTENT-HASH: 0f799fe974011c12

## Blocking
- none

## Polish
- none

## Checked
- delta review (English, fy5-4): only figures.json changed (new entries for option figures used in the exercise sets, which already passed); lesson text unchanged (git tree clean for the lesson files).
- Rebuilt with `python scripts/build.py fy5-4`; page opened at 390 px after its own scripts ran: scrollWidth = clientWidth = 390 (no horizontal overflow), no KaTeX error nodes, no page errors.
- Opened a 390 px contact sheet of every visible lesson figure (hero illustration, vector/path figure, road-bend diagrams, graphs, force diagrams for fy5-4; swing hero, spring/pendulum diagram, reference-circle, sine graphs and simulated-data graph for fy5-7): all render complete, unclipped, labels in KaTeX, colours per convention, in the language of the page (aria-labels in English, decimal comma in Finnish axes, decimal point in English).
- The lesson's own figures are unchanged in this language; the new figure texts only add entries and replace none that the lesson shows.
- The screenshot script (scripts/screenshot.py) crashes on a stage heading in this lesson page, so captures were made with a separate script; review/shots not refreshed.

## Scores
illustrations 5 · typography 5 · Finnish 5 · accessibility 5
