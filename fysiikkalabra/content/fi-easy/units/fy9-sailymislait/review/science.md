VERDICT: PASS
CONTENT-HASH: c1b7d026abcd2b8a

Science review of the Selkeä suomi translation of fy9-sailymislait (source content/fi/units/fy9-sailymislait/, reviewed PASS at c2716084d9c1d0b9, still current). Reviewer 2026-11-04.

Checks: `check_i18n.py` fi-easy 0 errors; `practice.py check` OK (6 tasks, 95 points, same as fi). A script compared every `$…$` formula and every bare number in unit.md, teacher.md and sovella/solutions.md with the source: none missing and none added, and the heading count is the same. All JSON values that are not text (answers, tolerances, correct flags, points, criteria keys, ids) are identical. I read every changed string in inquiry.json, exit-ticket.json and tasks.json beside the Finnish one. No sentence changes the physics, a condition or a direction of reasoning. The rewordings keep the conditions: impulse "niin pieni, ettei sillä ole merkitystä", "kun vain paino tekee työtä", nimellisteho, and the constant-deceleration assumption. figures.json keeps every number with a decimal comma.

## Blocking
None.

## Polish
1. unit.json key_concepts, "liikemäärä": "Törmäyksessä kokonaisliikemäärä säilyy" leaves out the condition. The unit names this exact mistake ("Liikemäärän säilymistä käytetään ilman ehtoa", Yleisiä virheitä). Fix: "Kun ulkoisten voimien impulssi on törmäyksen aikana pieni, kokonaisliikemäärä säilyy eli pysyy samana." That is still under 25 words.
2. sovella/tasks.json s6 d), criteria[3] detail: "osa energiasta muuttuu ääneksi ja järkäleen energiaksi" is vague and does not match solutions.md ("järkäleen sisäenergiaksi"). Fix: "järkäleen sisäenergiaksi".
3. teacher.md, 15–25 min ("liike-energiasta katoaa lähes osuus"), and solutions.md s5 b) ("katosi noin puolet liike-energiasta"): energy does not disappear. For S2 readers, write "muuttuu muiksi energiamuodoiksi". The Finnish source has the same wording, so this is optional.
