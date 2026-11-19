VERDICT: PASS
CONTENT-HASH: de64c6015046f816
Mode: delta (round 3)

## Blocking

## Polish
- content/fi-easy/FY4/fy4-10/exercises/solutions.md:65 (ice-hockey Kaava) — "joten $\Delta E$ on sama kuin $\tfrac12 m_1 v_1^2 - \tfrac12 (m_1 + m_2)\,v'^2$" turns the final symbolic equation into words. A display formula reads more clearly, and the shared layout could wrap it on a phone. The earlier items (the capital after the semicolon "; Kappaleiden …", "joten …, joten …", the ballistic pendulum's equation in words, the L2-10 items) are still open. This change does not touch them.

## Checked
- Hash de64c6015046f816 at the start and the end.
- The only change is "$\Delta E = \tfrac12 m_1 v_1^2 - \dots$" → "$\Delta E$ on sama kuin …". The physics is unchanged and right: in a completely inelastic collision, the decrease in kinetic energy is $E_\text{k,ennen} - E_\text{k,jälkeen}$ with $v_2 = 0$.
- Recomputed: $v' = 85 \cdot 6{,}0 / 160 = 3{,}1875\,\text{m/s}$ and $\Delta E = 1530\,\text{J} - 812{,}8\,\text{J} = 717{,}2\,\text{J}$. These are unchanged.
- No number, answer, unit or tolerance changed.
- Captures opened: none. I judged from the diff and the packet.
