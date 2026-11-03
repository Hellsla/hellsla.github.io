VERDICT: FAIL
CONTENT-HASH: ad2b40581b17ae1a

## Blocking
- inquiry.json:siirto (`siirto`) — the "new situation" uses exactly the numbers of the fluorescence figure (365 nm to 520 nm, 3,40 eV and 2,38 eV, with the "lämpöä" arrows); the student only subtracts two labels they can read off the theory figure, and hint 3 repeats them. It is not a transfer and the answer is on the page before the student acts — fix: change the task to other wavelengths (e.g. 405 nm to 530 nm, an unlabelled energy), or ask for the share of energy lost as heat for a different dye.
- inquiry.json:ennuste-1 prompt — "Ylemmät tasot ovat yhä lähempänä toisiaan" gives away the reason for the right answer ("välit pienenevät") before the student commits; only the "tasaisin välein" distractor is then a real choice — fix: drop that sentence and let koe-1 and the explain item show the convergence; the feedback can name it afterwards.

## Polish
- Predictions come before the theory, but "energiataso" and "perustila" are first met only in the sim's howto and are never defined there (Pohdinta/Ennusta never says an atom has allowed energies); add one sentence to the sim `model` or the ennuste prompts: "Atomin elektroniverhon energia voi olla vain tietyillä arvoilla, joita sanotaan energiatiloiksi."
- The opening question (why the Sun's H line at 656 nm is dark although cold H absorbs only UV) is answered only in the optional `pohdi`; the core text says merely "kaasukehän atomit absorboivat omat aallonpituutensa". Add one sentence in Ydinajatus that the solar atmosphere is hot enough for some atoms to be at n = 2.
- `tunnista`: the distractor feedback relies on the difference 405/410 nm and 436/434 nm, which cannot be read from the 331 px phone capture (about 1 px per nm), and the 577/579 pair appears as one line. The task still works through the missing 656 nm and the green 546 nm; say so first in the feedback. Finnish: "lähellä $589\,\text{nm}$:ä" → "$589\,\text{nm}$:n lähellä".
- koe-1/koe-2 mostly compute E_n = -13,6/n^2 and λ = hc/ΔE, so what emerges is arithmetic; it is acceptable because the tables feed a real conflict (ennuste-2 against the hook's "same places"), but the conclusion model answer could name that the spacing law of the levels is data given, not found.
- Exit ticket question 2 repeats tarkistus-1/the summary; the first question is the better core test.

## Checked
- Path: Pohdinta, retrieval, two refutable predictions, sim and experiments, theory, staged example, error item, transfer, checks, exit ticket; one lesson's workload.
- Ennuste-2 sets up a real conflict with the hook; each wrong option's feedback repairs its misconception.
- Example staged one step per stage; units and significant figures shown.
- Etsi virhe: genuine unit error, feedback names it.
- Figures 390 px (levels, fluorescence, spectra) legible, colour with labels; sim at 390 and 1280 px readable, UV/IR greyed.
- Check 1 distractors misconception-based; explain criteria observable.
- Fluorescence explained through energy conservation, matches glossary.
