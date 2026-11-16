"""physics_phrases.py catches the sentences the 2026-10-28 audit found (and the 2026-11-15 proofreading's P1 and P8),
passes their corrections, and passes every Finnish lesson, unit, exercise set and Sovella itsenäisesti file now except
the sentences listed in docs/physics-phrases-known.tsv, which work queue 18 corrects (NOTES.md §10).

  python scripts/test_physics_phrases.py"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import physics_phrases as P

CAUGHT = {   # the audit's original sentences (FY1–FY3, 2026-10-28)
    "scale-half": ["Kun mittaus tehdään vain kerran, virhe-arvio on puoli asteikkoväliä $d$:",
                   "Viivaimen pienin asteikkoväli on 1,0 mm, ja yksittäisen lukeman virhe-arvio on puoli asteikkoväliä."],
    "scale-max": ["Virhe-arvio ei voi olla asteikkoväliä suurempi."],
    "never-on-line": ["**Miksi** mittauspisteet eivät koskaan osu täsmälleen samalle suoralle, ja silti niistä voi lukea lain?"],
    "outlier-drop": ["Se näkyy selvästi muista poikkeavana tuloksena, joka tarkistetaan ja jätetään pois.",
                     "Selvästi poikkeava tulos tarkistetaan ja jätetään pois."],
    "half-range-mean": ["Keskiarvon epävarmuus on puolet vaihteluvälistä."],
    "dive-exhale": ["Noustessa on hengitettävä koko ajan ulos."],
    "phase-energy": ["Olomuodon muutos vaatii energiaa, mutta ei nosta lämpötilaa."],
    "uncertainty-max": ["Mittausepävarmuus kertoo, kuinka paljon lukema voi enintään poiketa todellisesta arvosta."],
    "efficiency-below-100": ["Hyötysuhde on aina alle $100\\,\\%$, joten tulos $330\\,\\%$ on mahdoton."],
    "phase-bonds": ["Kun jää sulaa, vesimolekyylien sidokset katkeavat."],
    "heat-stored": ["Kuuma kivi sisältää paljon lämpöä."],
    "friction-creates": ["Kitka synnyttää lämpöenergiaa."],
    "all-fuels-co2": ["Kaikki polttoaineet tuottavat palaessaan hiilidioksidia."],
    "absolute-zero-stop": ["Absoluuttisessa nollapisteessä hiukkasten liike pysähtyy kokonaan."],
    "heat-direction": ["Lämpö siirtyy aina lämpimämmästä kappaleesta kylmempään."],
    "heat-into": ["Matka on pitkä, joten energiasta muuttuu lämmöksi yli puolet.",            # teacher 2026-11-15, P1
                  "Liike-energia jää lopulta lämmöksi.", "Joulen lain mukaan resistanssissa lämmöksi muuttuva teho on $RI^2$.",
                  "Loput energiasta meni värähtelyyn, ääneen ja lämpöön."],
    "liikekitka": ["Liukuvaan laatikkoon vaikuttaa liikekitka $F_\\mu = \\mu N$.", "Laatikon ja sillan välinen liikekitkakerroin on $0{,}30$."],   # P8
    "higher-line-ahead": ["Kuvaajasta nähdään myös, kumpi kappale on edellä milloinkin: se, jonka viiva on ylempänä.",
                          "Lukema $x_\\text{B} - x_\\text{A}$ on B:n etumatka: se on positiivinen, kun B on edellä, ja nolla kohtaamishetkellä."],   # fy4-12, 2026-10-30
}
PASSED = [   # their corrections and nearby right statements
    "Lukema $x_\\text{B} - x_\\text{A}$ kertoo, kuinka paljon suurempi B:n paikkakoordinaatti on, ja se on nolla kohtaamishetkellä.",
    "Kun mittalaitteen asteikolta luetaan arvo, lukeman epävarmuutta voidaan yksinkertaisessa tilanteessa arvioida esimerkiksi puoleksi pienimmästä asteikkovälistä.",
    "Lukeman epävarmuus on siis pienempi kuin asteikkoväli, mutta mittauksen kokonaisepävarmuus voi olla tätä suurempi.",
    "Mittauspisteet eivät yleensä osu kaikki täsmälleen samalle suoralle.",
    "Tulosta ei poisteta pelkästään siksi, että se poikkeaa muista.",
    "Selvästi poikkeava tulos tarkistetaan, ja se jätetään pois vain, jos virheen syy löytyy.",
    "Tässä harjoituksessa keskiarvon epävarmuutta arvioidaan yksinkertaisesti puolella vaihteluvälistä.",
    "Noustessa ei saa koskaan pidättää hengitystä: hengitetään normaalisti koko nousun ajan.",
    "Sulaminen ja höyrystyminen vaativat energiaa, mutta eivät nosta lämpötilaa.",
    "Mittausepävarmuus kuvaa mittaustulokseen liittyvää epävarmuutta. Se ei yleensä tarkoita ehdotonta suurinta mahdollista poikkeamaa oikeasta arvosta.",
    "Hyötysuhde on enintään $100\\,\\%$. Todellisissa laitteissa se jää usein alle $100\\,\\%$.",
    "Lämpövoimakoneen hyötysuhde on aina alle $100\\,\\%$, koska osa lämmöstä on luovutettava kylmempään ympäristöön.",
    "Sulaessa molekyylien väliset vuorovaikutukset heikkenevät, mutta molekyylien sisäiset sidokset eivät katkea.",
    "Kuuman kiven sisäenergia on suuri, ja sitä siirtyy lämpönä ympäristöön.",
    "Kitka muuntaa liike-energiaa sisäenergiaksi.",
    "Hiiltä sisältävät polttoaineet tuottavat palaessaan hiilidioksidia.",
    "Absoluuttisessa nollapisteessä hiukkasten energia on pienimmillään.",
    "Absoluuttisessa nollapisteessäkään kaikki hiukkasten liike ei lakkaa.",
    "Lämpötilaeron vuoksi energiaa siirtyy nettomääräisesti lämpimämmästä kappaleesta kylmempään.",
    "Yleinen virhekäsitys: hyötysuhde on aina alle $100\\,\\%$.",
    "Kuvaajassa ylempänä oleva viiva tarkoittaa suurempaa paikkakoordinaattia.",
    "Kun kappaleet liikkuvat $x$-akselin positiiviseen suuntaan, ylempänä oleva viiva kuuluu edellä olevalle kappaleelle.",
    "Kitkan tekemä työ muuttaa liike-energiaa sisäenergiaksi, joka siirtyy lämpönä ympäristöön.",
    "Lämpövoimalan polttoaineteho jakautuu sähkötehoksi ja hukkalämmöksi.",
    "Näin siirtyvää energiaa sanotaan lämmöksi.",
    "Lämpöteho on $2{,}0\\,\\text{kW}$.",
    "Liukuvaan laatikkoon vaikuttaa liukukitka $F_\\mu = \\mu N$, ja sen suurin lepokitka on täysin kehittynyt lepokitka eli lähtökitka.",
    "Liukukitkaa sanottiin aiemmin myös liikekitkaksi.",
]
FY2_HEAT = "Kitkan vuoksi osa liike-energiasta muuttuu lämmöksi."   # FY2 keeps lämpöenergia and its wording (P1)
DISTRACTOR = '{"choices": [{"text": "Hyötysuhde on aina alle 100 %.", "feedback": "Ei. Hyötysuhde on enintään 100 %."}, {"text": "Enintään 100 %.", "correct": true, "feedback": "Oikein."}]}'
TAUGHT = '{"choices": [{"text": "Hyötysuhde on aina alle 100 %.", "correct": true, "feedback": "Oikein."}]}'

bad = 0
for rid, texts in CAUGHT.items():
    for t in texts:
        got = {p[2] for p in P.problems_in("lesson.md", t)}
        if rid not in got: bad += 1; print(f"FAIL not caught [{rid}]: {t}")
for t in PASSED:
    got = P.problems_in("lesson.md", t)
    if got: bad += 1; print(f"FAIL false alarm [{got[0][2]}]: {t}")
if P.problems_in("lesson.md", FY2_HEAT, "FY2"): bad += 1; print("FAIL heat-into flagged an FY2 text (P1: FY3–FY9 only)")
if not P.problems_in("lesson.md", FY2_HEAT, "FY4"): bad += 1; print("FAIL heat-into missed an FY4 text")
if P.course_of(P.ROOT / "content/fi/units/fy9-lampo") != "units" or P.course_of(P.ROOT / "content/fi/FY2/fy2-1") != "FY2": bad += 1; print("FAIL course_of")
if P.problems_in("inquiry.json", DISTRACTOR): bad += 1; print("FAIL a wrong option's own text was flagged")
if not P.problems_in("inquiry.json", TAUGHT): bad += 1; print("FAIL a correct option's claim was not flagged")
KNOWN, seen = P.known(), set()   # docs/physics-phrases-known.tsv: hits already in the texts when their rule came
for folder in P.finnish_units():
    for f, line, rid, msg, s in P.problems(folder):
        key = (str(folder.relative_to(P.ROOT / "content/fi")), f, rid, s)
        if key in KNOWN: seen.add(key); continue
        bad += 1; print(f"FAIL {folder.relative_to(P.ROOT)}/{f}:{line} [{rid}] {msg}\n    «{s}»")
for k in sorted(KNOWN - seen): print(f"note: {P.KNOWN.name} row no longer found (delete it): {k[0]}/{k[1]} [{k[2]}]")
print(f"{len(seen)} known sentence(s) still to correct ({P.KNOWN.relative_to(P.ROOT)}, work queue 18)")
print("test_physics_phrases:", "OK" if not bad else f"{bad} failure(s)")
sys.exit(1 if bad else 0)
