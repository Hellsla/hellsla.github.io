VERDICT: PASS
CONTENT-HASH: 889350cdbeb1cd52
Delta review (aids paragraph, 2026-11-14) of the version passed at dffabae2d7e958c9.

## Blocking
None.

## Polish
None. (The sentence leaves out "fysiikan kokeessa"; the paragraph's first sentence already ties it to the real exam, so the meaning is the same.)

## Checked
- The one changed paragraph (Apuvälineet / Aids): "calculator" narrowed to the computer's calculator program, plus the new sentence that a separate calculator or a book of tables is not allowed. It agrees with YTL Reaaliaineiden kokeiden määräykset ja ohjeet §3 ("ei saa käyttää apuvälineinä erillisiä laskimia eikä erillisiä taulukkokirjoja"), source recorded in fi review/developer.md.
- No contradiction with the rest of the paragraph: "the exam's tables and formulas" are the digital materials inside the exam, not a separate book; the closing pointer to the Board's regulations is kept.
- No other place in the unit mentions a calculator or tables as an aid (grep).
- fi, en and fi-easy say the same thing.
- Hash checked at start and end with `python3 scripts/units.py hash fy9-harjoituskoe --lang fi-easy`.
