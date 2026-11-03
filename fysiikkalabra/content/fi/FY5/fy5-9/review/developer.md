VERDICT: DONE

Round 1 fix.

Blocking (inquiry.json): koe-5 prompt now also asks "Miksi jaksonaika kasvaa suurilla kulmilla?"; johtopaatos prompt asks "Miksi massa vaikuttaa jousella mutta ei heilurilla?"; tarkistus-3 prompt adds "ja mitä tämä kertoo jaksonajasta". No answers revealed; criteria kept.

Polish: inquiry.json calc "kulmakiihtyvyys" -> "ratakiihtyvyys $a_\text{t} = -g\sin\alpha$"; lang/fi.json sims.fy5-9.selite "Jousella punainen nuoli on voima, ..."; lesson.md: damping/clock sentence (the clock's weight or spring keeps the amplitude), linking sentence in "Miksi amplitudi ei muuta jaksonaikaa", units in the three symbol lists as LaTeX; figures.py: E_p label moved off the parabola, x = A / x = -A labels in the spring figure, A arrow on the peak in x(t) (figures regenerated into lesson.md).
FY10 investigation "Putoamiskiihtyvyyden määrittäminen heilurin avulla" exists (content/fi/tutkimukset/fy10-heiluri), reference kept.
Energy colour: palette has no free energy colour (orange = acceleration here, green = E_k); violet kept for E_p, not changed.
Exercises: L1-05 frictionless + "metreinä" in question; L1-04 situation + real check (average force x distance); L1-01 "alle kilogramman"; L2-01 plausibility sentence; L3-03 clock wording and rounding warning (0,9997 gives 26 s). answers.py unchanged.
Sim canvas: paints after "Aseta alkutila" at 390 px (136010 drawn pixels, verified in browser); blank koe captures are a capture artifact, no change.
