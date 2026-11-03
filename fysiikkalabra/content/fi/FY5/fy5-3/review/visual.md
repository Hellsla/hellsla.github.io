VERDICT: FAIL
CONTENT-HASH: b8e74f9726d4330d

## Blocking
- [Major] simulation, `sim-390`, `sim-1280`, `exp-koe-1-390`, `exp-koe-3-390` — the "Nopeuden muutos" panel (the sim's point: $\Delta\overline{v}$) is drawn with labels $\overline{v}_1$, $\overline{v}_2$, $\Delta\overline{v}$, $\Delta t = T/12$ at about 8–9 px and a vector triangle about 70 px tall inside a 366 px canvas; at 1280 px it floats in a narrow strip with large empty space, at 390 px it leaves about 80 px of dead space below, and in koe-3 the $\Delta\overline{v}$ label touches the canvas edge — a student cannot read which arrow is which on a phone, and this panel carries the lesson's central idea — fix: scale the panel up (arrows about 1.5 times longer, labels at least 12 px at 390 px) and keep the labels clear of the canvas edge.

## Polish
- [Minor] lesson `Esimerkki` step 7 (`example-390-2`) — the Järkevyys sentence is cut into five fragments by chain boxes, with nested fractions at about 8 px — write the cross-check as its own sentence ending in the chain.
- [Minor] `exit-ticket` answer 2, `open-exit-1280` — the inline chain "$9{,}0\,\text{cm} : 3{,}0\,\text{cm} = 3{,}0$" wraps after the colon ("inline maths stays on one line") — shorten the sentence before it or turn it into a separate line.
- [Minor] lesson Kaava paragraph — "$1\,\text{min} = 60\,\text{s}$: $45\,\tfrac{1}{\text{min}} = …$" lets the colon read as a ratio, and the legend writes "(1/s)" while the text stacks $\tfrac{1}{\text{s}}$ — use "Esimerkiksi" and one unit form.
- [Minor] `exp-koe-3-390-1` — the opened optional Koe 3 text has no side padding (flush to the edge); table header "v irti (m/s)" does not match $v_\text{irti}$ in the text; `dv` figure and sim draw $\overline{v}_1$ in a paler blue than $\overline{v}_2$ without saying why.
- [Minor] `inquiry.json` wording — "kahdestoistaosakierroksen takaa" is clumsy ("kierroksen kahdestoistaosan takaa"); "Mallin arvot kumoavat tämän:" opens five feedback texts (mechanical); task prompts write the answer unit plain ("yksikössä m/s") while solutions write $\text{m/s}$.

## Checked
- contact-1; fig-1 (hero) and figs 2–5 (option figures, `open-ennusta-1280`), figs 6–9 (`tangent`, `release`, `dv`, `two-radii`: geometry, equal vector lengths, 2:1 ratio checked from source); top-390, top-1280, intro-1280
- sim-390, sim-1280, lab-1280-1, exp-koe-1-390, exp-koe-3-390-1, stage-tutki-390-1/2
- example-390-1/2; theory-1280-1..3, fig-row-1280, stage-selita-390-1/3; stage-ennusta-390-1/2; stage-sovella-390-1/2
- open-tarkista-1280-1..3, stage-tarkista-390-1, open-exit-1280
- Not opened: contact-2..6, selita 2/4/5, tutki-3, L1 parts 2/3/5.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 3
