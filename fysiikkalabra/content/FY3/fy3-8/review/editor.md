VERDICT: FAIL
CONTENT-HASH: 62f4509be3500ac5

The lesson tells one story. The bridge-joint question is answered by the worked example, and the theory, sim, exercises and exit ticket all use ΔL = αL₀ΔT. Its length fits the FY3 siblings (Ydinajatus 240 words, against 184–383 in the other lessons). The levels are 5/4/3, and the level-3 tasks reach holes, bimetals and a liquid in a container. One goal is half met. The micro model explains expansion only in solids. Liquids and gases are just said to expand more, gases appear in no exercise, and the air row in the table is never used.

## Blocking
- lesson.md:12 — The goal "mikromalli …; kiinteät aineet, nesteet ja kaasut" is only half met. Liquids and gases are said to expand more, but the lesson gives no particle-level reason. — Fix: add two sentences. A liquid's particles are not held at fixed positions and attract each other more weakly. A gas's particles are far apart and nearly free, so at constant pressure the volume grows much more. Point on to fy3-9.

## Polish
- lesson.md:21 — "Nesteiden ja kaasujen … lasketaan samalla tavalla" clashes with line 12 ("kaasuja tarkastellaan kaasulakien avulla"). — Fix: write "nesteiden (ja vakiopaineessa kaasujen)".
- lesson.md:40 — The row "ilma (vakiopaineessa)" is used nowhere. — Fix: add a short gas-versus-liquid comparison in an exercise or exit question, or drop the row.
- lesson.md:67 — All three misconceptions are already stated as facts at lines 6, 10 and 12. — Fix: shorten those statements and let this section explain them.
- exercises.json:4 — L1-01 (steel, two temperatures, ΔL in mm) has the same structure as the worked example. — Fix: vary the material or the quantity asked for.

## Checked
- The lint was run. The L1-03 and L1-05 findings are already with the fixer.
- The goals in meta.json match curriculum.json. The MAOL guide ties lämpölaajeneminen to the micro model.
- The motivating question is answered in the worked example.
- Each formula appears in display form once, with its symbols named. γ ≈ 3α is used in L2-02 and L3-03.
- Level counts are 5/4/3. Every level-3 task asks for reasoning.
- The misconceptions return in L3-01 and in exit-ticket questions 2 and 3.
- The sim's 20 °C reference, ΔT, ΔL and L match the lesson and sim-spec.
- The lesson stays within FY3 scope (no vectors, no gas-law formulas).
- It hands over cleanly to the micro model in fy3-9.
