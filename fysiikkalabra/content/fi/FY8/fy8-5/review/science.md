VERDICT: PASS
CONTENT-HASH: 8c4a1518d4ca3b47

Follow-up review of the fix commit 2c31ff041 (delta from 922733549dfa158a, whose full review is kept below). Change: inquiry.json:6 `learn[1]` now reads "tulkitsemaan orbitaalin elektronin kvanttitilaksi ja sen kuvan alueeksi, jonka sisällä elektroni havaitaan valitulla todennäköisyydellä."

## Blocking

None.

## Polish

1. lesson.md:274 — "Esimerkiksi $2\text{p}$-orbitaali on yksi vetyatomin tiloista": there are three 2p orbitals; "kukin kolmesta $2\text{p}$-orbitaalista" avoids reading 2p as one state.
2. inquiry.json:110 (sim lead, student-facing) and :3 — "satunnaisista osumista syntyy orbitaali" → "…orbitaalin kuva"; misconception and tarkistus criterion "orbitaalin raja" means the drawn boundary (C).

## Checked

- New learning goal is right and matches the lesson: orbital = quantum state, its picture the region of chosen probability (Ydinajatus heading and :274, Tiivistelmä :1442).
- Consistency: grep of "orbitaali" definitions — no remaining sentence defines the orbital itself as the region.
- New definition: one-electron quantum state (standing wave) whose amplitude squared gives the detection probability; 90 % surface a chosen threshold. Consistent across Ydinajatus, Tiivistelmä, misconception, tarkistus-1/4 and the sim's calc box.
- Nodes: $n-1$ in total, 2s spherical, 2p planar; "more nodes, higher energy" restricted correctly; tarkistus-2 one correct option.
- Recomputed: 1s 90 % radius $2{,}661\,a_0 = 0{,}141\,\text{nm}$ (50 % $0{,}071$, 95 % $0{,}167\,\text{nm}$); most probable $a_0 = 0{,}0529\,\text{nm}$; 2s peak $0{,}277\,\text{nm}$, node $0{,}106\,\text{nm}$; 2p peak $0{,}212\,\text{nm}$.
- Example: $\Delta E = 1{,}889\,\text{eV}$, $\lambda = 656\,\text{nm}$; $3\text{s}\to2\text{p}$ same line in hydrogen.
- Shell counts $n^2$, $2n^2$; virhe 18; C and N configurations.
- ennuste-1 (SD $0{,}95\,\%$ at $N = 1000$); siirto $2700$ (mistakes $5400$, $3000$); tarkistus-3 $10{,}2\,\text{eV}$ (mistakes $17{,}0$, $3{,}4$). All agree with lesson-answers.py.
- STM caption correct. Hash same at start and end.
