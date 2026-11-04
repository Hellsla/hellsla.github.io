VERDICT: PASS
CONTENT-HASH: 72dca8a81fc7dc58

## Blocking
None. The round-1 item is fixed: the fy8-s3-lin alt text now says "from r = −2 to 22 centimetres" in `figures.json` and in the `solutions.md` aria-label. No "r = 2 to 22" is left.

## Polish
- **s1 "the lower one" no longer has an antecedent.** Since the rename to first/second excited state, "from the second excited state to the lower one" appears in the s1 a criterion (tasks.json), the Substitution and the Answer. The physics is still right (4.19 → 1.97 eV), but the phrase now leans on the old upper/lower pairing. It also sits right next to the listed common error (green taken as second excited → ground). Suggestion: "to the first excited state" in all three. In the s1 c task text, "the lower one only after about 110 s" can stay; "the first one" would be cleaner.
- First/second excited state (text) and 1st/2nd (figure) are correct for these three oxygen levels (¹D at 1.97 eV, ¹S at 4.19 eV). "Upper excited state" appears nowhere else.
- Carried over: s5 a "about a third more than now" (factor 1.36) is correct, since 2^0.447 = 1.364.
- Carried over: s2 c "The half-life 4.47·10⁹ a : 87.7 a ≈ 5·10⁷ times longer" is missing "is". Grammar only.
- Carried over: the "Hyväksytään myös" and "Yleisiä virheitä" headings stay in Finnish. That is the editorial reviewer's call.

## Checked
Hash 72dca8a81fc7dc58 at start and end.
- **Diff HEAD~1.** It changes only the s3 alt text and the level renames, in figures.json, solutions.md and tasks.json (s1 a criteria, s1 b, s1 c). No number, answer, tolerance or point value changed. practice.py check reports OK.
- **Sanity scan.** The answers.py values still match the solutions: 296 nm, 1193, 1107 nm, 5.594 MeV, 1791 W, 0.566 mSv, 36.2 cm, 7.16, 135 s, 3.67 %, 3.49 a, 82 988.
- **Round-1 physics wording checks still hold.** These cover energy levels and photons, the bands, collisional de-excitation, the dose chain, 1/r² with background, the W⁻ decay, the moderator, and Oklo.
