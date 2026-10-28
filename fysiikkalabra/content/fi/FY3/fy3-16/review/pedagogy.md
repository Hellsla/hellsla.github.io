VERDICT: PASS
CONTENT-HASH: 719f2047818de2b8

Round 2: the round-1 Blocking item (check-c2 only the other side of check-1) is fixed. Delta review of the diff: check-c2 replaced by 'Sulamislämpö kylmälaukussa' (1,0 kg ice vs 1,0 kg water at 0 °C); a 'learn' array only reformatted.

## Blocking
- none
## Polish
- exit-ticket.json q2 (sauna: why rocks cool more when water evaporates than if it only warmed) is criteria 2 and 4 of check-3 and its model answer; by NOTES §11 a repeat. Not in the round-1 Blocking and check-3 is optional, so Polish: replace it, e.g. by a condensation or freezing item.
- exit q1 (melt 0,40 kg ice and warm to 25 °C) is the check-2 skill; acceptable as a quick item.
- check-c2 distractor 4 ('Jää, koska jää on kylmempää kuin vesi') picks the right object for a wrong reason; fine, its feedback repairs, but the prompt does not say how warm the surroundings are (the feedback assumes 8 °C); say 'kunnes sisältö lämpenee noin 8 °C:seen'.
- distractor 3: option text about conduction is weaker than the others.
## Checked
- Round-1 Blocking: new check-c2 asks a different concept from check-1 (the size of the melting energy against warming water, not the temperature after the ice has melted); check-1's feedback no longer states its answer.
- Computed: 4190 * 1,0 * 8 = 33 520 J ~ 34 kJ; 334 / 33,5 = 10,0 ('noin kymmenesosan') right. Physics right: 334 kJ/kg, ice absorbs far more energy.
- Each wrong option is a real misconception (same temperature = same capacity, better conductor, colder = lasts longer); feedback of each repairs and none points at another. LaTeX; Finnish clear; titles 1-4; exit text 'kaksi' matches two questions.
