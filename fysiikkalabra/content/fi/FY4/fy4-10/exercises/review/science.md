VERDICT: PASS
CONTENT-HASH: 58dc2743acb32b70
SCOPE: delta added-exercise from f73c86410af7bc40 base 81db4a6fd727
## Blocking

## Polish
- exercises/solutions.md fy4-10-L2-09 Järkevyys — tarkistus voisi todeta, että liike-energia pienenee ($0{,}184\,\text{J} \to 0{,}064\,\text{J}$), jolloin kuvaajan törmäys on fysikaalisesti mahdollinen. Huomio on siirtynyt edelliseltä kierrokselta.

## Checked
- `ex-vt-kaarryt` on muuttunut vain esitykseltään (`ticks_below=True`). Data, suorat, nimiöt ja kuvaus ovat ennallaan, ja nopeudet $0{,}8$, $-0{,}4$, $0{,}2$ ja $0{,}6\,\text{m/s}$ osuvat yhä $0{,}2\,\text{m/s}$:n ruutuviivoille.
- Laskin vastaukset uudelleen yhdessä skriptissä `python -I answers.py`:n rinnalla. L2-09 antaa $m_\text{B} = 0{,}50 \cdot 0{,}6 / 1{,}0 = 0{,}30\,\text{kg}$, L3-06 antaa $m_\text{B} = 0{,}60\,\text{kg}$ ja $\Delta E_\text{k} = 0{,}054 - 0{,}018 = 0{,}036\,\text{J}$. Molemmat täsmäävät exercises.json:n kanssa.
- L2-09: liikemäärä on $0{,}28\,\text{kg}\cdot\text{m/s}$ ennen ja jälkeen, ja liike-energia pienenee, joten kuvaaja on mahdollinen.
- L3-06: täysin kimmottomassa törmäyksessä levossa olevaan kohteeseen menetetty osuus on $m_\text{B}/(m_\text{A}+m_\text{B}) = 2/3$, mikä pitää paikkansa.
- Ehdot: kitka jätetään huomiotta, ja säilymislakia käytetään törmäyksen yli. Merkinnät ovat samat kuin luvussa.
- Hash 58dc2743acb32b70 sekä alussa että lopussa.
