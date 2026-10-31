VERDICT: PASS
CONTENT-HASH: 171ddef650c8a971

## Blocking
None.

## Polish
- teacher.md has no model answer for the echo extension. Add: with the source next to the microphone, the time between the direct sound and the echo covers the path $2L$, so $v = 2L/\Delta t$. The student page rightly leaves this open.

## Checked
- Card (ex-14, item 22) is covered, with no invented equipment or safety values.
- Two microphones: the source is behind microphone 1 on the same line and the signals share one time axis. The travel time over $d$ is therefore $t_2 - t_1$, and the moment the sound was made is not needed. For an off-axis source, $|r_2 - r_1| < d$, so $v$ comes out too large, as teacher.md says.
- Graph of $d$ against the mean $t_2 - t_1$: the slope is $v$. A constant error in $d$, or a constant delay in one signal, only moves the intercept. The single quotients are affected most at short distances. The model figure has no data points and its dashed line is parallel to the model line.
- Uncertainty: relative uncertainties add in a quotient, $\Delta(t_2-t_1) = \Delta t_1 + \Delta t_2$, and the slope uncertainty is $(v_\text{max}-v_\text{min})/2$ or the fit's standard error.
- $v = v_0\sqrt{T/T_0}$ with $v_0 \approx 331\ \text{m/s}$ at $273{,}15\ \text{K}$ in dry air, T in kelvins, and humidity raising $v$ slightly: correct. Independence from loudness and pitch, and the wind and temperature conditions: correct.
- Sampling is posed as a comparison between the sample interval and the predicted travel time, with no invented rates. The note on unsynchronised phones is correct.
- Figures: the signal sketch is labelled as not data, and all labels are LaTeX. Hearing safety is qualitative, with no sound levels.
- Revision to 171ddef650c8a971: the new hero shows the boards struck in a corridor, with a wave front centred on the clap, a tape measure, no thermometer reading and no detector. The setup arcs are now clear of $d$. The echo-overlap sentence and teacher.md's late-onset item are correct: the weaker pulse is read late, so $v$ comes out slightly too small. The neutral equipment list and the prerequisite reasons make no physics errors.
