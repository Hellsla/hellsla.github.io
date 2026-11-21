VERDICT: FAIL
CONTENT-HASH: 98ad64a10c15cc2c

## Blocking
- A (limit value rounded to the wrong side, new box line 128-130): the task asks "At most how many molecules"; 6.0e4/12.6 = 4762, and the answer rounds it up to 4.8e3, which exceeds the bound. Guardrail "Values and significant figures": an "enintään" value is rounded down. Fix: "\approx 4.7 \cdot 10^{3}" (or 4760).

## Polish
None.

## Checked
batch delta review, round 2: 12.6 eV as the minimum per ionisation makes "at most" physically right; the visible-light comparison (1.7-3.3 eV) is correct. Alpha/beta box: 5.49e6/34 = 1.61e5, approx 1.6e5 ion pairs each, with the same W stated; beta range of metres (about 20 m in air for 5.5 MeV) vs alpha about 4 cm matches line 141 and the table, so beta ionises far less per cm. Correct.
