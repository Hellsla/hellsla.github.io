VERDICT: PASS
CONTENT-HASH: fda82020fb029110

Follow-up review of the fix commit 2c31ff041 (delta from ac40aeea284452d7). Changes: lesson.md:333 glosses "vakiojännitelähteestä eli lähteestä, jonka jännite pysyy samana"; inquiry.json:471 Etsi virhe feedback now starts "Kun tyhjä kondensaattori ladataan lähteellä, jonka jännite pysyy samana, lähde antaa energian $QU$."

## Blocking

## Polish

## Checked
- Both changes are physically right: the half holds for an empty capacitor and an ideal constant-voltage source, independent of $R$; the gloss defines the term correctly.
- Consistency: grep of "puolet"/"$QU$" — lesson.md:333 ("ei yleinen laki"), siirto hints, mistakes and solution (:490–507) and the Etsi virhe feedback say the same.
- Total charge: theory, misconception and Tiivistelmä agree ($+Q$, $-Q$, total zero, energy in the field).
- Dielectric table and reasons; polarisation mechanism checked.
- Plate formula conditions stated; $U_\text{max} = E_\text{max}d$, paper 160 V.
- Worked example: $W = 6{,}75\,\text{J}$, $P = 6{,}75\,\text{kW}$, $Q = 0{,}045\,\text{C}$, 3,4 s at 2 W.
- Sim numbers: $C = 88{,}5\,\text{pF}$; 44/89 nC, 11/44 µJ; glass 0,18 kV, 7,9 µJ; breakdown above 3 kV/mm; lesson-answers.py agrees.
- Kertaus 150 kV/m, Etsi virhe 0,034 J, transfer 190 µJ (mistakes 381, 0, 42,3), TV 12 J, exit 1,2 mC.
- Each choice has exactly one correct option; captions correct.
- Hash same at start and end.
