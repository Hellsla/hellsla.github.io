VERDICT: PASS
CONTENT-HASH: 23fcb0bdb4e00944

## Blocking

## Polish
- exit-ticket.json:8 — the model answer writes $x = x_0 + vt$, while lesson.md and inquiry.json use $s = s_0 + vt$ throughout (no $x_0$ anywhere in the lesson) — write $s = s_0 + vt = 4\,\text{m} + 3\,\text{m/s} \cdot 2\,\text{s} = 10\,\text{m}$ so the exit ticket uses the lesson's symbols.

## Checked
- delta review: new exit-ticket item (cart from $4\,\text{m}$ at $3\,\text{m/s}$), recomputed in python: $s(1\,\text{s}) = 7\,\text{m}$, $s(2\,\text{s}) = 10\,\text{m}$, not $14\,\text{m}$.
- distance covered $3\,\text{m} \to 6\,\text{m}$ doubles with time; position does not because $s_0 \ne 0$: matches the lesson's distinction between paikka and matka (glossary) and the direct-proportionality goal.
- the item targets the "position proportional to time" misconception; time counted from the start ("lähtee") makes $t = 2\,\text{s}$ unambiguous; units consistent.
