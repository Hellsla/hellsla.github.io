VERDICT: PASS
CONTENT-HASH: 483576fe55c9f08f

## Blocking
(none)

## Polish
- [Minor] solutions.md c-kohdan "Leikkauskohdasta saadaan lisämassa $$…$$. Se on noin kolmasosa…" and the Io velocity "Esimerkiksi Iolle $$…$$. Siitä saadaan…" — display maths inside a sentence followed by ". Capital" reads as a new sentence after a loose formula; the build moves the full stop into the maths and the fi page reads well, so this is only a style note — optionally write "…$$, mikä on noin kolmasosa jousen massasta."
- [Minor] fi-easy split paragraphs: some new paragraphs are two or three short sentences ("Kallistuminen siirtää kuormaa vain senttejä. Ympyrän säteenä voi siis käyttää…"). They are fine as steps, but they do not all follow the Periaate/Kaava/Sijoitus labels; acceptable for the simpler language.

## Checked
- Source diff `git diff 2dc38e00^ -- content/fi-easy/FY5/sovella` (solutions.md paragraph splits, three tasks.json text splits with `\n\n`).
- Freshly built site/FY5-sovella.html (fi), read as HTML structure only: split paragraphs become separate `<p>`; display maths, aligned chains and the `\text{,}` / `\text{.}` punctuation handling are intact. I opened no screenshot; no screenshot or image was opened for this delta. This is a text-only paragraph split, with no figure, table or maths change, so no capture was needed for judgement.
- Every split sits at a sentence boundary; no inline maths or unit is cut; LaTeX units and the decimal comma are unchanged. No plain-text quantity was added.
- The set's figures were not in the diff and were not re-reviewed.
- The fi-easy page (site/fi-easy/FY5-sovella.html) does not exist, as expected for a draft set.
- Hash at start and end: 483576fe55c9f08f.

## Scores
illustrations 4 (not in the diff) · typography 4 · Finnish 4 · accessibility 4
