VERDICT: PASS
CONTENT-HASH: 12818391684b0010

## Blocking
(none)

## Polish
- inquiry.json (simulaatio, `calc`) — d is the root mean square but is called "keskimääräinen poikkeama", which an S2 student reads as the plain average of the lengths. The calc box shows the formula, but the first use does not warn. Fix: add "(neliöllinen keskiarvo)" to the readout label or the calc lead sentence.
- inquiry.json (koe-1, koe-2) — the "Näytä laskettu paras suora" checkbox is visible from the first experiment and shows the answer the student is meant to find by moving the slider. Fix: say in the intro "Älä käytä valintaruutua ennen kuin olet kirjannut mittaukset", or lock it in koe-1 and koe-2. The checkbox is only needed in koe-3.
- inquiry.json (tarkistus-2, prompt) — "Retkeläinen oli siis jo kulkenut matkaa, kun kello käynnistettiin" gives away that b is not 0, which is the trap this task tests. Fix: drop the sentence and leave the situation to the data.
- lesson.md (fi-easy, "Lineaarinen malli" paragraph) — this paragraph is dense for S2: it holds interpolation, extrapolation and curvature, about 130 words. Fix: split it at "Suoraa voi jatkaa" and gloss "interpolointi" and "ekstrapolointi" the first time ("arvio mitattujen pisteiden väliltä / niiden ulkopuolelta").
- inquiry.json (hook) — the long sentences and the shift from "kärry" to "kuvaaja" are heavy for a fi-easy opening. Fix: shorten it to three sentences.

## Checked
- The hash at the start and the end matches the packet (12818391684b0010).
- The learning path follows the slot's goals: graph, fit, slope and constant, when the line does not fit. The Miksi question is answered by the experiments and the model answer.
- Ennuste 1 and 2 can be refuted by d in koe-1 and koe-2. The distractors are misconceptions (polyline, line through one point, b = 0, the first point), and the feedback gives numbers that repair them.
- Koe 3 makes the pattern in the residuals visible, and its choice question separates "small d" from "random residuals". It is a good model-fit check.
- The simulation at 390 px has a legible graph, a readout and closed boxes behind the named buttons. The kettle figure is legible, with the read-off points marked and the dashed line at 40 °C.
- The worked example has seven stages, one step each. The data match the line (largest deviation 0,8 °C). The reasonableness check uses the table.
- Etsi virhe uses the real consecutive slopes. The cyclist task's figure description gives the grid readings (data) but not the slope. Both numeric tasks have mistake feedback for the typical slips (b ignored, k and b swapped).
- Core path: tarkistus-3, siirto, kertaus and pohdi are optional. The workload fits one lesson.
- The exit ticket tests the equation from two points and the physical meaning of b.
- The exercise set is not judged here.
