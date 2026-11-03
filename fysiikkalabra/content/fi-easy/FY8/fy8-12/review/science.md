VERDICT: PASS
CONTENT-HASH: 64f08e977bf97066

## Blocking

## Polish
- lesson.md:269 — "Kantama tarkoittaa matkaa, jonka jälkeen hiukkanen pysähtyy varmasti" is acceptable (C); "matka, jonka jälkeen yksikään hiukkanen ei enää pääse läpi" would match the later sentence in Kaava exactly.
- lesson.md:368 — "Intensiteetti kertoo, kuinka paljon säteilyä tulee läpi tietyssä ajassa" is a fair simplification (C); "... tietyn pinnan läpi tietyssä ajassa" would be more exact.
- lesson.md (Yleinen virhekäsitys, "Steriloinnissa ja lääketieteessä") — same note as the Finnish review: true for sterilisation and diagnostics; 15–18 MV radiotherapy makes some photoneutrons. C at this level.

## Checked
- Every number in lesson.md, inquiry.json, exit-ticket.json and figures equals the Finnish original (the only extra digits are the ½ written as \tfrac{1}{2}).
- Recomputed: 1,6·10⁵ ion pairs; example 23,8 → 24 mm with the 6,25 % / 3,1 % brackets; Al 25 mm 0,60; apron 5,57 % and mistakes 84,7 / 94,4 / 12,0; check 2: 12 mm (400), 24 mm (200), 48 mm (50).
- Word-level diff against the Finnish original: the simplifications split sentences and add short definitions (positiivinen ioni, viritys, DNA, radikaali, kantama, intensiteetti, nettopulssimäärä); none changes a claim, condition or option.
- Predictions 1 and 2, Etsi virhe, concept check: exactly one correct option each; feedback and model values (5/550/577, 9/4/535, 590/332/175/89/57; net 586/328/171) unchanged.
- Model limitations kept (no alpha energy loss in air or window, no bremsstrahlung, ideal detection, no dead time); "Lukemat ovat mallin arvoja".
- Causality kept: dense alpha track → double-strand breaks; indirect effect via water radicals; neutron moderation by near-equal mass protons.
- Exit ticket answers say the same as the theory (single-photon energy; gamma does not activate; neutrons mainly do).
