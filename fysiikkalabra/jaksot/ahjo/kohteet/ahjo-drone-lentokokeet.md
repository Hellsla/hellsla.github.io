## Pikastartti

Lentokoe on mittaus, ei näytös. Päätät etukäteen, mitä mittaat ja miten, ja toistat lennon samalla tavalla niin monta kertaa, että näet tulosten vaihtelun.

1. Kirjoita mittaussääntö: mitä mitataan, mistä pisteestä ja millä välineellä.
2. Jaa roolit: lentäjä, tähystäjä tai turvavastaava ja kirjaaja.
3. Käy tarkistuslista läpi ja lennä.
4. Kirjaa tulos lentopöytäkirjaan heti lennon jälkeen.

### Kokeile

Tee kolme lyhyttä leijuntaa Air:bitillä ja kirjaa jokaisesta kesto ja ajautumisen suunta ja matka.

### Muokkaa

Muuta yhtä asiaa, esimerkiksi lentäjää tai akkua, ja toista sama koe. Pidä kaikki muu samana.

### Haasta itsesi

Suunnittele koe, jolla erotat toisistaan dronesta ja lentäjästä johtuvan ajautumisen.

## Haaste

Kaksi lentoa ei ole koskaan täsmälleen samanlaisia. Akku tyhjenee, ilma liikkuu ja lentäjä oppii. Siksi yksi lento ei todista mitään. Tavoite on mitata niin, että voit sanoa, johtuuko ero muutoksesta, jonka teit, vai tavallisesta vaihtelusta.

## Oppimistavoitteet

Työn jälkeen osaat

- kirjoittaa mittaussäännön ja noudattaa sitä
- toistaa mittauksen ja laskea keskiarvon ja vaihteluvälin
- muuttaa yhtä asiaa kerrallaan
- nimetä mittauksesi suurimmat virhelähteet.

## Lähtötaso ja ennakkotaidot

[Dronelabran turvallisuusperehdytys](ahjo-drone-perehdytys.html) on käyty ja opettaja on kuitannut sen.

## Laitteet ja materiaalit

| Tarvike | Mihin |
|---|---|
| Lentokuntoinen drone ja ohjain | Air:bit 2 tai kameradrone |
| Täyteen ladatut akut | Mittaussarja aloitetaan aina täydellä akulla |
| Maalarinteippi | Lähtöpiste, laskeutumismerkki ja lentoalue |
| Mittanauha ja sekuntikello | Etäisyydet ja ajat |
| Pehmeä alusta | Air:bitin lentoalueelle |
| Suojalasit | Lentoalueella oleville |
| Lentopöytäkirja | Saat pohjan tunnin sivulta |

## Turvallisuus ja perehdytys

