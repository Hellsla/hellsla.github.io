VERDICT: PASS
CONTENT-HASH: bda32f11d42469e5

## Blocking
(none)

## Polish
- lesson.md:14 — aria-label of the Ydinajatus figure says "Kaavakuva", but it is not in Kaava — "Havainnekuva".
- lesson.md:72 — aria-label sentence "Kun hiukkasia on kaksi kertaa enemmän, kun … , paine on 2p" is hard to follow — rewritten (diff).
- lesson.md:212 — "puolet pienempi tilavuus" is not idiomatic Finnish, and "tai … tai" is ambiguous — "paine kaksinkertaistuu, kun … tai kun tilavuus puolittuu".
- solutions.md:63 — "pienenee 17-osaan" is clumsy — "on noin 17 kertaa pienempi ja paine 46 kertaa suurempi".
- solutions.md:39 — "Huoneen paineessa ja lämpötilassa" — "Huoneenlämmössä ja normaalipaineessa".

## Diff
```diff
--- a/lesson.md
+++ b/lesson.md
@@ -11,7 +11,7 @@
 
 Mittauksissa havaitaan, että pV/(nT) on kaikille kaasuille sama luku, kun paine ei ole kovin suuri eikä lämpötila kovin matala. Se on moolinen kaasuvakio R = 8,31 J/(mol·K). Siitä saadaan ideaalikaasun tilanyhtälö pV = nRT, joka sitoo yhteen kaasun neljä tilaa kuvaavaa suuretta. Kaasun laatu ei näy yhtälössä lainkaan. Samassa paineessa ja lämpötilassa yhtä suuressa tilavuudessa on siis aina yhtä monta moolia kaasua, olipa kaasu heliumia tai ilmaa. Tämä vastaa alun kysymykseen: pallot sisältävät yhtä monta hiukkasta, mutta heliumhiukkaset ovat paljon kevyempiä.
 
-<svg viewBox="0 0 600 300" role="img" aria-label="Kaavakuva: kaksi yhtä suurta palloa samassa paineessa ja lämpötilassa. Kummassakin on yhtä monta hiukkasta ja 0,21 mol kaasua. Heliumpallon kaasun massa on 0,83 g ja ilmapallon 6,0 g, koska ilman hiukkaset ovat raskaampia." style="max-width:100%;font-family:system-ui,sans-serif;font-size:24px">
+<svg viewBox="0 0 600 300" role="img" aria-label="Havainnekuva: kaksi yhtä suurta palloa samassa paineessa ja lämpötilassa. Kummassakin on yhtä monta hiukkasta ja 0,21 mol kaasua. Heliumpallon kaasun massa on 0,83 g ja ilmapallon 6,0 g, koska ilman hiukkaset ovat raskaampia." style="max-width:100%;font-family:system-ui,sans-serif;font-size:24px">
   <ellipse cx="150" cy="110" rx="100" ry="98" fill="currentColor" fill-opacity="0.08" stroke="currentColor" stroke-width="3"/>
   <polygon points="141,218 159,218 150,206" fill="currentColor"/>
   <line x1="150" y1="218" x2="150" y2="232" stroke="currentColor" stroke-width="2"/>
@@ -69,7 +69,7 @@
 
 Kun tilanyhtälö ratkaistaan paineen suhteen, nähdään, että paine kaksinkertaistuu, kun hiukkasten lukumäärä tai kelvinlämpötila kaksinkertaistuu tai kun tilavuus puolittuu. Paine on siis suoraan verrannollinen hiukkasten lukumäärään ja kelvinlämpötilaan ja kääntäen verrannollinen tilavuuteen, eli $p \propto NT/V$.
 
-<svg viewBox="0 0 600 300" role="img" aria-label="Kaavakuva neljästä kaasuastiasta. Vasemmalta: lähtötila, jossa paine on p. Kun hiukkasia on kaksi kertaa enemmän, kun kelvinlämpötila on kaksinkertainen eli hiukkaset liikkuvat nopeammin tai kun tilavuus on puolet, paine on 2p." style="max-width:100%;font-family:system-ui,sans-serif;font-size:24px">
+<svg viewBox="0 0 600 300" role="img" aria-label="Kaavakuva neljästä kaasuastiasta. Vasemmalta oikealle: lähtötilassa paine on p. Paine on 2p, kun hiukkasia on kaksi kertaa enemmän, kun kelvinlämpötila on kaksinkertainen eli hiukkaset liikkuvat nopeammin tai kun tilavuus on puolet." style="max-width:100%;font-family:system-ui,sans-serif;font-size:24px">
   <rect x="15" y="20" width="120" height="155" fill="currentColor" fill-opacity="0.08" stroke="currentColor" stroke-width="3"/>
   <line x1="40" y1="50" x2="53" y2="56" stroke="currentColor" stroke-width="2"/>
   <circle cx="40" cy="50" r="6" fill="currentColor"/>
@@ -209,7 +209,7 @@
 ## Tiivistelmä
 - Ideaalikaasun tilanyhtälö on $pV = nRT$, missä $R = 8{,}31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}}$ ja T on kelvineinä.
 - Ainemäärä n kertoo kaasun määrän mooleina, ja $n = m/M$. Hiukkasten lukumäärä on $N = nN_\text{A}$.
-- Paine on verrannollinen lausekkeeseen NT/V: kaksinkertainen hiukkasmäärä tai kelvinlämpötila tai puolet pienempi tilavuus kaksinkertaistaa paineen.
+- Paine on verrannollinen lausekkeeseen NT/V: paine kaksinkertaistuu, kun hiukkasmäärä tai kelvinlämpötila kaksinkertaistuu tai kun tilavuus puolittuu.
 - Kun kaasun määrä pysyy samana, $p_1V_1/T_1 = p_2V_2/T_2$, ja siitä saadaan erilliset kaasulait.
 - Samassa paineessa, lämpötilassa ja tilavuudessa on aina yhtä monta moolia kaasua, kaasun laadusta riippumatta.
 - Ideaalikaasumalli toimii hyvin tavallisissa oloissa ja pettää suurissa paineissa ja matalissa lämpötiloissa.
--- a/solutions.md
+++ b/solutions.md
@@ -36,7 +36,7 @@
 **Kaava:** n = m / M
 **Sijoitus:** n = 425 g / 44 g/mol = 9,659 mol ≈ 9,7 mol
 **Vastaus:** 9,7 mol
-**Järkevyys:** Grammat supistuvat, joten yksiköksi jää mooli. Pullossa hiilidioksidi on suuren paineen vuoksi osittain nesteenä, mutta ainemäärä kertoo molekyylien määrän olomuodosta riippumatta. Huoneen paineessa ja lämpötilassa kaasu veisi noin 9,7 · 24 l ≈ 230 l.
+**Järkevyys:** Grammat supistuvat, joten yksiköksi jää mooli. Pullossa hiilidioksidi on suuren paineen vuoksi osittain nesteenä, mutta ainemäärä kertoo molekyylien määrän olomuodosta riippumatta. Huoneenlämmössä ja normaalipaineessa kaasu veisi noin 9,7 · 24 l ≈ 230 l.
 
 ## fy3-10-L2-01
 **Annettu:** V = 10,0 l = 0,0100 m³, m = 2,40 kg, θ = 15 °C, M = 32,0 g/mol = 0,0320 kg/mol
@@ -60,7 +60,7 @@
 **Kaava:** p₁V₁/T₁ = p₂V₂/T₂, josta T₂ = T₁ · p₂V₂ / (p₁V₁)
 **Sijoitus:** T₁ = 303,15 K. T₂ = 303,15 K · 4600 kPa · 0,0300 l / (101 kPa · 0,500 l) = 828,4 K. θ₂ = 828,4 − 273,15 = 555,3 °C ≈ 555 °C
 **Vastaus:** 555 °C. Polttoaine syttyy, koska 555 °C on paljon yli 250 °C.
-**Järkevyys:** Tilavuus pienenee 17-osaan ja paine kasvaa 46-kertaiseksi, joten pV kasvaa 2,7-kertaiseksi ja kelvinlämpötila samoin. Siksi dieselmoottori ei tarvitse sytytystulppaa. Yksiköitä ei muuteta perusyksiköiksi, koska ne supistuvat suhteessa.
+**Järkevyys:** Tilavuus on noin 17 kertaa pienempi ja paine 46 kertaa suurempi, joten pV kasvaa 2,7-kertaiseksi ja kelvinlämpötila samoin. Siksi dieselmoottori ei tarvitse sytytystulppaa. Yksiköitä ei muuteta perusyksiköiksi, koska ne supistuvat suhteessa.
 
 ## fy3-10-L2-04
 **Annettu:** n = 1,00 mol, θ = −30 °C, p = 102 kPa = 102 000 Pa, R = 8,31 J/(mol·K)
```

