VERDICT: FAIL
CONTENT-HASH: d6e581ceff728ce3

## Blocking
- lesson.md:108 and inquiry.json `hook` (text) — "lasin pohjalle voi jäädä jäätä" / "lasin pohjalla voi silti kellua jäätä": ice floats, it does not stay on the bottom, and "kellua pohjalla" contradicts itself. A student who knows this stops trusting the opening. Fix: "Entä miksi lasissa voi kellua jäätä vielä pitkään, vaikka juoma oli huoneenlämpöistä?" and in the hook "Kun lämpö on tasoittunut, lasissa voi silti kellua jäätä."

## Polish
- sim (readout and bars at the initial state, captures #2, #27) — before pressing *Sekoita* the sim already shows "Lopputila: T = 0,0 °C, jäätä jäljellä 24,7 g" and the bars for exactly the scenario of prediction 1, so a student can read the answer without committing and the *Sekoita* step adds nothing. Fix: show the final-state line only after mixing, or start koe-1 from a state that is not the prediction's.
- inquiry.json `ennuste-1` correct-option feedback gives "26,6 °C", which is also the answer of koe-1's numeric question; the reveal needs only 3 rows, so a student can read it before the slider search. Fix: leave the number out of the feedback (it stays in the Johtopäätös model answer).
- Figures 2 and 3 use different scenarios side by side: the before/after figure has ice at 0 °C and 25 g left, the energy-balance figure ice at −10 °C and 35,5 kJ. A reader compares the two and sees numbers that do not match. Fix: name the change in the caption or draw the 0 °C case.
- lesson.md "Esimerkki" stage 3 opens with the combined formula for T and never writes the basic balance $Q_\text{luovutettu} = Q_\text{vastaanotettu}$ before it (house rule "start from the basic principle"); the last stage is near 130 words. Split the sanity check and the energy-balance check.
- Finnish: koe-1 solution "Raja-tapauksessa" → "Rajatapauksessa"; koe-2 solution "kun $0{,}10\,\text{kg}$ jäätä sulattaminen vaatii" → "kun $0{,}10\,\text{kg}$ jään sulattaminen vaatii"; tarkistus-2 solution "(yhtäsuuruudessa $T = 0\,{}^\circ\text{C}$)" is unclear: delete it. The koe-1 prompt "jolla jäätä ei ole … mutta T ei ylitä 0 °C:ta" has no slider value that fits (27,0 gives 0,3 °C): "Rajaa väli, jonka sisällä jää loppuu".

## Checked
- Learning path follows fy3-6 and fy3-7; slot goals met. Freezing cases 3-4 go a little beyond "sulaako kaikki jää" but are tied to the formula and an optional check.
- Prediction 1 can be refuted (15 °C against 0 °C with ice left); wrong options' feedback repairs the misconception; koe-1 locks and varies one quantity.
- Core path is one lesson; retrieval, ennuste-2, koe-2, Etsi virhe, siirto and the explain check are optional.
- Example has the seven stages; the numbers I recomputed are correct (6,05 °C, 18,8 kJ balance).
- Etsi virhe and the mistake feedbacks name the real misconceptions; the exit ticket tests the core idea (numbers verified).
- Figures 2 to 4 legible at 390 px; colour plus labels; the graph matches the text (26,6 °C).
- Wide layout at 1280 px: the sim beside the experiment, one reading column.
- Not done: playing the sim by hand (captures only). At 390 px the *Veden massa* label sits tight under the chart (a visual matter).
