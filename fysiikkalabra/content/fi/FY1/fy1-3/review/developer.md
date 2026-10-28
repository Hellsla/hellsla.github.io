VERDICT: DONE

assets/sims/fy1/fy1-3/sim.js: dot plot now places dots on integer collision levels (one diameter each), then sets step = min(d + 1,5, (yLow - yHigh)/maxLevel) from the real top level, so the tallest stack ends at the plot top, below the T and mean labels. Dot x positions and simState keys unchanged; adds simState.dotTop (top edge of the highest dot).
tests/sims/fy1-3.json: three new assertions (sat 0 / sat 0,05 / sat 0 with sys +0,30, n = 40): dotTop is below the T and mean labels and inside the canvas. No existing assertion changed.
