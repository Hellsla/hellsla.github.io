VERDICT: PASS
CONTENT-HASH: fc1b77921967a9ae
SCOPE: delta: round 2, the fixes of round 1 in fy9-kokeellisuus-s7 and -s8; the intro and older tasks s1-s6 untouched
Round 2: delta against the version round 1 reviewed (fix round 1).

## Blocking
- (none)

## Polish
- (none of substance). The s8 c Principle sentence "kutsutaan systemaattiseksi" from fi does not occur in this text.

## Checked
- Round 1 Blocking 1 (s8 b heating as a cause of nonlinearity) is fixed in the S2 text. Criterion 3 now reads "tulos on ekstrapolointia ... Käämin ja virtalähteen on kestettävä tällainen virta. Tulos on vain arvio, ja se pitää tarkistaa mittaamalla". Järkevyys says "Mallin $B = \mu_0 n I$ mukaan riippuvuus pysyy suorana, mutta sitä ei ole mitattu tällä alueella", and "ekstrapolointi" is explained as "arvio mittausalueen ulkopuolelle", which helps an S2 reader.
- Round 1 Blocking 2 is fixed: the "$12 : 6{,}2 \cdot 2{,}5\,\text{A}$" item is gone. The b mistake is now $I = kB$ or no reliability assessment.
- Round 1 Polish is done. s8 d (model answer and criterion 3) names the drift: of the current under a voltage-set supply, or of the sensor with temperature. s8 a Vastaus says "kaksinumeroisia". In s7 a the scale error clause has also been added ("Väärä asteikko eli kalibrointi antaisi silti suoran origon kautta"), which is correct.
- Rounding is the same as in fi and matches the data: s7 c $14\,\%$, s8 c $3\,\%$ and $0{,}6\,\%$ with the reason, b $4{,}9\,\text{A}$. The tolerances are the same as in fi. The decimal comma is used, units are language-neutral, and the chains are aligned rows.
- The numbers were recomputed in the same script as fi: s7 0,2152 ± 0,005, c 0,24 / 0,21 / 14,3 %, d 4,5 % and 0,93 %; s8 2,467 mT/A, 1963 1/m, 4,86 A, 3,08 % and 0,645 %. All agree. Points are still 14 + 14, and the intro "Kahdeksan tehtävää" matches the 8 tasks.
- Packet rebuilt (fixed text present), `practice.py check: OK`; the hash is the same at start and end.
