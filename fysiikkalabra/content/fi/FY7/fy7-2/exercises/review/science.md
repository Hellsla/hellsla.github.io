VERDICT: PASS
CONTENT-HASH: 170abd26da60b9ca

## Blocking

## Polish
- solutions.md fy7-2-L1-09 Järkevyys — "Tehtävän 2-2" hard-codes a running number, which the build assigns and which changes if the tasks are reordered — name the task by its situation instead ("koulun elektronisuihkuputken tehtävässä").
- solutions.md fy7-2-L3-05 Vastaus c) — the relativistic correction $\tfrac{3}{4}(v:c)^2 \approx 0{,}3\,\%$ is correct but goes past what the lesson teaches (FY8 / later). The plan allows relativity "only in a subordinate clause". You could keep it as a side remark and base the judgement on the lesson's condition, "vauhti pieni valon nopeuteen verrattuna".
- solutions.md fy7-2-L3-05 b) — $n = 31{,}9$ is rounded to 32 crossings, so 16 revolutions. The answer is the same either way: $t = (n/2)T$ gives $1{,}047\,\mu\text{s}$ and $16T$ gives $1{,}050\,\mu\text{s}$, both $1{,}05\,\mu\text{s}$. One clause saying that the last crossing brings the proton to the extraction radius would make the rounding explicit.

## Checked
- All 18 numeric answers recomputed in one script from the task text with my own formulas. They agree with exercises.json and answers.py, and every shown answer is inside its tolerance (L2-04 2,049 → 2,0 and L2-05 1,025 → 1,0 within 3 % and 5 %).
- L3-05 (the changed task): $v = qBr/m = 1{,}915 \cdot 10^{7}\,\text{m/s}$, $E_\text{k} = 3{,}07 \cdot 10^{-13}\,\text{J}$ ≈ $1{,}9\,\text{MeV}$, $qU = 9{,}61 \cdot 10^{-15}\,\text{J}$, $n = 31{,}9$, $T = 65{,}6\,\text{ns}$, $t = 1{,}05\,\mu\text{s}$, $v/c = 0{,}064$. The new data 0,200 m and 60,0 kV carry the three significant figures the answer is given with. The check $32 \cdot qU \approx E_\text{k}$ and the period from $2\pi r/v$ are real checks.
- Directions: L2-05, positive charge with $\overline{v}$ to the right and $\overline{B}$ into the page → force up. L2-08, positive charge with $\overline{v}$ up and $\overline{B}$ out of the page → force to the right, so the electron's force is to the left: option C. Both checked with cross products. The two right-hand-rule wordings (fingers in L2-05, palm in L2-08) are both correct.
- L2-08 force diagrams: one body, one interaction (the field). The weight is left out on a stated numeric basis ($8{,}9 \cdot 10^{-30}$ vs $2{,}4 \cdot 10^{-16}\,\text{N}$). The velocity is drawn and labelled as not a force. Each wrong figure shows exactly the error its feedback names.
- L2-09 figure: the points come from the deuteron mass. At $1{,}5 \cdot 10^{6}\,\text{m/s}$, $r = 15{,}66\,\text{cm}$, read as 15,7, so $m = 3{,}35 \cdot 10^{-27}\,\text{kg}$. The figure gives B and the description gives the same information without revealing the mass.
- L3-04: $r^2$ values recomputed. The least-squares slope through the origin is $0{,}1182\,\text{cm}^2/\text{V}$, giving 22,8 u, so sodium-23. The origin line is given a physical reason, and the check at 400 V gives 6,9 cm.
- L2-05 / L2-06 example data: H⁺, H⁻ and H₂⁺ are consistent with the radii. The Mg-like masses are 25,1 u and 25,9 u, and the abundances add up to 100 %.
- L1-06 and L2-07: exactly one correct option, every distractor really wrong, and each feedback's physics is right ($T = 2\pi m/(qB)$ does not depend on $v$).
- Every solution states its principle, solves symbolically before substituting, and gives its conversions and a rounding reason. The notation matches the brief.
- Scope: everything is inside FY7 "varatun hiukkasen liike" plus FY6's $W = qU$ and $E = U/d$. The cyclotron fits the thematic topic hiukkaskiihdytin.
