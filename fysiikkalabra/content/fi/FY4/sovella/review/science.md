VERDICT: PASS
CONTENT-HASH: 78c0faf56737d1db

## Blocking
None.

## Polish
- fy4-s1 c, voimakuvio: the dashed $\overline{G}_x$ is now drawn at 25 % of $G$ (true value 7 %), so $\overline{G}_x + \overline{G}_y$ no longer closes exactly on $\overline{G}$; the drawn resultant is about 14° off $\overline{G}$. The text alternative says that small forces are drawn longer; it could add "ja komponentit". This is not a physics error: the order along each axis is right and the figure is not presented as to scale.
- The $\overline{G}_x$ label still sits well to the right of its short arrow, which ends inside the body.
- Carried over: the spec uses wax A's friction (a note "voide A" would tie it to the text); s2 c $8{,}74$/$8{,}75$; s3 c "pääosin selkänoja"; the e intercept $0{,}43$ is at the edge of a fair reading.

## Checked
- Delta: the content hash is unchanged since round 1 (78c0faf56737d1db). Only the renderer changed (`scripts/fbdspec.py` `_keep_order`, `scripts/fbd.py` `component(k=)`). All judgements from round 1 carry over.
- Re-rendered with `python3 scripts/fbdspec.py show content/fi/FY4/sovella/solutions.md`, screenshotted in Playwright, and read the drawn lengths from `fbdspec.LENGTHS` on the forces' scale:
  - $G = 706{,}3$, $N = 704{,}6$ and $G_y = 704{,}6$, so the $y$ sum is visibly zero.
  - Along $x$: $F_\mu$ is lifted to the floor, $105{,}9$ (true $21{,}19\,\text{N}$). $G_x$ is $176{,}6$ (true $mg\sin\alpha = 49{,}27\,\text{N}$).
  - In the picture the downhill $\overline{G}_x$ (about 40 px) is clearly longer than the uphill $\overline{F}_\mu$ (about 24 px). The visible sum points down the slope, the same way as $\overline{a}$ (356°), and agrees with "painon rinteen suuntainen komponentti on suurempi kuin kitka". The round-1 blocking item is fixed.
- The text alternative still says "pienet voimat on piirretty pitemmiksi kuin mittakaava antaisi".
- `python3 scripts/test_fbdspec.py` passes, including the new test that $G_x$ stays longer than $F_\mu$ on a 4° slope.
- Physics of the diagram unchanged: the object, the three interactions ($G$, $N$, $F_\mu$), no driving force and no air resistance, the axes along the slope.
- The hash was 78c0faf56737d1db at the start and the end.
