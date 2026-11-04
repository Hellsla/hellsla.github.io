VERDICT: DONE
Round-1 fixes (science, visual blocking; listed polish).

- sim.js: the field-line step is now Φ(20, 20, 3) : 6,5, so no line sits exactly on the receiver wire. At z = 3 mm, R1 = 20 mm six lines are drawn dark and the readout says 6. At 20 mm it is still 1. tests/sims unchanged and passing.
- figures.py, charger: the same step of 6,5. Labels $\text{puhelin}$ (both phones), $\text{lähetinkäämi}$ (left) and $\text{vastaanotinkäämi}$ (right), all at 24 px with leaders. The aria-label names the green triangle. Height 350 → 380.
- figures.py, hob: eddy-current marks are now violet #7048e8, and the coil's current marks are copper. The aria-label says so. The "teräskattila" label moved 8 px left.
- lesson.md: one sentence before the charger figure explains the green lines, the triangle and the darker lines. The decibel clause now says that losses in series add in dB while their power ratios multiply. The Järkevyys sentence no longer starts with a number. Figures regenerated.
- inquiry.json: Φ0 headers are `$\Phi_0\ (\mu\text{Wb})$`. In ennuste-kela, the koe-2 intro (now adds 35 mm), the johtopäätös model and criterion 3, the voltage grows to about 35 mm (1,25 V) and then falls, so each distance has its own best coil size (values from lesson-answers.py sim-e0-35-20mm). Both check-1 feedbacks now say "samalla kelan virralla", and "eikä pohja lämpene" became "pohja lämpenee vain vähän".
