VERDICT: FAIL
CONTENT-HASH: b8d7e629c4b251af

## Blocking
- lesson.md:161, 282; inquiry.json tarkistus-3 model — B: lämpöenergia ei "voi enää käyttää hyödyksi" / "ei voi kerätä takaisin" / "ei voi enää kerätä takaisin ja käyttää". Väite pätee vain, kun lämpö on hajaantunut ympäristön lämpötilaan; ympäristöön siirtyvä lämpö lämmittää esim. huoneen, ja yhteistuotannossa se otetaan talteen (itse L3-02-ratkaisu sanoo näin). Tarkistus-3:n kriteeri ja sanasto sanovat oikein "ei enää helposti hyödynnettävissä". Fix: korvaa kolme kohtaa sanoilla "ei ole enää helposti hyödynnettävissä".
- lesson.md:229 (kuva tikapuut, nimiö "omena 1 J") — B: energia-asteikolla nimiö lukee, että omenan energia on 1 J, mutta saman luvun tarkistus-2 antaa omenan energiaksi 300 kJ (ruoka). 1 J pätee vain omenan nostamiselle metrin (aria-label ja sim sanovat niin). Fix: nimiö "omena metrin ylös 1 J".

## Polish
- inquiry.json ennuste-1 / koe-1: ruoan 10 MJ on ravintoarvo (elimistön hyödynnettävä), bensiinin 32 MJ lämpöarvo (palamisessa vapautuva); ohjeistuksen mukainen yksi lause eron sanomiseksi sopisi koe-1:n intron.
- inquiry.json siirto solution: "kaikki tiedot tunnetaan gigajoulen tarkkuudella" on oletus (360 GJ voi olla kahdella numerolla); sano "oletetaan".
- lesson.md:103: tasaisella ajolla energia kuluu ilmanvastukseen ja vierintävastukseen, ei vain pysähtyessä; "pysähtyessä" voi jättää pois.

## Checked
- Recomputed all numbers in one script: 340 kJ, 600 kJ, 66 MJ, 51 GJ, 100, 7,3, 3,2; sun 1361 W/m2 · pi R2 · 3600 s = 6,25e20 J = 625 EJ vs 620 EJ (2023), 1000 h = 41 d.
- Joule/omena (0,1 kg · 9,81 · 1 m = 0,98 J), prefix ladder, figure sailyminen widths (24/72/96 = 200/600/800) and tikapuut positions (1,6 GJ, 140 TJ) are to scale.
- Predictions: exactly one correct option, distractor feedbacks right; experiments isolate "kohde", simState gives E_MJ and E_EJ.
- Sim values (AA 2,5 Ah·1,5 V = 14 kJ, U-235 8,2e13 J/kg, OL3 138 TJ/vrk, 28 objects) fit lesson; limits stated.
- Scope: no E_k/E_p expressions, no W=Fs, no chain-efficiency product. Exit ticket, example, ketju table consistent.
- Hash start = end.
