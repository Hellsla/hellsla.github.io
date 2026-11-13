VERDICT: FAIL
CONTENT-HASH: 81704aa1f77b917f
Delta review (merge of #523 solution practice into #522, 2026-11-13) of the version passed at bac2ad0da5027489.

## Blocking
1. inquiry.json, task with the electron in the potential graph (solution, **Kaava**), class B (internal consistency). The merged line "Potentiaaliero on $U = V - V_0$. Sähkökentän tekemä työ $W = eU$" defines $U$ as end minus start. The unit's formula *sähkökentän tekemä työ* $W = QU$ defines $U = U_{AB} = V_A - V_B$ (start minus end, unit.md line 356). The result is right only because two signs are flipped at once: $e$ is the magnitude of the charge, and $U$ has the opposite sign to the unit's $U$. A student who uses the unit's definition with $Q = -e$ meets an apparent contradiction. Corrected text: "**Kaava:** Elektronin varaus on $Q = -e$ ja kuljettu jännite $U = V_0 - V$, joten sähkökentän tekemä työ on $W = QU = (-e)(V_0 - V) = e(V - V_0)$. Työ muuttuu liike-energiaksi $E_\text{k} = \tfrac12 mv^2$. Alussa liike-energia on nolla, joten $\tfrac12 mv^2 = e(V - V_0)$, ja vauhti on $v = \sqrt{\dfrac{2e(V - V_0)}{m}}$". The Sijoitus line is unchanged.

## Polish
(none)

## Checked
- Electron: $v = \sqrt{2e\cdot150\,\text{V}/m} = 7.264\cdot10^6$ m/s. Charging: $t = sW_0/(3\eta UI) = 3.86$ h. s5 capacitance: $b = 93 - 70.8 = 22.2$ pF.
- The number and the direction of motion are right. The finding concerns only the sign convention of $U$ against the unit's #522 formula (guardrail 6).
Every number in the changed lines was recomputed with an independent script (scratchpad fy9merge/sci_fi.py); `units.py hash` gave the same value at the start and the end. LaTeX in all added lines has balanced `$` and braces.
