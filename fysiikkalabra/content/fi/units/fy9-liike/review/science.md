VERDICT: PASS
CONTENT-HASH: 67b2709b5b162498
SCOPE: full review of unit fy9-liike (unit.md, inquiry.json, teacher.md, Sovella s1-s8, answers.py); the new ```pysahdy boxes judged first.

## Blocking
- (none)

## Polish
- The kartta figure (pre-existing) says "matka nopeuskuvaajasta → kuvaajan alla pinta-ala", but the text and the new third pysahdy box say the signed area is the *siirtymä*, with the part below the axis counted negative. Distance is the area with every part counted positive. A student who has just read the box may read the figure as a contradiction. "siirtymä" in the figure (or "matka: alat positiivisina") would match.
- Pysahdy 3: "pienentää siirtymää" is right. Adding "mutta kasvattaa matkaa" would tie the box to the Ydinajatus distinction between displacement and distance. Optional.
- s4 c model answer: "noin $65$–$100\,\text{km/h}$". With $4{,}5 \pm 1\,\text{s}$ the range is $65$–$103\,\text{km/h}$, so "noin $65$–$105$" would be the honest figure. The conclusion is unchanged.
- s8 d (carried from the last report): $14{,}7\,\text{m}$ from two-figure data. Round it to $15\,\text{m}$.

## Checked
- Pysahdy boxes. 1: the slope of the $(t,x)$ graph is velocity and the area under $(t,v)$ is displacement, right and as in the paragraph above it. 2: $v>0$, $a<0$, so the speed decreases. Right, and it matches the formula text, Yleisiä virheitä and lt-4. 3: the area below the axis counts negative and reduces the displacement, right and as in the paragraph above it. Each box has exactly one correct answer, and none goes beyond FY1/FY4.
- The inquiry model change in tarkistus-3 only adds paragraph breaks. Its physics is right: the car starts from rest and the moped passes at $t=0$, so the speeds are equal at $4\,\text{s}$ and the car catches up at $8\,\text{s}$ with twice the moped's speed.
- One script recomputed every number from the task data with my own formulas and printed it beside answers.py. All agree:
  - inquiry: tram $450\,\text{m}$; scooter $22{,}5\,\text{m}$; elk $46{,}8\,\text{m}$; dog $8{,}0\,\text{s}$ (the distractor $5{,}12\,\text{s}$ also checks); ball $-1{,}81\,\text{m/s}$; lift $16{,}0\,\text{m}$; cyclist $30\,\text{km/h}$.
  - s1: $12{,}0\,\text{s}$, $1{,}25\,\text{m/s}^2$, $17{,}5\,\text{m}$; d: $15{,}4\,\text{s}$, $307\,\text{m}$, $77\,\text{m}$.
  - s2: $8{,}84\,\text{m}$; $0{,}625\,\text{s}$ and $7{,}08\,\text{m}$; Moon $8{,}68\,\text{m}$; $5{,}87$ and $-6{,}13\,\text{m/s}$.
  - s3: my own regression gives $-0{,}642\,\text{m/s}^2$, a start at $9{,}84\,\text{s}$ and a stop at $48{,}8\,\text{s}$, so $486\,\text{m}$ against the read-off $481\,\text{m}$. Both are inside the tolerance and the accepted range.
  - s4: $81{,}8\,\text{km/h}$, $0{,}59$ and $17{,}8\,\text{km/h}$.
  - s5: $0{,}9375\,\text{m/s}^2$, range $0{,}741$–$1{,}224\,\text{m/s}^2$.
  - s6: $8{,}88\,\text{m/s}^2$, $\pm 0{,}10$, $9{,}3$ times the uncertainty; corrected $9{,}77\,\text{m/s}^2$; two-point $8{,}92\,\text{m/s}^2$.
  - s7 and s8 as before.
- Every multiple-choice item has exactly one correct option, and the distractor feedback is right: lt-1 to lt-6, keskinopeus, rata, tangentti, edellä and tarkistus-1.
- Rubric criteria ask only what their part asks, and the points add up. Hyväksytään myös covers the alternative methods.
- Physics is right throughout. The models are stated: constant acceleration, air resistance neglected, extrapolation flagged in s3 d. The s6 scale correction goes the right way. Scope is FY1/FY4 kinematics.
- The hero is now a raster image with no quantities, so there is nothing to check for physics.
- `practice.py check` OK. Hash $67b2709b5b162498$ at start and end.
