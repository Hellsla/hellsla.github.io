VERDICT: FAIL
CONTENT-HASH: 33257cb2bee355da

## Blocking
- lesson.md:76 — "Loppulämpötila on lämpötasapaino, ei keskiarvo." mixes a quantity with a state: the glossary defines lämpötasapaino as a "tila" (state), the final temperature is the tasapainolämpötila; the sentence also leaves unclear what is not an average — fix: "Tasapainolämpötila ei yleensä ole alkulämpötilojen keskiarvo." (in the diff)

## Polish
- lesson.md:6 — "Kilogramman vettä lämmittäminen ... kilogramman rautaa" is ungrammatical (object in partitive as a noun phrase) — "Kilogramman veden lämmittäminen ... kilogramman raudan lämmittäminen" (in the diff)
- lesson.md:71 and exit-ticket.json:7 — "Kilon vettä ja kilon rautaa" (wrong case) — "Kilon veden ja kilon raudan lämmittäminen" / "Kilo vettä ja kilo rautaa saavat" (in the diff); also "erisuuret" -> "erisuuruiset" (lesson.md:71)
- exercises.json L1-04 — "veden lämpömäärä Q" treats Q as a property of the water, against the glossary entry for lämpö — "veteen siirtyvä lämpömäärä Q" (in the diff)
- exercises.json L1-02 — "jossa on rautaa 2,4 kg" is clumsy — "jonka massa on 2,4 kg" (in the diff); sim-spec.md:1 "Nappi" -> "Painike"
- Not in the diff: lesson.md:23 uses "tasapainolämpötila", which is not in glossary.json (the lesson meta lists only 5 terms); consider adding it to the glossary.

