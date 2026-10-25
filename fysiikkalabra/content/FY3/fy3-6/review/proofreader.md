VERDICT: PASS
CONTENT-HASH: 3b97e896fb63eae2

## Blocking
(none)

## Polish
- lesson.md:8 — "hiekka ... kuumenee samalla energialla moninkertaisesti" lacks a comparative; "vedessä lämpö jakautuu syvemmälle" treats lämpö as something stored (glossary: lämpö is a transfer) — add "enemmän"; "vedessä lämpeneminen ulottuu syvemmälle".
- lesson.md:87 — last sentence is heavy: "veden lämpökapasiteetti 0,300 kg · 4190 … = 1257 J/K on paljon suurempi kuin …" — "veden lämpökapasiteetti on … = 1257 J/K, mikä on paljon enemmän kuin …".
- solutions.md:L2-04 Järkevyys — "noin 7,5-kertainen" has no referent — add "kauhan lämpökapasiteettiin verrattuna".

## Diff
```diff
--- a/lesson.md
+++ b/lesson.md
@@ -5,7 +5,7 @@
 ## Ydinajatus
 Kun kappaleeseen siirtyy lämpöä, sen sisäenergia kasvaa ja lämpötila nousee. Kokeissa havaitaan, että tarvittava lämpömäärä on suoraan verrannollinen sekä lämpötilan muutokseen että kappaleen massaan: kaksi kertaa suurempi lämpötilan nousu vaatii kaksinkertaisen lämpömäärän, ja kaksinkertainen vesimäärä vaatii kaksinkertaisen lämpömäärän. Lisäksi lämpömäärä riippuu aineesta. Kilogramman veden lämmittäminen yhdellä asteella vaatii noin 4,2 kJ, mutta kilogramman raudan lämmittäminen vain noin 0,45 kJ. Aineelle ominainen kerroin on ominaislämpökapasiteetti c, jonka yksikkö on J/(kg·K). Se kertoo, kuinka paljon energiaa tarvitaan yhden kilogramman lämmittämiseen yhdellä kelvinillä, ja sama määrä vapautuu, kun aine jäähtyy yhden kelvinin.
 
-Tärkeä syy on, että veden ominaislämpökapasiteetti on poikkeuksellisen suuri: vesi lämpenee auringossa hitaasti ja jäähtyy illalla hitaasti, kun taas hiekka, jonka c on noin viidesosa veden arvosta, kuumenee samalla energialla moninkertaisesti. Lisäksi aurinko lämmittää vain hiekan ohutta pintakerrosta, kun taas vedessä lämpö jakautuu syvemmälle. Suuren ominaislämpökapasiteettinsa vuoksi järvet tasaavat rannikon lämpötiloja ja vesi on hyvä lämmönsiirtoaine lämmitysputkissa.
+Tärkeä syy on, että veden ominaislämpökapasiteetti on poikkeuksellisen suuri: vesi lämpenee auringossa hitaasti ja jäähtyy illalla hitaasti, kun taas hiekka, jonka c on noin viidesosa veden arvosta, kuumenee samalla energialla moninkertaisesti enemmän. Lisäksi aurinko lämmittää vain hiekan ohutta pintakerrosta, kun taas vedessä lämpeneminen ulottuu syvemmälle. Suuren ominaislämpökapasiteettinsa vuoksi järvet tasaavat rannikon lämpötiloja ja vesi on hyvä lämmönsiirtoaine lämmitysputkissa.
 
 Kun kuuma ja kylmä kappale laitetaan yhteen eristettyyn astiaan, lämpöä siirtyy kuumemmasta kylmempään, kunnes molemmilla on sama lämpötila. Tätä tilaa sanotaan lämpötasapainoksi. Energia säilyy: kuuman kappaleen luovuttama lämpömäärä on yhtä suuri kuin kylmän vastaanottama. Eristettyä astiaa, jossa tämä mitataan, sanotaan kalorimetriksi, ja mittausta kalorimetriseksi mittaukseksi. Sillä voidaan määrittää tuntemattoman aineen ominaislämpökapasiteetti, kun veden ominaislämpökapasiteetti tunnetaan.
 
@@ -84,7 +84,7 @@
 ```latex
 c_\text{m} = \frac{5656{,}5\,\text{J}}{0{,}200\,\text{kg} \cdot 75{,}5\,\text{K}} = 374{,}6\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \approx 3{,}7 \cdot 10^2\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}
 ```
-Tulos ilmoitetaan kahdella merkitsevällä numerolla, koska veden lämpötilan muutos 4,5 K tunnetaan vain kahden numeron tarkkuudella: jos loppulukema olisi 0,1 K suurempi eli 24,6 °C, tulos olisi 383 J/(kg·K). Arvo on lähellä kuparin ominaislämpökapasiteettia 385 J/(kg·K), joten kappale on luultavasti kuparia. Häviöttömässä kalorimetrissä 0,200 kg:n kuparikappale nostaisi veden 24,6 °C:seen (kokeile simulaatiossa); mitattu 0,1 K pienempi lukema selittyy sillä, että osa lämmöstä siirtyi kalorimetrin astiaan ja ilmaan. Huomaa myös, että vesi lämpeni vain 4,5 K, vaikka metalli jäähtyi 75,5 K: veden lämpökapasiteetti 0,300 kg · 4190 J/(kg·K) = 1257 J/K on paljon suurempi kuin kappaleen 0,200 kg · 374,6 J/(kg·K) ≈ 75 J/K.
+Tulos ilmoitetaan kahdella merkitsevällä numerolla, koska veden lämpötilan muutos 4,5 K tunnetaan vain kahden numeron tarkkuudella: jos loppulukema olisi 0,1 K suurempi eli 24,6 °C, tulos olisi 383 J/(kg·K). Arvo on lähellä kuparin ominaislämpökapasiteettia 385 J/(kg·K), joten kappale on luultavasti kuparia. Häviöttömässä kalorimetrissä 0,200 kg:n kuparikappale nostaisi veden 24,6 °C:seen (kokeile simulaatiossa); mitattu 0,1 K pienempi lukema selittyy sillä, että osa lämmöstä siirtyi kalorimetrin astiaan ja ilmaan. Huomaa myös, että vesi lämpeni vain 4,5 K, vaikka metalli jäähtyi 75,5 K: veden lämpökapasiteetti on 0,300 kg · 4190 J/(kg·K) = 1257 J/K, mikä on paljon enemmän kuin kappaleen 0,200 kg · 374,6 J/(kg·K) ≈ 75 J/K.
 
 ## Yleinen virhekäsitys
 Moni ajattelee, että lämpömäärä ja lämpötila ovat sama asia, tai että samaan lämpötilaan lämmitetyt kappaleet ovat saaneet saman määrän energiaa. Kilon veden ja kilon raudan lämmittäminen 20 °C:sta 60 °C:seen vaatii vedelle lähes kymmenkertaisen energian. Toinen virhe on laskea tasapainolämpötila keskiarvona. Kun 1,0 kg 80-asteista vettä kaadetaan 3,0 kg:aan 20-asteista vettä, veden ominaislämpökapasiteetti c on yhtälön molemmilla puolilla ja supistuu pois:
--- a/solutions.md
+++ b/solutions.md
@@ -68,7 +68,7 @@
 **Kaava:** c₁m₁(T₁ − T) = c₂m₂(T − T₂), josta T = (c₁m₁T₁ + c₂m₂T₂) / (c₁m₁ + c₂m₂)
 **Sijoitus:** c₁m₁ = 900 J/(kg·K) · 0,25 kg = 225 J/K ja c₂m₂ = 4190 J/(kg·K) · 0,40 kg = 1676 J/K. T = (225 J/K · 95 °C + 1676 J/K · 18 °C) / (1901 J/K) = 27,11 °C ≈ 27 °C
 **Vastaus:** 27 °C
-**Järkevyys:** Veden lämpökapasiteetti on noin 7,5-kertainen, joten kauha jäähtyy noin 68 K mutta vesi lämpenee vain noin 9 K. Keskiarvo 56,5 °C olisi väärin.
+**Järkevyys:** Veden lämpökapasiteetti on noin 7,5-kertainen kauhan lämpökapasiteettiin verrattuna, joten kauha jäähtyy noin 68 K mutta vesi lämpenee vain noin 9 K. Keskiarvo 56,5 °C olisi väärin.
 
 ## fy3-6-L3-01
 **Annettu:** vesi c = 4190 J/(kg·K), m_v = 20 kg, 10 °C → 40 °C; kivet c = 800 J/(kg·K), 300 °C
```

## Checked
- Changed text read in full: lesson.md Ydinajatus, Kaava (ΔT definition, C = cm, solving for T, weighted mean), Esimerkki (3,7·10², 24,6 vs 24,5), Yleinen virhekäsitys (35 °C working), Tiivistelmä; no blocking language error
- New exercises L2-01 and L2-04 and their solutions: grammar, case endings (kiuluun, kg:aan, °C:seen, 80-asteista) and Finnish terms (kiulu, lahdelma, saavi) correct
- Solutions notation T_alku/T_loppu consistent; decimal comma, thin-space units, minus sign U+2212 correct everywhere
- glossary.json "tasapainolämpötila" entry and meta.json glossary list: Finnish correct, consistent with lämpötasapaino and lämpökapasiteetti
- sim.js strings (labels, readout, flow text, note, "Upota") and sim-spec.md: grammar fine, terminology matches the glossary
- exit-ticket.json: unchanged and correct
- lint_lesson.py fy3-6: 0 errors, 0 warnings (not repeated)
- Diff dry-run with patch -p1 applies cleanly; touches no number, formula or LaTeX
- Proofreader hash unchanged during review (3b97e896fb63eae2 at start and end)
