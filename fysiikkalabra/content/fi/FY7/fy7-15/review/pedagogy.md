VERDICT: PASS
CONTENT-HASH: ce684c7f1daaa50d

## Blocking
(none)

## Polish
- inquiry.json "pohdi" and "tarkistus-3" (both optional) — the opening question (why polaroid glasses kill glare but dark glasses do not, why it returns when the head tilts) is asked of the student only in these two optional items; the required path never makes the student commit to an answer or return to it. Make "pohdi" required (or keep tarkistus-3) so the hook is closed by the student, not just by the text.
- inquiry.json "mittaus" — the prompt text already states `A = 360,7 lx`, which is the answer; the student only picks which of three given numbers is the slope. Drop `A` from the text and give the figure/two fit points so the student reads the slope (the solution already shows the two-point reading).
- inquiry.json "ennuste-yksi" — "polarisoimaton" and "polarisaattorikalvo" are used before the theory is read and the retrieval item is optional. Add one gloss sentence: "Polarisoimattomassa valossa sähkökentän värähtelysuunta vaihtelee satunnaisesti; kalvo päästää läpi vain yhdessä suunnassa värähtelevän osan." so the prediction can be argued.
- lesson.md "Yleinen virhekäsitys" / "Järkevyys" — "polarisaattori vain poistaa valoa eikä voi lisätä" reads as if a film adds light; write "eikä voi lisätä läpi pääsevän valon määrää". "Lähtevästä valosta läpi pääsee noin kolmannes" → "Alkuperäisestä valosta $ läpi pääsee noin kolmannes."
- exit-ticket.json Q1 — glass 1,50 and 56,3° are stated in the Brewster paragraph, so it tests lookup; use another medium (e.g. akryyli 1,49).

## Checked
- Path: prerequisite alignment, hook, predictions, sim, theory, example, error item, transfer, checks, exit: coherent; both slot goals covered; one-hour core path.
- Predictions can be refuted by the model values; each wrong option's feedback repairs its misconception.
- Example has seven stages, one step each; justification of halving and of Malus explained, not named.
- Siirto (Brewster, camera height) has three hints and real mistake values.
- Sim not opened; only the 390 px hero capture was available (hero legible, glasses contrast clear). Figure bodies not reviewed.
- Finnish: no errors found beyond the sentences above.
- Hash unchanged at end.
