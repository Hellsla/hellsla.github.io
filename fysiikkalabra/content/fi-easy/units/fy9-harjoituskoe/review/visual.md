VERDICT: PASS
CONTENT-HASH: ce391f02b226111a

Visual and editorial review, round 2, of the Selkeä suomi (fi-easy) translation of fy9-harjoituskoe. I built it with `python3 scripts/build.py fy9-harjoituskoe` (preview/fi-easy/fy9-harjoituskoe.html) and checked it in Playwright at 390 px and 1280 px, with every `details` open and every checkbox ticked.

Results: no console errors, no `.katex-error`, no visible `$`. scrollWidth equals the viewport at both widths. The figures render 298–358 px wide at 390 px (the inline force diagram and small plots 166–228 px) and are readable. figures.json is unchanged since round 1, so the decimal commas and the translated descriptions still hold. The osa1-7 item reads well at both widths.

Round-1 polish items: s4 d) now uses "on … Kuinka suuri teho muuttuisi silloin lämmöksi?"; s10 c) "kuin jos osa jousen massasta olisi punnuksessa"; s4 c) Järkevyys has "Teho kuitenkin jakautuu…". All fixed.

## Blocking
None.

## Polish
1. unit.md structure table at 390 px: the Pisteet cells "$4 \cdot 15$ p" and "$2 \cdot 20$ p" still wrap so that "p" sits on its own line, even with the no-break space now in place (Chrome allows a break after the KaTeX inline box). Moving the unit inside the math (`$4 \cdot 15\,\text{p}$`) fixes it, but check_i18n requires the formulas to match the source. So the fix must be made in the source first and then copied here. Cosmetic only.

## Shared issues
1. Same as Polish 1: content/fi/units/fy9-harjoituskoe/unit.md writes the table cells as `$4 \cdot 15$ p`, which wraps at 390 px.
