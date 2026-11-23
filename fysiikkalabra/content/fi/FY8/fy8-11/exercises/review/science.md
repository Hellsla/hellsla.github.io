VERDICT: PASS
CONTENT-HASH: c3c134567554661f
SCOPE: delta (work queue 8g, Kaava steps of the model solutions)

## Blocking

## Polish
- solutions.md (L2-02) — "$E = Q$" is a terse way of saying that the energy of one reaction is $Q$. Writing "$E = Q$ (yhden reaktion energia)" would be clearer. This is wording, not physics.

## Checked
- `git diff a7ec649ae6`: only solutions.md changed. exercises.json and answers.py are unchanged.
- I compared every field with whitespace normalised. Only the Kaava fields of L1-01, L1-02, L1-04, L2-02, L2-03, L3-01 and L3-02 changed.
- Each block starts from $Q = \Delta m\,c^2$ with $\Delta m = m_\text{alku} - m_\text{loppu}$, lists both sides, and then gives the reaction-specific form. This is the lesson's *Kaava: Reaktioenergia*.
- L1-01 Li + n → He + T: correct. L1-04 2D → He + n: correct. L2-02 D + T: correct, with energy per mass $Q/(m_\text{D} + m_\text{T})$. L2-03: the neutron balance $x = 2$ and $m_\text{U} + m_\text{n} - m_\text{Xe} - m_\text{Sr} - 2m_\text{n}$ are correct. L1-02: the given $\Delta m$ is used directly.
- L3-01: $E = Pt = NQ$ and $m = Nm_\text{U} = Pt\,m_\text{U}/Q$ are correct.
- L3-02: $\Delta m = 4m_\text{H} - m_\text{He}$ (atomic masses, so the annihilation of the positrons is included) and $N/t = P/Q$ are correct.
- The substitutions and answers are unchanged.
- The hash was c3c134567554661f at the start and at the end.
