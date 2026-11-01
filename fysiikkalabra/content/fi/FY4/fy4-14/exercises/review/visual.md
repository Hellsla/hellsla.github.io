VERDICT: FAIL
CONTENT-HASH: 3daf47c3361e7181

## Blocking
- [Major] solutions.md, all 12 `voimakuvio` diagrams (open-exercises-1280-1/2, L2-1280-1/2, L3-1280-5): every solution force diagram stretches to the full card width. Measured at 1280 px: L1-01 and L2-01 are 556 × 906 px, L1-03 is 736 px tall, and labels are about 60–90 px. At 390 px, L1-01 is still 460 px tall for two arrows. In L2-01 the box fills the card and the arrows run off the screen. The cause: `scripts/figlib.py` writes an inline `style="max-width:100%"`, which overrides `site.css` `.fig.fbd svg{max-width:min(100%,24rem)}`. — Why it matters: you cannot see the whole diagram or compare arrow lengths on one screen, and the solutions look broken. — Fix: make the 24rem cap win (`!important`, or no inline max-width on fbdspec output). The same template fix also clears the lesson finding.

## Polish
- [Minor] L1-05 diagram (open-exercises-1280-8): $\overline{F}_\text{r}$ is only an arrowhead at the box's lower corner, sitting on the ground line. Its label is above the $\overline{F}_\text{v}$ arrow, so a reader can pair the label with the wrong arrow. Fix: draw $\overline{F}_\text{r}$ with a visible shaft from the contact point, and put each label beside its own arrow tip.
- [Minor] L3-01 and L3-02 two-panel diagrams have no panel captions. Fix: add $\text{ennen}$ / $\text{heti jälkeen}$ and $\text{nousu}$ / $\text{lasku}$ above the panels, as the lesson figures do.
- [Minor] L3-02 Kaava: the inline "Laskussa $mg - F_\text{v} = ma_2$" breaks after the minus sign at 1280 px (L3-1280-3). Fix: write the two equations as one aligned chain per case, or break the sentence before "Laskussa".
- [Minor] L2-04 Vastaus is the only answer that states no direction. Fix: "$0{,}525\,\text{m/s}^2$ taaksepäin, liikettä vastaan, …".

## Checked
- open-exercises-1280-1, 2 and 8: L1-01, L1-02 and L1-05 at full size; the rest of L1 triaged from contact-5/6.
- open-exercises-L2-1280 via contact-6, including the L2-01 and L2-03 diagrams.
- open-exercises-L3-1280-3, 4 and 5: L3-02 diagrams, the ex-tangentti graph, and the L3-03 solution.
- ex-tangentti: the tangent passes the grid points (0; 2,0) and (2,0; 15,0) that the solution reads. Axes, units and ticks are correct, and the description matches the figure.
- Force-diagram sizes measured in a browser at 390 and 1280 px (all 12 solutions).
- The exercise texts were scanned for number–unit pairs outside LaTeX; I found none.

## Scores
illustrations 3 · typography 4 · Finnish 5 · accessibility 3
