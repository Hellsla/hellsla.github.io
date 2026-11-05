VERDICT: PASS
CONTENT-HASH: 8b572d40e2c95165

Round 2

## Blocking
(none) Round 1 had none; the round-1 fixes were checked and are correct.

## Polish
- exercises.json fy7-2-L3-05 c) — the constant-period argument was dropped (now v/c and the classical check), which removes the overlap with L3-02. The solution says "kolme merkitsevää numeroa kuten kentässä ja säteessä", but r = 0,20 m and U = 60 kV have two; say "kaksi merkitsevää numeroa" or give r as 0,200 m.
- exercises.json fy7-2-L2-05 c) — the table is needed only for the radii; acceptable. The new ion explanations (H^-, H2^+, 210 eV for a proton at 2,0·10^5 m/s, checked: correct) are a good fix.
- exercises.json fy7-2-L3-04 — task text allows a hand-fitted line, and the solution gives 22–23 u; add the answer tolerance to the answer-box line ("noin 23 u") only if students find 22,8 vs 22 confusing.

## Checked
- Round 1 Polish applied: L1-08 now v = 5,0·10^6 m/s (r = 1,42 mm, T = 1,79 ns, answer 1,8 ns) so identical numbers no longer hide the independence of T from v; L2-05 right-hand rule applied with finger directions and ions named; L3-04 "sovitettu suora" wording; L3-05 B = 1,00 T gives v = 1,92·10^7 m/s, E_k = 3,07·10^-13 J, 32 crossings, 16 revolutions, t = 1,05 µs, v/c = 6 %, correction ≈ 0,3 %; answer 1,05 µs agrees with answers.py.
- Järkevyys of L1-07 corrected to "8,5-kertainen" (0,4264 mT / 0,05 mT = 8,5).
- New tasks recomputed; counts 8/7/5; levels fit; MC distractors are real misconceptions with repairing feedback; no copy of the neon example.
- Screenshots not opened; phone fit relied on the passed 360 px layout check.

## Follow-up (8b572d40e2c95165: four solutions.md edits on top of the hash above)
- L1-02: the charge as a magnitude ($|q| = e$) and $|q|$ in the formula follow the lesson's sign convention instead of silently dropping the minus sign; answer and level unchanged.
- L2-03 and L3-02: the references now name chapters the student can find (*Homogeeninen sähkökenttä*, *Ympyrärata: jaksonaika ja ratanopeus*).
- No blocking issue; main's notes above stand.
