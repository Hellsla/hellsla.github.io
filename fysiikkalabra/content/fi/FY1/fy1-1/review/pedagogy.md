VERDICT: PASS
CONTENT-HASH: 3bed8018ff6ce0ef

## Blocking
(none)

## Polish
1. inquiry.json activity `pred-1` / `pred-2` prompts — "suuruusluokka" is used in the Ennusta stage before Teoria defines it, and `prior` does not list it. Fix: add a short clause to both prompts, e.g. "(yksi suuruusluokka = kymmenkertainen koko)", so the prediction is a real prediction and not a guess at the term.
2. inquiry.json `exp-2` — the question is a nesting multiple choice answerable from general knowledge, so it does not test pred-2 ("montako suuruusluokkaa") against the table the student recorded. Fix: ask a numeric "Neptunuksen radan ja Linnunradan n-arvojen erotus" (8) as exp-1 does, and keep the nesting choice as a second question or move it to the theory.
3. inquiry.json `kertaus` — "Mikä luku on $10^{-3}$?" is a generic item, not asked through the Pohdinta phenomenon (house rule from the 2026-11-13 read-through: the retrieval task belongs to its phenomenon). Fix: put it in the protoni/universe context, e.g. "Protonin koko on $1{,}7\cdot10^{-15}\,\text{m}$: mikä on $10^{-3}\,\text{m}$ jaettuna tuhannella?", or ask how many zeros follow the decimal comma.
4. Workload and repetition — the atom/proton gap (5 steps) is met four times: pred-1, exp-1, the ladder figure and the worked example (same pair, same result). The core path also holds three non-optional checks (`check-1` and `check-c2` test the same suuruusluokka skill) beside two transfer items, 20 exercises and five theory sections. Fix: give the worked example a different pair (e.g. Linnunrata and Aurinkokunta, or Maa and Aurinko) and make `check-c2` optional, so the core path keeps 1–2 checks.
5. Goal 1 (physics as a systematic, experiment-based science) rests on one theory paragraph, the optional `menetelmat` and exit-ticket question 2. No figure shows the cycle observation → model → prediction → test. Fix: add a small cycle figure under "Fysiikka rakentaa malleja ja testaa ne", and make `reflect` name the move "ennuste → mittaus → malli tukee tai ei" for pred-1 and pred-2.

## Checked
- Learning path: Pohdinta → 2 predictions → sim and 2 experiments → Teoria → reflect → example → transfer → checks is followable with only the prerequisites; the opening question is answered by the reflect ($42$ and $62$ steps) only after the student has predicted.
- Wrong-option feedback in pred-1, pred-2, `tunnista`, `vuorovaikutukset` and `virhe` repairs named misconceptions (atom drawn too large, difference read as ratio, gravity in the nucleus); right options name the evidence.
- Arithmetic verified: $1{,}1\cdot10^{-10}/1{,}7\cdot10^{-15}\approx6{,}5\cdot10^{4}$, $1{,}39\cdot10^{9}/2{,}4\cdot10^{4}\approx5{,}8\cdot10^{4}$, $4\cdot9{,}46\cdot10^{15}\approx3{,}8\cdot10^{16}\,\text{m}$, midpoint $-4$ (hius).
- Worked example has all seven stages, one step per stage, symbolic first; paragraphs under about 120 words; figures follow their paragraphs.
- Glossary terms (fysiikka, malli, kymmenpotenssi, suuruusluokka, valovuosi, atomiydin, perusvuorovaikutus) match their use in the text.
- Finnish: no case or glossary errors found ("$120\,\text{AU}$:n" correct); numbers with units are LaTeX.
- Captures: the exp-1 and sim screens at 390 px show nothing clipped; controls, readout and closed boxes (Käyttöohje, Mallin oletukset, Laskennan selitys) are understandable.
- Exercises were not judged (reviewed apart).
