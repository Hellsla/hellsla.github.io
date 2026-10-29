VERDICT: FAIL
CONTENT-HASH: 5d6ddd44c4b68caf

## Blocking
- lesson.md "## Esimerkki" (stages 2-3) — the worked example, the course's model solution, goes from the principle in words to $\Sigma F_x = 2F_1 - F_\text{v} = 0$ with no force diagram, against docs/force-diagrams.md ("diagram before any equation in every solution"). Add a fbd.py voimakuvio of the aircraft (rectangle, $\overline{G}$, nostovoima, two $\overline{F}_1$, $\overline{F}_\text{v}$) in the "Periaate" stage, before "Kaava ratkaistuna".
- inquiry.json "siirto" solution — starts "Kaava: $F_{AP} - F_i - F_r = 0$" without a "Voimakuvio:" step. Add the trailer as the chosen body with its three horizontal forces before the formula.

## Polish
- inquiry.json pred-1 / exp-1 — the prediction is about the frictionless case, but reveal `min: 2` accepts any two rows (matto + puulattia), which seem to support the wrong options; the "Oikein" feedback then quotes values the student never measured. Make the frictionless row required, or word the prediction for any surface.
- Simulation at 390 px — the graph and force diagram sit side by side at about half size; their labels are about 7 px. The force diagram is the evidence the experiment asks for: stack them below 500 px.
- lesson.md Ydinajatus — "tukivoima" and "kitkavoima" are used (and drawn) before they are named; add half a sentence each (slot says no complete diagrams yet).
- Workload — core path has 2 predictions, sim, experiment with numeric task, explain, interpret, example, error item, transfer, 12 exercises, 3 checks, exit ticket: about an hour and a half. Make "Etsi virhe" optional.
- inquiry.json check-3 — the lamp task asks for diagram and reaction forces at once; "Kirjoita sitten" could be a second, optional step.

## Checked
- Opening illustration matches the Miksi question (released stone, sweepers, house), FY3-level detail; labels LaTeX.
- Layout at 390 and 1280 px from captures; one column, figures beside their paragraphs; 768 via passing test.
- Chapter names used, no ids visible.
- Understanding before formulas: curling, friction experiment, sensor graph; third-law pairs on separate diagrams.
- Force plan: identify tasks present, draw task (check-3) with model figure and criteria; no figure or title gives the answer.
- Check distractors are misconception-based, with feedback that repairs them; Finnish and case endings fine.
