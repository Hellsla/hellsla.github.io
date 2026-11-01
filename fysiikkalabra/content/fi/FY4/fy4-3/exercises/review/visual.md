VERDICT: FAIL
CONTENT-HASH: 1b72d20a59f51860

## Blocking
- [Major] solutions.md, the vertical-only voimakuvio blocks in L1-01, L2-03, L2-04, L3-01 and L3-03 (open-exercises-1280-1/2, L2-1280-5/6, L3-1280-4/5) — a diagram with only vertical forces is scaled to the full card width. It stands about 1100 px tall at 1280 px, with labels about 90 px high, roughly four times the size of the horizontal diagrams in L1-02, L1-04 and L2-02 next to it — why it matters: one force diagram fills more than a screen, splits the solution in two, breaks the visual hierarchy and makes the diagrams in the set inconsistent with each other — fix: give a narrow fbd viewBox a max-width so it renders at the same scale as the wide ones, for example limited by its viewBox width in the fbd renderer.
- [Major] L3-03 voimakuvio (L3-1280-5) and L2-04 (L2-1280-6) — in L3-03 the short $\overline{G}_\text{v}$ arrow lies entirely inside the rectangle. Its label sits under the box, right beside the shaft of $\overline{F}_\text{o}$, so it reads as that arrow's name. In L2-04 the head of $\overline{G}_\text{m}$ is inside the box and its label sits far to the right of it — why it matters: the reader cannot tell which force the label names, in the very task about which force acts on what — fix: start the small weight from the centre and let it reach below the box, offset sideways from $\overline{F}_\text{o}$ or $\overline{G}_\text{k}$. Put each label at the tip of its own arrow.

## Polish
- [Minor] L1-01 Järkevyys — after the task's "johto", the last sentence switches to "naru" ("koska naru voi vain vetää") — fix: "koska johto voi vain vetää".
- [Minor] exercises.json L3-02 — the neglect is said twice ("kitka tikkua vasten jätetään huomiotta" … "Tikun voima jätetään huomiotta.") — fix: one sentence, "Tikun voimat magneetteihin, kitka mukaan lukien, jätetään huomiotta."
- [Minor] for science: L1-02 Vastaus says "kolme merkitsevää numeroa" for $850\,\text{N}$, while L1-04 calls a similar value "kymmenen newtonin tarkkuudella" — fix: word the precision of these values the same way.

## Checked
- level 1: open-exercises-1280-1 and -2 at full size, the rest (-3 to -8) on contact sheet 4
- level 2: open-exercises-L2-1280-6 at full size, -1 to -7 on contact sheet 5
- level 3: open-exercises-L3-1280-5 at full size, -1 to -6 on contact sheets 5 and 6
- every voimakuvio in the set, compared for scale and label placement
- exercise texts and solutions.md read in the packet: no plain-text quantities found

## Scores
illustrations 2 · typography 4 · Finnish 4 · accessibility 3
