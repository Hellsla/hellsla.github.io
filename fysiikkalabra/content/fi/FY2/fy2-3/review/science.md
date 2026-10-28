VERDICT: FAIL
CONTENT-HASH: 862bd2552b27cf19

## Blocking
- exit-ticket.json:12 — the model answer jumps from $5{,}0\,\text{W}$ to $0{,}0050\,\text{kW}$ without showing the conversion. This breaks the teacher's rule that unit conversions are done by substitution, and the same answer already does the min → h step that way. — Add "Sijoitetaan $1\,\text{W} = 10^{-3}\,\text{kW}$: $5{,}0\,\text{W} = 5{,}0 \cdot 10^{-3}\,\text{kW} = 0{,}0050\,\text{kW}$", as the worked example does.

## Polish
- inquiry.json:271, 275 and 278 (tarkistus-2) — the mistake feedback and the reasonableness check use $90\,\text{min} = 1{,}5\,\text{h}$ without a substitution. — Write $90\,\text{min} = 90 \cdot (1\,\text{h} : 60) = 1{,}5\,\text{h}$ once.
- inquiry.json:217 (siirto) — the mistake feedback gives $2{,}5\,\text{W} = 0{,}0025\,\text{kW}$ with no substitution step, and "tulos 21 900 olisi wattitunteja" has a bare number. — Write $2{,}5 \cdot 10^{-3}\,\text{kW}$ and $21\,900\,\text{Wh}$.
- inquiry.json:224 (siirto solution, reasonableness check) — "$60\,\text{Wh} = 0{,}06\,\text{kWh}$" converts without a substitution step. — Write $60 \cdot 10^{-3}\,\text{kWh}$.
- lesson.md:41 — the text reads $40\,\text{kJ}$ off the graph and then writes $40\,000\,\text{J}$ with no step between. — Write $40\,\text{kJ} = 40 \cdot 1000\,\text{J}$, or compute in kJ.

## Checked
- I recomputed every lesson, inquiry and exit-ticket number in one script, alongside lesson-answers.py: 0,54 MJ; 15 h; 120/60/4,8 kJ; 1000 W; 9,6 kWh → 1,92 €; 21,9 kWh; 800 W; 13,3; 0,15 and 0,24 kWh; 800 000 kettles; 43,8 and 36,5 kWh. All match, and the round-2 mistake value 13,3 is fixed.
- Every correct option is right, and so are the numbers in every distractor's feedback (1 h is 1/15 of the energy, 150 h is ten times too long, 5 h gives 1/3).
- Both figures are to scale: the graph slopes are 2000, 1000 and 80 W, the marked ΔE is 40 kJ over Δt = 20 s, and the bars are 400 : 200 : 16 px.
- The worked example has all seven stages, is solved symbolically first, converts W → kW and snt → € by substitution, and uses 2 significant figures.
- Olkiluoto 3 at about 1600 MW and the Tilastokeskus 2025 price of about 18 snt/kWh are as verified in earlier rounds. 20 snt/kWh is labelled as an example price.
- All round-2 blockers are fixed: the kWh/s claim, the 80 W in the aria-label, the 192 snt conversion, the exit ticket's min → h substitution and the plain-prose numbers.
- Scope is FY2: P = ΔE/Δt, kWh and price only, with no work, force or efficiency chain. There is no ×, and inline divisions use a colon.
