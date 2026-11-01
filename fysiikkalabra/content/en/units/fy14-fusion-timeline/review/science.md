VERDICT: PASS
CONTENT-HASH: 63a171be08f0db43

Science re-review of fy14-fusion-timeline and of the shared `timeline.json` events it uses, 2026-11-01. It covers commit 3ed55db3 and the timeline data commit d34ad4f1.

## Previous findings
1. Resolved. *Claims and checks* now says that the claims "all failed when others checked them". It adds that only ZETA's team withdrew its claim, that an inspection exposed Huemul, and that other laboratories could not repeat cold fusion. All three are correct.
2. Resolved (shared). `jet-decision-1978` is now dated 1978-05-30, with 25 October 1977, 30 May 1978 and 1 June 1978, and it cites Decision 78/471/Euratom.
3. Resolved (shared). `chicago-pile-1942` now says "four years".
4. Polish 1 resolved. The Kurchatov feedback now names the head of the Soviet atomic programme.
5. Polish 2 done. Sannikov is now on `culham-five-1969`; see Shared issues 2 and 3 for its wording.

## New content
- **task-geo:**
  - Its 23 ids are exactly the events from 2015 on in the data; `eurofusion-2014` is rightly left out.
  - Their countries are the seven named, and "Seven countries" is the only correct option.
  - The "five countries in the 1950s" matches the data: the US, UK, USSR, Argentina and Switzerland.
- **task-steps:** 1997 − 1958 = 39, which is correct and the only correct option.
- **Task 1:** the 16 counts are exactly what I recomputed from the data: 26/23/15/40, and 19-5-0-2, 5-7-9-2, 4-8-3-0, 6-26-8-0.
- **Small timelines:** the ids for Tasks 2 and 3 are the right events.
- **Rebalanced options** (`pred-geo`, `find-error`, `check-1`): the same facts, each with one correct option. Trinity was on 16 July 1945.

## Blocking
None.

## Polish
None in the unit.

## Shared issues
None open. In commits 525827b2 and b3bbc371 my three points on `timeline.json` are fixed:
- "the Council of the European Communities decided"
- "a Soviet colleague"
- "V. V. Sannikov"

`iter-first-module-2025` was rewritten, and I checked it against the ITER press release of 10 April 2025 (sector module #7; the first module, installed in May 2022, was taken out for repair). I also checked it against World Nuclear News (dimensional non-conformities in the welding joint region; corrosion cracks in the thermal shield piping). It is correct, and the earlier "stopped for about two years" is gone.
