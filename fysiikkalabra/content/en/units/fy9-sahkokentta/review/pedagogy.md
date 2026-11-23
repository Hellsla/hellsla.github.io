VERDICT: FAIL
CONTENT-HASH: e1ef3a1aeef83571

## Blocking
- s4 b: the prompt is now well-posed ("Estimate how short an air gap must be for breakdown to be certain" gives d <= U/E_max ~ 4 mm in the uniform-field model), but the rubric and the solution were not updated and now contradict it.
  - tasks.json s4 b `assumptions` detail: "The estimate is a lower limit ... an arc can strike across a clearly longer gap too". For the new question 4 mm is an upper limit for a gap that certainly breaks down, and a longer gap can still break down. "Lower limit" would teach students the opposite of what they computed.
  - solutions.md s4 b: **Find** still says "the smallest air gap that can break down". The model answer says "the smallest gap that breaks down is d = U/E_max". The estimate is called "a lower limit for the safety distance". The first two are the original ill-posed wording, and the third mixes two different quantities.
  - Yleisiä virheitä: "The 4 mm of part b is presented as a safe distance, although it is the lower limit of a uniform field". The fault it names is real, but "lower limit" is again the wrong term.
  - Fix: Find = "how short a gap breaks down certainly". Answer: "In a uniform field a gap of at most about 4 mm breaks down certainly. Near a thin conductor or the tip of the rod the field is stronger than U/d, and humid air and dirt weaken the insulation, so an arc can strike across a clearly longer gap too, so 4 mm is not a safe distance". Reword the criterion and the common mistake to match ("upper limit of the gap that certainly breaks down", not a safe distance).

## Polish
- s4 b criterion 4 says "a current of the order of amperes". The solution gives 1.2 A for an assumed 10 kOhm. The rubric could state that assumption.

## Checked
- practice.py check OK. Hash taken at the start.
- s4 a and c: well-posed, authentic, rubric points match the solution. The bird task corrects a real misconception (potential vs potential difference).
- s4 b: the prompt is consistent with its numbers (12 kV, 3 MV/m, 4 mm) and the first and fourth criteria. It is inconsistent with the `assumptions` detail and the solution (see Blocking).
- I did not re-read the other tasks (s1-s3, s5-s8) in detail. They were not changed since my earlier review, which did not flag them.
