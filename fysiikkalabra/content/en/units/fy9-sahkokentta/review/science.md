VERDICT: FAIL
CONTENT-HASH: e1ef3a1aeef83571
SCOPE: delta (since PASS at 2099e517d51d3416: commit 6d9de17f9a, only the s4 b question in sovella/tasks.json)

## Blocking
- **s4 b, solutions.md: the solution now contradicts the new question and is wrong in its direction (A, internal consistency 6).** The new question asks "how short an air gap must be for breakdown to be certain". Under the uniform-field model the answer is "at most about $4\,\text{mm}$": every gap up to $d = U/E_\text{max}$ breaks down, so $4\,\text{mm}$ is the *longest* gap that certainly breaks down. The solution still says:
  - the **Find** line: "the smallest air gap that can break down";
  - the model answer: "With the uniform field model the smallest gap that breaks down is $d = \ldots \approx 4\,\text{mm}$".

  A shorter gap breaks down even more readily, so "smallest gap that breaks down" gives the wrong picture. It also no longer matches the question. Fix, for example:
  - Find: "why the angler can get a shock without touching the conductor, and how short an air gap breaks down for certain";
  - model answer: "With the uniform field model the gap breaks down whenever it is at most $d = \tfrac{U}{E_\text{max}} = \ldots \approx 4\,\text{mm}$."

  The Finnish solution has the same wording ("Tasaisen kentän mallilla pienin läpilyövä väli", line 374) and needs the same fix, which then carries into en and fi-easy.

## Polish
- The 12 kV is the RMS value. Its peak is about $16\,\text{kV}$, which in the uniform model gives about $5\,\text{mm}$. This makes "certain at ≤ 4 mm" conservative, which suits the wording, so no change is needed. A model answer could mention it in one clause.

## Checked
- `units.py hash fy9-sahkokentta --lang en`: e1ef3a1aeef83571 at the start and at the end.
- The diff since my PASS: `git show 6d9de17f9a`. In this unit only the text of s4 b changed. The rubric, solutions.md and answers.py are unchanged. The en question matches fi ("kuinka lyhyen ilmavälin yli läpilyönti tapahtuu varmasti").
- The new wording is physically right. It now asks for an upper bound on the gap, which is what $U/E_\text{max}$ gives. It also agrees with the `assumptions` criterion and the solution's remark that $4\,\text{mm}$ is a lower limit for the safety distance, since arcs can strike across longer gaps too. It agrees with the common mistake "4 mm presented as a safe distance" as well.
- The rubric for s4 b fits the new question. The math criterion ($12\,\text{kV}/3\,\text{MV/m} \approx 4\,\text{mm}$, not 20 kV), the concept criterion, `assumptions` and the transfer criterion each ask only what the task gives and asks. The points total 1+2+1+1 = 5.
- I recomputed:
  - $20\,\text{kV}/\sqrt3 = 11.5\,\text{kV} \approx 12\,\text{kV}$;
  - $d = 12\,\text{kV}/3\,\text{MV/m} = 4.0\,\text{mm}$ (11.5 kV gives 3.8 mm; the peak value gives 5.4 mm);
  - $I = 12\,\text{kV}/10\,\text{k}\Omega = 1.2\,\text{A}$.

  These agree with answers.py (`s4-gap-mm`, `s4-I-body`).
- Everything else carries over from my previous full PASS unchanged.
