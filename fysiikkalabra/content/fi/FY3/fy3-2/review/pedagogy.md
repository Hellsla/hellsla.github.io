VERDICT: PASS
CONTENT-HASH: 1600528fa2521d70

## Blocking

## Polish
- lesson.md (nosturin kuvateksti) — "kuorman potentiaalienergia kasvaa" on FY4-sisältöä (E_p kuuluu FY4:ään) — kirjoita "kuorman energia kasvaa".
- inquiry.json (pred-3, prompt ja palaute) — "Teoriatiivistelmän malliin/kuvaan" — vaihe on nimeltään Teoria; kirjoita "Teorian kuvaan".
- inquiry.json (simulaatio, `text`) — johtosana on yli 30 sanaa ja sisältää käyttöohjeen; jätä "Valitse voima, matka ja aika ja paina *Vedä*." ja siirrä loput Käyttöohjeeseen.
- inquiry.json — kolme ennustetta ja kaksi koetta ovat tunnin työmäärälle runsaasti; pred-1 on jo optional, harkitse pred-2:n merkitsemistä vain ydinpolkuun jos aika käy vähiin.
- sim (390 px) — lukema W = 600 J näkyy jo ennen *Vedä*-painallusta, joten ennusteen 1 vastaus on luettavissa liukusäätimiä siirtämällä; ei estä oppimista, koska ennuste on jo sitouduttu.

## Checked
- Polku: fy3-1:n G = mg ja kuvaajan luku → W = Fs → pinta-ala → teho; alun repun kantamisen kysymys vastataan pred-3:n ja Teorian kautta.
- Joulen koe on tutkittavana datana (interpret), mallin arvot ja mittaukset erotettu johtopäätöksessä.
- Kokeet lukitsevat oikeat muuttujat (F,t / F,s) ja pred-3 myöntää, ettei sim testaa kohtisuoraa voimaa.
- Esimerkki seitsemässä vaiheessa, kolmio-pinta-ala symbolisesti ensin, järkevyys keskiarvovoimalla.
- Tarkistuskysymykset: pinta-alasuhde, kohtisuora voima, kuvaajan luku, selitys havaittavin kriteerein; harhaoptiot aidot.
- Poissa FY4:n asiat (cos α, E_k, työ-energia-lause).
- Kuvat (carry-lift, joule, work-graphs, lift-work) tukevat kappaleita; puhelimessa sim ja syöttökentät käytettävissä.
