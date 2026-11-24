VERDICT: PASS
CONTENT-HASH: db20b0cd98688b14

## Blocking
(none)

## Polish
1. inquiry.json, activity `simulaatio`, `calc` — the text contains a literal `\\n\\n` (JSON `\\n`) before `$$e = ...$$`, so Laskennan selitys probably shows "\n\n" as characters. No other lesson does this. Fix: use a real paragraph break or `\n\n`, and check the box on the page.
2. inquiry.json `koe-1` — Ennuste 1 (which position gives the largest voltage) can only be refuted by the student pausing the graph at the peak and noting the angle and flux. The table records only e0 and T, so nothing forces that step. Fix: make the pause an explicit step and have the `explain` criterion ask for it, as it already does. Consider a recorded measure such as Φ at the peak.
3. lesson.md "Mistä huippuarvo tulee" — "Vuo muuttuu pyöriessä epätasaisesti, joten $e$ on hetkellinen jännite" is confusing (non-sequitur). Better: "Vuon muutosnopeus vaihtelee pyöriessä, joten jännite $e$ vaihtelee ajan mukana. Siksi puhutaan hetkellisestä arvosta."
4. lesson.md derivation — the angle θ is first the angle between the velocity and the field, but the flux is later written with cos(2πft). One sentence linking θ = 2πft to the figure's coil position would help a student following the derivation alone. The step from "flux is cosine" to "its slope is sine" is stated, not shown. That is acceptable at this level, but the graph in the `phi-e` figure carries it.
5. hook — "Kaikki verkon voimalaitokset tuottavat jännitettä samalla taajuudella" is stated as fact. The wind turbine reaches 50 Hz only through the frequency converter (explained later). Soften: "Verkossa jännitteen taajuus on kaikkialla $50\,\text{Hz}$."

## Checked
- Learning path: hook → frequency retrieval → two predictions → sim → derivation → formula → effective values → staged example. The opening question is answered in "Miksi jännite on sinimuotoinen". Goals (generator, AC origin, sinusoidal reason, wind power) are all covered; nothing is added beyond them.
- Predictions: each has a wrong option that is a real misconception (flux maximum = voltage maximum; constant; quadrupling). Feedback is gated and names the model evidence.
- koe-1 varies only f, locks N and B, and measures e0 and T. The conclusion `explain` has observable criteria and ties the data to e0 = NBA·2πf. The sim computes e from dΦ/dt (not the formula), so the result emerges from the model.
- Sim captures at 390 and 1280 px: the picture and graphs are legible and the controls usable. The readout is short, the text sits behind Käyttöohje, Mallin oletukset and Laskennan selitys, and colour is explained.
- Worked example: seven stages, one step each, symbolic first, unit conversion and reasonableness check. It differs from the transfer task (a stationary coil with a rotating magnet, rpm conversion).
- The transfer task has three hints and four real mistake feedbacks (e0 vs U, rpm as Hz, √2 the wrong way, missing 2π).
- Error-spotting and the checks test concepts (mean vs effective vs peak). The exit ticket tests the 230 V → 325 V and stator-vs-rotor core ideas.
- Finnish and glossary terms are correct (generaattori, vaihtojännite, tehollinen arvo, huippuarvo). Units are in LaTeX and cases are right. Reading level is suitable for fi-easy.
- The exercise set was not judged (reviewed apart). The deterministic checks were not run (packet says so).
