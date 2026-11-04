VERDICT: FAIL
CONTENT-HASH: 683a2b867e60ff05

## Blocking
- assets/sims/fy7/fy7-16/sim.js:100, lesson.md:53, inquiry.json:237 — **A.** At z = 3 mm, R1 = 20 mm, only five lines are drawn darker. STEP = Φ/6 puts the sixth line exactly on the receiver wire, and the strict `lv < phiRx` test draws it faint. Node check: readout 6, dark 5; the figure likewise shows 5. The aria-label, sim-spec and koe-1 say six; koe-1 asks the student to count. — Fix: STEP = Φ(20,20,3) : 6,5, or a tolerant `<=`, in the sim and in the figure generator; regenerate the figure and check that 20 mm still gives one line.
- inquiry.json:99, :284, :288 — **B.** "Suurempi lähetinkäämi antoi suuremman jännitteen" holds only up to about R1 = 35 mm. At z = 20 mm the model gives 1,247 V at 35 mm and 1,229 V at 40 mm and the slider offers 35 mm. — Fix: in the feedback, the model answer and criterion 3, say the voltage grows up to about 35 mm and then falls (a best size for each distance).
- inquiry.json:428, :432 (check-1) — **B.** The feedbacks say high resistance gives much heating and low resistance little. That is true only at the same coil current; at a fixed EMF, FY6's P = U² : R predicts the opposite. The theory (lesson.md:202) states "samalla kelan virralla", but the feedbacks drop it. "Eikä pohja lämpene" also contradicts the theory's "lämpenemistä tulee vähän". — Fix: add the condition to both feedbacks, and change the absolute claim to "lämpenee vain vähän".

## Polish
- lesson.md:136 — the hob aria-label says the eddy-current symbols are violet; they are drawn copper.
- lesson.md:208 — "Desibelit lasketaan yhteen" may clash with FY5's "riippumattomien lähteiden desibelejä ei lasketa yhteen". Add one clause: losses in series multiply the power ratios.

## Checked
- All sim values (e0 against z and R1, 19,74 %, Φ0) recomputed independently; they agree.
- Field direction (× right, • left, so B is upward on the axis) and the hob's opposing eddy current are right.
- Fibre: 16,7 km halving, 1,58 % after 100 km, graph points, 4,9 µs/km; the Corning limits are right.
- The worked example (0,0502 mW) is complete and solved symbolically first. siirto 0,775 mT and its mistakes are right.
- Ravenscraft 47,3 % (+ mistakes), tarkistus-2 25,1 %, virhe 1 %, exit 20 dB.
- koe-1 and koe-2: initial values, locks and simState keys are right.
- Each prediction has exactly one correct option, and the distractor feedbacks are right.
