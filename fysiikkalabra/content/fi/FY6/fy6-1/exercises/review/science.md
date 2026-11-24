VERDICT: PASS
CONTENT-HASH: 295c391cac8e837b
SCOPE: delta md-paragraphs,numbers,reflow,teacher-figure,typography from 9415e187cfda526d base e238aa9

## Blocking

## Polish
- solutions.md:201 — L3-05 b) still writes $5{,}2 \cdot 10^{4}\,\text{s} : 3600\,\text{s/h} = 14{,}5\,\text{h}$ (the rounded value gives $14{,}4\,\text{h}$; unrounded $14{,}46\,\text{h}$). This was in the earlier report and is not part of this diff. The final $14\,\text{h}$ is right.

## Checked
- Hash read at start and end: 295c391cac8e837b, unchanged.
- Every changed Kaava step (lines 15–231) is now an aligned block that starts from the definition ($I = Q/t$, $U = E/Q$, $Q = Ne$) and then solves for the unknown in symbols. Each row is algebraically right and gives the same final symbolic form as before ($Q = It$, $E = UQ$, $t = Q/I$, $N = It/e$, $v = I/(ne)$, $Q = I_0 t_1 + \tfrac12 I_0 t_2$).
- L3-04 (line 191) now opens with $U = E/Q$ and $Q = It$ before $E_k = U_k I_k t$. The derivation is right and matches the Periaate.
- L3-05 (line 201): $N/t = I/e = nv$, where $n$ is the electrons per metre of wire ($1{,}3 \cdot 10^{23}\,\text{1/m}$). The units work out ($\text{m/s}$).
- The paragraph splits in L1-05 (kaavio-malli), L1-06, L1-07, L2-06 and L2-07 change no claim, number or option judgement. The model diagram description still matches the teacher-approved figure (cells in series − to +, current arrow from + along the top).
- I recomputed all 16 answers in one script with my own formulas. All agree with answers.py ($20\,\text{C}$, $1800\,\text{J}$, $30\,\text{s}$, $108\,\text{C}$, $9{,}99 \cdot 10^{17}$, $39{,}96\,\text{kJ}$, $11\,\text{C}$, $8{,}0\,\text{h}$, $1{,}2$, $9{,}36 \cdot 10^{19}$, $22{,}8\,\text{C}$, $140\,\text{J}$, $12{,}5\,\text{Wh}$, $0{,}0192\,\text{mm/s}$).
- Scope and notation are unchanged and stay inside the brief's formulas.
