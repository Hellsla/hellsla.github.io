VERDICT: FAIL
CONTENT-HASH: faf427df85f5c676

## Blocking
- solutions.md:236 (fy3-1-L3-04, Formula): **A.** The text reads $\dfrac{x}{m} = c\, g_\text{Earth} \quad (c\text{: spring constant})$. Here $c = x/(mg) = x/F$ is the extension per newton, the inverse of the spring constant $k = F/x$. So "spring constant" names the wrong quantity. It is also a FY4 term: the previous round removed it from L1-02 for exactly this reason. Fix: "$(c$: extension of the spring per newton$)$". The Finnish "jousen vakio" is ambiguous, and its matching "venymä newtonia kohti" would make the two languages agree. Also consider writing the first row's left side as $(x/m)_\text{Earth}$, which is the form the last row uses.

## Polish
- solutions.md (fy3-1-L2-05, Formula): the step from $G = m g$ to $g = \Delta G/\Delta m$ jumps over the reason (the slope of a line through the origin). One row such as "slope of the $(m,G)$ line" would make the derivation complete.
- solutions.md:19 (fy3-1-L1-02): the earlier note still applies. The check's product $0.50 \cdot 12 = 6.0$ has no units.

## Checked
- The diff changes only the Formula steps and splits paragraphs. All the split paragraphs have the same text as before, and no number, answer or Substitution changed.
- On disk every changed Formula step is an aligned block. Each starts from its basic equation ($G = mg$, the proportionality $x \propto F$, $F_\text{max} = m_\text{max} g_\text{Mars}$) and is solved symbolically to the form used in the Substitution: L1-02, L1-04, L2-01, L2-03, L2-04, L2-05, L2-06, L2-07, L2-08, L3-01, L3-02, L3-03, L3-04 and L3-05.
- Every algebra step checked. In L3-02, $m_\text{Moon} g_\text{Moon} = m_\text{Earth} g_\text{Earth}$ gives the same lifting force on Earth and on the Moon, as the task states. In L3-03 the scale reading $L = G/g_\text{Earth}$ is modelled correctly.
- Recomputed in one script: L3-04 $3.59\,\text{m/s}^2$, L3-05 $682\,\text{kg}$, L3-03 $68.75\,\text{kg}$. Each matches.
- The FY3 scope holds apart from the "spring constant" item above.
- The hash was the same at the start and the end.
