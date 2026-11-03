VERDICT: FAIL
CONTENT-HASH: 938cb46bc9a4e600

## Blocking
- inquiry.json:374 (siirto, solution, Järkevyys) — **A**: "punaisen valon alku on noin 650 nm: putki havaitsee näkyvän valon lähes punaiseen asti". Red starts at about 620–630 nm, so a 653 nm limit already reaches into the red. It contradicts exercises/solutions.md L1-03 (≈620 nm "oranssin ja punaisen valon rajalla"). — Fix: "…punainen valo alkaa noin 620 nm:stä, joten putki havaitsee näkyvän valon punaisen alkupäähän asti; syvää punaista, kuten 700 nm, se ei havaitse."

## Polish
- inquiry.json:272 (koe-3, solution, Järkevyys) — "punainen ja keltainen valo eivät irrota … kuten kokeessa 1 nähtiin": koe 1 tested only red at 650 nm. Write "kuten punaisella valolla kokeessa 1 nähtiin" or leave out the reference.

## Checked
- Round-1 blocking item fixed: lesson "Samanvärisellä valolla intensiteetti kertoo, kuinka monta fotonia…"; tarkistus-1 feedback "Teho kertoo, kuinka paljon energiaa…"; the sim's `model` box says the model intensity is a photon rate and that equal power at short wavelength gives fewer photons; koe-3 intro says "mallissa fotoneja tulee yhtä monta" ✓. Round-1 polish fixed as well (544 nm colours, "heikoimmin sidotun" in the energia aria-label) ✓.
- All numbers recomputed in one script: 500 nm 3,973·10^-19 J / 2,480 eV; hc = 1240 eV nm; example 4,905 − 3,653 = 1,252·10^-19 J = 0,782 eV; λ0 Na 543,9 nm, f0 Na 5,51·10^14, Zn 10,42·10^14 Hz; koe-3 300/400/500/540/545 nm → Ek 1,85/0,82/0,20/0,016/0 eV; siirto 652,6 nm, mistakes 4,59·10^14 Hz and 1,05·10^-16; tarkistus-1 4,88/1,91 eV; tarkistus-2 2,756 eV; exit 6,6·10^-19 J = 4,1 eV, 590 nm 2,10 eV, 470 nm 2,64 eV; kertaus 7,5/4,6·10^14 Hz ✓.
- Figures "energia" and "kuvaaja" are to scale (Na 4,34 eV at 16·10^14 Hz, parallel lines, slope h); "ilmio" and hero: 254 nm > Zn > 650 nm ✓.
- sim.js: E = hc/λ, emits iff E ≥ W, Ek = E − W, n = 0,4·I, electron speed ∝ √Ek, share 0,3–1 of Ek,max; the panel is to scale; light drawn in an approximate spectral colour, with UV shown as violet and said so in howto ✓.
- koe-1/2/3: the initial and locked values isolate the varied parameter; simState carries E, Ek and n ✓.
- Predictions and checks: exactly one correct option each, and every distractor's feedback is right ✓.
- The johtopäätös and tarkistus-3 model answers use model values and the right physics ✓.
- Scope is within FY8 (photon, quantisation, E = hf) and there is no de Broglie ✓.
