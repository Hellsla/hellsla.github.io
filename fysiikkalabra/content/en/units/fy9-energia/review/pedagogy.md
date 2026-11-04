VERDICT: PASS
CONTENT-HASH: 44d6a17aa7d17ef6

Pedagogy review of the English translation of fy9-energia.

## Blocking
None.

## Checks done
- Structure, task counts, the 75-minute plan, the six starting-level questions, the four Apply calculations, the six long problems, points and rubric criteria are the source's (check_i18n.py passes; numbers identical).
- Feedback per misconception is translated in full and keeps its diagnostic content (dividing by P0 instead of P1, adding loss percentages, minutes as seconds, kWh divided by 3.6, multiplying instead of dividing by eta).
- Chapter links are named by the English chapter titles (*Power*, *Efficiency*, *Fuels and heat of combustion*, ...), never by id, and match the links in "Review if needed".
- teacher.md is fully translated; its stage names (Think about it, Predict, Investigate, Theory summary, Apply, Check your understanding) match lang/en.json, and every task it names (*The wood chip power plant*, *The pumped-storage plant in the mine*, *The island's electricity*, *Frost and the electricity bill*, *The electric sauna stove*, *The pellet boiler*, *From fuel to wheels*) matches a title on the page.
- Rubric criteria remain observable ("Calculates ...", "Names sources of error and tells in which direction ..."); no formula is given away in prompts that the source did not give.
- Option lengths stay balanced in English (the correct option is not visibly the longest).

## Polish
1. inquiry.json activity 17 and tasks intro: "matriculation exam" is right for Finland; a one-time gloss ("the Finnish matriculation examination") in the tasks intro would help a reader outside Finland. Optional.
2. teacher.md "Fast and slower students": "Slower students" is fine, but "students who need more support" is the more usual teacher English.
3. Recurrent "the share of X in Y" phrasing (see science.md Polish 2) makes the efficiency definition harder to parse for students; "the fraction of Y that is X" is clearer.
