VERDICT: PASS
CONTENT-HASH: 9ece00a460a2d407

## Blocking
(none)

## Polish
- lesson.md "Three interactions of a photon in matter" — photoelectric, Compton and pair production, with the energy-range paragraph, go beyond the slot's goals (types, penetrating power, detection, biological effects through ionisation) and add reading load to a one-hour lesson. Shorten it to a few sentences, or make it optional, so the core path stays the ionisation density and the half-value thickness.
- lesson.md "Key idea" / inquiry.json `ennuste-2` — the prediction (a second plate lets through a quarter) is easy for a student who has just read "every half-life halves" in the prerequisites. Make it more arguable by asking for a thickness (for example, how many plates for under $10\,\%$) and leaving the quarter to the experiment.
- inquiry.json `koe-2` — alpha through $5\,\text{mm}$ of aluminium repeats experiment 1 (paper already stopped it). Let the intro say that only beta and gamma carry the evidence, to cut the work to two measurements.
- lesson.md "Types of radiation ionise in different ways" — the arithmetic reads "$5.49 \cdot 10^{6}\,\text{eV} : 34\,\text{eV}$"; in English use a fraction or "divided by" (the same in the worked example's "$I : I_0$").
- inquiry.json `tarkistus-2` — the solution's closing sentence ("same as the half-value thickness of iron") is useful, but the figure capture could not be viewed (the packet lists none); check that the figure shows only the curve and no value that gives away $12\,\text{mm}$.

## Checked
- The opening question (paper stops alpha, yet an alpha emitter is harmful inside the body) is answered in "Radiation in the body". Nothing is disclosed before the prediction.
- Predictions are committed before the evidence. Each wrong option's feedback cites the model values that refute it, and the experiments can refute them: aluminium stops beta, and lead's net count falls to about a quarter at $10\,\text{mm}$.
- Variable control is sound: experiments 1 and 2 vary only the source with barrier and plates locked, and experiment 3 varies only the thickness. The conclusion criteria are observable and call the numbers "values of the model".
- The simulation is justified: pulse counts emerge randomly (the "random variation" point is taught) and background subtraction is practised. The model's simplifications are stated in Mallin oletukset.
- The worked example has seven stages, each with one step, symbolic before numeric, with a reasonableness check that is a real one.
- The transfer task (lead apron) has three progressive hints. Its mistake values are real ($84.7$ upside-down exponent, $94.4$ stopped fraction, $12.0$ the division error) and I recomputed them.
- The concept check's distractors are real misconceptions (the tissue becomes radioactive, alpha always has more energy). The explain criteria match the question.
- The exit ticket tests the core ideas: photon energy against ionisation energy, and "irradiated is not radioactive".
- Workload: three experiments of three measurements plus a heavy theory section; acceptable, since the optional items are marked.
- Not verified from captures: figures, phone layout and the simulation in motion (no captures in the packet); I relied on the aria-labels and the deterministic tests.
