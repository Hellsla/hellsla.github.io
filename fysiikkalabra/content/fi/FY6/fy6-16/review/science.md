VERDICT: PASS
CONTENT-HASH: c1b357c0202a531a

## Blocking

## Polish
- content/fi/FY6/fy6-16/lesson.md:473 (Tiivistelmä, unchanged) — "lataus on pitkä suuri kuorma, ja ulkona kaapelin eriste voi vaurioitua" gives an outdoor-only reason for the RCD. Since tarkistus-1 now says the RCD protection is required indoors and outdoors, consider "jokaisella latauspisteellä on oma vikavirtasuojaus; ulkona eristeen vaurio on lisäksi todennäköisempi". It is not wrong as written; lesson.md:269 already says the RCD is the charging point's own.

## Checked
- inquiry.json:276 tarkistus-1, correct option: a long, high-power load needs its own dimensioned supply, and RCD protection is required for the charging point indoors and outdoors. Both are right (SFS 6000-7-722 requires each charging point to have its own residual-current protection, wherever it is).
- Feedback: the own group dimensions the wire and fuse for the long charging current, and the RCD trips when part of the current leaks to earth through a damaged cable and a person. Right, and it agrees with lesson.md:269.
- Still exactly one correct option. Both distractors are unchanged and still wrong: a group does not raise the charging power, and an RCD reacts to a leakage difference over 30 mA, not to load size.
- No numbers changed. The rest is unchanged since the last PASS (260d90edbd524cba).
- Hash identical at start and end.
