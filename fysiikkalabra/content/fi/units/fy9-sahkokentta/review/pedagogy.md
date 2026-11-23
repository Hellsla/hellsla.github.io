VERDICT: FAIL
CONTENT-HASH: e9115553fe1fb6c4

## Blocking
- s4 b: the reworded question is still not consistent with the solution. The task now says "kuinka lyhyen ilmavälin yli läpilyönti tapahtuu varmasti", but solutions.md s4 b still has `Kysytty: ... pienin ilmaväli, joka voi lyödä läpi` and the model answer says "pienin läpilyövä väli ... ≈ 4 mm". The old ill-posed wording survives there. U/E_max = 4 mm is the longest gap that breaks down in the uniform-field model, not the smallest. Any gap shorter than 4 mm breaks down too, so "smallest" is wrong. Fix the Kysytty line and the model answer to match, for example "suurin ilmaväli, jonka yli läpilyönti tapahtuu varmasti, on noin 4 mm".
- The task wording itself is still easy to misread. "Kuinka lyhyen" asks about a short gap, but the answer is an upper limit on the gap length. Suggested wording: "Arvioi, kuinka pitkän ilmavälin yli läpilyönti tapahtuu varmasti" or "enintään kuinka pitkän".

## Polish
- The rubric's assumptions criterion ("arvio on alaraja ... valokaari voi syttyä pidemmästäkin välistä") fits the corrected reading: the 4 mm figure is a lower bound for the longest breakdown gap. The solution's "alaraja turvaetäisyydelle" says the same thing and is fine. After the fix, check that all three texts (task, rubric, solution) call 4 mm the same kind of bound.

## Checked
- Read the s4 b task text, its rubric (4 criteria, 5 p) and the solution in the packet.
- The 12 kV (20/√3) reasoning and the 4 mm calculation are consistent between rubric and solution.
- The listed common mistake (using 20 kV) is real.
- I did not re-review the other tasks: this was a delta re-review of s4 b only.
