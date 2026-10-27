// node agent-office/test-web-review.cjs — no dependencies.
const assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const sandbox={window:{}};vm.createContext(sandbox);
for(const file of ['office-web-review.js','office-scene.js'])vm.runInContext(fs.readFileSync(__dirname+'/'+file,'utf8'),sandbox);
const labels=[];
const ctx={fillRect(...values){assert(values.every(Number.isFinite));},fillText(value){labels.push(value);},measureText(value){return {width:value.length*7};},save(){},restore(){},translate(){},scale(){}};
const state={id:'lesson',hash:'123abc',title:'A recorded lesson',eligible:true,science:{status:'PASS'},pedagogy:{status:'PASS'},checks:{passed:8,failed:0},included:true,publicationDecision:{status:'approved',contentHash:'123abc'}};
const before=JSON.stringify(state);let phase=0,external=true;
const scene=sandbox.window.AgentOfficeScene.create({getContext:()=>ctx},{state:()=>state,active:()=>new Set(),phase:()=>phase,still:()=>true,wholeWebReview:()=>external,speechEnabled:()=>true,event:()=>({merge:true})});
for(let index=0;index<6;index++){
  phase=index*7;labels.length=0;
  const result=scene.draw();
  assert.equal(result.step,index);
  assert.equal(result.caption,sandbox.window.OfficeWebReview.stages[index].caption);
  assert(!labels.some(text=>/RECORDED PASS|APPROVED|8 SAVED PASSES|A recorded lesson/.test(text)),'External illustration cannot reuse lesson approvals or claim completion');
  assert.equal(scene.nextHandoff(),index===5?0:(index+1)*7);
}
assert.equal(scene.hit({x:1100,y:400}),'chatgpt','The external review room is inspectable');
for(phase=0;phase<42;phase+=0.4)scene.draw(); // Exercise intermediate courier positions.
phase=42;assert.equal(scene.draw().step,0,'The illustrative feedback cycle can repeat');
external=false;phase=34;labels.length=0;scene.draw();
assert(labels.includes('RECORDED PASS'),'Returning to material mode restores its recorded evidence');
assert.equal(JSON.stringify(state),before,'Illustration never mutates material evidence');
console.log('PASS: six external-review stages, handoff stepping, repeat, room inspection and separation from recorded approvals');

// Publication must follow Lauri's visit, even when matching approval evidence exists.
external=false;
phase=31;scene.draw();assert.equal(scene.hit({x:150,y:668}),'teacher');
phase=34;assert.match(scene.draw().caption,/Lauri walks to the publisher/);
for(phase of [35,37]){
  labels.length=0;scene.draw();
  assert.equal(scene.hit({x:724,y:674}),'teacher','Lauri meets the publisher');
  assert(!labels.includes('APPROVED'),'Publication decision cannot precede the discussion');
}
phase=38;labels.length=0;scene.draw();assert(labels.includes('APPROVED'));
const approval=state.publicationDecision;delete state.publicationDecision;
phase=39.5;labels.length=0;scene.draw();
assert(!labels.includes('APPROVED'),'The illustrated visit cannot invent approval evidence');
state.publicationDecision=approval;
assert.equal(JSON.stringify(state),before);
assert(scene.portrait,'Human roles expose a portrait renderer');
console.log('PASS: Lauri visits the publisher before the decision; a visit alone never grants approval');
