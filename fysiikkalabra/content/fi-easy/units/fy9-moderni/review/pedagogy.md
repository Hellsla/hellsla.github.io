VERDICT: PASS
CONTENT-HASH: 99d9cf49a3fb1eb9

Pedagogy review of the Selkeä suomi (fi-easy) translation of fy9-moderni. It is judged against NOTES.md §12 and the source, which passed its reviews.

Summary: the translation turns long Finnish sentences into short connected ones. It explains a difficult word inside the sentence the first time it is used: intensiteetti eli voimakkuus, absorboituu eli ottaa vastaan, vaimenee eli heikkenee, etääntyy eli loittonee, kantama, ruuhi eli vanha puuvene, fissioituu eli halkeaa, interpoloimalla eli arvioimalla, lomitse eli niiden välistä. Physics terms stay and are explained. Instructions are clearer: "Ota taustasäteily huomioon.", the Tutki stage is split into numbered steps, and the multi-question prompts are split into separate questions. Feedback keeps one sentence per idea and its chapter link. The key concepts are five (3–5) and are the unit's central ideas, each with one or two plain sentences. The block renders after the opening as "Luvun tärkeät käsitteet", marked Vapaaehtoinen, with the fixed lead text. teacher.md is translated as a whole, keeps the 75-minute plan, and adds a short explanation of "diagnostinen testi". No step, hint, misconception, rubric criterion or point is lost.

## Blocking
None.

## Polish
1. inquiry.json activities[7].text: the "Tee näin:" steps are meant as a numbered list. There is no blank line before "1.", so the page shows them as one run-on paragraph ("Tee näin: 1. Päättele … 2. Määritä …"), and the one-action-per-line effect of §12 point 6 is lost. Fix: write "Tee näin:\n\n1. …".
2. sovella/tasks.json fy9-moderni-s5 text: the group's conclusion (the quote in "Ryhmän johtopäätös") keeps the source's long sentences. It is a quotation to evaluate, so the content must stay the same. Splitting it into 4–5 shorter sentences without changing its claims would help S2 readers.
3. inquiry.json activities[6].choices[1].feedback: "hyvin lyhyellä matkalla, muutaman solun matkalla" repeats itself. Suggestion: "antaa energiansa hyvin lyhyelle matkalle, vain muutaman solun matkalle".
4. unit.md Ydinajatus: "energia vaihtuu vain tietyn suuruisina paloina". Here "vaihtuu" can be read as "changes" rather than "is exchanged". "siirtyy" or "vaihtaa paikkaa" would be clearer; the same wording is in inquiry.json contribution.
