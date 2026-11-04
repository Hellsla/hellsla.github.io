VERDICT: PASS
CONTENT-HASH: 8a49e138f41872b8

## Blocking

## Polish
- inquiry.json:177 (johtopaatos prompt) — "miksi sama sulake ei suojaa ihmistä?" still uses the absolute wording. The model answer qualifies it correctly, but the prompt could read "miksi sama sulake ei huomaa ihmisen kautta kulkevaa virtaa?".
- fy6-16 lesson.md:265 (other chapter) — "suojausluokitus, esimerkiksi IP54" still conflicts with this chapter's glossary *suojausluokitus* (classes I–III). IP is the kotelointiluokka.

## Checked
- Round-1 blocking 1 is resolved. lesson.md:355, Yleinen virhekäsitys, the ennuste-1 feedbacks, the johtopaatos model answer and its criterion, and glossary *sulake* now say the same thing: the fuse misses the current through a person and protects a person only together with protective earthing, during an earth fault. This is consistent with tarkistus-3 and glossary *maadoitus*.
- Round-1 blocking 2 is resolved. lesson.md:227 and glossary *maadoitus* now say "uusissa asennuksissa" and warn that a colour does not show that a conductor is dead.
- Round-1 blocking 3 is resolved. lesson.md:477 and the iho text and its Järkevyys now give the conditions for the shoe result (intact and dry, dry floor, no other earthed contact) and say that shoes are no protection.
- All round-1 polish is resolved: fuse sized to the wire (now agrees with fy6-16:185), the class III 120 V DC limit, the overload trip timing in the example, and the maadoitus aria-label.
- The vaikutukset figure labels (10 mA ote ei irtoa, 30 mA hengitys vaikeutuu) now match the table, and the 0,5 / 10 / 30 / >50 mA thresholds agree with IEC 60479-1.
- The example's 19,6 A row (4500 W : 230 V) is correct, and its rounding to 20 A is justified.
- The hook edit drops the "vuorotellen" sentence, and this gives away nothing new.
- The diff introduces no new numeric or physics errors. All other lesson and inquiry numbers are unchanged from round 1 and were verified there.
