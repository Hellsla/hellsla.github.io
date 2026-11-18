VERDICT: PASS
CONTENT-HASH: 850efb4c05608c1f

## Blocking

## Polish
- exercises.json:214 (L2-06, the feedback on the wrong option "muuttuu solmuviivoilla lämmöksi"): "Solmuviivoilla ei synny tavallista enempää lämpöä" is not a P1 phrase (`lämmöksi`) and the physics is right. To match the corrected model answer it could say "sisäenergiaa" instead of "lämpöä". The option's own wording stays, because a wrong option keeps its words.

## Checked
- Hash 850efb4c05608c1f at the start and at the end (`--exercises --lang fi-easy`). It matches the packet. Delta review, round 1.
- solutions.md:157 (L2-06): "Energia ei muutu solmuviivoilla sisäenergiaksi" is correct physics. Destructive interference redistributes energy and converts none of it. Ordinary absorption in air happens everywhere and is not a nodal-line effect, so this is a fair simplification (C). The sentence follows the P1 guardrail and no longer uses "lämmöksi".
- The sentence agrees with the task's correct option and with the feedback on all three distractors (no conversion to internal energy, no return of energy to the speakers, speaker power unchanged). It also agrees with the brief's lesson sentence "Heikentävä interferenssi ei hävitä energiaa".
- The only "lämmöksi" left in the set is exercises.json:213. That is a wrong option and keeps its words on purpose. Exactly one option of L2-06 is correct.
- Every other hunk of the diff (L1-03, L1-0x hiljaiset kohdat, the aallonmurtaja task, L2-05, L3 vastamelu, L3 kaiutinaineisto, L2-10 a and d) only splits a paragraph in two. The words, numbers, symbols and units are unchanged, and the order of the reasoning steps is kept. My previous PASS of these solutions still holds.
- No answers.py, answer, unit or tolerance changed, so there was nothing new to recompute.
