VERDICT: PASS
CONTENT-HASH: 44f3a0f5513f3d73
SCOPE: delta added-exercise from 95f4812c2cd2b6b6 base 415cbc7c6bc3

## Blocking

## Polish
- exercises/solutions.md:309 — "esimerkiksi $434{,}0\,\text{nm}$, ne vastaavat siirtymiä $5 \to 2$ ja $6 \to 2$" pairs one line with two transitions. Write "$434{,}0\,\text{nm}$ ja $410{,}2\,\text{nm}$ vastaavat siirtymiä $5 \to 2$ ja $6 \to 2$". The model gives $434{,}2$ and $410{,}3\,\text{nm}$.
- exercises/solutions.md:310 — "vastaus ei riipu siitä, minkä taulukon rinnakkaisarvon valitset" is true for a different reason than the one implied. The box value comes from the level model alone, not from the table. Say that.

## Checked
- Hash 44f3a0f5513f3d73 at the start and the end. Only fy8-3-L2-09 was judged.
- Recomputed: $\Delta E_{3\to2} = 13{,}6 \cdot 5/36 = 1{,}8889\,\text{eV}$, which gives the box value 1,89 eV. answers.py also gives 1,888889. $\Delta E_{4\to2} = 2{,}550\,\text{eV}$.
- b) recomputed: 656,3 nm gives $3{,}027 \cdot 10^{-19}\,\text{J} = 1{,}889\,\text{eV}$ and 486,1 nm gives $4{,}087 \cdot 10^{-19}\,\text{J} = 2{,}551\,\text{eV}$. Every fine-structure value of the table (6562,7110…6562,8518 Å) gives 1,8894–1,8895 eV.
- The model wavelengths 656,5 nm and 486,3 nm are right, and the difference is 0,03 % (under 0,1 %). The air-wavelength remark is correct: most of the gap is air against vacuum.
- The task states Å, 1 Å = 0,1 nm, and that the table gives air wavelengths for the visible lines. Only verified NIST facts are attributed.
- Tolerance 0,02 (relative) and three significant figures from 13,6 eV are justified. Vastaus holds 1,89 eV.
- Line spectrum: the explanation from quantised levels and energy conservation is correct, and $E_n$ is given as data, as the scope requires.
