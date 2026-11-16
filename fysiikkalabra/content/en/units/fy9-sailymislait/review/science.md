VERDICT: PASS
CONTENT-HASH: f5227f32d90da96e
Delta review, work queue items 18 and 19 (2026-11-16), against the version previously passed.

## Blocking
- (none)

## Polish
- A: solutions.md model answer, same changed sentence: 'about half of the kinetic energy disappeared in test 2' would read better as 'was converted', since the unit elsewhere counts 'disappeared' as a mistake. The sentence itself says where the energy goes, so not blocking.

## Checked
- solutions.md model answer, tasks.json criterion, unit.md common mistake: kinetic energy (not momentum) is converted into internal energy and sound; momentum is not a form of energy. The three places now say the same thing, and the unit.md sentence is more exact than before ('kinetic energy' instead of 'energy').
- The rest of the model answer (rolling resistance as external impulse, -12 % and -3 %) is unchanged.
- No ADDED TASK in this unit's en diff; `python scripts/practice.py check units/fy9-sailymislait` is OK.
