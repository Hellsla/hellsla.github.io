VERDICT: PASS
CONTENT-HASH: 74e9de790a996e86
SCOPE: delta proofreading fixes 2026-11-15

## Blocking
- none

## Polish
- Euro task — "$1{,}37 \cdot 10^{3}\,\text{€}$ eli pyöristettynä kymmeneen euroon, koska ... kahden merkitsevän numeron tarkkuudella" gives three figures while citing two; say "kymmenen euron tarkkuudella (desimaalisääntö vähennyslaskussa)".
- L2 percentage task — $1{,}6 \cdot 10^{2}\,\%$ discards the clean $156\,\%$; the point (two figures from $10\,\text{A}$, $16\,\text{A}$) is fine, but the earlier reading "exact settings" was also defensible.

## Checked
- Rounding of a maximum down (11 A, $10{,}4\,\text{kW}$, $7{,}6\,\text{A}$) and of a minimum up ($7{,}2\,\text{A}$) is now explained and the Järkevyys sums ($24\,\text{A}$, $24{,}9\,\text{A}$) are correct; this is a real pedagogical improvement.
- exercises.json answers $11{,}478$ (tol. $0{,}043$) and $10{,}4$ accept both the shown and the exact limit and reject $12\,\text{A}$; answers.py matches.
- Caption marker removal touches no task text.
