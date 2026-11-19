# 8f: animaation jaetut primitiivit (demo)

Demo ei muuta yhtään sisältölukua: `demo.py` piirtää fy5-10/birth-kuvan aiheen (pulssi etenee narua, yksi merkitty kohta
vain nousee ja laskee) uusilla figlib-primitiiveillä. `demo.gif` ja `frames/` ovat 20 kuvaa yhdestä silmukasta,
`demo-still.svg` on sama kuva ilman animaatiota (still: pulssi juuri syntyneenä). Demon HTML näyttää LaTeX-tekstit raakana
(ei KaTeXia); sivulla ne piirtyvät kuten muissakin kuvissa.

Primitiivit (`scripts/figlib.py`, tarkistukset `scripts/test_figanim.py`): `motion` (yleinen), `oscillate` (siniliike,
aallon pisteet), `travel` (etenevä aalto/pulssi, leikkuuikkuna), `project` + `orbit` (kiertoliike ja sen projektio),
`drift` (suljettu seinäpomppurata, `bounce_speed`), `collide` (kahden kappaleen törmäys, `collision_frames`).
