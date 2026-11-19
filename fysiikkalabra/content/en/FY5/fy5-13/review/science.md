VERDICT: PASS
CONTENT-HASH: f42896c86b371ff2

## Blocking

## Polish
- inquiry.json:120 (`simulaatio.calc`) — still open from round 1: "$a = 1.0\,\text{mm}$" reads as the loudspeaker's amplitude for the tubes too. In the tube formulas, though, $U(0) = a\cot kL$ or $a\tan kL$, so off resonance the driven mouth moves much less than $a$ (my run: $0.06\,\text{mm}$ for the closed tube at $200\,\text{Hz}$). Fix: add "for the tubes $a$ only sets the scale".

## Checked
- Delta only (three wording changes, no numbers or symbols changed). I judged them against the sim's own formulas, recomputed in one script for $L = 0.85\,\text{m}$ and $v = 340\,\text{m/s}$.
- `calc`: "at an open end it is greatest at the natural frequencies" is correct and more accurate than before.
  - Open tube: both mouths reach $16.7\,\text{mm}$ at 200 and 400 Hz. Off resonance the driven mouth is $0.06\,\text{mm}$ at 100 and 300 Hz, against a maximum of $1.0\,\text{mm}$.
  - Closed tube: the open mouth carries the maximum $16.7\,\text{mm}$ at 100 and 300 Hz. At 200 and 400 Hz it is only $0.06\,\text{mm}$.
  - The old unconditional wording was therefore false off resonance; the added condition fixes it (B removed).
- Experiment 2 intro: asking for the node and antinode "at the peak frequencies" matches the model. At other frequencies the mouth is not an antinode.
- Conclusion model answer: "At the peaks there was always a node at the closed end and an antinode at the open end" is right. The closed end is a node at every frequency; the antinode at the mouth exists only at the peaks. The odd-quarter-wavelength conclusion follows.
- The numbers in the changed model answer are unchanged and still match the recomputation:
  - $16.7\,\text{mm}$ at the peaks;
  - $1.0\,\text{mm}$ at the closed tube's 200 and 400 Hz;
  - closed-tube peaks at 100, 300 and 500 Hz.
- No other file changed. The rest of the lesson stands as passed in round 1.
- Hash unchanged at the end.
