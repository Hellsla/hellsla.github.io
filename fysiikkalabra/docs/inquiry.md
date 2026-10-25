# Inquiry-based lessons: `inquiry.json`

A lesson folder may carry `inquiry.json`. When it does, `scripts/build.py` lays the page out as inquiry stages
and the student acts before being told: a phenomenon, a prediction, an investigation, the model, a transfer task,
three checks. Without the file the lesson renders in the classic layout (theory, simulation, exercises, exit
ticket), byte for byte as before. The lesson's other files are unchanged by the framework: `lesson.md` still holds
the theory, `exercises.json` the 5/4/3 exercises, `exit-ticket.json` the three quick checks, `sim.js` the physics.
`inquiry.json` only says where those parts go and adds the activities between them.

The pedagogical brief behind this format is `docs/inquiry-spec.md`. Pilot: `content/FY3/fy3-2/inquiry.json`.

Validate: `python scripts/inquiry.py <id>` (also run by `lint_lesson.py` and refused by `build.py`); errors name
the lesson, the file and the field, e.g. `fy3-2 inquiry.json: activities[2].choices[1].feedback: every choice
needs misconception-specific feedback`. Tests: `python scripts/test_inquiry.py`.

## Format (version 1)

```json
{
  "version": 1,
  "contribution": "One sentence: what this lesson adds that earlier lessons did not (markdown, LaTeX allowed).",
  "prior": ["What the student already knows and where it came from (fy3-1)", "..."],
  "activities": [ { "id": "pred-1", "stage": "ennusta", "type": "choice", "...": "..." } ]
}
```

Stages, in the order the page shows them (empty stages are not rendered; a stage may hold any number of
activities, so stages repeat, combine or are omitted by what the lesson needs):

| id | heading | typical content |
|---|---|---|
| `herata` | Herätä kiinnostus | `hook`, a retrieval `choice` on prior learning |
| `ennusta` | Ennusta | `choice` predictions with `reveal` tied to an experiment; competing explanations (`layout: "models"`) |
| `tutki` | Tutki | `sim`, `experiment` (guided, controlled variables), `interpret` (table, figure, measurements) |
| `selita` | Selitä | `theory` (Ydinajatus, Kaavat), `reflect` |
| `sovella` | Sovella | `theory` (Esimerkki), error-spotting `choice`, `numeric` transfer task, `exercises` |
| `tarkista` | Tarkista osaamisesi | three checks: a conceptual `choice`, a `numeric` or representational task, an `explain`; then `exit` |

Every activity has `id` (lowercase, unique), `stage`, `type`, optional `title` (plain text) and optional `hints`
(at most three strings, shown progressively: a guiding question, the representation or relationship, a worked
intermediate step). Text fields are markdown with `$…$` LaTeX. Activity types:

| type | fields | renders as |
|---|---|---|
| `hook` | `text`, optional `question` | the phenomenon, in the lesson's voice, and the question it raises |
| `text` | `text` | a paragraph wherever one is needed |
| `choice` | `prompt`, `choices: [{text, correct?, feedback}]`, optional `justify`, `reveal`, `layout`, `solution` | radio buttons; feedback for the chosen option after *Vastaa*. With `reveal: {"after": "<experiment id>", "min": n}` the choice is a **prediction**: it locks on commit and its feedback stays hidden until that experiment has recorded `min` measurements. `justify: true` adds an optional written reason. `layout: "models"` presents the options as competing explanations. |
| `experiment` | `intro`, `initial: {param: value}`, `locked: [param]`, `vary: param`, `measure: [key or {key, label}]`, optional `units`, `min`, `question` | a guided investigation on the page's simulation: *Aseta alkutila* sets `initial` and locks `locked`, the student changes `vary`, *Kirjaa mittaus* records `vary` and every `measure` key of `simState` into a table, *Nollaa* resets. A linked prediction is revealed at `min` rows (default 2); the optional `question` (a `choice`, `numeric` or `explain`) appears at the same point. |
| `interpret` | `text`, optional `question` | a supplied representation (markdown table, inline SVG, measurements) and a question on it |
| `numeric` | `prompt`, `answer`, `unit`, `tolerance` (relative, default 0.02), optional `mistakes: [{value, feedback}]`, `hints`, `solution` | the same browser-side check as the exercises (decimal comma or point, empty and non-numeric input asked again, two tries before pointing at the solution) plus feedback for listed common mistakes |
| `explain` | `prompt`, `model`, `criteria: [text]`, optional `pair` | a written explanation; a button shows the model answer and the self-assessment checklist |
| `reflect` | `prompt`, `predictions: [choice ids]` | the student's own predictions beside the evidence verdict, "Muuttaisitko ennustettasi?" and a reason |
| `theory` | `sections: ["Ydinajatus", "Kaavat", …]` | those `## ` sections of `lesson.md` (each placed once; sections placed nowhere are appended to Selitä) |
| `sim` | optional `text` | the free-exploration simulation (at most one; needed before any `experiment`) |
| `exercises` | optional `text` | the three exercise levels (at most one) |
| `exit` | optional `text` | the exit ticket (at most one) |

