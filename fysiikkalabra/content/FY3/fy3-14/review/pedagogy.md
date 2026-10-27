VERDICT: FAIL
CONTENT-HASH: 833cfd37a6beef62

## Blocking
- Solutions L2-03, L2-04 and L3-03, line Sijoitus, at 390 px: the single long inline fraction does not wrap, spills out of the solution box and is cut at the screen edge (L3-03: the numerator terms "334 000 · 0,100 J − …" and the denominator "· 0,600 kg" are unreadable; page scrollWidth grows to 574 px when solutions are open). This is the step where the student plugs in numbers, so a phone student who could not solve the task cannot follow it. Fix: use display math with `aligned` lines (as the worked example's Sijoitus does) or split into Q-terms on separate lines; the 360 px layout test does not open solutions, so it did not catch this.

## Polish
- Example stage 5 computes T with the "kaikki jää sulaa" formula before stage 6 states Q_v > Q_j; stage 2 says to check first, so put the comparison at the start of Sijoitus (or at the end of stage 4).
- Example stage 3 gives T = (Q_v − Q_j)/(c_v(m_v+m_j)) with only a sentence; one line showing c_v m_v T_v − Q_j = c_v(m_v+m_j)T would let a weak student see where it comes from (the lesson's Kaava section has the balance, the example does not).
- Example stage 7 Järkevyys is about 100 words with three checks; split or drop one.
- L3-02 Sijoitus never writes the total Q_j = 6300 + 100 200 J that the "ei sulattamaan kokonaan" claim compares with; add it.
- L3-03 Kaava is one dense paragraph with inline algebra (two long equations); display lines would read better at 390 px.
- Inline "0 °C:seen" breaks across lines in L3-03 Sijoitus ("0 °C" / ":seen"); join with a no-break wrapper.

## Checked
Round 1 Blocking items are fixed: L1-03 Järkevyys now compares melting with cooling correctly; L3-03 Kaava names each term of the balance (water cools, freezes, new ice cools to T; ice warms to T), shows the algebra and writes the numerator terms with units. Worked example has seven stages and renders well at 390 px (captures 1-3); all 16 tasks have a Näytä ratkaisu button, level 1 solutions are uniform, short and followable. Opened L3-03 solution at 390 px in the browser. Not re-judged: inquiry, figures and simulation (unchanged by this round; deterministic inquiry tests pass).