Katso aiheet [lentoa edeltävä tarkastus](ahjo-turvallisuus.html#drone-tarkastus), [lentoalue ja roolit](ahjo-turvallisuus.html#drone-lentoalue) ja [hätäpysäytys](ahjo-turvallisuus.html#drone-hatapysaytys). Ne ovat valmisteilla, kunnes koulu on hyväksynyt ne.

- Tarkistuslista käydään läpi ennen jokaista mittaussarjaa.
- Air:bitillä lennetään matalalla: leijuntakorkeus on $10$–$30\,\text{cm}$. Dronessa ei ole korkeuden eikä paikan pitoa.
- Mittaus tehdään vasta, kun potkurit ovat pysähtyneet. Lentoalueelle ei mennä lennon aikana.
- Lento lopetetaan heti, kun akun varoitus tulee.
- Muutettu drone tai ohjelma testataan ensin ilman potkureita.

## Työvaiheet

### Air:bitin leijunta

1. Teippaa lattiaan lähtöpiste ja aseta drone siihen micro:bitin näyttö lentäjään päin.
2. Kytke akku ja odota, että drone on kalibroitunut. Älä liikuta sitä.
3. Käynnistä moottorit painamalla A ja B yhtä aikaa.
4. Lisää kaasua askel kerrallaan. Valmistajan mukaan drone nousee, kun kaasu on noin 50–60 prosenttia.
5. Kun drone alkaa nousta, pienennä kaasua hieman, jotta korkeus pysyy.
6. Leiju sovittu aika, esimerkiksi viisi sekuntia, ja laske kaasu alas.
7. Mittaa, kuinka kauas lähtöpisteestä drone laskeutui ja mihin suuntaan.

### Tarkkuuslaskeutuminen

1. Teippaa laskeutumismerkki ja lähtöpiste sovitun matkan päähän toisistaan.
2. Lennä lähtöpisteestä merkille ja laskeudu.
3. Mittaa etäisyys merkin keskipisteestä dronen keskikohtaan.
4. Toista vähintään viisi kertaa.

## Kuvat ja esimerkkikoodi

Lentopöytäkirjan rivi voi näyttää tältä. Luvut ovat keksitty esimerkki.

| Lento | Lentäjä | Akku | Kesto (s) | Ajautuminen (cm) | Suunta | Havainto |
|---|---|---|---|---|---|---|
| 1 | A | täysi | 5 | 40 | vasemmalle | nousi vinoon heti |
| 2 | A | täysi | 5 | 25 | vasemmalle | |
| 3 | A | käytetty | 5 | 55 | taakse | kaasua piti lisätä |

Keskiarvo lasketaan jakamalla tulosten summa niiden määrällä. Vaihteluväli on pienin ja suurin tulos.

## Testaa ja mittaa

Hyvä mittaussarja täyttää nämä ehdot:

- Jokainen lento on kirjattu, myös epäonnistunut.
- Sama henkilö mittaa samalla säännöllä.
- Sarjassa on vähintään kolme, mieluiten viisi toistoa.
- Vain yhtä asiaa on muutettu sarjojen välillä.
- Jokaisella luvulla on yksikkö.

Vertaa kahta sarjaa: jos keskiarvojen ero on pienempi kuin sarjan sisäinen vaihtelu, eroa ei voi pitää varmana.

## Jos jokin ei toimi

Ohjeet ovat valmistajan vianetsinnästä.

- **Moottorit pyörivät, mutta drone ei nouse:** tarkista, että jokaisessa moottorissa on oikeaan suuntaan pyörivä potkuri ja että akku on ladattu. Tarkista myös, ettei moottori ole vaurioitunut.
- **Drone kaatuu heti:** potkuri tai moottori on väärässä kulmassa. Vertaa osakarttaan.
- **Drone ajautuu aina samaan suuntaan:** irrota akku, aseta drone tasaiselle alustalle ja käynnistä uudelleen, jotta se kalibroituu. Tarkista, että potkurit ovat ehjät ja akku on keskellä.
- **Tulokset vaihtelevat paljon:** lyhennä leijunta-aikaa, käytä täyttä akkua ja pidä lentäjä samana.

## Jatkotehtävä

Kuvaa leijunta ylhäältä tai sivusta paikallaan pysyvällä kameralla ja mittaa ajautuminen videolta ohjeen [Videoanalyysi](tvt-videoanalyysi.html) avulla. Saatko saman tuloksen kuin mittanauhalla?

## Dokumentoi

Liitä projektipäiväkirjaan

- mittaussääntö ja koejärjestelyn piirros
- lentopöytäkirja
- keskiarvot ja vaihteluvälit
- suurin virhelähde ja ehdotus sen pienentämiseksi.

## Opettajalle: valmistelu

- Rajaa lentoalue ja varaa pehmeä alusta. Valmistajan mukaan korkeaa tilaa ei tarvita, ja matto on kovaa lattiaa parempi.
- Päätä lentovuorojen pituus ja kiertojärjestys. Yhdellä lentoalueella lentää yksi drone kerrallaan. Muut ryhmät toimivat kirjaajina tai käsittelevät dataa.
- Akun lataus kestää valmistajan mukaan noin tunnin. Lentoaikaa minuutteina valmistaja ei ilmoita, joten mittaa se itse ennen tuntia ja mitoita vuorot sen mukaan.
- Valmistajan ohjeessa ei ole ajautumisen korjaamiseen muuta keinoa kuin kalibrointi tasaisella alustalla.
- Hätäpysäytys on ohjaimen ravistus. Valmistaja varoittaa käyttämästä sitä yli kahden metrin korkeudesta, koska drone putoaa.
