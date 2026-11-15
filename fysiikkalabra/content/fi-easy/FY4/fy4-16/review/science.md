VERDICT: PASS
CONTENT-HASH: 40b05f162c9c2e30

## Blocking
None.

## Polish
1. lesson.md:407 — "Liikkuvassa hississä lattian tukivoima on liikkeen suuntainen" sounds as if the force points the way the lift moves. When the lift goes down, the force points the other way, and the next sentence repairs that only afterwards. — Write "liikesuoran suuntainen" (along the line of motion) instead.

## Checked
- inquiry.json:19 hook: the new wording ("seuraa vaa'an lukemaa, kun hissi lähtee ylös, kulkee ja pysähtyy") makes no physics claim. It no longer gives away the scale's behaviour before the prediction. Nothing it says contradicts the force-plate graph (650/589/550 N).
- inquiry.json:178 conclusion prompt: "lähes" was dropped, so the sleds now stop "yhtä kauas". This matches the model $x_1 + x_2 = h/\mu$: the slope table sums to exactly 60,0 m on both sides, under the conditions lesson.md already states (constant μ, no air drag, short bend). It also matches the hook, the question, the Miksi line and the section "Miksi pulkat pysähtyvät yhtä kauas". No text anywhere still says "lähes".
- lesson.md:407: the support force's work is right now. It does no work on a body sliding along a fixed surface. In a moving lift its work is positive going up and negative going down. This closes Polish 1 of my previous report. Polish 2 (index notation) was not in this diff and is not judged here.
- The content hash is the same at the start and the end (40b05f162c9c2e30, fi-easy).
