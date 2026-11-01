VERDICT: FAIL
CONTENT-HASH: 0e9004dded5fe968

## Blocking
- [Major] solutions.md L1-05, L2-02, L3-01 slope `voimakuvio` (open-exercises-1280-8, open-exercises-L2-1280-3, open-exercises-L3-1280-1) — the forces along the slope cannot be read:
  - $\overline{F}_\mu$ is a bare arrowhead on the box corner, with no line.
  - $\overline{G}_x$ is a stub of a few pixels hidden inside the box, at its centre.
  - The $\overline{G}_x$ label sits outside the box on the right, about 100 px from its arrow.
  
  Why it matters: in L1-05 the whole point is that $\overline{G}_x$ and $\overline{F}_\mu$ are equal and cancel, and in L2-02 their difference drives the acceleration. The figure shows neither, so the diagram does not support the "Kaava" line beside it (standard 7: forces and components clearly apart, labels that read).
  
  Fix: draw the slope-parallel forces at a larger scale, as L1-04 already does with "vaaka- ja pystyvoimat eri mittakaavassa", say so under the figure, and give $\overline{F}_\mu$ and $\overline{G}_x$ visible lines of equal length in L1-05. Then put each label at its own arrow.

## Polish
- [Minor] solutions.md L1-04 Järkevyys — "$6\,\text{s} : 0{,}8 \approx 7{,}5\,\text{s}$": the $6$ is a speed. Write $6\,\text{m/s} : 0{,}8\,\text{m/s}^2 \approx 7{,}5\,\text{s}$. (for science: wrong unit in the estimate)
- [Minor] solutions.md L3-03 Järkevyys — "$\tfrac12(v_1^2 - v_2^2) : a \approx 1232 : 20{,}5 \approx 60\,\text{m}$" drops the units in the middle, and the line above gives $\approx 20\,\text{m/s}^2$ while this one uses $20{,}5$. Keep the units and use one value.
- [Minor] figure `ex-hissi` (L3-02, open-exercises-L3-1280-2) — the y-axis numbers are every $200\,\text{N}$, but the task needs $650\,\text{N}$ and $800\,\text{N}$. Number the ticks every $100\,\text{N}$, as `hissi-kuvaaja` does.
- [Minor] solutions.md L1-03, L2-03 — "Voimakuvio" comes before "Periaate", while every other solution has Periaate first. Use one order.
- [Minor] exercises.json L3-03 — "Kuinka suuri on ilmanvastus keskimäärin tällä matkalla, jos se oletetaan vakioksi?" Both "keskimäärin" and "oletetaan vakioksi" are there. Keep one: "Kuinka suuri on ilmanvastus, jos se oletetaan vakioksi tällä matkalla?"

## Checked
- contact-4, -5, -6 for triage
- open-exercises-1280-4, -5 (L1-03 diagram on a slope), -8 (L1-05); L1-01, -02 and -04 in the contact sheet
- open-exercises-L2-1280-3 (L2-02 diagram); L2-01, -03 and -04 in the contact sheet
- open-exercises-L3-1280-1 (L3-01 two-panel diagram); L3-1280-2 cropped (`ex-hissi` graph); L3-02 and -03 in the contact sheet
- PLAIN_QTY scan of exercises.json and solutions.md: no number with a unit in plain text

## Scores
illustrations 3 · typography 4 · Finnish 4 · accessibility 4
