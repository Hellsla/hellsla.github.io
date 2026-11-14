VERDICT: PASS
CONTENT-HASH: 8701713dc6e7b8e3

## Blocking
None. The changed text is correct, followable and does not disclose the answer before the student acts.

## Polish
1. lesson.md line 3 — "perinteisen ketjuhissillä toimivan" is clumsy and "ketjuhissillä" is not a natural case form; better: "perinteisen ketjuhissillä varustetun vuoristoradan" (same in inquiry.json explain prompt).
2. lesson.md line 3 — the hook "jos junalle ei anneta myöhemmin lisää energiaa" already hints that energy is the key; acceptable for a Miksi question that the student has not yet resolved, but "Miksi ... ensimmäinen mäki on yleensä korkein?" alone would leave more to the student's prediction.
3. Earlier polish (E_mek0 = E_p0 + E_k0 beside the E_mek definition; "tässä W ei sisällä painon työtä") still open, not part of this diff.

## Checked
- Miksi question: the chain-lift qualification fixes the earlier overgeneralisation ("aina"); still answerable with the prerequisite (fy4-7) and the lesson's goals.
- Explain prompt in inquiry.json: matches the lesson's Miksi; criteria (ketjuhissin työ antaa energian, kitka ja ilmanvastus vievät sen sisäenergiaksi) still assess exactly what the prompt asks.
- "negatiivinen, kun ne vastustavat liikettä": physically and pedagogically better than "aina"; consistent with the sentence about reversal of motion and with the ei-konservatiivinen voima glossary entry.
- Context sentence flow (siirtymä vs. matka, then friction, then "Kummassakin tapauksessa") remains coherent.
- Hash unchanged at start and end.
