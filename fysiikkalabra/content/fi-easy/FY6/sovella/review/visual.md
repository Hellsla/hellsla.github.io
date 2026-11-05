VERDICT: PASS
CONTENT-HASH: eb7e7e6059e14f57

Scope (teacher's ruling "katselmoi vain muuttuneet osat"): `git diff e7fb0232a -- content/*/FY6/sovella` plus what the changed sentence touches. This translation did not exist at e7fb0232a. Its diff since its last PASS (24b2a3b87) is one sentence, the fy6-s4 d **Principle/Periaate** in solutions.md, the same change as in fi. The packet's full mode was narrowed to that scope.

## Blocking
None.

## Polish
None in scope.

## Checked
- **Build:** `scripts/screenshot.py FY6-sovella --lang fi-easy` refuses, because the module task set is captured only in fi. So I opened preview/fi-easy/FY6-sovella.html, rebuilt this session by build.py FY6-sovella, in Playwright with every box open.
- **Captures:** my own captures are /tmp/claude-0/-home-user/e4f8157e-e9a5-5f12-8890-46da1aaca3f9/scratchpad/fi-easy-390.png and /tmp/claude-0/-home-user/e4f8157e-e9a5-5f12-8890-46da1aaca3f9/scratchpad/fi-easy-1280.png.
- **s4 d PERIAATE:** the new sentences render, with $+Q$ and $-Q$ inline in KaTeX. There are 0 .katex-error elements, and scrollWidth equals the viewport at 390 and 1280 px.
- **Language:** the Finnish is plain and natural.
- **Hash:** the same at the start and at the end.

## Scores
illustrations 5 · typography 5 · Finnish 5 · accessibility 5 (the changed text only)
