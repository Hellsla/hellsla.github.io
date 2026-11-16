VERDICT: PASS
CONTENT-HASH: 74a741769156fbc5

## Blocking
None.

## Polish
- k4-d rubric, criterion 1: the comparison is written "$7{,}07$ vs. $1{,}11$ ja $2{,}83\,\text{MeV}$". Since the task text no longer gives the helium-4 value, a student who carries a wrong a) value into d) should still get these 2 p, as the intro promises. Adding "(tai a-kohdan oma arvo)" would make that explicit.
- k3-c Sijoitus (from round 1, unchanged): the text writes $0{,}217 \cdot 15 = 3{,}25$, but the product is $3{,}255$. The factor $0{,}0386$ belongs to $3{,}255$ ($e^{-3{,}25} = 0{,}0388$). The result $31$ holds either way.
- k4-c Muunnokset: the aligned row "$= 5{,}030151$" leaves out the unit, and the next row "$\cdot\,1{,}6605 \cdot 10^{-27}\,\text{kg}$" multiplies it. This is correct, but "$5{,}030151 \cdot 1{,}6605 \cdot 10^{-27}\,\text{kg/u} \cdot \text{u}$" or "$\ldots\,\text{u} \cdot 1{,}6605 \cdot 10^{-27}\,\text{kg/u}$" would carry the unit through.

## Checked
The hash was 74a741769156fbc5 at the start and at the end. This was a delta review against the version I passed in round 1 (word diff of tasks.json, solutions.md and answers.py).
- **k4 d.** The task now gives only D $1{,}11$ and T $2{,}83\,\text{MeV}$ per nucleon and refers to the helium-4 value from part a. Both stated values are right ($1{,}112$ and $2{,}827\,\text{MeV}$ from the atomic masses), and part a is now not given away. The model answer and the rubric still compare per-nucleon binding energies. That holds here because the nucleon number is conserved and the free neutron has no binding energy: in total, $28{,}3 > 2{,}22 + 8{,}48\,\text{MeV}$. The Coulomb-barrier reasoning is unchanged and correct.
- **Intro.** "$1\,\text{u} = 931{,}5\,\text{MeV}/c^2$ eli $1\,\text{u} = 1{,}6605 \cdot 10^{-27}\,\text{kg}$" is correct.
- **k4-c rubric detail.** "$17{,}59\,\text{MeV}$ eli $2{,}818 \cdot 10^{-12}\,\text{J}$" is correct.
- **solutions.md reflow.** Every chain that was joined or re-broken into aligned rows has the same numbers, signs, units and order as before: k1-b, k2-b/c, k3-c, k4-a/b/c, k5-a/b/c, k6-a/d, k7-a/b/c/d. The aligned blocks are mathematically valid: each continuation row is "$\cdot$", "$-$", "$=$" or "$\approx$" of the line before. The typo fix (Valosähköisessä) is wording only.
- **Recomputed in my own script.**
  - k1-b: $W = 3{,}71 \cdot 10^{-19}\,\text{J} = 2{,}32\,\text{eV}$.
  - k2: $h = 6{,}76$, $7{,}37$ and $6{,}18 \cdot 10^{-34}\,\text{J}\,\text{s}$.
  - k3-c: $30{,}9 \approx 31$.
  - k4: $E_\text{s} = 28{,}30\,\text{MeV}$, $7{,}07\,\text{MeV}$ per nucleon, $Q = 17{,}59\,\text{MeV}$, $3{,}37 \cdot 10^{14}\,\text{J/kg}$, ratio $1{,}1 \cdot 10^{7}$.
  - k5: $656{,}5\,\text{nm}$, $121{,}6\,\text{nm}$, $2{,}80\,\text{eV}$.
  - k6-d: $31{,}4\,\text{mm}$.
  - k7: $0{,}321$, $1540\,\text{MBq}$, $511\,\text{keV}$, $2{,}43\,\text{pm}$, $5{,}32\,\text{mSv}$.

  All agree with answers.py and the solutions.
- **Rubric sums.** Unchanged, and practice.py check is OK.
