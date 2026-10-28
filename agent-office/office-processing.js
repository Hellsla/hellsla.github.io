'use strict';
// Illustrative work periods; saved commit times never become measured task durations.
window.OfficeProcessing = {
  duration:56,
  testTasks:['Calculations','Simulation','Exercises','Mobile layout'],
  publishTasks:['Collecting pages','Checking the bundle','Preparing upload','Deployment handoff'],
  testing(phase,{external=false,retry=false,material=true}={}) {
    if(!material)return null;
    const cycle=phase%(external?42:this.duration);
    const [start,arrival,finish,end]=retry?[35,37,40,42]:[7,10,13.5,17];
    if(cycle<start || cycle>=end)return null;
    const stage=cycle<arrival?'delivery':cycle<finish?'working':'returning';
    const progress=Math.max(0,Math.min(1,(cycle-arrival)/(finish-arrival)));
    return {stage,progress,start,arrival,finish,end,
      task:this.testTasks[Math.min(3,Math.floor(progress*4))],
      travel:stage==='delivery'?(cycle-start)/(arrival-start):stage==='returning'?(cycle-finish)/(end-finish):0};
  },
  publication(phase,state) {
    const cycle=phase%this.duration;
    const approved=Boolean(state?.eligible && state.science?.status==='PASS' && state.pedagogy?.status==='PASS' && cycle>=38 && state.publicationDecision?.status==='approved' && state.publicationDecision.contentHash===state.hash);
    const matching=approved && state.deploymentDecision?.contentHash===state.hash;
    const deployed=Boolean(matching && state.deploymentDecision.status==='published' && cycle>=49);
    const failed=Boolean(matching && state.deploymentDecision.status==='failed' && cycle>=49);
    const stage=!approved?'waiting':cycle<39?'approved':cycle<43?'delivery':cycle<49?'working':deployed?'published':failed?'failed':'unverified';
    const progress=Math.max(0,Math.min(1,(cycle-43)/6));
    return {approved,deployed,failed,stage,progress,
      transfer:Boolean(matching && state.deploymentDecision.status==='published' && cycle>=48 && cycle<49),
      transferProgress:Math.max(0,Math.min(1,cycle-48)),
      task:this.publishTasks[Math.min(3,Math.floor(progress*4))]};
  }
};
