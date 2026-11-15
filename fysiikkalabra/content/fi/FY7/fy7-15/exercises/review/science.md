VERDICT: FAIL
CONTENT-HASH: 039f947b5c91a8ac

## Blocking
- content/fi/FY7/fy7-15/exercises/exercises.json:92 — B, scope and consistency. L1-09 is a Malus calculation. Situations A, C, D and E need $I = I_0\cos^2\theta$ (150, 240, 100 and 125 W/m²), but the task has no "Syventävä tehtävä." lead. The scope note puts Malus's law in the extension material, and the teacher's decision of 2026-11-15 makes every Malus/Brewster calculation an extension task. Left unmarked, it looks like a core-path task that needs extension physics. — Fix: begin the text with "Syventävä tehtävä.\n\n" as in the other 14 tasks.
- content/fi/FY7/fy7-15/exercises/exercises.json:336 — B, the same problem. L3-03 computes $E = (E_\text{max} - E_\text{t})\cos^2\theta + E_\text{t}$ = 117 lx with Malus's law and has no lead. — Fix: the same lead.

## Polish

## Checked
- The hash is the same at the start and the end.
- Diff against 528023bb26^, field by field in a script. Fourteen tasks (L1-02, L1-03, L1-04, L1-05, L1-07, L1-08, L1-10, L1-11, L2-01, L2-02, L2-03, L3-01, L3-02, L3-04) gain only the prefix "Syventävä tehtävä.\n\n". No answer, unit, tolerance, choice, data, figure or core flag changed, so the earlier recomputation of all 22 answers still stands.
- Each newly marked task really uses Malus's law (L1-02, L1-03, L1-07, L1-10, L2-01, L2-02, L3-01, L3-04) or Brewster's law (L1-04, L1-05, L1-08, L1-11, L2-03, L3-02).
- Together with L2-04 to L2-08 and L3-05, 20 of the 22 calculation tasks are now marked. The two left out are listed under Blocking.
- The core tasks L1-01 (halving only) and L1-06 (qualitative glare) stay unmarked and core. That is right: neither needs Malus or Brewster.
- Level 2 has no core task (L2-01 and L2-02 have core: false), so no task is both extension and core.
- Recomputed L1-09 (D 100 < E 125 < A 150 < B 200 < C 240 W/m²) and L3-03 (404 · 0,250 + 16 = 117 lx). Both are correct; only the marking is missing.
