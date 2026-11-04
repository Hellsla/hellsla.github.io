VERDICT: FAIL
CONTENT-HASH: 82dfe66a8cba123a

## Blocking
- solutions.md:174 (L3-04 Vastaus, c) — A: "Koko aktiivisuus pienenee tuhannesosaan vasta noin 240 000 vuodessa" has no basis. The 240 000 a (L3-03) is the time for Pu-239's *own* activity to fall to 1/1000, not the total activity of the fuel. — Write "Plutonium-239:n oma aktiivisuus pienenee tuhannesosaan vasta noin 240 000 vuodessa (tehtävä L3-03)".
- exercises.json:294 (L3-04 text) — B: the data start at removal from the reactor, with one 30 a half-life "koko ajan". Short-lived nuclides (Cs-134, Ce-144, Ru-106, Pu-241) dominate the first years, so a single Cs-137/Sr-90 exponential holds only from about 10 a after discharge. In b), "250 a before interim storage" is also a false picture. — Add "Aika t lasketaan noin 10 vuotta poiston jälkeen, kun lyhytikäiset fissiotuotteet ovat jo hajonneet", and phrase b) as "kunnes fissiotuotteiden aktiivisuus on 10 TBq/t" with no storage condition. The numbers and the answer are unchanged.
- solutions.md:184 (L3-05 Vastaus) — A: "kolme merkitsevää numeroa kuten hyötysuhteessa 0,33": 0,33 has two significant figures, and so does 92 %. — Give 540 kg (two significant figures, limited by η and 92 %). In a), give 1500 MW and 1000 MW (or say why three are kept). The stored 543 can stay within tolerance, or be changed to 540.

## Polish
- solutions.md:135 (L1-08) — "Q = n e, … e = 1,602·10⁻¹⁹ J" uses e (the elementary charge) for one electronvolt. Write Q = 200·10⁶ · 1 eV = 200·10⁶ · 1,602·10⁻¹⁹ J.
- solutions.md:172 (L3-04) — "koska aktiivisuuden mittaus on epätarkka": use the guardrail sentence ("…eivät yleensä sijaitse täsmälleen samalla suoralla mittausepävarmuuden vuoksi"). In b), say that the extrapolation runs from 50 a to 250 a.
- exercises.json:294 (L3-04) — 3000 TBq/t is about 10× low for 10 a old fuel (~10⁴ TBq/t); scaling ×10 would be more realistic.
- exercises.json:191 (L2-06) — reactor powers are correct (see Checked). The source could be made more specific: "TVO:n ja Fortumin verkkosivut / STUK, tilanne 2024".

## Checked
- Hash 82dfe66a8cba123a at the start and at the end.
- All 17 numeric answers recomputed in one script with my own formulas (new tasks: 3,204; 1859,6; 34,64 TWh; 249,7 a; 543,0 kg). All are within 0,6 % of exercises.json and answers.py.
- Reactor powers: OL1 890, OL2 890, OL3 1600, LO1 507, LO2 507 MW (net) match Pohjolan Voima/TVO and Fortum (Loviisa EIA summary: 507 MW net and 1500 MW thermal per unit; uprates in 2018), so they are valid for 2024. η = 0,338 makes the 0,33 in L3-05 realistic.
- L2-05: the consecutive ratios are 1,009–1,016, as the solution says. A least-squares k = 1,01238 gives N₅₀ = 1849, which is within the 3 % tolerance. "Supercritical" is correct.
- L3-04: fit λ = 0,02285 1/a, T½ = 30,3 a, A₀ = 3006, verified.
- MC L1-06, L1-07, L2-07: exactly one correct option in each, and the feedback is right. L3-05 c): 1,86·10⁶ t of coal, correct.
