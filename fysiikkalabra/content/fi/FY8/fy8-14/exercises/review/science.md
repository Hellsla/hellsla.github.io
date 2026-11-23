VERDICT: PASS
CONTENT-HASH: c25c9461478e13cd

## Blocking

## Polish
- exercises.json fy8-14-L2-08 and L2-09 — the earlier tolerance notes still apply (reading accuracy against 6 % and 4 %). They are not part of this diff.
- solutions.md:177 (L3-01) — the Kaava step introduces its symbols together with their values ($n = 5$, $k = 1{,}3$, $N = 30$, $D_\text{kerta} = 2{,}0\,\text{Gy}$). The rows themselves are symbolic and correct. Optionally move the values to Annettu.

## Checked
- The hash was c25c9461478e13cd at the start and the end. Scope: delta on solutions.md since the version I passed (commit 3edafc26c2).
- A script removed the Kaava steps, collapsed whitespace and compared the rest of the file: it is identical, so only the Kaava steps changed. exercises.json and answers.py are unchanged.
- L2-04 (line 144) goes from the inverse-square law and $H = \dot H t$ to $H = \dot H_1 (r_1/r_2)^2 t$. Recomputed: $10\,\mu\text{Sv}$.
- L3-01 goes from $D_\text{keila} = D_\text{kerta}/n$ and $D_\text{tulo} = k D_\text{keila}$ to $D = N k D_\text{kerta}/n$. This is correct, because only one beam passes through the entry point. Recomputed: $15{,}6\,\text{Gy}$, so $16\,\text{Gy}$.
- L3-02 uses $I_\text{A}/I_\text{B} = 2^{d/d_{1/2}^\text{luu} - d/d_{1/2}^\text{kudos}}$. The sign is right: the beam through bone is weaker, so the ratio is above 1. Recomputed: $8{,}87$.
- L3-03 derives $d = d_{1/2}\ln(I_0/I)/\ln 2$ step by step. Recomputed: $16{,}86\,\text{mm}$, so $17\,\text{mm}$.
- L3-04 goes from $A_\text{kuv} = A_0(\tfrac12)^{t/T_{1/2}}$ to $A_0$, then $H = kA_0 + H_\text{TT}$. Recomputed: $A_0 = 218{,}9\,\text{MBq}$ and $H = 10{,}16\,\text{mSv}$.
- L3-05 runs from the attenuation law to $d_{1/2} = d_{20}\ln 2/\ln(R_0/R_{20})$ and on to $d_x$. Recomputed: $9{,}147\,\text{mm}$ and $12{,}10\,\text{mm}$.
- Every Kaava step starts from the basic law and ends in the symbolic form used in Sijoitus. No physics or notation changed against the brief.