## Diff
```diff
--- a/lesson.md
+++ b/lesson.md
@@ -3,7 +3,7 @@
 > **Miksi** uimarannan hiekka polttaa jalkapohjia jo aamupäivällä, kun vesi on vielä viileää, vaikka aurinko on paistanut molempiin yhtä kauan?
 
 ## Ydinajatus
-Kun kappaleeseen siirtyy lämpöä, sen sisäenergia kasvaa ja lämpötila nousee. Kokeissa havaitaan, että tarvittava lämpömäärä on suoraan verrannollinen sekä lämpötilan muutokseen että kappaleen massaan: kaksi kertaa suurempi lämpötilan nousu vaatii kaksinkertaisen lämpömäärän, ja kaksinkertainen vesimäärä vaatii kaksinkertaisen lämpömäärän. Lisäksi lämpömäärä riippuu aineesta. Kilogramman vettä lämmittäminen yhdellä asteella vaatii noin 4,2 kJ, mutta kilogramman rautaa vain noin 0,45 kJ. Aineelle ominainen kerroin on ominaislämpökapasiteetti c, jonka yksikkö on J/(kg·K). Se kertoo, kuinka paljon energiaa tarvitaan yhden kilogramman lämmittämiseen yhdellä kelvinillä, ja sama määrä vapautuu, kun aine jäähtyy yhden kelvinin.
+Kun kappaleeseen siirtyy lämpöä, sen sisäenergia kasvaa ja lämpötila nousee. Kokeissa havaitaan, että tarvittava lämpömäärä on suoraan verrannollinen sekä lämpötilan muutokseen että kappaleen massaan: kaksi kertaa suurempi lämpötilan nousu vaatii kaksinkertaisen lämpömäärän, ja kaksinkertainen vesimäärä vaatii kaksinkertaisen lämpömäärän. Lisäksi lämpömäärä riippuu aineesta. Kilogramman veden lämmittäminen yhdellä asteella vaatii noin 4,2 kJ, mutta kilogramman raudan lämmittäminen vain noin 0,45 kJ. Aineelle ominainen kerroin on ominaislämpökapasiteetti c, jonka yksikkö on J/(kg·K). Se kertoo, kuinka paljon energiaa tarvitaan yhden kilogramman lämmittämiseen yhdellä kelvinillä, ja sama määrä vapautuu, kun aine jäähtyy yhden kelvinin.
 
 Veden ominaislämpökapasiteetti on poikkeuksellisen suuri. Siksi vesi lämpenee auringossa hitaasti ja jäähtyy illalla hitaasti, kun taas hiekka, jonka c on noin viidesosa veden arvosta, kuumenee samalla energialla moninkertaisesti. Samasta syystä järvet tasaavat rannikon lämpötiloja ja vesi on hyvä lämmönsiirtoaine lämmitysputkissa. Koko kappaleen lämpökapasiteetti C = cm kertoo, kuinka monta joulea kappaleen lämpötilan nostaminen yhdellä kelvinillä vaatii; sen yksikkö on J/K.
 
@@ -68,10 +68,10 @@
 Arvo on lähellä kuparin ominaislämpökapasiteettia 385 J/(kg·K), joten kappale on luultavasti kuparia. Pieni ero selittyy sillä, että osa lämmöstä siirtyi kalorimetrin astiaan ja ilmaan. Huomaa, että vesi lämpeni vain 4,5 K, vaikka metalli jäähtyi 75,5 K: veden lämpökapasiteetti 1257 J/K on paljon suurempi kuin kappaleen 75 J/K.
 
 ## Yleinen virhekäsitys
-Moni ajattelee, että lämpömäärä ja lämpötila ovat sama asia, tai että samaan lämpötilaan lämmitetyt kappaleet ovat saaneet saman määrän energiaa. Kilon vettä ja kilon rautaa lämmittäminen 20 °C:sta 60 °C:seen vaatii vedelle lähes kymmenkertaisen energian. Toinen virhe on laskea tasapainolämpötila keskiarvona: kun 1,0 kg 80-asteista vettä kaadetaan 3,0 kg:aan 20-asteista vettä, lopputulos ei ole 50 °C vaan 35 °C, koska massat ovat erisuuret. Kolmas virhe on muuntaa ΔT kelvineiksi lisäämällä 273: lämpötilan muutos on sama kummallakin asteikolla.
+Moni ajattelee, että lämpömäärä ja lämpötila ovat sama asia, tai että samaan lämpötilaan lämmitetyt kappaleet ovat saaneet saman määrän energiaa. Kilon veden ja kilon raudan lämmittäminen 20 °C:sta 60 °C:seen vaatii vedelle lähes kymmenkertaisen energian. Toinen virhe on laskea tasapainolämpötila keskiarvona: kun 1,0 kg 80-asteista vettä kaadetaan 3,0 kg:aan 20-asteista vettä, lopputulos ei ole 50 °C vaan 35 °C, koska massat ovat erisuuruiset. Kolmas virhe on muuntaa ΔT kelvineiksi lisäämällä 273: lämpötilan muutos on sama kummallakin asteikolla.
 
 ## Tiivistelmä
 - Lämpömäärä on verrannollinen massaan ja lämpötilan muutokseen: $Q = c m \Delta T$. Ominaislämpökapasiteetti c riippuu aineesta, ja vedellä se on suuri, 4190 J/(kg·K).
 - Lämpökapasiteetti $C = cm$ kertoo, kuinka monta joulea koko kappaleen lämmittäminen yhdellä kelvinillä vaatii.
-- Eristetyssä astiassa kuuman luovuttama lämpömäärä on yhtä suuri kuin kylmän vastaanottama: $c_1 m_1 (T_1 - T) = c_2 m_2 (T - T_2)$. Loppulämpötila on lämpötasapaino, ei keskiarvo.
+- Eristetyssä astiassa kuuman luovuttama lämpömäärä on yhtä suuri kuin kylmän vastaanottama: $c_1 m_1 (T_1 - T) = c_2 m_2 (T - T_2)$. Tasapainolämpötila ei yleensä ole alkulämpötilojen keskiarvo.
 - Kalorimetrisellä mittauksella määritetään tuntemattoman aineen ominaislämpökapasiteetti veden avulla.
--- a/exercises.json
+++ b/exercises.json
@@ -11,7 +11,7 @@
     {
       "id": "fy3-6-L1-02",
       "level": 1,
-      "text": "Valurautainen paistinpannu, jossa on rautaa 2,4 kg, nostetaan liedeltä mökin pöydälle. Pannun lämpötila laskee 220 °C:sta 25 °C:seen. Kuinka suuren lämpömäärän pannu luovuttaa ympäristöön? Anna vastaus kilojouleina.",
+      "text": "Valurautainen paistinpannu, jonka massa on 2,4 kg, nostetaan liedeltä mökin pöydälle. Pannun lämpötila laskee 220 °C:sta 25 °C:seen. Kuinka suuren lämpömäärän pannu luovuttaa ympäristöön? Anna vastaus kilojouleina.",
       "answer": 210,
       "unit": "kJ",
       "tolerance": 0.02
@@ -27,7 +27,7 @@
     {
       "id": "fy3-6-L1-04",
       "level": 1,
-      "text": "Mökin paljussa on 1200 kg vettä. Yön aikana vesi jäähtyy 38 °C:sta 31 °C:seen. Kuinka suuri on veden lämpömäärä Q? Anna vastaus etumerkkeineen megajouleina (negatiivinen Q tarkoittaa, että vesi luovuttaa lämpöä).",
+      "text": "Mökin paljussa on 1200 kg vettä. Yön aikana vesi jäähtyy 38 °C:sta 31 °C:seen. Kuinka suuri on veteen siirtyvä lämpömäärä Q? Anna vastaus etumerkkeineen megajouleina (negatiivinen Q tarkoittaa, että vesi luovuttaa lämpöä).",
       "answer": -35,
       "unit": "MJ",
       "tolerance": 0.02
--- a/exit-ticket.json
+++ b/exit-ticket.json
@@ -4,7 +4,7 @@
     "a": "Q = cmΔT = 4190 J/(kg·K) · 2,0 kg · 50 K = 419 000 J ≈ 420 kJ."
   },
   {
-    "q": "Kilon vettä ja kilon rautaa saavat saunassa saman lämpömäärän. Kumman lämpötila nousee enemmän ja suunnilleen kuinka moninkertaisesti?",
+    "q": "Kilo vettä ja kilo rautaa saavat saunassa saman lämpömäärän. Kumman lämpötila nousee enemmän ja suunnilleen kuinka moninkertaisesti?",
     "a": "Raudan. Sen ominaislämpökapasiteetti 450 J/(kg·K) on noin yhdeksäsosa veden arvosta 4190 J/(kg·K), joten sama lämpömäärä nostaa raudan lämpötilaa noin yhdeksän kertaa enemmän."
   },
   {
--- a/sim-spec.md
+++ b/sim-spec.md
@@ -1 +1 @@
-Kalorimetri. Eristetyssä astiassa on vettä, johon upotetaan kuuma tai kylmä kappale. Säätimet: veden massa 0,10–1,00 kg ja alkulämpötila 5–60 °C; kappaleen aine valikosta (vesi 4190, jää ei mukana, alumiini 900, hiekka 800, rauta 450, kupari 385 J/(kg·K)), kappaleen massa 0,05–1,00 kg ja alkulämpötila 0–100 °C. Nappi ”Upota” käynnistää animaation, jossa molempien lämpötilat lähestyvät toisiaan ajan funktiona ja asettuvat tasapainolämpötilaan T = (c₁m₁T₁ + c₂m₂T₂)/(c₁m₁ + c₂m₂); lähestymisen aikaskaala on vain havainnollistus (eksponentiaalinen, muutama sekunti), ei fysikaalinen malli. Piirrä vasemmalle astia, jossa veden ja kappaleen väri kuvaa lämpötilaa, ja oikealle (t, T)-kuvaaja molemmille käyrille sekä tasapainolämpötilan vaakaviiva. Tekstinä kankaan alla: tasapainolämpötila, veden ja kappaleen lämpökapasiteetit C = cm, kappaleen luovuttama ja veden vastaanottama lämpömäärä (yhtä suuret), ja huomautus, kumpi lämpenee. simState sisältää mW, TW0, cB, mB, TB0, Teq, CW, CB, Q ja running. Ei satunnaisuutta, ei olomuodon muutoksia (kappaleen alkulämpötila pysyy välillä 0–100 °C ja vesi nesteenä).
+Kalorimetri. Eristetyssä astiassa on vettä, johon upotetaan kuuma tai kylmä kappale. Säätimet: veden massa 0,10–1,00 kg ja alkulämpötila 5–60 °C; kappaleen aine valikosta (vesi 4190, jää ei mukana, alumiini 900, hiekka 800, rauta 450, kupari 385 J/(kg·K)), kappaleen massa 0,05–1,00 kg ja alkulämpötila 0–100 °C. Painike ”Upota” käynnistää animaation, jossa molempien lämpötilat lähestyvät toisiaan ajan funktiona ja asettuvat tasapainolämpötilaan T = (c₁m₁T₁ + c₂m₂T₂)/(c₁m₁ + c₂m₂); lähestymisen aikaskaala on vain havainnollistus (eksponentiaalinen, muutama sekunti), ei fysikaalinen malli. Piirrä vasemmalle astia, jossa veden ja kappaleen väri kuvaa lämpötilaa, ja oikealle (t, T)-kuvaaja molemmille käyrille sekä tasapainolämpötilan vaakaviiva. Tekstinä kankaan alla: tasapainolämpötila, veden ja kappaleen lämpökapasiteetit C = cm, kappaleen luovuttama ja veden vastaanottama lämpömäärä (yhtä suuret), ja huomautus, kumpi lämpenee. simState sisältää mW, TW0, cB, mB, TB0, Teq, CW, CB, Q ja running. Ei satunnaisuutta, ei olomuodon muutoksia (kappaleen alkulämpötila pysyy välillä 0–100 °C ja vesi nesteenä).
```

## Checked
- lint_lesson.py: 0 errors, 0 warnings (not repeated here)
- Decimal comma in all text; decimal point only in JSON values; minus sign U+2212 in text (solutions.md, exercises.json), hyphen-minus only in JSON numbers
- Space between number and unit everywhere; no "80 N voimalla" type case errors (kg:n, °C:sta, °C:seen, K:ssa all inflected correctly)
- Terminology against glossary.json: ominaislämpökapasiteetti, lämpökapasiteetti, lämpömäärä, lämpötasapaino, kalorimetri, sisäenergia, kelvin used consistently; kelvin never called "aste" (ΔT in K, "yhdellä asteella" only as everyday wording)
- solutions.md, exit-ticket.json, sim.js strings (labels, readout, note) read through: grammar, quotation marks (”Upota” in sim-spec) and punctuation fine
- Reading level suitable for 16-19-year-olds; no numbers, formulas, LaTeX or JSON values touched in the diff
- Diff verified with patch --dry-run from the lesson folder (-p1)
