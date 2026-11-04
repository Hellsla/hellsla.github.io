VERDICT: PASS
CONTENT-HASH: 33436c68cf95a6c5

## Blocking

## Polish
- inquiry.json:602 — tarkistus-3 still says the filament "noudattaa likimain Ohmin lakia" and that its resistance grows as it heats; lesson.md:269 and 380 now both give the rising resistance as the reason. Optional: say the filament's resistance limits the current, I = U : R, for a lamp rated for that battery.
- inquiry.json:121 — the example voltages in koe-1 still leave out 6,0 V, which ennuste-1 compares (1,91 V, 12,4 mA).
- assets/sims/fy6/fy6-14/sim.js (ledPicture) — the canvas literals `$\text{virta yli } 20\,\text{mA}$` and `$\text{estosuunta: ei virtaa}$` are still not drawn through `__('key')` (FY6 thread rule; not physics).

## Checked
- Round 2: diff cab03926 judged against the round-1 blocking items.
- siirto mistake value is now 1.56 = 5,2 V · 0,30 A, which matches its feedback.
- siirto answer is now 24,8 W (24,76 W): three significant figures from the given values, which the tolerance accepts.
- lesson.md:269 — the reverse-direction claim now carries its condition ("alle diodin läpilyöntijännitteen"), consistent with the sim's model box.
- lesson.md:565 — η = P : (GA) now states that P is the power at the maximum power point; 0,92 W : 6,0 W ≈ 15 % is unchanged and right.
- figures.py teho: the label is now "maksimitehopiste", regenerated into lesson.md; it is a label change only, and the numbers are unchanged.
- No new physics errors in the diff; the round-1 recomputation of every other number still holds (none of those numbers changed).
