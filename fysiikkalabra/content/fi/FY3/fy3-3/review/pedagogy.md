VERDICT: PASS
CONTENT-HASH: eced6a5c7d9e54b5

## Blocking
(none)

## Polish
- lesson.md:130 (micro-model caption) — "nuolen pituus kuvaa hiukkasen nopeutta", but in the animated figure the arrow groups have opacity 0 from 3 % to 97 % of the cycle; the capture shows only dots, so a student sees no arrows. Fix: say that speed shows as how fast the dots move, and that arrows appear in the still or print version, or keep the arrows visible during the animation.
- inquiry.json exp-1/exp-2/simulaatio — the measure column "p mitattu" and "mitattu paine kaksinkertaistui" in the johtopaatos model answer call model values "measured". The model text explains the counting, but the rule is "model values". Fix: "p laskettu törmäyksistä" or "p (malli)" and "laskettu paine".
- inquiry.json virhe — the correct option is the only one that contains a full calculation and is the longest, so length gives it away. Fix: shorten it to "Suhde pitää laskea kelvineinä, ei celsiusasteina." and keep the numbers in the feedback.
- inquiry.json pred-1 — the options are numerically explicit (12x, 2x, 1,4x), but the prompt gives 27 °C and 327 °C without hinting at the kelvin conversion, which is right for a prediction. Consider adding pr-pumppu's conversion retrieval ("kelvin") to the core path; today only a student who opens the optional retrieval meets Celsius differences, and the lesson's key step (K) first appears in the feedback. Acceptable as is.
- lesson.md:223 — "kuvaa raja-arvoa" is vague. Fix: "ja kuvaa vain raja-arvoa, jota kaasu lähestyy".

## Checked
- Path from the hook (tyre) through prediction, the key experiment (exp-1), explain, theory and example to the check; the opening question is answered by the mikromalli and the exit ticket, and the answer is not shown before commitment (feedback is gated, the hook gives no answer).
- Slot goals (system, state variables, temperature, micro-model, kelvin, absolute zero) are all covered. The scope is held: no ideal gas law or Boyle's law, and pressure stays qualitative.
- Core path is one lesson's work: pred-1, exp-1, explain, 3 checks. The optional items (pred-2, exp-2, reflect, siirto, check-3) are marked optional.
- exp-1 can refute the predictions: pressure arises from counted hits, so it is noisy and not a formula readout. Volume is locked and T varies; the model says that speed ∝ √T is an assumption.
- The pred-3 models (Aino, Bea, Cem) each have feedback that repairs the misconception; the correct speaker is Bea, one of three, no pattern.
- The worked example has seven stages, one step each; the figure (extrapolation at 390 px) is legible, with the axis shifted and explained. Solving symbolically comes first; the independent check is in the example.
- The micro-model, scene and extrapolation figures are recognisable and uncluttered; colour is paired with a label (cold/hot, p1/p2).
- Check-2 (extrapolation) and the siirto solutions have all seven parts; the mistakes (404, 83,8, 0, −123) are real.
- Finnish: glossary terms right (systeemi, tilanmuuttuja, absoluuttinen nollapiste), case after number+unit right, "ei kelvinastetta" noted.
- Sim at 390 px: controls and readout understandable; text is behind Mallin oletukset and Laskennan selitys. Not checked: the exercise set (reviewed apart) and the 1280 px captures beyond the figures above.