Rules the validator enforces: `version` is 1; `contribution` is non-empty; ids are unique; every choice has
feedback and exactly the correct options marked; `reveal.after` names an experiment; `locked` does not contain
`vary`; `theory` sections exist in `lesson.md` and appear once; `reflect.predictions` are activity ids; hints
are at most three. What it cannot check, the reviewers do (below).

Guidance, not enforced: a prediction before every investigation; no feedback that answers the opening
question before the student has committed; the varied parameter alone changes in an experiment; model values
from a simulation are called model values, measurements measurements; the three checks in Tarkista cover a
concept, a representation or calculation, and an explanation or transfer; the exercise counts stay 5/4/3.

## Page behaviour (`templates/inquiry.js`)

Everything runs in the browser; nothing is sent anywhere. A student's choices and written answers are kept in
memory and copied to `localStorage` (per device, wrapped in try/catch) so a reload does not lose a committed
prediction; the page works without storage. Feedback uses text and an `aria-live` output, never colour alone.
Controls are native (`radio`, `textarea`, `button`, `details`), 40 px tap targets, keyboard operable. Reduced
motion is respected by the simulation embed. Without JavaScript the page shows every stage, the prompts and the
options; feedback, experiments and the model answers need it.

## Simulation interface

A sim exposes an adapter by calling, once in `setup()`:

```js
if (window.defineSimAdapter) window.defineSimAdapter({
  params: { F: { input: sF.elt, unit: 'N' }, s: { input: sS.elt, unit: 'm' }, t: { input: sT.elt, unit: 's' } },
  reset: () => { sF.value(60); sS.value(10); sT.value(5); u = 0; running = false; },
  step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
});
```

`window.simAdapter` then has `params`, `capabilities` (`set`, `lock`, `reset`, `pause`), `get()` (one frame is
drawn, then `window.simState` is returned, so values are fresh even while the sketch is paused off-screen),
`set({name: value})` (writes the control and fires `input` and `change`), `lock(name, on)` (disables the control
and marks its label "(vakio)"), `reset()`, `pause()`, `resume()`. The physics stays in the sim and
`window.simState` is untouched, so `tests/sims/<id>.json` keeps passing. An `experiment` whose parameters the
adapter does not declare shows its setup and a note instead of the buttons; a sim without an adapter still
offers free exploration.

## Migrating a lesson

1. Read `meta.json` goals and prerequisites and the curriculum slot; write `contribution` and `prior`.
2. Decide which stages the lesson needs and what the student should do first. Not every lesson needs an
   experiment: a lesson without a sim uses `interpret` on a table or figure, or a competing-models `choice`.
3. Write the predictions so that the investigation can refute them; write every wrong option's feedback as a
   misconception repair, not "väärin".
4. Place the existing theory (`theory`), the sim (`sim`), the exercises and the exit ticket. Keep the worked
   example and the exercises; add one transfer `numeric` with hints and mistakes, one error-spotting `choice`.
5. Add the sim adapter to `sim.js` (parameters that experiments set or lock; reset; step).
6. `python scripts/check_lesson.py <id>`, `python scripts/test_inquiry.py`, look at the preview at 360 and 1280 px.
7. `inquiry.json` is lesson content: it is in the content hash, so both reviews must pass the lesson again.

## Testing

`scripts/test_inquiry.py` covers validation messages, classic-layout compatibility, every activity type's
rendering, prediction-before-feedback sequencing, initial conditions, locked controls, recording, reset,
numeric handling (comma, invalid, mistake feedback, retries), progressive hints, model answer, reflection,
reload persistence, keyboard commit and the 360 px layout. These prove the mechanics, not the learning: whether
a sequence teaches is answered in the classroom (see the evaluation plan in the migration pull request).
