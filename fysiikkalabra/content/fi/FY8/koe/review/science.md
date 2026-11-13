VERDICT: FAIL
CONTENT-HASH: f88ddf35762aaa28

## Blocking
1. **(A) fy8-k1 g, Perustelu and Yleisiä virheitä.** The options are $12{,}8$, $16$, $20$ and $32\,\text{h}$. The solution explains a distractor of $7{,}8\,\text{h}$ ("lineaarinen päättely"), which is not an option. It never explains $12{,}8\,\text{h}$, which comes from $3{,}2 \cdot 4{,}0$. A stray fragment also follows: "… vakiomäärän väheneminen. ja $32\,\text{h}$ syntyy …". The common-mistakes line "lasketaan puoliintumisaika lineaarisesti (g)" refers to no option. Make the options and the explanations match: either put $7{,}8\,\text{h}$ back as an option, or explain $12{,}8\,\text{h}$ by its real error.
2. **(A) fy8-k1 h, Perustelu.** The options are $5 \cdot 10^{3}$, $5 \cdot 10^{5}$, $5 \cdot 10^{7}$ and $5 \cdot 10^{9}$. The solution explains $50$ and $5 \cdot 10^{4}$, which are not options, and leaves $5 \cdot 10^{3}$ and $5 \cdot 10^{5}$ unexplained. Each distractor needs a real error behind it, and the feedback must name it. For example, $5 \cdot 10^{5}$ comes from reading the energy as $2\,\text{MeV}$ or from losing two powers of ten.
3. **(A) fy8-k7 c, Järkevyys.** The solution says $2{,}4\,\text{pm}$ is "noin tuhannesosa atomin koosta". An atom is about $0{,}1$–$0{,}3\,\text{nm}$, so the ratio is about $1/40$–$1/100$, not $1/1000$. Correct it, for example to "noin sadasosa atomin koosta" or "paljon atomia pienempi".

## Polish
- fy8-k2 c, Kuvaajan lukeminen: $(5{,}08;\ 2{,}02)$ is the lower end of the second bar (the $590\,\text{nm}$ point), not the third. The numbers are right.
- fy8-k7 e: "saastuttaisi valmistuslaitoksen" is not a sound reason. A $\text{TBq}$-scale batch is a radiation-shielding and dose problem, not contamination. Say "vaatisi raskaan säteilysuojauksen" or drop it.
- fy8-k4 d, third criterion: it largely repeats criteria 1 and 2 (assessment overlap, not physics).

## Checked
- I recomputed every number in one script and compared it with answers.py and the solutions:
  - k1: b ($f_0 = 5{,}61 \cdot 10^{14}\,\text{Hz}$, $W = 3{,}7 \cdot 10^{-19}\,\text{J} = 2{,}3\,\text{eV}$), d ($5{,}4$, distractors $3{,}0$ and $0{,}6$), e ($2{,}74$, $3{,}96$, $1{,}32\,\text{V}$), g ($20\,\text{h}$), h and i
  - k2: frequencies, the read slope ($6{,}84 \cdot 10^{-34}$), the least-squares $h$ ($6{,}81 \cdot 10^{-34}$), the extreme lines through all five bars ($7{,}37$ and $6{,}18$, so $\Delta h = 0{,}60 \cdot 10^{-34}\,\text{J}\,\text{s}$), and the points sitting below $hf/e$ by $0{,}02$–$0{,}07\,\text{V}$
  - k3: $\lambda$, $N(15) \approx 31$, $\sqrt{N}$ and the deviations
  - k4: $28{,}30\,\text{MeV}$, $7{,}07\,\text{MeV}$, $17{,}59\,\text{MeV}$, $3{,}37 \cdot 10^{14}\,\text{J/kg}$
  - k5: $656{,}5\,\text{nm}$, $121{,}6\,\text{nm}$, $2{,}80\,\text{eV}$
  - k6: $\mu = 0{,}114\,\text{mm}^{-1}$, $d_{1/2} = 6{,}1\,\text{mm}$, $d = 31{,}4\,\text{mm}$, $3{,}9\,\%$
  - k7: $0{,}321$, $1540\,\text{MBq}$, $511\,\text{keV}$, $2{,}43\,\text{pm}$, $5{,}32\,\text{mSv}$, $\text{C-11}$ $0{,}0022$ and $2{,}7\,\text{TBq}$
- All of round 1's blocking items are fixed: k1 d distractor origins, the k2 c extreme lines, and the direction in k2 d with a colour-dependent error affecting the slope.
- All of round 1's polish items are fixed except g and h, whose rewrite caused blocking items 1 and 2.
- Each choice item has exactly one correct option. The physics of a, c, f, i and j is right. The figure fy8-k1-stop and its alt text match the data ($0{,}24\,\text{V}$ at $6{,}2 \cdot 10^{14}\,\text{Hz}$).
- The binding-energy and fusion explanation is right, and tunnelling is credited in Hyväksytään myös. The k5 d standing-wave wording keeps out of de Broglie.
- k6 combines the inverse-square law with exponential shielding and the public limit of $1\,\text{mSv}$. Its assumptions are stated.
- The exam stays within the FY8 scope. The points add up: $20 + 2 \cdot 15 + 20 = 70$.
- The content hash was the same at the start and the end.
