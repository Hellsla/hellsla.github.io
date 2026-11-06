VERDICT: PASS
CONTENT-HASH: 32e78172ab301d83

## Blocking

## Polish
- solutions.md:163 (L1-09) — the inline checks $v_1 = 2\pi\cdot 1{,}2\,\text{m}\cdot 0{,}267\,\tfrac{1}{\text{s}} \approx 2{,}0\,\text{m/s}$ and the same for $v_2$ come to about 280 px by a text estimate, which is borderline. Visual reviewers should measure; if they are too wide, split them at "≈".

## Checked
- Diff against HEAD~1: only L1-09 (type 6, Ennuste muutoksesta) is new. The large diff of exercises.json is reformatting only (the JSON parses to the same tasks).
- answers.py run once; all numeric answers recomputed and inside tolerance.
- L1-09 physics: $v = 2\pi r f$; $r$ is multiplied by 2 and $f$ by 0,5, so $v$ is unchanged. Recomputed: $v_1 = v_2 = 2{,}01\,\text{m/s}$. The note that the unit of $f$ cancels in a ratio is right.
- Distractors match the dependences read wrongly: only $r$ (×2), only $f$ as if all points of the carousel had one speed (÷2, the chapter's own point), and $v \propto T$ (×4). Each feedback gives the right reason.
- The correct option is not identifiable by form; every option is a short sentence with a factor. Its feedback gives only the product $rf$.
- Example values (radius 2,4 m, 16 and 8 rpm) are realistic. No angular quantities are used, as the scope note requires.
