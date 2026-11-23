VERDICT: PASS
CONTENT-HASH: 2b6ae75f760733f9
SCOPE: delta caption-label,md-paragraphs,numbers,reflow,typography from d29240691e2c2f1f base b5600a6
Delta (queue 8g): twelve solutions now give the Kaava step as aligned rows that start from energy conservation or work ($\Delta E_\text{k} + \Delta E_\text{p} = 0$, $E_\text{k} = W$, $E_{\text{k},A} + E_{\text{p},A} = E_{\text{k},B} + E_{\text{p},B}$). Several Mallivastaus and Sijoitus paragraphs were split with the words unchanged, and captions lost their marker. No data, substitution or answer changed.

## Blocking
- none

## Polish
- solutions.md:86, :171 and :234, Kaava: the step from $E_\text{k} = W$ to $\tfrac{1}{2}mv^2 = eU$ uses $W = eU$, but no row states it. Line 76 does state it ($E_\text{k} = W = qU$). Fix: write $E_\text{k} = W = eU$ on the first row, as line 76 does.
- solutions.md:106: $E_{\text{k},\text{e}} = W = eU$ is right in magnitude. The lesson writes $W_{AB} = qU_{AB}$ with the sign, though, and for the electron $q = -e$ and $U_{AB} < 0$. Fix (optional): write $\lvert q \rvert U$, as the lesson's $\tfrac{1}{2}mv^2 = \lvert q \rvert U$ does.

## Checked
- Every new Kaava chain is algebraically right and ends in the formula its unchanged substitution uses.
- Line 46: $\Delta E_\text{p} = e(V_2 - V_1)$ and $\Delta E_\text{k} = e(V_1 - V_2)$ have the right signs. The potential falls from 200 V to 50 V, so $\Delta E_\text{k} = 150\,\text{eV}$.
- Line 96: energy conservation with $E_\text{p} = -eV$ follows the lesson's $E_\text{p} = qV$ with $q = -e$, and the electron gains energy towards higher potential.
- Line 116: adding $V = Ex$ makes the turning-point chain explicit. The proton's kinetic energy becomes potential energy, and $d - x = 4{,}34\,\text{mm}$.
- Line 208: I derived $y = \tfrac{1}{2}\,\tfrac{eU_\text{p}}{md}\,\tfrac{mL^2}{2eU_\text{k}} = \tfrac{U_\text{p}L^2}{4dU_\text{k}}$ myself and got the same result. The mass and the charge cancel, and $y = 2{,}78\,\text{mm}$.
- One script recomputed every substitution: 150 eV; −75 eV; −120 eV; 4,39·10⁵ m/s; 284 V; 6,80·10⁶ m/s; 42,86; 4,34 mm; 2,52·10⁷ m/s; 2,78 mm; 8,39·10⁶ m/s. All agree with the solutions.
- Paragraph splits (L3 and mallivastaus items, histogram task): words and numbers unchanged; the physics passed earlier still holds.
- Notation follows the lesson: $E_\text{p} = qV$, $W$, $E_\text{k}$, $V = Ex$, $E = U : d$.
- Content hash checked at the start and the end.
