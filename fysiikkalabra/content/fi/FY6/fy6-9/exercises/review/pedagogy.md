VERDICT: FAIL
CONTENT-HASH: 0fcb8d2cc4f7c3c6

## Blocking
- exercises.json fy6-9-L2-06 — the lead before the parts is one paragraph of about 47 words (situation, data and the student's calculation together), over the 45-word rule — add "\n\n" after "...pysyvät tässä mallissa vakioina." and put "Oppilas laskee: ..." (the claim) in its own paragraph. Parts a), b) and the answer-field line stay as they are.

## Polish
- fy6-9-L1-08 repeats the structure of L1-04 (t = Q : I) and differs only by the mAh conversion; consider a different context or ask for the time to reach a given share of the capacity.
- solutions.md fy6-9-L2-06 — the answer to a) (loss goes to resistances) sits only in Periaate; the Vastaus line states b) only. Add one sentence for a) to Vastaus.
- Plan docs/exercise-bank/FY6.md: the constant-current/constant-voltage graph task and the "higher charger voltage fills it faster" error task were replaced by L2-07 and L2-06; update the plan or add them later.
- Outside the Finnish set: the English translation of the untouched L2-01 (preview/en/fy6-9, state "open") overflows by 8 px at 360 px (inline "0.40\,\Omega"). This is the failing "layout 360 px" check; none of the new tasks is the cause.

## Checked
- All eight new tasks recomputed: L2-05 9,3225 Wh, L2-06 1,5 Wh, L2-07 0,40 Ω (fit gives 2,5 A/V), L3-04 77,45 % and R_s 0,10 Ω, L3-05 7,125 h and 6,0 h. Each answer matches its solution.
- Levels fit: L1-06..08 one step or concept, L2-05..07 data/error/experiment, L3-04..05 multi-part modelling and data interpretation in YO style.
- Concept tasks L1-06 and L1-07 have misconception-based distractors, each with its own feedback.
- Solutions follow the house stages; the physics in L3-04 c) (cut-off voltage reached sooner at high current, R_s I² loss) is explained.
- No duplicate of the worked example. Total 20 tasks (8/7/5).
- Only L2-06 has a lead over about 45 words; the other leads are 14–38 words and already have breaks where there are several paragraphs.
- Finnish and number+unit case forms (for example "$450\,\text{V}$:n") are fine in the new texts.
- Exercise captures at 1280 px are the only ones in the packet; the content hash is unchanged at the start and end.
