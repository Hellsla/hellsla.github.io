VERDICT: PASS
CONTENT-HASH: 3a0bf763fcdbcffc

## Blocking
None.

## Polish
None. Both points from the previous review (hash 286f657b6056c4fd) are fixed:
- **Vessel heating.** "Kuvaajan alku ja loppu" now says that the vessel's lag only shifts the line. It also says the vessel keeps warming with the water for the whole run, so its heat lowers the slope and therefore $\eta$, and that it counts as a loss. This is correct and matches Teoriaa lyhyesti and teacher.md.
- **Mittaa.** Both $T$ and $T_0$ now affect the uncertainty of $\Delta T$ only for a single-reading $\eta$. An error in $T_0$ shifts every point equally and leaves the slope unchanged. Both statements are correct and no longer seem to contradict.

## New text
- **Käsittele question 4** asks students to compute $\eta = Q/E$ from the last point and compare it with the slope. The tuki check says the single-point value includes the start-up lag, the error of one reading and, at the last point, the larger end losses. All three are correct. The lag puts the line's $Q$-intercept below the origin, so $Q/E$ at any point is below the slope. End losses lower the last $Q$ further. A student should therefore normally find the last-point value lower than the slope, and the explanation covers this. The slope gives the energy share in the linear part, and the graph shows whether that share stays constant. This is consistent with the research question and with the teacher.md misconception about single-point $\eta$.

- **Reorder at hash 3a0bf763fcdbcffc:** Q4 now follows Q3. The lag/vessel text and the single-point text are now one tuki block after Q4. The text is unchanged, and the physics is unaffected.

## Checked (unchanged since the previous review)
- **Models:** Model 1: $Q = \eta E$ is a line through the origin with slope $\eta$ and no unit. Model 2: $a = \eta UI/(cm)$, so $\eta = cma/(UI)$, with the condition that $U$ and $I$ stay constant.
- **Start-up lag:** at constant power it shifts the line but not the slope. Correct.
- **Uncertainty:** $\Delta a/a + \Delta m/m + \Delta U/U + \Delta I/I$ is a valid worst-case estimate in both models, because systematic scale errors are invisible to the fit. An error in $T_0$ does not change the slope.
- **Safety:** the card's blank current limit stays the teacher's limit. No voltage or current value is invented.
- **Figures:** they match figures.py. The model graphs have no ticks or points, and there are no fabricated data or readings. The circuit diagram shows the ammeter in series and the voltmeter across the heater.
- **Consistency:** the predictions, theory, tuki blocks, questions, teacher.md and goals agree.
