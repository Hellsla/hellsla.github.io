VERDICT: PASS
CONTENT-HASH: 9f35c8b8291f8ed1

## Blocking

## Polish
- solutions.md:19 (fy3-1-L1-02): the check's last product, $0.50 \cdot 12 = 6.0$, has no units. Consider writing $0.50\,\tfrac{\text{cm}}{\text{N}} \cdot 12\,\text{N} = 6.0\,\text{cm}$. This is style only.

## Checked
- The delta is solutions.md:19 alone. "spring constant" is now "extension per newton", which is the right name for $x/F$ (cm/N). The old wording named the inverse of $k$, a quantity outside FY3, so the fix is correct.
- Recomputed: $2.0\,\text{cm}/4.0\,\text{N} = 0.50\,\text{cm/N}$ and $0.50 \cdot 12 = 6.0\,\text{cm}$. This matches the answer.
- "spring constant" no longer appears in exercises.json or solutions.md. The FY3 scope holds.
- The wording matches the Finnish fix (venymä newtonia kohti). No number or symbol changed, so the previous report's checks still stand.
- The hash was the same at the start and the end.
