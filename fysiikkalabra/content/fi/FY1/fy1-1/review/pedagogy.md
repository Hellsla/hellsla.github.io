VERDICT: FAIL
CONTENT-HASH: 700f60a819aca0b5

## Blocking
- exit-ticket.json item 2 answer — `$\text{B}$` is written with a single backslash, so JSON turns `\t` into a tab and the page shows "Kohde extB siis noin" (capture open-exit-1280) — write `$\\text{B}$`.
- inquiry.json exp-1/exp-2/exp-3 `names.L` ("leveyden eksponentti") — the recorded table still opens with an unexplained column of L values (-9,00, -9,10 ...) next to n; after "Siirry kohteeseen vetyatomi" L is -9,10 while n is -10, which contradicts the revision's aim (the teacher's complaint was L values). The status line also says "Säädä leveyden eksponentti" — hide or rename the column ("näkymän leveys, ei tarvita") and change the hint text so only n is the student's number.

## Polish
- The core path is clear: opening question, "Siirry kohteeseen" (menu readable at 390 px), pred-1 and pred-2, and the ladder figure ("5 askelta ⇒ 10^5 = 100 000 kertaa suurempi") are good. But predictions and exp-1 ask for "suuruusluokkaa" (steps), while the section asks "kuinka monta kertaa"; add one sentence linking the two (askeleet → kertoja) at the experiment's question.
- Menu has 44 entries, including both "avaruuden raja" and "havaittava maailmankaikkeus"; the student only needs about 8 named in the experiments. Group or shorten the list.
- Workload: 5 theory sections, 3 predictions or experiments, 2 interpret items and 4 Sovella tasks in one lesson; consider moving more to optional.
- Formula k = d_suurempi/d_pienempi: say in a sentence that the colon form (d_suurempi : d_pienempi) means the same.

## Checked
- Shots were stale (before the edits); regenerated with screenshot.py.
- No × as a multiplication sign in lesson.md, inquiry.json or the exit ticket; \cdot is used throughout.
- Fig 2 and fig 3 (ladder) are legible and clear at 390 px.
- exp-1 intro, the preview and the menu items for vetyatomi, protoni, kvarkki and Neptunuksen radan säde exist.
- Example is staged in seven steps; its solution follows the rubric.
- The hash was unchanged at the end.
