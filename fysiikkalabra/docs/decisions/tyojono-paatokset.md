# Työjonosta kirjatut päätökset

Siirretty `tyojono.md`:stä (työjono 0b, 2026-11-17) sellaisenaan. Päätökset ovat voimassa. Niiden sääntöosat ovat myös `fysiikkalabra/CLAUDE.md`:ssä tai `.claude/commands/lesson.md`:ssä.


Opettaja vertasi kolmea vaihtoehtoa 14.11. ja valitsi B:n: nykyinen 38 rem:n palsta säilyy, ja asettelu korjataan
kohdan 8e mukaan (kohta 11, U3). Entinen kohta 7 (keskitetty tekstiraita ja marginaaliraita) poistettiin jonosta.
Perustelu: marginaaliin mahtuva kuva olisi noin neljänneksen pienempi, ja Teoria olisi ainoa keskitetty vaihe.

## luvut ilman käsitekortteja (opettaja 2026-11-13)

Luvut fy3-13, fy3-14, fy3-16 ja fy4-16 jäävät ilman omia kortteja ja alleviivauksia (#526:n siirtojen jälkeen).
Kortteja ei lisätä niihin.

## mallit takaisin alkuperäisiin (opettaja 2026-11-16)

Opettaja 16.11: "Palaa alkuperäiseen" (tokenit loppumassa). #620 (kaikki roolit Fable, 15.11) on peruttu: agentit ja
komennot ajetaan taas `/lesson`-komennon mallitaulukon mukaan (Sonnet, tiedekatselmointi Opus), ja Fable vaatii
opettajan sanan.

## kevyempi katselmointi, viisi rinnakkain (opettaja 2026-11-16)

Opettaja 16.11 (tokenien säästämiseksi): "jos pyöristyskorjaus niin ei tarvitse täyttä katselmointia", "Rajoitetaan
rinnakkaisuus viiteen", "Ei uusia täysiä kierroksia hiontahuomioista".
- Muuttunut luku, kaava, symboli, yksikkö, vastaus, toleranssi tai `answers.py` vaatii tiedekatselmoijalta deltan, ei
  täyttä katselmointia (`reviews.py` RULES `numbers`, `answers`): se katsoo muuttuneet rivit asiayhteydessään ja
  tarkistaa niiden laskut. Uusi tehtävä tai uusi sisältö ja simulaation koodi katselmoidaan kuten ennen.
- Rinnakkain enintään viisi työntekijää (juuren `CLAUDE.md` sääntö 3).
- Polish-huomioista ei ajeta uutta katselmointikierrosta: ne kirjataan PR:ään, ja vain Blocking- ja Major-huomiot
  korjataan ja katselmoidaan uudelleen.
