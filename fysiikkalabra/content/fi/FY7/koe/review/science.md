VERDICT: PASS
CONTENT-HASH: 54aea9709824828a

## Blocking
None.

## Polish
- k4 c Sijoitus: $\tfrac{150 \cdot 230\,\text{V}}{12{,}37\,\text{V}} = 2789$, not $2788$. The value $2788$ comes from the unrounded $12{,}374\,\text{V}$. The answer $\approx 2790$ and the tolerance are unaffected. Either write $2789$ or use $12{,}374\,\text{V}$ in the chain.
- k6 d Mallivastaus and the conclusion criterion still say "noin yhdeksässä vuodessa", while c's remark gives about $9{,}7\,\text{a}$ when the transformer losses are counted. Saying "noin $9$–$10$ vuodessa" in d would make the two agree. The conclusion is unchanged either way.

## Checked
I recomputed every number of tasks.json and solutions.md in my own script. Everything agrees with answers.py and the solutions:
- k1: d $0{,}08\,\text{V}$ and its distractors; i $73{,}7^\circ$; h $0{,}12\,\text{m}$ and $3{,}0\,\text{m}$; one correct option in a–j.
- k2: $r^2$ and the bars $\pm 2r\Delta r$. The read slope gives $1{,}81 \cdot 10^{-5}\,\text{m}^2/\text{V}$, $B^2k = 1{,}16 \cdot 10^{-11}$ and $1{,}72 \cdot 10^{11}\,\text{C/kg}$; least squares gives $1{,}74 \cdot 10^{11}\,\text{C/kg}$. Both extreme lines stay inside all five bars (checked). They give $1{,}68$ and $1{,}85 \cdot 10^{11}\,\text{C/kg}$, so $\pm 0{,}08 \cdot 10^{11}\,\text{C/kg}$ ($4{,}8\,\%$).
- k3: $0{,}30\,\text{V}$, $0{,}50\,\text{A}$, $0{,}060\,\text{N}$, $0{,}15\,\text{W} = I^2R$. The current runs up the rod both by Lenz's law and by $q\overline{v}\times\overline{B}$.
- k4: $40\,\text{Hz}$; $U = 12{,}374\,\text{V}$, shown as $12{,}4\,\text{V}$ with the two-figure reading caveat, and $12{,}37\,\text{V}$ carried into c. Also $339{,}3\,\text{m}^2/\text{s}$, $0{,}0516\,\text{T}$, $I_1 = 3{,}72\,\text{A}$ and $U_1 I_1 = 46\,\text{W}$.
- k5: $3{,}327$, $3{,}347$ and $3{,}321\,\mu\text{m}$; $\pm 27$, $12$ and $6\,\text{nm}$; $d/\lambda = 6{,}26$, $73{,}4^\circ$. The new b remark compares $k = 2$ and $k = 3$ correctly: the gap $0{,}026\,\mu\text{m}$ exceeds the sum $0{,}018\,\mu\text{m}$.
- k6: $600\,\text{A}$, $1{,}728\,\text{MW}$ ($14{,}4\,\%$, drop $2{,}88\,\text{kV}$); $109\,\text{A}$, $57{,}1\,\text{kW}$; $500$ turns; $6912$ and $228{,}5\,\text{MWh}$; $334\,175\,\text{€}$, $8{,}98\,\text{a}$. The new remark checks: $120\,\text{kW}$, $24\,000\,\text{€}$, $310\,000\,\text{€}$, $9{,}67\,\text{a}$, and $177\,\text{kW}$ is under a tenth of $1{,}73\,\text{MW}$.
- k7: $b = 2{,}758 \cdot 10^{-3}\,\text{m} \cdot \text{K}$ through the origin. The read points $550$ and $1100\,\text{nm}$ lie on that line ($552$ and $1103\,\text{nm}$). All $\lambda T$ products are below the literature value; the deviation is $4{,}8\,\%$ against a random $2{,}6\,\%$, and the emissivity argument points the right way. Also $9{,}47\,\mu\text{m}$ and $5269\,\text{K}$. The new e argument uses the operating range ($1{,}32$–$0{,}97\,\mu\text{m}$) and $0{,}78\,\mu\text{m}$ at $3695\,\text{K}$, both correct, and the rubric matches it.

Also checked:
- Points: Osa 1 is $20$ p, k2–k5 are $15$ p each, k6 and k7 are $20$ p each, and every rubric adds up to its part's points.
- Every criterion asks only what its part gives.
- The scope is FY7 only (polarisation stays qualitative).
- The figure data match the tasks.
- The round-2 Polish items are all addressed.
- The hash was unchanged at the start and the end.
