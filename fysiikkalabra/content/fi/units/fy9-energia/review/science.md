VERDICT: PASS
CONTENT-HASH: 5d7daab35c8d643b

Delta review of the course rename FY12 → FY9 (commit 3052d352). Previous all-PASS hash: d64ab1c8503f8cb7. The hash was the same at the start and the end of this review.

I checked that the change is only the rename: every file of `content/fi/units/fy9-energia/` and `lessons/units/fy9-energia/` (review/ excluded) at 3052d352 equals the file at 47782fdd with `fy12` → `fy9` and `FY12` → `FY9` replaced, and nothing else. No `fy12`/`FY12` remains in the unit's sources or in the built preview.

## Blocking

None.

## Polish

None new. The Polish items of the previous science report still apply as written there.

## Checked

- No number, formula, unit or model text changed; the earlier full recomputation (previous report at d64ab1c8503f8cb7) stands.
- `lessons/units/fy9-energia/sovella/answers.py` runs without error after the rename, and `python3 scripts/practice.py check units/fy9-energia` passes with the same point total as before.
- Task ids follow `fy9-energia-s<n>` in tasks.json, solutions.md headings and the preview (`id`/`data-id`).

## Shared issues

- `docs/figures/catalog.json` still lists sources under `fi:units/fy12-*/inquiry.json` (outside the unit; regenerate the catalog).
