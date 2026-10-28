# Concept review: heat transfer (science)

Reviewed from `review-concepts/packet-heat-transfer.md`; context opened only for fy2-8 koe-1 (all choices), fy3-12 lesson line 261 and fy3-12 solution line 98. Numbers recomputed: fy2-1 L1-02/03, fy3-12 tase (240 + 150 = 390), check-2 (240 − 100 = 140; atmosphere 290 in = 290 out), L1-05 (238 W/m²), fy3-15 L1-03 (4,20 kW), Sovella c/d (400 W, η ≈ 0,59): all agree.

## Contradictions

1. `content/fi/FY2/fy2-1/lesson.md` (lines 19 and 109, B) — "energiaa, joka *siirtyy* lämpimämmästä kylmempään lämpötilaeron vuoksi" — drops "nettomääräisesti", which fy3-12 (lines 3, 12–13, 98–100) and fy3-16 state: the colder body also radiates. Fix (line 19): "Sana **lämpö** taas tarkoittaa fysiikassa energiaa, joka *siirtyy* lämpötilaeron vuoksi: energiaa siirtyy nettomääräisesti lämpimämmästä kappaleesta kylmempään. Kappaleella on lämpöenergiaa, ja lämpönä energiaa siirtyy kappaleesta toiseen." Fix (line 109): "- Kappaleella on lämpöenergiaa; lämpö on energiaa, joka siirtyy lämpötilaeron vuoksi, nettomääräisesti lämpimämmästä kylmempään."
2. `content/fi/FY2/fy2-8/inquiry.json` (koe-1.question.choices[2].feedback, B) — "Kaasumolekyyli lähettää eteenpäin vain sen säteilyn, jonka se on imenyt maanpinnalta." — teaches photon re-emission; fy3-12 check-2.solution says the atmosphere radiates according to its temperature ("säteilee alas hieman enemmän kuin ylös, koska alempi ilma on lämpimämpää"), and the guardrail says every body radiates. Fix: "Ilmakehä säteilee vain sitä energiaa, jonka se on saanut, ja suurin osa siitä on peräisin maanpinnan lämpösäteilystä, jota kaasut imevät."
3. `content/fi/FY3/fy3-12/lesson.md` (line 2, Miksi, B) — "vaikka maapallo säteilee avaruuteen yhtä paljon energiaa kuin saa Auringosta" — the same lesson (lines 23–24), L1-05 and check-3 say it radiates what it *absorbs*; 30 % of what it receives is reflected. Fix: "vaikka maapallo säteilee avaruuteen yhtä paljon energiaa kuin imee Auringosta"
4. `content/fi/FY2/fy2-8/inquiry.json` (ennuste-1.choices[0].feedback, B) — "niiden poistaminen ei lisäisi maanpinnalle tulevaa energiaa" — without "Auringosta" this reads against fy3-12 (tase), where the surface receives 150 W/m² from the atmosphere as well, which removing the gases would take away. Fix: "joten niiden poistaminen ei lisäisi Auringosta maanpinnalle tulevaa energiaa."

## Guardrail breaks

None beyond items 1–2. The net-transfer wording is used in fy3-12 (Ydinajatus, Tiivistelmä) and fy3-16 (line 136, pred-1); conduction, convection and radiation are defined the same way in fy3-12 and FY3 Sovella; "ilmakehä ei tuota energiaa" (fy3-12) agrees with fy2-8; vacuum allows only radiation (fy3-12 tase, L-solution).

## Consistent

- Fysiikka tieteenä (fy1-1): no heat-transfer physics, only radiation pulses; nothing to judge.
- Energialajit (fy2-1): radiation energy and conversions fine; apart from item 1.
- Energian muuntuminen (fy2-2): radiation → chemical chain consistent.
- Hyötysuhde (fy2-4), Energiantuotantotavat (fy2-6): incident radiation as input, consistent.
- Energiantuotanto ja ilmastonmuutos (fy2-8): greenhouse mechanism agrees with fy3-12 (Sun passes, thermal radiation absorbed and partly re-radiated down; CO₂ < 0,5 ‰); apart from items 2 and 4.
- Kaasun tekemä työ (fy3-11): nothing on transfer to judge.
- Lämmön siirtyminen (fy3-12): energy balance tables, imbalance and new equilibrium consistent; apart from item 3.
- Energiantuotanto (fy3-15), Q = cmΔT (fy3-6), tilanmuuttujat (fy3-3), soveltava tunti (fy3-16), FY3 Sovella: consistent.
