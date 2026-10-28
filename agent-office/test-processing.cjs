// node agent-office/test-processing.cjs — work must take time; deployment needs evidence.
const assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const box={window:{}};vm.createContext(box);
for(const file of ['office-web-review.js','office-processing.js','office-floor.js','office-scene.js'])vm.runInContext(fs.readFileSync(__dirname+'/'+file,'utf8'),box);
const model=box.window.OfficeProcessing;
const text=[];
const ctx={fillRect(...values){assert(values.every(Number.isFinite));},fillText(s){text.push(s);},measureText(s){return {width:s.length*6};},save(){},restore(){},translate(){},scale(){}};
let phase=0;
const state={id:'sample',hash:'v1',eligible:true,science:{status:'PASS'},pedagogy:{status:'PASS'},checks:{passed:4,failed:0},included:true};
const scene=box.window.AgentOfficeScene.create({getContext:()=>ctx},{phase:()=>phase,state:()=>state,still:()=>true,speechEnabled:()=>false});
for(const [time,task] of [[10,'Calculations'],[11,'Simulation'],[12,'Exercises'],[13,'Mobile layout']]){
  phase=time;text.length=0;
  const frame=scene.draw();
  assert.equal(frame.testing.stage,'working');assert.equal(frame.testing.task,task);
  assert.deepEqual(Array.from(frame.positions.developer),[925,525],'Material waits beside the test operator');
  assert.deepEqual(Array.from(frame.positions.science),Array.from(box.window.OfficeFloor.home.science),'Reviews wait for the test period');
  assert(text.includes(task),'The active check is drawn on the testing screen');
}
phase=17;assert.equal(scene.draw().testing,null);
assert.deepEqual(Array.from(scene.draw().positions.developer),Array.from(box.window.OfficeFloor.home.developer));
state.science.status='FAIL';state.eligible=false;
for(phase of [37,38,39])assert.equal(scene.draw().testing.stage,'working','Corrections get a real illustrated re-test pause');
assert.equal(state.science.status,'FAIL','A re-test does not invent a passing review');
state.science.status='PASS';state.eligible=true;
phase=50;assert.equal(scene.draw().publication.stage,'waiting','HTML in Git is not publication approval');
state.publicationDecision={status:'approved',contentHash:'v1'};
phase=40;assert.equal(scene.draw().publication.stage,'delivery');
for(phase of [43,45,48]){
  const frame=scene.draw();assert.equal(frame.publication.stage,'working');assert(!frame.publication.deployed);
}
phase=50;text.length=0;assert.equal(scene.draw().publication.stage,'unverified');
assert(!text.includes('Published version'),'Preparation cannot invent deployment success');
state.deploymentDecision={status:'published',contentHash:'old'};
assert(!scene.draw().publication.deployed,'An old deployment does not publish this version');
state.deploymentDecision.contentHash='v1';
phase=48.5;assert(scene.draw().publication.transfer);assert(!scene.draw().publication.deployed);
phase=49;text.length=0;assert(scene.draw().publication.deployed);assert(text.includes('Published version'));
state.deploymentDecision.status='failed';assert(scene.draw().publication.failed);assert(!scene.draw().publication.deployed);
state.publicationDecision.contentHash='old';assert.equal(scene.draw().publication.stage,'waiting');
assert.equal(model.testing(38,{external:true,retry:true}).stage,'working');
assert.equal(model.testing(42,{external:true,retry:true}),null,'External example remains a 42-second cycle');
console.log('PASS: material waits during four tests and re-tests; approval gates handoff; preparation, stale evidence and failure never claim successful deployment');
