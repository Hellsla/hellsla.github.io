VERDICT: DONE

- sim.js: the animation now follows the transferred heat q = u·Q_end, one side at a time. Water cools to 0 °C, freezes, then cools as ice. Ice warms to 0 °C, melts, then the melt water warms. No liquid shows below 0 °C, no ice above it. The chart axis autoscales to 0–50, 0–100 or 0–250 kJ.
- tests/sims/fy3-14.json: four per-frame assertions over full runs (cases 1–4) for the above (the old sim fails them). Two autoscale assertions. Label and calc assertions updated to the new scale; none loosened. 63 pass.
- lesson.md: vaihe 4 reads 6,05 °C ≈ 6,0 °C. Result "below the midpoint". The all-water-freezes exception is in the misconception and the summary. Figure 3's dot is now "alun lasi" (explained in the text). Figure 2 shows its data visibly in LaTeX (ice −10 °C).
- inquiry.json: the hook is a qualitative glass of juice. Ennuste 2's correct option reads "Noin 13 g enemmän …". The howto's pale-segment sentence is fixed. The Koe headers read "jää (g)". The calc text gives the scale rule.

All checks ok; layout ok at 360, 1280 and 1920 px. At 768 px, lab-side is 18 px too wide, as in fy3-9: a shared-template issue, not fixable here.
