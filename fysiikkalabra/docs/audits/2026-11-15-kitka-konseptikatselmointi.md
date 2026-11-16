# Konseptikatselmointi: internal-energy (kitka), työjono 8m, 2026-11-15

Tiedekatselmoija (Opus medium) `concepts.py packet internal-energy` -paketista PR #618:ssa, kun kitkatermit vaihdettiin.
Uudet termit (liukukitka, lepokitka, täysin kehittynyt lepokitka eli lähtökitka) ovat yhtenäiset kaikkialla, eikä
liikekitkaa ole enää sisällössä. Alla olevat löydökset ovat 8m:ää vanhempia ja kuuluvat työjonon kohtaan 18 (kurssi
kerrallaan); 8m ei korjannut niitä. Selostus sanatarkasti katselmoijan raportista (englanniksi).

## Contradictions
1. **$F_{\mu 0}$ means two things (B).** Any static friction in FY4/fy4-6/lesson.md:314/316 and :384 ("$F_{\mu 0} \le \mu_0 N$"),
   units/fy9-kokeellisuus/sovella/tasks.json c.criteria[0], FY4/koe/solutions.md:181 ("$F_{\mu 0} = ma$"); its greatest value
   (lähtökitka) in fy4-6:318 ("$F_{\mu 0} = \mu_0 N$") and fy9-voimat/unit.md:239. fy4-6:384 labels static friction $\overline{F}_\mu$
   but gives its size as $F_{\mu 0}$; the fy5-4 diagrams label lähtökitka $\overline{F}_\mu$. Fix: $F_{\mu 0}$ for lähtökitka only;
   "Lepokitka on $F_\mu \le \mu_0 N$" in fy4-6:314/384 and the fy9-kokeellisuus criterion, "joten $F_\mu = ma$" in FY4 koe.
2. **Friction "uses up" energy in FY4 and FY9 (B)**, against FY2 fy2-1 ("Kitka muuttaa energiaa, ei kuluta sitä") and
   fy9-sailymislait: FY4/koe tasks.json a.criteria[0] and solutions d) "kitkan työ kuluttaa liike-energian"; FY4/sovella solutions
   "kunnes liike-energia on kulunut loppuun"; fy4-16 solutions "Potentiaalienergian väheneminen kuluu kitkan tekemään negatiiviseen
   työhön"; fy4-16 lesson (heading, line 35) "kitka vie energiaa"; fy9-lampo/sovella b) line 288 and tasks.json:632 "kuluu
   ajovastusten työhön"; fy9-sailymislait/sovella "metriä kohti kuluu vähemmän liike-energiaa". Fix pattern: "Kitkan negatiivinen
   työ muuttaa liike-energian sisäenergiaksi" and "potentiaalienergian väheneminen on yhtä suuri kuin ajovastusten ja jarrujen
   sisäenergiaksi muuttama energia".
3. **fy9-energia says "lämpöenergiaksi" (B)**: unit.md:291, inquiry.json lt-1 choices 0–2 (P1 covers FY9). Fix: "Se on muuttunut
   lumen, jalasten ja ilman sisäenergiaksi." / "Kitka ja ilmanvastus muuttavat mekaanista energiaa sisäenergiaksi, ja kokonaisenergia säilyy."

## Guardrail breaks
4. **A.** FY4/fy4-10/exercises/solutions.md:207 (L3-04): "liike-energia muuttuu kitkan tekemäksi työksi" → "kitkan negatiivinen työ muuttaa liike-energian sisäenergiaksi".
5. **A.** FY5/fy5-4/exercises/solutions.md:312 (L3-05): "kitkan ei tarvitse tehdä koko työtä" → "kitkan ei tarvitse antaa koko keskipisteeseen osoittavaa voimaa" (also oikoluku §9).
6. **B.** FY4/fy4-8/lesson.md:300: "kitka … vähentää kappaleen energiaa" → "kappaleen mekaanista energiaa".
7. **B.** units/fy9-voimat/inquiry.json:490 (tarkistus-2.mistakes[0]): "osa työnnöstä kuluu …" → "se on työntöä pienempi, koska työnnön ja voiman $P$ erotus kiihdyttää A:ta ja kumoaa A:n kitkan."
8. **B.** units/fy9-lampo/sovella solutions d) line 308, tasks.json:688: engine braking is mostly pumping and throttling, not friction → "muuttuu moottorissa kitkan ja ilman pumppaamisen kautta sisäenergiaksi, joka siirtyy jäähdytysjärjestelmän ja pakokaasun mukana lämpönä ilmaan."
9. **Heat-into sentences the checker does not catch** (add to the item-18 round): units/fy9-lampo/sovella/solutions.md:315; units/fy9-energia/unit.md:381 "yleensä lämmöksi"; FY7/koe/solutions.md:288 "Seitsemäsosa tehosta lämmöksi"; FY8/fy8-2/lesson.md "osa energiasta muuttuu lämmöksi".
