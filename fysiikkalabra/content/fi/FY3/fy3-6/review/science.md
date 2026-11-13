VERDICT: FAIL
CONTENT-HASH: 026f61d1646501f3

## Blocking
- inquiry.json:35 (kertaus, the "kylmyyttä" option's feedback): **B**. "Energiaa siirtyy aina kuumemmasta kylmempään" breaks the guardrail on net transfer: both bodies radiate, so only the *net* transfer, which is the heat, goes from hot to cold. Fix: "Lämpötilaeron vuoksi energiaa siirtyy nettomääräisesti kuumemmasta kylmempään, ja vesikin lämpenee …" (or "Lämpönä energiaa siirtyy …").

## Polish
- lesson.md:177: "Eristetyssä astiassa kuuman kappaleen 1 luovuttama lämpömäärä on yhtä suuri kuin kylmän kappaleen 2 vastaanottama". An insulated vessel still takes up heat itself. Add "kun astian oma lämpökapasiteetti jätetään huomiotta", as the worked example, the tasks and the sim's model box already say.
- lesson.md:68: "hiekka … kuumenee samalla energialla moninkertaisesti enemmän". Add "kilogrammaa kohti" (or "yhtä suuri massa"). The figure says "sama m", but the sentence does not.
- lesson.md:175: "lämpenee ja jäähtyy hitaasti". Speed also depends on the heating power. "… sen lämpötila muuttuu vähän tietyllä lämpömäärällä" is more exact. The same applies to "lämpenee hitaasti" in the tarkistus-3 model answer.
- inquiry.json:379 (tarkistus-3, criterion 1): the task gives no c values, and "noin viisinkertainen … maahan verrattuna" depends on the kind of soil. Drop "maahan" or write "moninkertainen".

## Checked
- I recomputed every number in one script: the worked example (5656,5 J; 374,6 → 3,7·10² J/(kg·K); 383 at 24,6 °C; Cu lossless 24,6 °C; C_v = 1257 J/K, C_m ≈ 75 J/K), the misconception (35 °C; ratio 9,3), ennuste-1 (26,8 / 44,0 °C; 8,5 / 30 kJ), ennuste-2 (40,0 / 55,0 / 63,1 °C), Etsi virhe (6,6 °C wrong, 30,0 °C right, and the Kelvin shift is invariant), siirto (29,09 kg; mistakes 220 and 21,3), tarkistus-1 (4500 vs 838 J/K), check-c2 (35 and 65 °C), tarkistus-2 (890,6; mistakes 768 and 501; 134 J/K), exit ticket (419 kJ; ×9). All agree.
- In every choice exactly one option is correct, and each distractor's feedback is right.
- Rounding is justified: 4,5 K (2 s.f.) in the example, 8,0 K in siirto, 3 s.f. in tarkistus-2.
- Q = cmΔT carries its condition (no change of state) in Kaava. The sign convention is stated, and the two positive sides of the balance are explained.
- The T derivation is symbolic before substitution, and so is c_m in the example and the solutions.
- Figures: water-sand ΔT bars are 20 vs 105 px (5,25 vs 5,24, to scale as the label says). The c-bars are within 0,5 px at 93,4 px/1000. The calorimeter numbers match the example, and the figure is labelled "ei mittakaavassa".
- sim.js implements T = ΣCT/ΣC and Q = C_B(T_B0 − T) = Q_W. The exponential approach is labelled as illustration, and the speed changes only the pace. Its default (Cu 0,2 kg, 100 °C) gives the 24,6 °C the example cites.
- koe-1 locks everything except cB, and its "800" matches an option value. koe-2 locks everything except mB, and 0,2/0,5/0,8 kg are inside the slider range. simState provides Teq and CB. The 390 px capture shows 26,8 °C for sand.
- The model answers (johtopäätös, tarkistus-3) agree with the theory, and the values are called model values.
- Scope: within FY3 "aineen lämpeneminen ja jäähtyminen", with no later-course physics.
