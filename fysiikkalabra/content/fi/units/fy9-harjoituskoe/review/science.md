VERDICT: PASS
CONTENT-HASH: 1c760d7d1d71cc80
Delta review (aids paragraph, 2026-11-14) of the version passed at c47364fb7325d02e.

## Blocking
None.

## Polish
None.

## Checked
- The one changed paragraph (Apuvälineet / Aids): "calculator" narrowed to the computer's calculator program, plus the new sentence that a separate calculator or a book of tables is not allowed. It agrees with YTL Reaaliaineiden kokeiden määräykset ja ohjeet §3 ("ei saa käyttää apuvälineinä erillisiä laskimia eikä erillisiä taulukkokirjoja"), source recorded in fi review/developer.md.
- No contradiction with the rest of the paragraph: "the exam's tables and formulas" are the digital materials inside the exam, not a separate book; the closing pointer to the Board's regulations is kept.
- No other place in the unit mentions a calculator or tables as an aid (grep).
- fi, en and fi-easy say the same thing.
- Hash checked at start and end with `python3 scripts/units.py hash fy9-harjoituskoe --lang fi`.