## Checked
- Lint clean (0 errors, 0 warnings); not repeated. No stage markers (`<!-- vaihe -->`), LaTeX, numbers or JSON values touched by the diff.
- New text read in full: Ydinajatus paragraphs, both figure aria-labels and labels (helium, ilma, alku, 2N, 2T, V/2), Kaava (N = n N_A, p ∝ NT/V), five stages of the example, the three misconception bullets, the summary.
- Misconception bullets, staged example lead-ins (Tunnetut ja kysytty, Kaava ratkaistuna, Sijoitus, Tulos, Järkevyys) and symbolic Kaava lines in solutions.md read correctly; reversed L2-01 and L3-02 are clear Finnish.
- Glossary terms (ideaalikaasu, tilanyhtälö, ainemäärä, mooli, moolinen kaasuvakio, moolimassa, Avogadron vakio, yhdistetty kaasulaki, ylipaine, ilmanpaine, kelvin) used consistently and match definitions.
- Case after number plus unit (37 °C:n, 250 °C:n, 101 kPa:n, 20 °C:n, 20 °C:n huoneilmassa) correct; no "80 N voimalla" pattern; decimal comma, thin-space style, minus U+2212 in Finnish text.
- sim.js strings (hidas, nopea, osuma seinään, mitattu/ennuste, V = … %, Nollaa mittaus, readout lines, note paragraph) and sim-spec.md agree and are grammatical; fi() gives comma and U+2212; Finnish quotes ”…” in sim-spec.
- exercises.json texts and exit-ticket.json: grammar and terminology fine; no changes needed.
- Reading level suits 16 to 19-year-olds; paragraphs short.
