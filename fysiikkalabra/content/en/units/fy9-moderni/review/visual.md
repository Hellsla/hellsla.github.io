VERDICT: FAIL
CONTENT-HASH: c37db221e87fd6f8

Visual & editorial review, round 2, of the English translation of fy9-moderni. Preview rebuilt with
`python3 scripts/build.py fy9-moderni` → preview/en/fy9-moderni.html and checked in Playwright at 390 and 1280 px with
every details element opened: scrollWidth 390/1280 (no horizontal overflow), no console errors, no KaTeX errors, no
raw `$`. Round-1 Polish 2 (subscripts) is fixed: the concept map draws `hf = E_\text{u} - E_\text{l}`.

## Blocking
1. NOT FIXED from round 1. unit.md, concept map `<svg data-fig="kartta">`: the three branch headings are still
   Finnish, `\textbf{fotoni ja atomi}`, `\textbf{ydin}`, `\textbf{säteily ja ihminen}` (seen in the 390 px
   screenshot). Cause unchanged: scripts/figlib.py `translate()` replaces only `\text{}`, `\mathrm{}`,
   `\textsf{}`, not `\textbf{}`, so no figures.json entry can reach these labels, and a reviewer may not edit
   scripts/. Done in this round: the three translations are now in figures.json
   (`"fotoni ja atomi": "the photon and the atom"`, `"ydin": "the nucleus"`,
   `"säteily ja ihminen": "radiation and people"`). Remaining fix: add `textbf` to the regex in figlib.translate
   (shared, below), then redraw with `python3 scripts/units.py figures fy9-moderni --lang en` (or translate_kit
   apply) and rebuild. The SVG was deliberately not hand-patched: the next redraw would overwrite it.

## Polish
2. sovella/solutions.md keeps `### Yleisiä virheitä` / `### Hyväksytään myös`: correct, they are parse keys
   rendered as "Common mistakes" / "Also accepted". No change.

## Shared issues
- scripts/figlib.py `translate()` (line 56): `\\(?:text|mathrm|textsf)\{` → add `textbf`. Every FY9 unit's
  concept map in content/en/units/ still shows Finnish `\textbf{}` headings (aallot, energia, kaasut, lampo,
  magnetismi-valo, moderni, sahkokentta, sailymislait, tasavirta, voimat, ympyraliike).
