VERDICT: PASS
CONTENT-HASH: f2fded5d7d8d5960

## Blocking

## Polish
- meta.json:30 (key_concepts, spektri) — "Värien viuhka, joka syntyy, kun prisma erottaa valkoisen valon väreiksi" defines the term by one example, while glossary.json and the fy7-9 box define spektri as the distribution of radiation by wavelength. True as stated and follows lesson.md:94, so not blocking; better: "Valon jakautuminen värien eli aallonpituuksien mukaan. Prisma erottaa valkoisen valon spektriksi…" so the two chapters' boxes say the same.
- lesson.md:310 (carried) — aria-label "n = 1,332" vs $n = 1{,}3315$ in the text.

## Checked
- Re-review of the new "Luvun tärkeät käsitteet" box; rest unchanged since the PASS (hash f2fded5d7d8d5960 at start and end).
- Dispersio: n depends on wavelength; violet's n larger in water and glass (normal dispersion, visible) → violet refracts more. Matches glossary.
- Spektri: colours already in white light, prism does not colour it (Newton, lesson.md:127).
- Poikkeamakulma: δ defined as turn from the original direction; violet's δ larger in a glass prism — correct.
- Sateenkaari: refraction in, reflection from the back surface, refraction out; primary red ≈ 42° (42,3°) from the antisolar point — matches glossary and the lesson's numbers.
- Vastapiste: point opposite the sun at the head's shadow; the bow is an arc centred on it.
- check_i18n.py fi-easy: 0 errors. Box at 390 px: no overflow, $42^\circ$ and δ render.
