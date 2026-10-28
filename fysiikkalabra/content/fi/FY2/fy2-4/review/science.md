VERDICT: PASS
CONTENT-HASH: 3d76e58b5c55fcf6

## Blocking

## Polish
- inquiry.json koe-1, siirto, tarkistus-2 (solutions and hints) and exit-ticket.json q1: numeric substitutions use `\dfrac{…}{…}` (for example $\dfrac{900\,000\,\text{J}}{3600\,\text{s}}$). The worked example and the prose use the colon. If the colon rule also covers numeric substitution, write $a : b$. Keep the symbolic fractions.
- lesson-answers.py:820 computes 333 %, but inquiry.json virhe says $3{,}3 = 330\,\%$. Align the comment with the text.
- sim.js:899 "Nuolten paksuudet ovat suhteessa tehoihin": the input arrow is always 100 px, so the widths compare only within one picture. Add "saman kuvan sisällä".
- inquiry.json koe-1 intro: the reason given for locking $P_\text{o}$ (load dependence) has no effect in a constant-η model. This is wording only, because t is still isolated.

## Checked
- One Python run recomputed every lesson-answers.py key and every inquiry and exit-ticket number, and all match. The values are: 36 kJ; 1200 J (70, 1,3, 0,75); 24, 15 and 45 kW; 75 % (25, 0,75); 2,0 W; 30 % and 100 %; 250 W (1250, 15 000); 80 % (20, 125); 70 % and 150 J; 50 and 150 W; and the cm example's 80 %.
- Both round-2 blockers are fixed. The kertaus 1,3 J feedback now argues from units. The worked example converts $36\,000\,\text{J} = 36 \cdot 1000\,\text{J} = 36\,\text{kJ}$ and $360\,\text{kJ}$ by substitution.
- The round-2 polish was taken: the heater qualifier, the stale lesson-answers line, and koe-1 calling 25 % a model input.
- The formulas $\eta = E_\text{a}/E_\text{o} = P_\text{a}/P_\text{o}$ (steady power, t cancels) and $E_\text{o} = E_\text{a} + E_\text{h}$ are correct and inside FY2 scope. There is no work, $Q = cm\Delta T$, chain or Carnot.
- The figures are to scale: 6/120 px is 5 %; 4,8/96 and 4,8/16 px give inputs in the ratio 1 : 6 with equal useful bands.
- The sim implements the model and states its limits. The canvas and readout are LaTeX (1280 px capture).
- Koe-1 and koe-2 lock laite and $P_\text{o}$ and vary t. Their values are in slider range, and simState gives Eo, Ea and Eh.
- The worked example has seven stages and solves symbolically first. Its conversions are by substitution, its 2 s.f. are justified, and its check is real.
- The siirto, koe-1 and tarkistus-2 solutions are complete and correct. There is no ×, and numbers with units are in LaTeX.
