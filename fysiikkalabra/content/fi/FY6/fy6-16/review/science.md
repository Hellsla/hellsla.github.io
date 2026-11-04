VERDICT: FAIL
CONTENT-HASH: ad41a8dfa1fbe5f2

## Blocking
- lesson.md:309 — B: "Pääsulake kestää lyhyen ylikuorman, mutta pitkään jatkuessa se palaa" says any lasting overload blows the fuse. That holds only when the overload is large enough. A 25 A gG fuse must not blow within 1 h at 1,25 · 25 A ≈ 31 A, and it blows within 1 h only at 1,6 · 25 A = 40 A, so the figure's 29,0 A on L2/L3 would in practice never blow it. inquiry.json:93 and :168 already say "voi palaa", which is right. — Fix: "…mutta jos ylikuorma on riittävän suuri ja jatkuu pitkään, se voi palaa, ja koko talo pimenee." (Leave the design rule as it is: the summed phase current must not stay above the fuse rating.)

## Polish
- lesson.md:265 — "sulake ei tietäisi, mistä virta tulee" is not how a fuse works: it protects the cable whatever the source of the current. The real reasons are a load close to the rating for hours, the sockets and contacts heating, and other loads tripping the fuse in the middle of a charge. Say that.
- lesson.md:466 — "Hyötysuhde jää usein alle 100 %, joten verkosta otetaan enemmän": charging always has losses, so "usein" weakens the conclusion. Keep the guardrail sentence in Ydinajatus and here write "Latauksessa hyötysuhde on alle 100 %…".
- inquiry.json:71 — distractor "noin puolitoista kertaa … 400 V": 400 : 230 ≈ 1,7. "noin 1,7 kertaa" states the misconception more faithfully.
- lesson.md:265–267 — optional, C-level: SFS 6000-7-722 also requires DC fault-current protection (an RCD of type B, or type A with 6 mA DC detection). "Oma vikavirtasuoja" is a fair simplification.

## Checked
- Every number in lesson-answers.py, recomputed independently in one script: battery 64 kWh, 356 km, 10,7 h; charging times 25,6 / 12,1 / 4,03 h; worked example 11,04 kW, 3,86 h, 42,7 kWh, 6,40 €, 3,48 h, 213 km; phase currents 13,04 / 8,70 / 16 A → L1 37,7 A, L2/L3 29,0 A; 17,25 kW; 8,25 kW; 3,26 A; reel 0,567 Ω and 56,7 W; contact 10 W; siirto 0,34 Ω, 87,0 W, distractors 43,5 W and 5,44; tarkistus-2 9,06 h (8,15 and 3,02); exit ticket 11 040 W and 50 kWh. All agree.
- P = 3UI is stated with its condition (the same I in every phase conductor, U = 230 V phase to neutral). 400 V is named correctly as the line-to-line voltage.
- Efficiency: the guardrail sentence is used; losses become internal energy and leave as heat; the grid energy is W_akku : η everywhere.
- Cable heating uses 2l (out along the phase conductor, back along the neutral) in the text, formula, siirto and its hints and mistakes.
- vaiheet figure is to scale (100 px per 10 A; 13,05 / 16 / 8,7 A; the dashed line at 25 A). kayra matches the model: 11,0 kW until 4,53 h, exponential tail with τ = 0,646 h, end at 6,01 h and 1,1 kW = 99 %, tail sample checked.
- Predictions 1 and 2 and the kertaus, virhe and tarkistus-1 items each have exactly one correct option, and every distractor's feedback is right.
- Standards: SFS 6000-7-722 (each charging point has its own circuit and its own RCD), the 30 mA RCD, IP54 as an example (dust protected, splash water), Tukes. Typical values are labelled as examples (Lukuarvojen lähteet, source_note, "esimerkiksi").
- Scope: three-phase power is taught only as three single phases; Kirchhoff's current sum is used per phase conductor; breakdown strength is linked to the LOPS goal.
