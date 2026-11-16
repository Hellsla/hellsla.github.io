VERDICT: FAIL
CONTENT-HASH: 3553a67e94c63318

## Blocking
- [Major] solutions.md:7 (L1-01 Sijoitus; captures fy5-5-ex-L1-01-390-0, fy5-5-ex-L1-01-1280-0) — the one equation is set in two unlike halves at both widths: a white formula box that holds only "F = 6,674 · 10⁻¹¹ N·m²/kg² ·" (ending in a dangling "·"), and below it, outside the box, on the page background and in larger type, "[70 kg · 55 kg / (0,80 m)²] = 4,015 · 10⁻⁷ N= 0,4015 µN". The builder lifts the leading inline formula of the step into an eq-chain and leaves the other three pieces as a paragraph — the student reads a finished boxed line and then a separate equation that starts with a fraction; the neighbours L1-02, L1-04 and L2-08 show the same calculation whole in one box, and round 2's version of this step did too — write the step as its neighbours are written (solutions.md:19–23): `$$\begin{aligned} F &= 6{,}674 \cdot 10^{-11}\,\tfrac{\text{N}\cdot\text{m}^2}{\text{kg}^2} \\ &\quad \cdot \dfrac{70\,\text{kg} \cdot 55\,\text{kg}}{(0{,}80\,\text{m})^2} \\ &= 4{,}015 \cdot 10^{-7}\,\text{N} \\ &= 0{,}4015\,\mu\text{N} \end{aligned}$$`. The inline pieces suit a sentence (as in the lesson's etsi-virhe prompt), not a step that consists of the formula alone.

## Polish
(none)

## Checked
- Round 3, delta: the one re-set chain, solutions.md:7. The content hash changed while I worked (8f25c3eda4431789 → 3553a67e94c63318); every capture named here was taken after that edit, from the rebuilt preview.
- Own captures from preview/fy5-5.html?ratkaisut=1, levels and solutions opened, in /tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/vis3-fi-1: fy5-5-ex-390-1.png, fy5-5-ex-1280-1.png (L1-01 beside the untouched L1-02, L1-04, L2-08), and at double scale fy5-5-ex-L1-01-390-0.png, fy5-5-ex-L1-01-1280-0.png.
- Nothing clipped, scrollWidth 390 and 1280.

## Scores
illustrations 5 · typography 3 · Finnish 4 · accessibility 4
