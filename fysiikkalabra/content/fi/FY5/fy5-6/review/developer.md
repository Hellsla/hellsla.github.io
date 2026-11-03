VERDICT: DONE

Round 1 (fix). check_lesson.py fy5-6: all ok.

inquiry.json: koe-1 numeric tolerance 0.01 -> 0.001 (accepts 7,66-7,68, rejects 7,60); koe-1/koe-2 Alkutila: names with $v$/$h$/$m$ and `values` maps so h, m, v render as LaTeX with units (v as $7{,}00\,\text{km/s}$), no shared script changed; escape-speed clause removed from the virhe feedback; kertaus optional.
lesson.md: worked example gamma M shown as 3,98438e14 (chain gives 7659,7); bare (kg), (m), (m/s), (s) -> LaTeX; Painottomuus uses F for the gravitational force. Figures regenerated from figures.py (figures.py only, no figcat).
figures.py: cannon trajectories grey dashed / ink / green dotted; vr label "geostationaarinen"; paino figure labels F; Earth-orbit overlay circle grey instead of orange.
lesson-answers.py: stale comment fixed.
exercises.json / solutions.md: L3-02 task "Älä pyöristä välituloksia ennen vähennystä." and note in Muunnokset, untaught approximation removed from Järkevyys; L3-01 grammar and r vs h named; L2-04 "$650\,\text{N}$ eli $6{,}5 \cdot 10^{2}\,\text{N}$".
Not done: unit field "m/s²" in LaTeX (no format precedent; a plain unit is read by the lint).
