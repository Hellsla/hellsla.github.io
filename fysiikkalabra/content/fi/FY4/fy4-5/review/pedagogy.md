VERDICT: PASS
CONTENT-HASH: 0277f559f7d013b3

## Blocking

## Polish
- inquiry.json (siirto, palikka/vaaka -ratkaisu, voimakuvio) — labels $\overline{N}$ and $\overline{F}_y$ touch ("NF_y") because N starts near the body's right edge, where F_y's dashed component also stands. — Move N to the left on the base or shift the F label.
- inquiry.json (kyltti-ratkaisu) — the dashed $T_{1x}$ and $T_{2x}$ run along the body's top edge, so they read as part of the outline. — Lift the components a little above the edge or mark the body edge.
- inquiry.json sim "model" — the new sentence (T vs F with one symbol) is long and sits in a box that is already dense. — Split it in two: "Narun voimaa merkitään yleensä T:llä. Simulaatiossa sekä vetoa että työntöä merkitään F:llä, koska ne vaihtuvat."
- inquiry.json exp-1 solution, Vastaus — "Erotuksessa ratkaisee desimaalien määrä, ei merkitsevien numeroiden määrä" is more than a 17-year-old needs here. — Cut to the first two sentences.

## Checked
- Hook "vuorotellen" and the lesson.md "alustaansa" wording are clearer; the opening question still reads as one question and is not answered by the text.
- Added T/F symbol note is honest about the simulation's single symbol and consistent with the glossary (jännitysvoima T); it does not give away the exp-1 answer.
- Added voimakuvio blocks (exp-1, palikka, kala, kyltti) are placed after the Voimakuvio paragraph and before the Kaava, so each solution draws before it calculates; verified in rendered captures.
- Kala: T longer than G, a up beside the body in orange, not a force. Kyltti: T_1, T_2 distinct symbols, dashed components, G alone downwards.
- exp-1 diagram: N 146 N + F_y 50 N = G 196 N, a to the right; consistent with the table.
- The Vastaus rewrite (whole newtons, accuracy about 1 N) is correct and removes the previous odd significant-figure claim.
- Hash 0277f559f7d013b3 at start and end.
