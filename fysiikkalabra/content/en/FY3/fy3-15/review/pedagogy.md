VERDICT: PASS
CONTENT-HASH: d89bf7dd1d8a286a

## Blocking
(none)

## Polish
- inquiry.json `kaukolampo` — the numeric question (waste heat in full district-heating mode, 48 MW) does not itself test pred-2 (electricity falls by 40 MW while heat rises by 232 MW); the refuting comparison is only in the solution's reasonableness line. Ask for the electricity lost per megawatt of heat, or add that comparison to the prompt, so the prediction is confronted by an act, not by reading the solution.
- inquiry.json `kertaus` — the heat-engine retrieval (800 MJ / 280 MJ) is not asked through the hook's power-plant situation (CLAUDE.md: retrieval belongs to its phenomenon). Use the condenser case: $Q_1$ fuel, $W$ electricity, $Q_2$ to the sea.
- inquiry.json `check-3` — four criteria in one answer is a lot for a 16-19-year-old; the fourth (what the heat replaces) goes beyond the lesson text, which never mentions separate heating plants. Drop it or add one sentence to the lesson.
- lesson.md "Common misconception" — the first paragraph states the misconception but the open question "is the energy lost?" is only answered in the next paragraphs; open with the correct statement in bold, then the misconception.
- exit-ticket.json — near duplicate of the pysahdy check and the Etsi virhe item (product of three efficiencies). A question on the other core idea (why overall efficiency rises but electricity falls) would test more.

## Checked
- Path: hook -> pred-1 and pred-2 -> three table tasks -> conclusion -> theory -> reflect -> example -> transfer; all three slot goals (energy chain, condensing vs CHP efficiencies, conservation) covered, nothing outside FY3 scope.
- Prior alignment: heat-engine balance and Q = cmΔT are in `prior` with chapter names.
- Predictions can be argued from the premises; the data (efficiency table, two-mode table) can refute pred-1 and pred-2; wrong-option feedback names the misconception and points to the evidence without stating the number early.
- No simulation is justified; sim-spec reason is sound; tables and figures serve as the investigation.
- Speakers: only one of four (Cem) is right; no letter references.
- Figures (Sankey, bar chart, stacked graph) legible at 390 px, to scale, colour accompanied by labels; stacked graph and Sankey beside the paragraph they explain.
- Worked example: seven stages, one step each, symbolic first, reasonableness; different numbers from the investigation task.
- Workload about one lesson: three core numeric tasks, one optional, 1 explain, 3 checks.
- Mistake values in numeric tasks are real slips (loss of whole fuel power, P2 instead of loss, subtraction of one term only).
- Hash at start and end identical.
