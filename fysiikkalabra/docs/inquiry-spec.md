# Inquiry-based learning: the brief (teacher, 2026-10-25)

The brief the inquiry framework (`docs/inquiry.md`) implements, kept verbatim so that authors and reviewers judge against the same text.

```text
Implement inquiry-based learning across the entire Fysiikkalabra framework and migrate all existing lessons to use it.

Do not stop after a pilot. Use one lesson to validate the architecture, then apply it to every existing lesson and update the authoring workflow for all future lessons.

FIRST INSPECT

Read applicable repository instructions, CLAUDE.md, curriculum.json,
the build script, templates, styles, lesson content, simulations,
tests, and authoring/reviewer instructions.

Inventory:
- Existing authored lessons.
- Curriculum slots without authored content.
- Existing simulations and their capabilities.
- Existing exercise formats.

Report these categories separately. Do not generate full lessons for
empty curriculum slots as part of this task.

GOAL

Make every authored lesson a coherent experience in which students:
- Encounter a meaningful phenomenon or problem.
- Activate prior knowledge.
- Make a prediction or initial explanation.
- Investigate evidence.
- Connect observations to a physical model.
- Apply their understanding in a different situation.
- Check and revise their understanding.

Keep the physics rigorous, aligned with LOPS 2019, and written in
natural Finnish.

Engagement should come from curiosity, meaningful decisions, and
discovering relationships—not decorative animation or gamification.

1. BUILD A FLEXIBLE SHARED FRAMEWORK

Add a documented, versioned inquiry.json format alongside each
lesson’s existing files.

Support reusable activity types such as:
- Prediction with choices or a short explanation.
- Controlled simulation experiment.
- Open investigation with multiple valid solutions.
- Interpretation of a graph, table, diagram, or supplied measurements.
- Comparison of competing explanations.
- Error-spotting.
- Worked example with optional prediction steps.
- Numerical application.
- Written explanation with self-assessment criteria.
- Exit-ticket questions.

Implement the activity types needed by existing lessons first.
Do not build unused speculative features.

Separate:
- Lesson content and experiment definitions.
- Shared rendering and interaction behavior.
- Simulation-specific physics.

Validate lesson data and give useful errors identifying the lesson
and invalid field.

Preserve compatibility with existing content during migration.
Provide sensible rendering for lessons without simulations.

2. USE A COMMON LEARNING STRUCTURE WITHOUT FORCING IDENTICAL LESSONS

Use this default progression:

Herätä kiinnostus → Ennusta → Tutki → Selitä → Sovella →
Tarkista osaamisesi.

Allow stages to repeat, combine, or be omitted when pedagogically
justified. Do not render empty sections.

Choose activities according to the learning objective:
- Simulations when manipulating variables provides useful evidence.
- Graphs or measurements when interpreting evidence is central.
- Competing models when conceptual explanation is central.
- Worked examples when a calculation method needs scaffolding.
- Diagrams or supplied observations when simulation would add little.

Do not add a simulation to every lesson.
Do not turn every lesson into the same slider exercise.

Place a meaningful student action near the beginning.
Keep full theory and navigation accessible.
Gate answer feedback where appropriate, not access to the material.

3. CONNECT LESSONS INTO A LEARNING PROGRESSION

Use curriculum goals and prerequisites to identify:
- What students should already know.
- What this lesson introduces.
- What later lessons will develop.

Start with a short retrieval or prediction that uses prior learning.
Avoid repeating entire explanations from preceding lessons.

Make the new conceptual contribution explicit.
Use consistent terminology, symbols, units, and representations
across lessons.

Do not reveal a later lesson’s entire investigation prematurely.

4. DESIGN PURPOSEFUL INVESTIGATIONS

For each lesson, choose a small number of high-value activities.

Where applicable:
- Present a puzzle or competing explanations.
- Ask students to commit to a prediction.
- Offer an optional justification.
- Let students collect or inspect evidence.
- Show their initial prediction during reflection.
- Ask whether they would revise it and why.
- Return to the opening question.

Treat revising an explanation as normal scientific reasoning.

Include multiple-solution challenges where appropriate.
Avoid unnecessary required work; replace repetitive tasks rather
than continually adding activities.

Separate essential learning from optional exploration and practice.

5. STANDARDIZE SIMULATION INTEGRATION

Inspect existing simulations before changing them.
Retain useful behavior and existing test interfaces.

Provide a small consistent adapter for:
- Reading state.
- Setting supported parameters.
- Resetting.
- Pausing and resuming, where meaningful.

Preserve window.simState where already used.

Declare simulation capabilities so the framework does not display
unsupported controls.

Keep physical calculations inside the simulation or its model.
Do not duplicate equations in shared UI code.

Guided investigations must:
- Set explicit initial conditions.
- Identify controlled and adjustable variables.
- Lock appropriate controls.
- Compare initial and final measurements.
- Reset both parameters and animation state reliably.

Free exploration should remain available where appropriate.

Clearly distinguish:
- Predictions from observations.
- Model values from simulated measurements.
- Instantaneous values from averages.
- Representations from physical reality.

Explain assumptions and limitations briefly at the point of use.

6. CONNECT REPRESENTATIONS

Where educationally useful, connect:
- The physical phenomenon or diagram.
- Measurements and units.
- Graphs or tables.
- Verbal explanations.
- Mathematical relationships.

Use consistent labels and quantity conventions.

Do not display the answer to a prediction prematurely in a formula,
readout, caption, or feedback panel.

Do not remove equations merely to create artificial suspense when
students already learned them in a prerequisite lesson.

7. IMPROVE ASSESSMENT AND FEEDBACK

Support:
- Numeric answers with explicit units and tolerance semantics.
- Multiple choice with misconception-specific feedback.
- Predictions followed by evidence-based comparison.
- Written explanations with model answers or assessment criteria.

For numerical inputs:
- Accept Finnish decimal commas and decimal points.
- Handle empty, invalid, and non-finite values.
- Permit retries.
- Explain common mistakes when they can be identified reliably.
- Avoid fragile exact floating-point comparisons.

Do not pretend to assess written reasoning with a numerical checker.
Separate numerical and explanation components when needed.

Use progressive optional hints:
1. A guiding question.
2. A relevant representation or relationship.
3. An intermediate worked step.

Include error-spotting and transfer tasks where they serve the lesson.
Do not require every activity type in every lesson.

Preserve differentiated practice and repository-required exercise
counts unless a change is explicitly authorized.

Finish each lesson with three concise checks covering:
- Conceptual understanding.
- Quantitative or representational application.
- Explanation or transfer.

Adapt these to the lesson’s goals rather than forcing calculations
into lessons where they are inappropriate.

8. ACCESSIBILITY AND PRESENTATION

Follow the existing visual conventions.

Provide:
- Responsive mobile and desktop layouts.
- Native accessible controls.
- Keyboard operation and visible focus.
- Clear labels, instructions, and units.
- Feedback that does not depend on color.
- Reduced-motion support.
- Textual access to important visual information.
- Screen-reader feedback that avoids announcing continuous updates.

Keep instructions short and near the relevant action.
Avoid excessive clicking and unnecessarily fragmented reading.

Optional paired-discussion suggestions must also work independently.

Do not add accounts, tracking, messaging, points, badges, confetti,
a backend, or major dependencies.
Maintain static GitHub Pages compatibility.

9. MIGRATE ALL EXISTING AUTHORED LESSONS

First validate the shared architecture with fy3-2.
Then continue through every existing authored lesson.

For each:
- Check goals and prerequisites.
- Choose appropriate inquiry activities.
- Preserve useful theory, exercises, and simulations.
- Add lesson-specific feedback and reflection.
- Check scientific accuracy.
- Run relevant validation.

Do not mechanically copy the pilot’s questions or interactions.

For curriculum slots without content:
- Leave them clearly identified as unauthored.
- Provide reusable authoring guidance and examples.
- Do not present empty inquiry shells as completed lessons.

If a lesson cannot be migrated, identify the exact blocker.
Do not silently omit it or claim site-wide completion.

10. UPDATE FUTURE AUTHORING AND REVIEW

Update relevant authoring commands, templates, examples, and reviewer
instructions so inquiry design is the default for future lessons.

Authors should specify:
- Learning goals and prerequisites.
- The lesson’s new conceptual contribution.
- A motivating question.
- What students predict.
- What evidence they inspect or collect.
- How evidence connects to the model.
- Likely misconceptions and corresponding feedback.
- A transfer task.
- Appropriate checks of understanding.

Reviewer criteria must evaluate:
- Physics and mathematics.
- Alignment with prerequisites and curriculum.
- Quality of student reasoning.
- Meaningful use of interaction.
- Control of experimental variables.
- Premature answer disclosure.
- Feedback quality.
- Accessibility and workload.

Document the data format, simulation interface, migration approach,
and how to author and test a new lesson.

Keep unrelated agent workflows unchanged.

11. TEST THE FRAMEWORK AND EVERY MIGRATED LESSON

Run existing relevant tests and add focused coverage for:
- Data validation.
- Backward compatibility.
- Each implemented activity type.
- Prediction and feedback sequencing.
- Controlled variables.
- Initial/final comparisons.
- Reset behavior.
- Numeric input handling and retries.
- Model-answer and self-assessment behavior.
- Keyboard interaction and mobile layout.
- Navigation and prerequisite links.

For each migrated lesson, verify that its intended activities render
and work, and that its physics assertions pass.

Use local HTTP browser testing if file:// access is restricted.
Do not disable browser security or weaken assertions.

Distinguish passed, failed, skipped, and unrun checks.
Do not claim that automated tests establish pedagogical effectiveness.

12. WORKING CONSTRAINTS

Preserve unrelated user changes.
Use ignored preview/ outputs for development.
Do not regenerate published site/ files.
Do not change reviewed status.
Do not commit, push, or publish.

Proceed through architecture, migration, authoring updates, and
validation without stopping after the first successful lesson.

FINISH

Report:
- Shared framework changes.
- Every authored lesson migrated and its validation outcome.
- Any authored lessons still blocked, with reasons.
- Curriculum slots that remain unauthored.
- Authoring and reviewer updates.
- Remaining limitations.
- A short classroom evaluation plan.

The classroom evaluation should examine whether students can explain
their experimental choices, interpret evidence, revise explanations,
and transfer ideas. Click counts and completion speed alone do not
demonstrate learning.
```
