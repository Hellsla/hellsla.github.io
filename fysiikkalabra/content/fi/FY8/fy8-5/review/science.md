VERDICT: PASS
CONTENT-HASH: 922733549dfa158a

Full review (scope: a changed line carries a number). Changes of this round: the section heading and text now say the orbital describes the electron's quantum state (the atom's allowed standing wave) that sets the detection probabilities; the 90 % region is presented as an illustration with a conventional threshold, not as the definition; the Tiivistelmä says the same.

## Blocking

None.

## Polish

1. lesson.md "Orbitaali kuvaa elektronin kvanttitilaa", last sentence — "Esimerkiksi $2\text{p}$-orbitaali on yksi vetyatomin tiloista": there are three 2p orbitals (the Kaava section says so). "Esimerkiksi kukin kolmesta $2\text{p}$-orbitaalista on yksi vetyatomin tiloista" avoids reading "2p" as a single state.

## Checked

- New definition: orbital = one-electron quantum state (standing wave) whose amplitude squared gives the detection probability; the 90 % surface as a chosen threshold, ~1/10 of measurements outside. Consistent across Ydinajatus, Tiivistelmä, misconception, tarkistus-1/4 feedback and the sim's calc box ("raja on pinta, jolla todennäköisyystiheys on sama ja jonka sisään jää $p$").
- Nodes: $n-1$ in total, 2s spherical node, 2p nodal plane; "more nodes, higher energy" restricted to hydrogen (and same-shape states in many-electron atoms) — correct; tarkistus-2 one correct option.
- Recomputed: 1s 90 % radius $2{,}661\,a_0 = 0{,}141\,\text{nm}$ (50 % $0{,}071$, 95 % $0{,}167\,\text{nm}$); most probable radius $a_0 = 0{,}0529\,\text{nm}$; 2s peak $0{,}277\,\text{nm}$, node $0{,}106\,\text{nm}$; 2p peak $0{,}212\,\text{nm}$.
- Example: $\Delta E = 1{,}889\,\text{eV}$, $\lambda = 656\,\text{nm}$ (Hα); $3\text{s}\to2\text{p}$ same line in hydrogen — correct.
- Shell counts $n^2$ orbitals, $2n^2$ electrons; virhe 18; carbon and nitrogen configurations; filling order for light atoms — correct.
- ennuste-1 values: SD of the in-fraction at $N = 1000$ is $0{,}95\,\%$, so $90{,}1$–$91{,}8\,\%$ and 82 outside are plausible model values; siirto $2700$ (mistakes $5400$, $3000$); tarkistus-3 $10{,}2\,\text{eV}$ (mistakes $17{,}0$, $3{,}4$). All agree with lesson-answers.py.
- STM caption (tunnelling current between tip and surface) — correct.
- Hash same at start and end.
