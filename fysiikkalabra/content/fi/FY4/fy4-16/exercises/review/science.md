VERDICT: PASS
CONTENT-HASH: ffcdfb1fd3bb1799

## Blocking

## Polish
- solutions.md:359 (L2-08) — "lähtökorkeusvaikuttaa" is missing a space, and two "joten" clauses run in a row. Fix: "…joten epävarmuusvälit ovat selvästi erillään. Lähtökorkeus siis vaikuttaa matkaan."
- exercises.json:347 (L2-08, correct feedback) — "kasvu on todellista" dropped the earlier "todennäköisesti". The guardrail says a true value lies in a range only *todennäköisesti*, and the solution itself calls Δx an estimate. With a difference of about 10 × 2Δx the claim is physically safe, but "kasvu on hyvin todennäköisesti todellista" keeps the wording the same everywhere.

## Checked
- Round 2: commit ea64e7381, checked against the regenerated packet. Read from the text only; nothing was rendered.
- The criterion is now 2Δx: two intervals $x \pm \Delta x$ overlap exactly when the difference is less than 2Δx. The criterion is applied consistently in the Periaate, the option 1 feedback, the correct feedback and the solution. Mass differences 0,7 m < 2,0 m (overlap); height differences 20,6 and 19,2 m ≫ 2,0 m.
- The stem now says "pelkän taulukon perusteella". Option 4 (80 m from 8,00 m, which the lesson's model $x = h/\mu$ predicts) is therefore rightly unsupported: it goes past the measured range, and its feedback says how far (twice the range) and which assumption it rests on (the same μ).
- The absolutes are removed from options 3 and 4. Option 3 ("massa ei vaikuta", from 0,7 m) is still wrong for the right reason (no difference shown is not equality, and an effect under 2 m would hide in the uncertainty). The correct option is not identifiable by length or hedging.
- Round-1 item fixed: "noin kaksikymmenkertaisia".
- Hash ffcdfb1fd3bb1799 at both start and end.
