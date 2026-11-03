VERDICT: PASS
CONTENT-HASH: 5b16741581f0e401

## Blocking

## Polish
- answers.py L2-02 — the comment "dE = 3,0237 eV" disagrees with the solution's $3{,}0244\,\text{eV}$, which my recomputation also gives. The comment is the only problem; the answer, 6, stands.
- solutions.md fy8-3-L3-01 — the count of 3 assumes each atom takes energy from one collision while in its ground state. An atom already at $n = 2$, hit again, could reach higher levels. The task's wording ("perustilassa oleviin") implies the assumption, but naming it in the Periaate would close the gap (C, optional).

## Checked
- One script recomputed all 12 answers from the task text: −0,850 eV; 12,75 → 12,8 eV; 2,551 eV; 1,511 eV; 457,0 THz; 434,2 nm; n = 6,02 → 6; 620,0 nm; 1,900 eV; 3 lines; 468,9 nm; 6,80 eV. All match exercises.json and answers.py.
- L2-03 figure (`lessons/FY8/fy8-3/figures.py` levels_task): $E_3 = -3$ and $E_2 = -5\,\text{eV}$ sit on the 1 eV grid, as the solution reads them.
- L3-01: $E_3 - E_1 = 12{,}09 \le 12{,}5 < 12{,}75\,\text{eV}$. The lines are 3→1, 3→2 and 2→1, and the 102, 122 and 656 nm values are right.
- L3-02: the He⁺ levels $-54{,}4\,\text{eV}/n^2$ are right, and the 1876/4 check is valid.
- L3-03: a 10,2 eV photon can only ionise an atom at n = 2, not excite it, and $E_\text{k} = 6{,}8\,\text{eV}$.
- L2-04: ionisation needs no matching level difference (stated), and $E_\text{k} = 1{,}9\,\text{eV}$.
- Every solution solves symbolically first, shows the eV↔J conversions and justifies its rounding by the limiting datum: 13,6 eV, or the 2,0 eV read off the figure.
- Scope: within the FY8 notes ($E_n$ given, no derivation).
