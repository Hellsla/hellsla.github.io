VERDICT: PASS
CONTENT-HASH: 017653cf72f2fca8
SCOPE: delta caption-label,md-paragraphs,numbers,reflow,teacher-figure,typography,wording from 5d5b49dbc8de8981 base 98218de

## Blocking

## Polish
- solutions.md fy6-2-L2-03 and L3-04 Formula — the new blocks label the loop and junction equations "$\Sigma U = 0$" and "$\Sigma I = 0$", the notation of the later Kirchhoff chapter; the equations themselves ($U_\text{battery} = U_\text{m} + U_\text{lamp}$, $I_1 = I_2 + I_\text{m}$) are what the solutions already used — drop the labels or say in words "the voltages of the loop add up to the source voltage".
- solutions.md fy6-2-L2-07 Formula — the new symbol $s$ for half the range is easily read as a standard deviation, and L3-04 uses $s$ for the relative decrease and L1-03 for $\Delta U : U$ — name it in words where it is introduced ("estimate of the spread $s$") or pick distinct symbols.
- solutions.md fy6-2-L3-05 Formula — the last row $\Delta R = \tfrac{\Delta R}{R} \cdot R$ is circular as written — write $\Delta R = \left(\tfrac{\Delta U}{U} + \tfrac{\Delta I}{I}\right) R$.
- Previous polish on L2-10 Answer wording still applies.

## Checked
- Diff only: Formula lines rewritten as aligned blocks (the packet's diff view drops `&` and `\\`; checked in the file that each is a proper aligned block), starting from $\Delta x = p\cdot x + n\cdot r$, the loop sum and the junction sum; algebra in L3-04 ($U = U_0 : (1 + R_1/R_2 + R_1/R_\text{m})$) correct, and the moved derivation text from Substitution into Formula loses no step.
- Recomputed in one script: 10.6 %, 3.20, 2.17 %, 0.1522 V, 12.49 V, 0.08245 V, 5.714 V, 4.76 %, 0.0486 V, 5.997 V / 0.05 %, 117.71 Ω, 2.90 Ω, 2.98: all agree.
- L2-03 $U_\text{lamp} = R_\text{lamp} I \approx 0$ with the condition $I \approx 0$ stated: correct model of a voltmeter in series.
- exercises.json: only "Example data:" removed from two captions; the Given lines still say example data. answers.py unchanged.
- Guardrails: half the range is still "a simple estimate of the spread, not the uncertainty of the mean"; error limit as manufacturer's limit; consistency criterion unchanged.
- Picture fy6-2-multimeter-task teacher-approved; code still shows 1,37 V on the 20 V range.
- Hash read at start and end: unchanged.
