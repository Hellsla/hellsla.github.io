VERDICT: PASS
CONTENT-HASH: 3e3fdacfe3d4a70d
SCOPE: delta: round 2 (fi), s7 "Yleisiä virheitä" last bullet changed from a one-row aligned block to an inline formula; s7, s8 and s1-s6 otherwise not re-judged.

## Blocking
- (none)

## Polish
- s8 b) Sijoitus: the printed chain `(-1,14 m/s²) · 2,0 s = -2,29 m/s` does not multiply out (-1,14 · 2,0 = -2,28); the value comes from the unrounded a = -1,1433. Write a = -1,143 m/s² in the chain or note the exact value. Same in all languages.
- s8 d) Järkevyys sums to 12,25 m (2,29 + 6,87 + 3,09) while the Sijoitus row gives 12,2 m; use 12,23 (unrounded parts) or round the same way in both.
- s7 d) k ≈ 0,31 kg/m in one place and 0,315 / 0,3147 in the next; use one value consistently.
- s7 precision wording: a) and c) justify two significant figures "kuten luetuissa nopeuksissa", but 18,6 and 44,5 m/s have three; reword the reason (Δv = 6,0 m/s, F_v with two figures). Answers are right.

## Checked
git diff of unit content (excluding review/) between the round 1 fix commit's parent and now: only solutions.md line 575, formatting only. Same numbers and units: 100 : 75 · 48 m/s = 64 m/s, still marked as the erroneous proportional-to-mass claim, correct contrast v_t ∝ √m. No other content difference. Hash differs from the round 1 report because of that edit and the review files. Round 1 Polish items stay recorded.
