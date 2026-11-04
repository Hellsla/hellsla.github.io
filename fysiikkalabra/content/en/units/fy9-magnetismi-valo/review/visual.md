VERDICT: FAIL
CONTENT-HASH: b3d1941baccbd2d3

# fy9-magnetismi-valo (en): visual & editorial review of the translation, round 2

Rebuilt with `python3 scripts/build.py fy9-magnetismi-valo` → preview/en/fy9-magnetismi-valo.html and checked in
Playwright at 390 and 1280 px with every details element opened: no page errors, no KaTeX errors, no raw `$`,
scrollWidth 390 / 1280 (no horizontal scroll), `html lang="en"`, decimal point throughout.

## Blocking
1. NOT FIXED. unit.md "Key idea", figure `kartta` (concept map): the three branch heads are still drawn in Finnish,
   **voimat kentässä**, **induktio**, **valo** (screenshots at 390 and 1280). The translator did its part: figures.json
   now has "voimat kentässä": "forces in a field", "induktio": "induction", "valo": "light". But
   `scripts/figlib.py` `translate()` still matches only `\\(?:text|mathrm|textsf)\{`, not `\textbf{}`, so these
   entries are never applied (`units.py figures --check` reports "up to date" with the Finnish heads), and
   hand-editing the SVG would fail that check. Fix outside this reviewer's scope (scripts/ may not be edited here):
   add `textbf` to the regex in `figlib.translate` (and to MISSING reporting), then run
   `python3 scripts/units.py figures fy9-magnetismi-valo --lang en`. No change to the translation files is needed.

## Polish
2. Figure `ympyra` at 390 px: the $r = mv/(qB)$ label in the top-right corner is close to the figure's expand
   button. Same in the source; a figures.py change would fix both languages.

Fixed since round 1: Polish 3 (`ympyra` now "$\overline{B}$ into the page", label box widened, fits at 390),
Polish 4 (lt-4, rata, s2 wording).

## Shared issues
- `scripts/figlib.py` `translate()` ignores `\textbf{}`: same Finnish heads in every FY9 concept map (aallot,
  energia, kaasut, lampo, moderni, sahkokentta, sailymislait, tasavirta, magnetismi-valo) and fy14-fusion-reactions,
  in en and fi-easy.
