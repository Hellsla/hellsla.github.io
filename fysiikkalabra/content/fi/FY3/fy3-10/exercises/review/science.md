VERDICT: PASS
CONTENT-HASH: 67c156379d17e0ac
Round: 1

## Blocking
(none)

## Polish
- exercises.json:297 (L2-08 text) — $V = 2{,}0\,\textsf{l}$ has two significant figures, so a careful student may call row 3's "$T \approx 301\,\text{K}$" (three) a fault, which weakens "exactly one wrong row". Give $V = 2{,}00\,\textsf{l}$ (row 1 then $0{,}00200\,\text{m}^3$).
- exercises.json:321 and :326 (feedback D, "ei virhettä") — "koska pullossa on huoneenlämpöistä ilmaa" / "ei sovi suljettuun pulloon": the task never says the air is at room temperature. Either state it in the task or phrase the check as "574 °C olisi uunin lämpötila, ei tavallisen pullon".
- The task does not exercise the lesson's other warned mistakes (mixed kPa/m³ units, heavy gas); row 1 touches units only as a correct line. Optional.

## Checked
- New task L2-08 (virheen löytäminen), recomputed: pV = 200 J, nR = 0,6648 J/K, T = 300,8 K ≈ 301 K; θ = 27,7 °C ≈ 28 °C (273,15 or 273 gives 28); the wrong row gives 573,8 ≈ 574 °C.
- Rows 1–3 really correct (100 kPa = 10⁵ Pa, 2,0 l = 0,0020 m³, T = pV/(nR)); row 4 is the only error; "Laskussa ei ole virhettä" last, as docs/exercise-types.md asks.
- Each feedback's physics right; "200 J" for the numerator is the right unit (Pa·m³ = J), and the reason that T is already in kelvins (R's unit) is right.
- Row 4 is the lesson's warned Celsius/Kelvin confusion; option texts of similar length and form.
- Notation as in the brief ($pV = nRT$, $R = 8{,}31$, $\theta$, rigid closed bottle = fixed n and V).
- Renders: L2 screenshot 12 at 1280 px (options, solution). Phone width judged from text: the longest inline chain (row 3) is a displayed fraction plus "≈ 301 K", about 260 px.
- answers.py and other tasks unchanged since the previous PASS; hash identical at start and end.
