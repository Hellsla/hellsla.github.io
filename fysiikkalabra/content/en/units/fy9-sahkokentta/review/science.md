VERDICT: PASS
CONTENT-HASH: 12b4cb1f1fce7b8a
SCOPE: delta (since my FAIL at e1ef3a1aeef83571: commit 6b08a5f2cf, only s4 b in sovella/tasks.json and solutions.md)

## Blocking
None.

## Polish
- `sovella/review/packet-visual.md` (en and fi) still quotes the old "smallest air gap that can break down" wording. It is a generated packet, not content, so regenerating it before the next visual review is enough.
- Carried over: 12 kV is an RMS value. Its peak, about 16 kV, gives about 5 mm, so "certain up to about 4 mm" is on the conservative side. One clause could say this; it is optional.

## Checked
- `units.py hash fy9-sahkokentta --lang en` gave 12b4cb1f1fce7b8a at the start and at the end.
- I read the diff in `git show 6b08a5f2cf`. In en it changes only the s4 b task text, the `assumptions` detail, the solution's Find line and model answer, and one common-mistake line. The rubric's math, concept and transfer criteria and answers.py did not change.
- s4 b is now consistent everywhere (6, internal consistency):
  - Task: "Estimate up to what length of air gap breakdown is certain."
  - Find: "the longest air gap across which breakdown is certain".
  - Model answer: "the longest gap across which breakdown is certain is d = U/E_max ≈ 4 mm".
  - Rubric `assumptions` detail and the solution's next paragraph: "a lower limit for the safety distance, not a safe distance".
  - Common-mistake line: "only the gap across which breakdown is certain in the uniform field model".
  - All of these give one upper bound on the gap, which is the direction U/E_max gives. The "smallest gap" error from my FAIL is gone.
- Physics: under the uniform-field model, every gap d ≤ U/E_max breaks down, so 4 mm is the longest certain gap. Real conditions (strong field near a thin conductor and the rod tip, humidity, dirt, the fishing line) let an arc strike across longer gaps. The text says so, which is why 4 mm is presented as a lower limit for the safety distance. No A or B finding.
- Recomputed:
  - 20 kV/√3 = 11.5 kV, rounded to 12 kV;
  - 12 kV / 3 MV/m = 4.0 mm (11.5 kV gives 3.8 mm; the peak value gives 5.4 mm);
  - 12 kV / 10 kΩ = 1.2 A.

  These match answers.py (`s4-gap-mm`, `s4-I-body`). The math criterion still uses 12 kV, not 20 kV.
- s4 b points total 1+2+1+1 = 5, unchanged. Every criterion asks only what the task gives and asks.
- The en wording matches fi in tasks.json line 510 ("enintään kuinka pitkän ilmavälin yli läpilyönti tapahtuu varmasti") and in solutions.md lines 370, 374 and 397.
- Everything else carries over from my earlier full PASS, unchanged.
