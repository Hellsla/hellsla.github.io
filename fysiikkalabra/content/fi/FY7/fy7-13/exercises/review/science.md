VERDICT: FAIL
CONTENT-HASH: 758b4377e0856694

## Blocking
- exercises.json:213, 218, 223, 224, 227, 235, 236; solutions.md:168–170 (fy7-13-L2-07): **A, a definition error (guardrail "Keep the terms apart").** The task calls the reading uncertainty an error: "Lukemisvirhe on aina noin $\Delta x = 2\,\text{mm}$", and it says "suhteellinen virhe" for $\Delta x : x$. An error is the unknown, signed difference from the true value. A difference that is "always 2 mm" would be a systematic error, and measuring a farther maximum does not remove a systematic error in the same sense. The brief's lesson calls the same quantity "epävarmuus $\Delta x = 0{,}2\,\text{cm}$", so the exercise also contradicts the theory. Fix: write "Lukeman epävarmuus on aina noin $\Delta x = 2\,\text{mm}$" and "suhteellinen epävarmuus" in the text, the answer, all four options and their feedback, and the solution. The physics of the options stays as it is.

## Polish
- solutions.md:78 (L2-03): "ero johtuu mittausepävarmuudesta" should say *mittausvirheestä*, or "mahtuu mittausepävarmuuden rajoihin".
- exercises.json:300 (L2-10, figure spectrum-q): at 250 lines/mm the second-order spectrum starts at about $20\,\text{cm}$ ($\sin\theta = 0{,}200$), which is inside the drawn screen. The to-scale figure shows the first order only. A short note in the task ("kuvassa on vain ensimmäinen kertaluku") would stop anyone thinking higher orders are missing. This is a teacher-approved figure, so this is not blocking.
- solutions.md:212 (L3-05): "$x = \dfrac{2x}{2}$" reads like an identity. Write it as "maksimin etäisyys reiästä on puolet välimatkasta $2x$".
- solutions.md:154 (L2-05): three significant figures can be defended because most $x_k$ have three, but $x_1 = 6{,}3\,\text{cm}$ has two. Say "kuten useimmat $x_k$ ja $L$".

## Checked
- I recomputed all 21 numeric answers in one script with my own formulas. Each one agrees with exercises.json and answers.py within 0.2 %.
- L2-05 (the red-laser fix): the per-point values are 625–638 nm, the slope through the origin is $0{,}06337$ and $\lambda = 634\,\text{nm}$. That is plausible for a red laser, and the line through the origin has its physical reason stated ($k = 0$ at $\theta = 0$).
- L3-04 (the 2-sig-fig fix): the table matches $\cos^2(\pi x / 5{,}0\,\text{mm})$ to within $0{,}015$. The minima at $2{,}5$ and $7{,}5\,\text{mm}$ and the peak at $10{,}0\,\text{mm}$ check out. $6{,}3 \cdot 10^2\,\text{nm}$ lies inside the 2 % tolerance.
- L3-05 (the separator fix): $d$ per row is 0.7389, 0.7375, 0.7368 and 0.7363 µm, with mean 0.7374 µm. The second-order sine is 1.44, the deviation is −0.36 %, and the zeroth order goes back through the hole. The "(L; 2x)" separator is now clear.
- L2-08: $x$ goes from $13{,}03$ to $19{,}88\,\text{cm}$ (factor 1.53). Exactly one option is correct, and every distractor's feedback is right.
- L1-06 and L2-07: exactly one correct option each, and the feedback physics is right.
- L3-01 order overlap, L3-02 CD pitch of $1{,}6\,\mu\text{m}$ with two orders per side, and L3-03 calibration: all correct.
- setup-q is to scale at 2.2 px/cm: $x_2 = 69{,}98\,\text{cm}$, $L = 1{,}20\,\text{m}$, and $k = 3$ falls off the screen. spectrum-q: the red edge is at $17{,}8\,\text{cm}$ and violet at $10{,}1\,\text{cm}$. The descriptions match the figures and do not give the answer away.
- L1-09: He 587.56 nm gives 20.64°.
- The symbols, $\tan\theta = x : L$, and the hilayhtälö's condition (perpendicular incidence) match the brief in every solution, and each unknown is solved symbolically first.
