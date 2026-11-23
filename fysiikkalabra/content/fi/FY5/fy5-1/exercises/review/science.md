VERDICT: PASS
CONTENT-HASH: 845bbf8761a73937

## Blocking

## Polish
- content/fi/FY5/fy5-1/exercises/solutions.md:149 — L2-06 Kaava: the row `\Sigma M = g\,(m_A r_A + m_B r_B \\ &\qquad - m_C r_C - m_D r_D)` is split by hand inside the bracket (house rule: never split a chain by hand for the layout) — write it on one row and let the layout wrap it.
- content/fi/FY5/fy5-1/exercises/solutions.md:149 — `\Sigma M = M_A + M_B - M_C - M_D` treats $M_C$, $M_D$ as magnitudes, while the lesson's convention is signed moments summed ($\Sigma M = M_1 + M_2 + \ldots$). This is correct as written because the Periaate gives the signs; optionally write $\Sigma M = M_A + M_B + M_C + M_D$ with $M_C = -G_C r_C$, or say "suuruudet" (C, not an error).

## Checked
- Hash was the same at the start and the end. I judged only the diff: Kaava steps turned into aligned blocks, and some paragraphs split in L1-07, L3-01 and L3-04.
- Every new Kaava block starts from the basic equation ($M = Fr$, a lever arm relation, $\Sigma M$ as the sum) and ends in the symbolic form that Sijoitus substitutes into: L1-01, L1-02, L1-03, L1-05, L2-01, L2-02, L2-03, L2-04, L2-05, L2-06, L2-07, L3-01, L3-02, L3-03, L3-04, L3-05 and L1-10.
- Every algebra step is right: $F = M/d$, $r = M/F$, $F = M/(d\sin\alpha)$, $r_2 = F_1 r_1/F_2$, $F_\text{k} = F_\text{p} d/R$, $M = F(d-e)$ and $M = Fd\cos 45^\circ$.
- The signs agree with the Periaate in L2-03 (+, −) and L3-03 (both moments counterclockwise, $2Fd$).
- I recomputed every Sijoitus number in one script: 37,5; 9,6; 150; 0,30; 17,21; 29,75; 7,0; 230,9; 25,1; 0,1177; 21,6; 61,87; 1,0; 48; 787,5/70,875/47,25/31,5; 240/165,5/200; 15. All match. Answers, units and tolerances are unchanged.
- The paragraph splits in Mallivastaus, Periaate and Vastaus change no wording and no number.
