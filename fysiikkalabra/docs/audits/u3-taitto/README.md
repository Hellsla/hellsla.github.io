# U3 Teorian taitto, vaihtoehto B (työjono 11 U3 ja 8e)

Ennen = `main` (e63b19cb), jälkeen = tämä haara. Kuvat: Teoria-vaihe (`#selita .act-theory`), `<sivu>-<leveys>-ennen|jalkeen.webp`;
fy3-8, fy4-3 ja fy1-1 leveyksillä 390, 1280, 1440 ja 1920 px. Valokuvat on ladattu ennen kuvaa.

Teoria-vaiheen korkeus (px):

| sivu | leveys | ennen | jälkeen |
|---|---|---|---|
| fy3-8 | 1280 / 1440 | 3567 | 3728 |
| fy3-8 | 1920 | 4176 | 4312 |
| fy4-3 | 1280 / 1440 | 3030 | 3217 |
| fy4-3 | 1920 | 3545 | 3765 |
| fy1-1 | 1280 / 1440 | 6259 | 6125 |
| fy1-1 | 1920 | 7203 | 7111 |

Sivu ei lyhene kaikilla: kun valokuva tulee kuvateksteineen tekstin viereen, rivin korkeus on kuvan korkeus (aiemmin kuva kelluisi
tyhjässä oikeassa reunassa ilman korkeutta, tai jäi vasempaan palstaan tekstin alle). Vastineeksi teksti on rivin yläreunassa, ei
tyhjää tilaa tekstin ylä- eikä alapuolella, ja kuva on aina viereisen kappaleen vieressä.

Muutokset: `scripts/build.py` (`fig_rows`: teksti ylös, kuvaa korkeampaa kuvaa varten sen alle seuraavat kappaleet `.fig-more`,
valokuva ja kuvateksti oikealle palstalle, `table_pairs`: kaksi pientä taulukkoa vierekkäin, työstetyn esimerkin vaiheissa kuva
aina tekstin alla), `templates/site.css`, `scripts/check_layout.py` (uusi tarkistus `figgap`), `scripts/test_fig_row.py`.
