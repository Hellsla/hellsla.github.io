VERDICT: PASS
CONTENT-HASH: 108ac8263d630987

## Blocking

## Polish
- exercises/solutions.md fy2-2-L3-03 Järkevyys: "samasta ainemäärästä" — ainemäärä on mooleja; tarkoitus on massa. Fix: "samasta massasta".
- figure tikapuut-kohteet (alt text / task L1-05): kuvaus sanoo asteikon ulottuvan "10 TJ:iin", mutta kuvan asteikko jatkuu kymmenpotenssiin 10^14 J (100 TJ). Fix: "100 TJ:iin" tai sama muotoilu kuin tehtävässä ("ja yli").
- exercises.json fy2-2-L1-05: vastaus 100 000 on kuvasta luettu suuruusluokka (todellinen AA 2,5 Ah · 1,5 V = 13,5 kJ ja salama 1–5 GJ antaisivat noin 70 000–400 000); tehtävä sanoo jo "suuruusluokka", joten ok, mutta 2 % toleranssi on ahdas kuvan ulkopuolisille luvuille. Harkitse maininta "käytä kuvasta luettuja arvoja".

## Checked
- Recomputed all 12 answers in one script: 54000, 2,27, 140, 3, 1e5, 3,0, 1,28, 6,0, 954,5, 6 (5,64 ylös), 3194, 1,16e7; answers.py and exercises.json agree within tolerance, units right.
- Rounding reasons fit the limiting datum (L1-04 whole MJ, L3 integer, others 2 s.f.).
- L2-03: absorbed-light assumption stated in the task; E_lämpö = E_sähkö correct.
- L3-02: 370 TJ (OL3 4300 MW_th · 86400 s = 372 TJ), 140 TJ electricity, rest to sea stated in task; CHP remark is a fair qualitative simplification.
- L3-03: 370 TJ / 8,2e13 J/kg = 4,5 kg U-235; 32 MJ/l; no scope breach (no W=Fs, no chain efficiency product).
- L1-05 figure: AA at 10^4 J, lightning 10^9 J, five intervals; teeveden kiehautus 84 kJ ~ 10^5 J right.
- Data realistic: TNT 4,2 GJ/t, suklaa 22 MJ/kg, bensiini 32 MJ/l, Suomi 790 TJ/vrk, talo 72 GJ/a. Notation matches lesson. Hash start = end.
