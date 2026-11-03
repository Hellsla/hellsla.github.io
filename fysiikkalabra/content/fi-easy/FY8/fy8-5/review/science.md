VERDICT: PASS
CONTENT-HASH: 774f10014b91374f

## Blocking

## Polish

## Checked
- The round-1 blocker is fixed at lesson.md:208. It now reads "Solmukohta on kohta, jossa kieli pysyy paikallaan" and "Kupukohta on kohta, jossa kieli värähtelee eniten". Both are correct definitions for a standing wave, and they agree with the figure text (one, two and three kupua).
- The round-1 polish point is fixed at lesson.md:1447, which now reads "$90\,\%$:n rajan ulkopuolelta".
- A script compared lesson.md, inquiry.json and exit-ticket.json with content/fi/FY8/fy8-5. Every $…$ formula and number is identical, and so is every non-string JSON value and id. The only formula change is a figure label (orbitaalissa → orbitaalilla).
- I read every sentence not in the source. The other glosses are correct:
  - kvantittuminen
  - kuori (same n)
  - alikuori (same shape)
  - pallosymmetrinen
  - amplitudi
  - perustila
  - histogrammi
  - odotusarvo
  - läpivalaisu
  - Pauli
  - elektronikonfiguraatio
- Conditions are kept: "Vetyatomissa" on more nodes giving higher energy (Ydinajatus, Tiivistelmä, tarkistus 2), "saman muotoisiin tiloihin", "likimain", "keskimäärin", "odotusarvo" and "ei mitata näin suoraan".
- Recomputed in one script: 656.47 nm, 10.2 eV and 2700. These match the text.
- lang/fi-easy.json sims/fy8-5 is the same as fi apart from the split legend sentence.
- Every choice item has exactly one correct option. The exit ticket is 1s² 2s² 2p³.
