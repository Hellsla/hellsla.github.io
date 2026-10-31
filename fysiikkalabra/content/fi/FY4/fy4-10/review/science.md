VERDICT: PASS
CONTENT-HASH: 3ce5496422f13f04

## Blocking

## Polish
- lessons/FY4/fy4-10/lesson-answers.py:12 — the new comment says this file uses "fourth-order Runge–Kutta (RK4), as in model.js". That is not true. Lines 28–32 are a velocity Verlet step (half kick, drift, force, half kick). Only model.js uses RK4. Fix: "Velocity Verlet steps of 0,2 ms here (model.js uses RK4 with the same step)". The numbers are not affected: they agree with the closed forms below.
- assets/sims/fy4/fy4-10/sim.js:36–48 (fitRun) — carried over from round 3. On a narrow screen the arrows can get short at the worst settings (scale down to 0,39 of the default). The experiment settings are not affected.
- inquiry.json `simulaatio.calc` — carried over: in the kimmoton case, E_sis also counts the bumper's energy when it relaxes off contact.
- sim.js:224, 242 — carried over: the label *nyt* could read *jälkeen* once the run has ended.

## Checked
- The diff since b0bde749 in assets/sims/fy4/fy4-10 and content/fi/FY4/fy4-10 has two parts. sim.js line 71 changed by one line. review/carry.tsv is new. Nothing else changed. lesson-answers.py changed only its comment, in b0bde749 itself.
- `DEC` (sim.js:266) is a `const` inside the p5 closure. It is set before p5 calls `setup`, so line 71 cannot hit it uninitialized. No page errors or console errors in any of the three languages.
- I built with `python3 scripts/build.py fy4-10` and checked the preview in Playwright. The mass options are:
  - fi: `0,20 kg | 0,40 kg* | 0,60 kg`
  - en: `0.20 kg | 0.40 kg* | 0.60 kg`
  - fi-easy: `0,20 kg | 0,40 kg* | 0,60 kg`
- The option values are still `0.2/0.4/0.6`. So the adapter's `m1`/`m2` presets and `reset`, the model and the experiments are unchanged. The readout uses the same decimal sign as the options in each language (0,240 / 0.240 kg·m/s).
- `node tests/models/fy4-10.test.js`: 4791 checks pass.
- I ran lesson-answers.py and it still gives the round-3 values:
  - elastic (0,200; 0,800), (0; 0,600), (−0,120; 0,480)
  - sticky 0,400 / 0,300 / 0,240 m/s
  - explosion (−0,632; 1,265), (−0,775; 0,775), (−0,849; 0,566), each with 0,24 J
  - worked example 1,14 m/s with 15 %
- I carried my round-3 findings forward: physics, conditions, experiments, numbers and assessment items. The text they judge has not changed.
- The hash is the same at the start and at the end (3ce5496422f13f04).
