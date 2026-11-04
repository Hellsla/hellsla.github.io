VERDICT: PASS
CONTENT-HASH: 2e8775fbbc612d04

## Blocking

## Polish
- lesson.md (Common misconception) — carried over from round 1: "used in sterilisation and medicine ... not enough to change nuclei" holds for sterilisation and diagnostics; 15–18 MV radiotherapy makes some photoneutrons. C at this level.

## Checked
- Round-1 polish done: assets/sims/fy8/fy8-12/sim.js:149 uses `__('gm_putki')`; en.json gives "GM tube"; shot fy8-12-sim-1280.png shows it.
- sim.js diff is that one label line: source, barrier, half-value thickness, background and `simState` unchanged, so the experiments' values from round 1 stand.
- Scripted comparison against content/fi: every number of lesson.md, inquiry.json, exit-ticket.json and figures.json matches; the only aria-label difference is a digit inside the HTML entity `&#x27;` (apostrophe), not data.
- Round-1 recomputations unaffected: 5,49 MeV / 34 eV = 1,61·10⁵; 5,5 mm · log2 20 = 23,8 → 24 mm; Al 25 mm → 0,60 (μ ≈ 0,21 1/cm at 662 keV); apron 0,5^(0,50/0,12) = 5,6 %; check 2 halvings 800 → 400 → 200 → 50.
