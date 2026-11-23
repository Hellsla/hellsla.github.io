VERDICT: PASS
CONTENT-HASH: a6713c0322ee81f2
SCOPE: delta (work queue 8g, Kaava steps of the model solutions)

## Blocking

## Polish
- The round-1 polish items (the answers.py:49 comment 216,6 → 214,7, and the L3-06 tolerance wording) are still open. They were not part of this change.

## Checked
- `git diff a7ec649ae6`: only solutions.md changed. exercises.json and answers.py are unchanged.
- I compared every field with whitespace normalised. Only the Kaava fields of L3-04 and L3-05 changed. The rest are paragraph splits.
- L3-04 a): it starts from $Q = (m_\text{alku} - m_\text{loppu})c^2$ with $m_\text{alku} = m_\text{U} + m_\text{n}$ and $m_\text{loppu} = m_\text{Ba} + m_\text{Kr} + 3m_\text{n}$. The simplification to $(m_\text{U} - m_\text{Ba} - m_\text{Kr} - 2m_\text{n})c^2$ is correct.
- L3-04: the Sijoitus now substitutes into that simplified form ($-2 \cdot 1{,}008665\,\text{u}$). I recomputed $235{,}043930 - 140{,}914411 - 91{,}926156 - 2{,}017330 = 0{,}186033\,\text{u}$, which gives $173{,}29\,\text{MeV}$, as stated.
- The atomic masses are consistent: the electron counts balance (56 + 36 = 92).
- L3-05: $E = Lt = \Delta m_\text{a}c^2$ is correct. The mass fraction $f = (4m_\text{H} - m_\text{He})/(4m_\text{H})$ is correct. $\Delta m_\text{a} = f\,m_\text{vety}$ correctly states the meaning of $f$. The reserve $0{,}70\,M$ is unchanged.
- The hash was a6713c0322ee81f2 at the start and at the end.
