VERDICT: FAIL
CONTENT-HASH: 837c54c17f1db8f8

## Blocking
- lesson.md:160; inquiry.json:396, :109 (sim `model`), :213 (koe-3) — **B**: intensity is equated with photon number ("Valon intensiteetti kertoo, kuinka monta fotonia pinnalle osuu sekunnissa"; tarkistus-1 feedback "Teho kertoo, kuinka monta fotonia lamppu lähettää sekunnissa"). That holds only at one frequency: intensity = photon flux · hf, so at equal intensity short-wavelength light carries fewer photons (1 W at 254 nm is about 0,4·10^18 photons/s; 100 W at 650 nm is about 3·10^20). The sim's slider is a photon rate (n = 0,4·I whatever λ is), so in koe-3 ("Intensiteetti on nyt 50 %; muuta vain aallonpituutta") n stays constant while λ varies, and that is not what a real constant intensity would give. — Fix: lesson.md:160 "Samanvärisellä valolla intensiteetti kertoo, kuinka monta fotonia…"; tarkistus-1 feedback "Teho kertoo, kuinka paljon energiaa lamppu lähettää sekunnissa; punaisia fotoneja tulee paljon, mutta yksikään ei riitä…"; add one sentence to the sim `model`: "Mallin intensiteetti on fotonien määrä sekunnissa; todellisessa valossa saman tehon lyhytaaltoisessa valossa on vähemmän fotoneja."

## Polish
- lesson.md:183 — "Natriumilla λ0 ≈ 544 nm, joten … vihreä … irrottavat": 544 nm lies inside green, so yellowish green (545–570 nm) does not free electrons; write "sinivihreä, sininen ja violetti" or "osa vihreästä".
- lesson.md:126 (energia aria-label) — "alempi vaakaviiva on elektronin energia metallissa": this is the energy of the most loosely bound electron. The wording is acceptable as a simplification (C), but "heikoimmin sidotun elektronin energia" would be exact.

## Checked
- Every number in the lesson and inquiry recomputed in one script (hc/λ, E_k,max, λ0 = 543,9 nm, f0 Na 5,51·10^14 / Zn 10,42·10^14 Hz, 500/400 nm → 0,20/0,82 eV, 540 nm → 0,016 eV, siirto 652,6 nm, tarkistus-2 2,756 eV, exit 6,6·10^-19 J = 4,1 eV): all agree within rounding.
- Worked example 0,782 eV: symbolic first, the conversions and the two-decimal rounding reason are right.
- Figure "energia" to scale: 60,1 px/eV; red 1,91, green 2,28, violet 3,05 eV, bracket 0,77 eV ✓.
- Figure "kuvaaja" to scale: f0 Na 5,51, Zn 10,42 (·10^14 Hz), Na 4,34 eV at 16·10^14 Hz, parallel lines, slope triangle 4,14·10^-15 eV s, on the line ✓.
- Figure "ilmio" and hero: 254 nm (4,88 eV) > Zn 4,3 eV > 650 nm (1,91 eV); leaves fall only under UV ✓.
- Wave-model vs photon-model claims (threshold, no delay, intensity, frequency); multiphoton caveat "tavallisessa valossa" present ✓.
- sim.js: E = hc/λ, emits when E ≥ W, Ek = E − W, n = 0,4·I, panel to scale; the sim's limits (every photon frees one electron, typical W) stated in the `model` box ✓.
- koe-1/2/3 initial and locked values isolate the varied parameter; simState carries E, Ek, n ✓.
- Predictions: exactly one correct option each; distractor feedback correct; johtopäätös model answer uses model values ✓.
- Scope: within FY8 central contents (photon, quantisation); no de Broglie ✓.
