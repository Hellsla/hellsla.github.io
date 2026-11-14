VERDICT: PASS
CONTENT-HASH: 90895d9429b95817
SCOPE: delta added-exercise from 628ca4af401209e3 base 81db4a6fd727

## Blocking

## Polish
- answers.py:3 (docstring) — teksti "Mars 3,71 m/s²" on eri arvo kuin L1-09:n MAFY-arvo 3,72 m/s². L2-04 käyttää omaa annettua arvoaan, joten tämä ei ole virhe.

## Checked
- Hash oli sama alussa ja lopussa. Arvioin vain tehtävät L1-09, L1-10 ja L2-09 (kierros 3).
- Kierroksen 2 blocking-havainto on korjattu: L2-09:n `"unit"` on nyt "m/s" (exercises.json:48), ja se vastaa kysymystä ja vastausta 0,47.
- L2-09: v_max = 2πA/T = 2π·0,030 m / 0,40 s = 0,471 m/s → 0,47 m/s. Lauseke johdetaan symbolisesti ehdoista ½mv² = ½kA² ja T = 2π√(m/k).
- L1-09: Marsin g = 3,72 m/s² on mafy-arvot.tsv:n VERIFIED-riviltä. T = 2π√(1,00/3,72) = 3,258 s → 3,26 s, ja toleranssi 4 % sopii.
- L1-10: E = ½·120·0,030² = 0,054 J.
- Kuvaaja-k on x = 3 cos(2πt/0,40) cm. Huiput ovat apuviivoilla, ja alt-tekstissä on samat arvot.
- Toistoa ei ole: inquiry-tarkistus kysyy samasta kuvasta jousivakion. L1-10 kysyy energiaa ja L2-09 nopeutta. L1-04 laskee energian annetusta amplitudista, mutta L1-10 lukee amplitudin kuvasta.
- Kaikkien kolmen tehtävän merkitsevät numerot vastaavat lähtötietoja, ja pyöristetyt vastaukset ovat toleranssin sisällä.
