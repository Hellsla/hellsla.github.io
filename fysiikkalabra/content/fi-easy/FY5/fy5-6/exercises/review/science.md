VERDICT: PASS
CONTENT-HASH: 2615e4af46870a85
SCOPE: delta added-exercise from 0be719f8b69971cc base 81db4a6fd727

## Blocking

## Polish

## Checked
- Hash oli sama alussa ja lopussa. Kierros 6: tarkistin kierroksen 5 korjaukset. Diffissä muuttuivat vain L1-11:n unit ja vihje sekä L1-10:n järkevyystarkistus.
- exercises.json:136 (L1-11): unit on nyt "m/s²". g = γM/r² = 1,448 m/s² → 1,45, kuten answers.py:ssä ja suomenkielisessä versiossa.
- L1-11:n vihje "Arvo on MAFY-taulukossa" on yksikössä. Haettava arvo on Kuun massa, 7,346·10²² kg VERIFIED-riviltä.
- L1-10: "alle tuhannesosa" on oikein, koska 5,93·10⁻³/9,81 = 6,0·10⁻⁴.
- Kaikkien tehtävien answer, unit ja tolerance ovat samat kuin suomenkielisessä versiossa. L1-10:n, L1-11:n ja L2-08:n luvut ovat samat.
