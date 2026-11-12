VERDICT: FAIL
CONTENT-HASH: 98de4a30c14d3cf8
Mode: delta
Round: 1

## Blocking
- exercises.json fy2-6-L1-10 text; solutions.md L1-10 Periaate — **B**. "Turvevoimala tuottaa … lämpöenergiaa teholla 2,0 MW" names the plant's output, but the solution sets it equal to the energy the fuel releases ("Sama energia vapautuu polttoaineen palaessa"), and that holds only at η = 100 %. The chapter *Polttoaineet ja lämpöarvo* teaches that "Vapautunut energia ei ole hyötyenergia". A real boiler at about 85–90 % burns about 800–850 kg, outside the 4 % tolerance. Fix: write in the text "Turpeen palamisessa vapautuu energiaa teholla 2,0 MW", or add "Oletetaan, että kaikki palamisessa vapautuva energia saadaan lämmöksi", and say the same in the Periaate.
- solutions.md fy2-6-L2-08 Järkevyys — **A**. "Suomessa tuulivoimaloita on satoja" is wrong (roughly 1 900 at the end of 2024). It also makes the check inconsistent: a few hundred 4 MW turbines at the chapter's roughly 30 % mean share cannot give 2,3 GW. Fix with a check that follows the chapter's model: "2,30 GW : 4 MW ≈ 580 voimalaa jatkuvasti nimellisteholla; koska keskiteho on noin kolmasosa nimellistehosta, voimaloita tarvitaan noin 1700, mikä on Suomen tuulivoimaloiden määrän suuruusluokka."

## Polish

## Checked
- Hash 98de4a30c14d3cf8 at the start and the end. I judged only the added L1-10 and L2-08.
- L1-10 recomputed: E = Pt = 2,0 MJ/s · 3600 s = 7200 MJ and m = Pt/H = 720 kg, the same as answers.py. H = 10 MJ/kg is the MAFY value (docs/mafy-arvot.tsv, VERIFIED). m is solved in symbols first, the conversion MW → MJ/s is right, and 12 kg/min is right. The hint is in `hints`.
- L2-08 recomputed: 20,2 TWh = 20 200 GWh, P = E/t = 20 200 : 8784 = 2,2996 GW, the same as answers.py (2,30). 2024 is a leap year, so 8784 h is right and is stated in the task, as the lesson asks.
- L2-08 figure: the wind bar prints 20,2 (TWh, Tilastokeskus 2024), and the description agrees. The figure gives no power, so it does not give the answer away. Three significant figures follow the read value, and the tolerance of 2 % fits.
- L2-08 solution: P = E/t is solved before substitution, and the back-substitution 2,30 · 8784 ≈ 20 200 GWh is a real check; only the turbine-count sentence is wrong.
