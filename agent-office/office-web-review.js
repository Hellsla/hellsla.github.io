'use strict';
// A user-described workflow, deliberately separate from committed lesson evidence.
window.OfficeWebReview = {
  stages: [
    {speaker:'teacher', message:'Please review the whole webpage, not just one lesson.', caption:'Lauri asks an external reviewer for a whole-webpage review: structure, navigation, consistency and the experience across pages.'},
    {speaker:'chatgpt', message:'A fresh pair of eyes on the whole webpage.', caption:'The external reviewer receives the webpage and Lauri’s question. This external perspective sits alongside the Claude lesson workflow.'},
    {speaker:'chatgpt', message:'Do the pages make sense together?', caption:'The external review considers the broader experience: clarity, visual hierarchy, mobile usability and how the parts fit together.'},
    {speaker:'teacher', message:'Which suggestions should we take forward?', caption:'The external reviewer returns suggestions to Lauri. Lauri weighs them against teaching goals and decides what needs changing.'},
    {speaker:'developer', message:'A focused change brief, then back to development.', caption:'Lauri turns selected feedback into a change brief for Claude development. Suggestions are not automatic instructions or approvals.'},
    {speaker:'checks', message:'Changes need checks and another look.', caption:'The developer checks the changes. Affected lessons need current independent reviews; Lauri can request another whole-webpage review. Publication remains a separate decision.'}
  ],
  frame(phase) {
    const cycle=((phase % 42)+42)%42;
    const index=Math.floor(cycle/7);
    return {...this.stages[index],index,progress:(cycle%7)/7};
  }
};
