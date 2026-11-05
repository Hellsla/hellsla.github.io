VERDICT: PASS
CONTENT-HASH: f527223788565a17

Science review of the Selkeä suomi translation of fy9-lampo (2026-11-04). Source: content/fi/units/fy9-lampo/ (passed its three reviews).

Checks: `check_i18n.py` fi-easy 0 errors; `practice.py check` OK (6 tasks, 95 points, same as fi); `units.py check` ok; `translate_kit.py changed` lists nothing. Every JSON text and every Markdown paragraph was compared with the source side by side. All numbers, answers, tolerances, correct options, formulas and units are the source's. I recomputed in one Python call: 13,79 kg; 2,027 kg; 180 mm; 0,886 K; 3,88 kg; c_jää 2083 J/(kg·K); s1 21,9 GJ and 17,4 h; s2 81,6 K, 1667 W and 35,8 %; s3 r = 2,26 MJ/kg and P_h = 70 W; s5 371 and 333 kJ/kg; s6 31,5 K, 133,7 K and 40,2 %. All match. The added explanations are correct physics: laavu, sohjo, kutistusliitos, kalibrointi, haruksen kiinnitys, kohvajää, konvektio and moottorijarrutus. The law conditions (constant pressure in a phase change, the validity range of the expansion formulas, the constant loss power in s3) were kept in plain words. Sign conventions (ΔU = Q + W) and the "lämpö is not stored" wording follow physics-guardrails.

## Blocking
None.

## Polish
1. sovella/solutions.md, s2 d) Mallivastaus, and tasks.json tasks[1].parts[3].criteria[1].text: "Takan pinta on vain vähän lämmin" reads more weakly than the source's "maltillisen lämmin". It also clashes with s2 a) Järkevyys ("Takan pinta tuntuu silloin kuumalta, mutta se ei polta"). Fix: "Takan pinta on kohtalaisen lämmin, paljon viileämpi kuin kamiinan pinta."
2. unit.json key_concepts "lämpötasapaino": the second sentence is the energy balance of an isolated system, not part of the definition. Fix: "Eristetyssä systeemissä luovutettu lämpö on yhtä suuri kuin vastaanotettu lämpö."
3. unit.json key_concepts "ominaislämpökapasiteetti": "kun kilogramman lämpötila nousee yhden kelvinin" is loose. Fix: "kun yhden aineen kilogramman lämpötila nousee yhdellä kelvinillä". The FY chapters say "tunnus", not "merkki", for a quantity's symbol. Use "Tunnus on $c$" here and in "ominaissulamislämpö".
4. tasks.json tasks[5].parts[3].text: the added gloss "kun kaasu nostetaan ylös ja vaihde on päällä" is correct but colloquial. Fix: "kun kuljettaja nostaa jalan kaasupolkimelta ja vaihde on päällä".

## Shared issues
None new. The developer report already notes that the 13 px labels of the reused fy3-7/melting-curve belong to the FY3 module.
