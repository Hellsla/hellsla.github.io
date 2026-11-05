VERDICT: PASS
CONTENT-HASH: d82481d212cae25e
Round 2: full review of the exercise set after the round-1 fixes (commit f8abf016e, diff from d0ea57642).

## Blocking
(none)

## Polish
- L2-07 (plan deviation, carried from round 1, not physics): it repeats the lesson's first misconception, and its calculation is the same as L1-02 and the Esimerkki. The plan asked for an error analysis of a LED that burns out without a resistor, explained with the characteristic curve. The planning side decides, or updates docs/exercise-bank/FY6.md.
- exercises.json L3-05 b) — the hint on how to find the operating point (load line or currents at the table voltages) was removed with the a) fix. That is fine at level 3, but the plan names "piirtämällä kuormasuora". If the drawing is meant, add "esimerkiksi piirtämällä kuormasuora ominaiskäyrän kanssa samaan kuvaajaan".

## Checked
- Hash d82481d212cae25e at start and end.
- Round-1 Blocking resolved: L3-05 a) now defines kynnysjännite as the glossary does (extend the steep straight part 2,05–2,10 V to the voltage axis). I recompute 2,05 V − 20 mA : 420 mA/V = 2,00 V, as in the solution and the new answers.py assert. The Järkevyys now compares 2,02 V with 2,0 V consistently.
- Round-1 Polish fixed: L1-06 gives the battery 9,0 V, so "diodin yli vain pieni jännite" holds; L1-08 `tolerance` 0.03.
- L1-06 and L1-07 after the rewrite: exactly one correct option, `answer` and answers.py equal its text, and every distractor is really wrong with correct feedback. The new estosuunta distractor ("virta kulkee takaisin") is wrong for the right reason.
- One script recomputed every new answer: L1-08 16,7 %; L2-05 207 Ω (red); L2-06 181 mW at 22 Ω; L2-07 387 Ω; L3-04 87,7 %, deficit Jan–Mar and Oct–Dec (853 vs 3370 kWh); L3-05 operating point 2,02 V, 13,78 mA. All agree.
- L3-05 renders at 1280 px without overflow (shots L3-1280-7, -8, taken after the fix).
- Levels 8/7/5, units, symbols and scope correct.
