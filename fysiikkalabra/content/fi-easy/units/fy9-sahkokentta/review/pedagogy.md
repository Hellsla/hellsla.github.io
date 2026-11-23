VERDICT: FAIL
CONTENT-HASH: debd72cf8d478220

## Blocking
- s4 b: the task text was fixed but solutions.md and one rubric line still carry the old, ill-posed framing, so prompt, rubric and solution contradict each other.
  - solutions.md line 370 "Kysytty": "pienin ilmaväli, jonka läpi sähkö voi lyödä". Line 374: "pienin väli, jonka läpi sähkö lyö, on d = U/E_max ≈ 4 mm".
  - The uniform-field model gives the longest gap that surely breaks down (breakdown for d ≤ 4 mm). It is not the smallest gap, because shorter gaps break down too. A student learning from the solution gets the opposite reading of the new prompt.
  - tasks.json s4 b assumptions criterion: "alaraja eli pienin mahdollinen arvo". That is unclear against "kuinka lyhyen ... varmasti". Say instead that 4 mm is a cautious (alaraja) estimate of the longest gap that breaks down, since field enhancement and moisture allow longer gaps.
  - The solution's "turvaetäisyyden alaraja" and the common mistake "tasaisen kentän alaraja" need the same fix.
  - Fix: use one wording in the "Kysytty" line, the model answer and the rubric. Example: "kuinka pitkän ilmavälin yli sähkö lyö varmasti läpi (tasaisen kentän malli: enintään noin 4 mm), ja miksi todellinen väli voi olla pidempi".
  - The prompt "Arvioi, kuinka lyhyen ilmavälin yli sähkö lyö varmasti läpi" is well-posed on its own. The "varmasti" comes from the uniform-field assumption, so the solution should say so.

## Polish
- s4 b: "kuinka lyhyen" is slightly odd Finnish. "Kuinka pitkän ilmavälin yli ... läpi" or "enintään kuinka pitkän" reads more naturally and avoids the confusion.
- fi-easy: the s4 solution does not link the 4 mm result to the unit's opening spark (3 mm, about 9 kV). A single sentence would tie it to the Ydinajatus.

## Checked
- All eight tasks demand application in new authentic contexts: s1 balls on threads, s2 capacitor and glass, s3 data and linearisation, s4 safety, s5 report critique and experiment design, s6 ion engine, s7 graph V(x), s8 LED. No heading names the formula.
- Each task has parts of rising demand and a rubric tied to the criteria keys. No points go to irrelevant things. Variety is good: graph (s3, s7, s8), experiment (s5), safety and communication (s4).
- Solutions show the principle first and give real common mistakes. Spot-checked numbers: s1, s2, s5 a (0.99 W, 16 %), s6 (40.2 km/s, 87.5 mN, 349 m/s), s8 (17 mA, 63 %, 127 Ω).
- Workload: 8 tasks, 95 points. teacher.md splits the hour realistically (2 in class, 2 at home, long tasks as homework).
- The fi-easy wording is plain and the sentences are short. The terms are explained (influenssi, läpilyöntilujuus, kammiovärinä).
- Not re-checked: the unit text and inquiry beyond the packet's checks (practice.py check OK).
- Hash at start and end: debd72cf8d478220.
