VERDICT: PASS
CONTENT-HASH: 09aa7395019efc50

## Blocking
None.

## Polish
- k7 b Kaava: $Q_\text{iv}$ and $Q_1$ are used without being named in Annettu/Kysytty (ilmanvaihto ja käyttövesi; taloon annettu lämpö). One short naming would help a student learning from the solution.
- k7 e Kaava: $Q_1$ is again unnamed there; the three lines (pumppu, öljykattila, päästö) are clear but "päästökerroin" in the last row could be a symbol with its unit.
- k2 b: Sijoitus ends at $-273\,{}^\circ\text{C}$ and Vastaus says "noin $-270$"; the rounding reason is given, but a one-clause bridge ("pyöristetään kahteen merkitsevään") would remove the jump.
- k6 c Kaava: $k$ is introduced as the slope after $P = cm\,\Delta T/\Delta t$; fine, but naming $k$ before its use in the Kuvaajan lukeminen step would read more smoothly.

## Checked
- Changed part only: the Kaava step of every model answer in fy3-k2 to fy3-k7 (k1 has single Perustelu steps, unchanged in form).
- Each Kaava now starts from the basic law and derives the working form before any number: k2 b (slope, line, zero condition, $\theta_0$), k3 a-c ($G=mg$, $p=p_0+G/A$, $pV=nRT$; $W=Fs$, $F=pA$), k4 a-c ($Q_1,Q_2,Q_3$ summed; $\eta = E_\text{hyöty}/E$, $E=m_\text{k}H$), k5 c-d (hydrostatic balance solved symbolically for $h_\text{max}$), k6 c-d ($P=Q/\Delta t$, $Q=cm\Delta T$; $Q=P\Delta t=sm$), k7 a, b, d, e ($P_i=U_iA_i\Delta T$, parallel sum; $\varepsilon=Q_1/W$, $\eta$ definitions). This matches the teacher's rule (basic principle, then derive, never open with the combined formula).
- Symbolic simplification runs to the end before the Sijoitus step; one equation per row, equals signs aligned.
- Kaava does not disclose the task's answer or model beyond what the solution should show; no step skips a stage a student could not follow.
- Single-formula Kaava steps (k3 d, k5 a) are a basic law ($\Delta U = Q - W$, $\Delta l=\alpha l_0\Delta T$), so no derivation is missing.
- Numbers in Sijoitus match answers.py output and the rubric details; practice.py check OK.
- Unchanged parts (task levels, workload, variety, rubric fairness) not re-judged in this delta.
