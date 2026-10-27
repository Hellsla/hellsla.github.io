VERDICT: PASS
CONTENT-HASH: a82e14d314957d41

## Blocking
(none) Round 2's overflow is fixed: L2-03, L2-04 and L3-03 now compute the intermediate values in a line of their own and show the substitution as short `aligned` display lines. `check_layout.py fy3-14` opens all solutions and passes at 360 px; page scrollWidth at 390 px is 390.

## Polish
- Example stage 5 computes T before stage 6 states Q_v > Q_j; put the comparison at the start of Sijoitus (stage 2 says to check first).
- Example stage 3 gives T = (Q_v − Q_j)/(c_v(m_v+m_j)) with a sentence only; one line c_v m_v T_v − Q_j = c_v(m_v+m_j)T would show the student where it comes from.
- Example stage 7 Järkevyys is about 100 words with three checks; split or drop one.
- L3-02 Sijoitus still never writes the total Q_j = 6300 + 100 200 J that the "ei sulata kokonaan" claim compares with.
- L3-03 Kaava is one dense paragraph with two long inline equations; display lines would read better at 390 px.
- "0 °C:seen" can break across lines (L1-03, L3-03 and others); join with a no-break wrapper.

## Checked
- Hash a82e14d314957d41 at start and end; checks.txt all ok (inquiry 63/0, layout 360 px).
- All 13 solutions read: seven labelled steps (Annettu to Järkevyys), principle stated with why, conversions explicit, intermediate values before substitution, Vastaus names the limiting datum; a weak student can follow each.
- L3-03 reasonableness check (energy balance 38 325 J both sides) is consistent.
- Worked example capture part 2 at 390 px: seven stages, display lines fit, no clipping.
- I did not re-open the solutions in the browser myself (they sit behind the staged page); I relied on the layout test.
