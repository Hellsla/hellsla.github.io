VERDICT: PASS
CONTENT-HASH: 5e217585a15dde17
Round: 2. Round 1 had one Blocking item (the 0,10 g bead with −20 nC would exceed the breakdown strength of air). It is fixed in 57a66480d: the task is now a dust grain in a vacuum chamber.

## Blocking

## Polish
- lessons/FY6/fy6-11/figures.py:404 (PK_DESC, carried over) — the descriptions do not say that the arrows start from the body; add "lähtevät kappaleesta" for a reader who cannot see the figure.
- exercises.json:253 (carried over) — still no distractor for the lesson's Yleinen virhekäsitys (force growing near a plate). The solution's Periaate now says "kaikkialla levyjen välissä", which is enough; an option for it stays optional.

## Checked
- Hash 5e217585a15dde17 at start and end; the packet was regenerated and read again.
- The new data are realistic: m = 1,0·10⁻¹² kg is a grain of radius about 5 µm, and q = −2,0·10⁻¹⁶ C is about 1250 e. Its surface field is about 7·10⁴ V/m, far below breakdown, and the vacuum removes air resistance as the brief's "tyhjiössä" does.
- Recomputed: F_s = |q|E = 2,0·10⁻¹¹ N down, G = 9,8·10⁻¹² N down, ratio 2,04. This matches the figures (PK_FS : PK_G, same pixel lengths), the four descriptions, the feedback and the answers.py comment.
- All "helmi" wording is replaced consistently in the stem, the feedback, the solution and the descriptions.
- Option A (force along the field) and option D (weight left out as for an electron) still catch mistakes the lesson warns about.
- The key is not identifiable by form ("Voimakuvio A–D").
- Formulas measured with KaTeX in Chrome at 390 px (formula widths only; figures not rendered): widest inline 268 px, under 300 px. G = mg is now on its own row.
