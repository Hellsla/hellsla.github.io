VERDICT: PASS
CONTENT-HASH: f7b8d233f6ae25a0
SCOPE: delta md-paragraphs,numbers,paragraphs,reflow,typography from 810265934d1de6e2 base cabadc3e6179

## Blocking
None.

## Polish
1. exercises/solutions.md (incline-friction tasks, Kaava) — "Kohtisuoraan rinnettä ei kiihtyvyyttä" has no verb — "Kohtisuoraan rinnettä kappale ei kiihdy, joten $\Sigma F_y = 0$".
2. exercises/solutions.md (energy tasks, Kaava) — "Nollataso lopputilanteen korkeudelle" is used without a gloss — add once "eli korkeus mitataan lopputilanteen kohdasta".
3. exercises/solutions.md (sled task, Kaava) — the step "jokaisen osan kitkatyö on $\mu mg x$" is the key idea of the tasks with several surfaces and is packed into one long sentence; give it its own sentence.

## Checked
- Rewrite only: each Kaava now starts from ΣF = ma (direction named), ΣF = 0 for constant velocity, E_alku = E_loppu + W for energy tasks, with E_k, E_p, F_μ = μN and N named before the combined formula; no number, answer or id changed.
- Sled task: the symbolic result v = √(2gL(sinα - μ1cosα)) moved from Sijoitus to Kaava, so Sijoitus substitutes into the last symbolic form as the house rule asks.
- Checked the new symbolic steps: μ = tanα, s = v²/(2μg), x = h/μ, F_v = mg + (E_k0 - E_k)/h all follow from the stated equations.
- Friction task now says N = mg horizontally before μmg = m|a|; the student no longer has to guess where N went.
- Parachute task: h from mean speeds is justified (uniform change within each interval) before the energy equation.
- Paragraph splits in Mallivastaus and Järkevyys are line breaks only; the long safety remark on snow friction now stands apart.
- Captures not opened: only solution wording and formula order changed; judged from the packet's diff.
- Hash the same at start and end.
