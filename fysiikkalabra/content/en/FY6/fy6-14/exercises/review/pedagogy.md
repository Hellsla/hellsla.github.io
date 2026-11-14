VERDICT: PASS
CONTENT-HASH: 3129e7b116601f43
SCOPE: delta added-exercise from ad1ab6804b19c83a base 8f23aa7ae3bd

## Blocking
- none

## Polish
- L2-09 solution, Principle: "The panel is a DC voltage source" is a loose description, because the graph shows a nearly constant current over most of the range. Say "The panel delivers electrical power P = UI at each point of its curve" and the reading step needs no model of the source.
- The level is on the lower side of level 2 (one reading and P = UI), but the two-step feel comes from reading a curve and a unit conversion, and L2-06 and L3-02 already carry the maximum-power demand.

## Checked
- Level 2: reading a current at a given voltage from a characteristic curve, mA to A, then P = UI; not the worked example and not a repeat of L2-06 (table, maximum power).
- Figure gives a curve starting at 200 mA, flat to about 4 V, falling to 0 at 6.0 V on a 1 V and 50 mA grid; the description matches and does not give the power. The reading at 4.0 V (200 mA) is unambiguous because the curve is flat there.
- Situation first, question last as its own sentence; the unit W is requested.
- Solution complete: given, principle, reading steps, formula, mA conversion, substitution (0.80 W), significant figures, and a reasonableness check against both 1.2 W (Isc * Uoc) and the maximum power.
- Arithmetic verified: 4.0 V * 0.200 A = 0.80 W; tolerance 4 % suits a read value.
- Fit: the set has table-based solar-cell tasks; this adds the graph form that the bank plan asks for.
