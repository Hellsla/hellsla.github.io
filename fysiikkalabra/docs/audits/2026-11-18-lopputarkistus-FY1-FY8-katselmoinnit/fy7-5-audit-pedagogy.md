VERDICT: PASS
CONTENT-HASH: b7de1d98afc92688

## Blocking
(none; no Critical or Major finding)

## Polish
1. lesson.md "## Kaava: Induktiolaki", paragraph after the formula ("missä $e_\text{ka}$ on keskimääräinen … myös silloin, kun vuo pienenee") — about 170 words with five ideas (symbols, constant rate, instantaneous value, units, sign and magnitude); the 120-word rule — split into "symbolit ja tasainen muutos", "hetkellinen arvo" and "etumerkki ja suuruus". Minor.
2. inquiry.json `siirto` — the "new situation" (shake flashlight, 600 turns, ΔΦ and Δt given) is the worked example's plug-in with new numbers, so it demands no transfer — give the flux as a graph or the field and the area, or ask for the time needed for a target voltage. Minor.
3. inquiry.json `tarkistus-3` (`optional: true`) and `learn` goal 3 — the derivation of $e = vBl$ has no prediction or experiment, and its only explain task is optional, so the third goal rests on theory text plus one calculation — make it non-optional or add a prediction. Minor.
4. inquiry.json `simulaatio` howto ("*Nopeus*-valikko muuttaa vain animaation tahtia, ei käämin vauhtia") — two different "speeds" on one screen; students will mix them — name the menu *Animaation tahti* in lang/fi.json (the teacher's permission is needed for interface text). Minor.
5. inquiry.json `virhe`, second distractor ("kierrosten lukumäärällä ei pidä kertoa: $0{,}36\,\text{V}$") — $0{,}36\,\text{V}$ is the wrong area without $N$, an unlikely path; a student's real error is rarer than the others. Also the left sign of $e$ at entry is asserted only, with the explanation deferred to the Lenz chapter — one sentence on the page would keep students from doubting the sign. Minor.

## Checked
- Path: Faraday's observation → flux → law → moving rod; a student with fy7-3 and the magnetic-force chapter follows; the opening dynamo question is answered in "Muutos synnyttää jännitteen".
- Both predictions are argued before the evidence (reveal after koe-1, min 2); the experiments can refute them (`e_sisalla`, v varied, B and N locked); wrong-option feedback names the misconception.
- Koe 1 and Koe 2 control variables properly; e·Δt = NΔΦ emerges from the model values and is consistent (1 mV·s = 1 mWb).
- Worked example: seven staged steps, units conversion shown, reasonableness check; it does not repeat the transfer task's numbers.
- Check 1 distractors are real misconceptions (strong field, steady motion); explain criteria are observable.
- Exit ticket: flux calculation plus "maximum flux, zero voltage" tests the core idea.
- Figures not opened (the packet lists no captures); judged from descriptions: they give a non-seeing reader the data.
- Finnish: glossary terms right, case after number and unit right; "indusoituu" in the photo caption differs from "syntyy" — minor.
- The exercise set was not in the packet and is not scored here.

## Scores
- 2 Conceptual clarity: 5 — the mechanism (magnetic force on electrons) is derived; the misconception is met head-on in its own paragraph; figures beside the points.
- 3 Pedagogical effectiveness: 4 — strong predict–test–explain; the transfer task and the optional rod explanation are the weaker links.
- 4 Exercise quality and variety: 4 — judged on the inline tasks only (the exercise set is not in the packet); the error-spotting, the numeric transfer and the checks have misconception-based feedback and complete solutions; the transfer is plug-in.
- 5 YO readiness: 4 — explain tasks with observable criteria; independent application is thin on the core path (see polish 2, 3).
- 6 Experimental reasoning: 4 — controlled variables, labelled model values, a product e·Δt to interpret; no uncertainty or noisy data (the sim is deterministic).
