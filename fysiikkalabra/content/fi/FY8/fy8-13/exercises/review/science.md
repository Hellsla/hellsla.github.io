VERDICT: PASS
CONTENT-HASH: 6bc95d2c0a5c1777

## Blocking

## Polish
- exercises/exercises.json (fy8-13-L2-10) — the earlier note still applies. The graph gives $d_{1/2} = 5{,}0\,\text{cm}$, while the lesson says concrete is "noin $4\,\text{cm}$" for Cs-137. Fix: a short clause saying the source or the concrete is a different one. This is not part of this diff.

## Checked
- The hash was 6bc95d2c0a5c1777 at the start and the end. Scope: delta on solutions.md, compared with the version I passed (commit db3d5c5081).
- The packet's diff mostly adds blank lines. A script removed the Kaava steps, collapsed whitespace and compared the rest of the file: it is identical, so the other changes are only paragraph splits. exercises.json and answers.py are unchanged since that pass.
- L2-01 Kaava runs $D_\text{T} = E/m$, then $H_\text{T} = w_\text{R} D_\text{T}$, then $H_\text{E} = w_\text{T} H_\text{T} = w_\text{T} w_\text{R} E/m$. The order of definitions is correct. Recomputed: $1{,}2\,\text{mSv}$.
- L2-02 runs from the inverse-square law to $H = \dot H t$, giving $t = \tfrac{H}{\dot H_1}(r_2/r_1)^2$. Recomputed: $4{,}17\,\text{h}$.
- L2-03 builds both rates, then $H_\text{A} - H_\text{B} = \dot H_1 t[(r_1/r_\text{A})^2 - (\tfrac12)^{d/d_{1/2}}]$. The factorisation is correct. Recomputed: $+5{,}0\,\mu\text{Sv}$.
- L3-02 computes the alpha contribution as $w_\text{T} H_\text{T}$. For whole-body gamma, $H_\text{E} = w_\text{R} D_\gamma$, justified in Periaate by $\Sigma w_\text{T} = 1$. Recomputed: $0{,}74\,\text{mSv}$.
- L1-07 (line 257) is a weighted sum over two tissues. Recomputed: $0{,}20\,\text{mSv}$.
- L3-05 runs from the attenuation law and the inverse-square law to $t = \tfrac{H}{\dot H_1}(r_2/r_1)^2\, 2^{d/d_{1/2}}$. The sign of the exponent is correct. Recomputed: $\dot H = 10{,}61\,\mu\text{Sv/h}$ and $t = 2{,}36\,\text{h}$, giving $2{,}4\,\text{h}$. An end-to-end table fit gives $d_{1/2} = 3{,}99\,\text{cm}$, so reading $4{,}0\,\text{cm}$ is right.
- Every new Kaava step starts from the basic laws and ends in the form substituted in Sijoitus.
