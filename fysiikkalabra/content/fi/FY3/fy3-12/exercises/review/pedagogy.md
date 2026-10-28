VERDICT: PASS
CONTENT-HASH: df8f923b0fdab0bc
## Blocking
## Polish
- exercises.json fy3-12-L1-01, L1-02, L1-03, L2-01, L2-02, L2-03, L3-03 — within one text the temperatures, U-values and powers are LaTeX but areas ("45 m²", "28 m²", "130 m²", "14 m²", "100 m²") and other quantities ("0,11 €/kWh", "2,0 m²") are plain; convert all numbers with units per task for a uniform look, e.g. "pinta-ala on $45\,\text{m}^2$".
- exercises.json fy3-12-L3-01 — "10,0 tunnissa" and "14 tunnin" are plain beside LaTeX values; same fix.
- solutions.md L3-03 Järkevyys — "joten säästö on silloin suurin" is ambiguous (sähkö- vai lämpösäästö?); "joten sähkösäästö on silloin vielä suurempi kuin laskettu".
## Checked
- Delta (numbers with units converted to inline LaTeX, plus the L3-03 Periaate and Järkevyys: pumppu "luovuttaa" sisälle lämpöä, ulkoilmasta tulee muu osa): no number, unit or answer changed.
- Case endings after math units read correctly (`$96\,\text{W}$:n`, `$30{,}0\,\%$:sta`, `$0{,}35\,…$:sta … $0{,}10\,…$:iin).
- The wording "luovuttaa" is consistent with the lesson's lämpökerroin definition (lämpöteho / sähköteho).
- L3-03 answer 984 kWh vs the solution's rounded 980 kWh lies within tolerance.
- Levels 5/4/3 unchanged; none repeats the worked example (wall plus windows).
- No captures available; phone readability rests on the passing layout checks.
