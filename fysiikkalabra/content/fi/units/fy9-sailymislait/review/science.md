VERDICT: PASS
CONTENT-HASH: 12315fb70075c238
Delta review, work queue items 18 and 19 (2026-11-16), against the version previously passed.

## Blocking
- (none)

## Polish
- A: s5 b model answer, changed sentence: "liike-energiasta katosi kokeessa 2 noin puolet" could read "liike-energiasta muuttui muihin muotoihin noin puolet", since the same answer argues that nothing disappears.

## Checked
- solutions.md s5 b, its rubric criterion in tasks.json and unit.md Yleisiä virheitä: kinetic energy becomes internal energy and sound, momentum is not a form of energy; the unit.md sentence now names kinetic energy and agrees with the neighbouring friction bullet. The rubric criterion matches the model answer.
- No task was added to this unit (item 19 touches other units); `python scripts/practice.py check units/fy9-sailymislait` OK; hash the same at start and end.
