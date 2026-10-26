// Run with node agent-office/test-journey.cjs; no dependencies.
const assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const context={window:{}};vm.createContext(context);
vm.runInContext(fs.readFileSync(__dirname+'/office-journey.js','utf8'),context);
const build=context.window.OfficeJourney.build;
const material=(hash,science,pedagogy)=>({id:'sample',hash,science:{status:science},pedagogy:{status:pedagogy},eligible:science==='PASS'&&pedagogy==='PASS',checks:{passed:3,failed:0}});
const snapshots=[[material('v1','FAIL','PASS')],[material('other-branch','PASS','PASS')],[material('v2','missing','missing')],[material('v2','PASS','missing')],[material('v2','PASS','PASS')]];
const events=['a','branch','b','c','d','e'].map((id,i)=>({id,snapshot:Math.min(i,4)}));
const history={events,snapshots},lineage={e:'d',d:'c',c:'b',b:'a',branch:'a',a:null};
const frames=build(history,lineage,events.at(-1),'sample');
assert.deepEqual(Array.from(frames,f=>f.event.id),['a','b','c','d']);
assert.deepEqual(Array.from(frames,f=>f.version),[1,2,2,2]);
assert.equal(frames[0].state.science.status,'FAIL');
assert(!frames[1].state.eligible);assert(!frames[2].state.eligible);assert(frames[3].state.eligible);
assert.equal(build(history,{},events.at(-1),'sample').length,1,'Missing lineage never invents ancestors');
assert.equal(build(history,{...lineage,a:'e'},events.at(-1),'sample').length,4,'Bad cyclic metadata cannot hang playback');
assert.equal(build(history,lineage,events.at(-1),'absent').length,0);
console.log('PASS: correction stages follow ancestry, exclude other branches, invalidate old passes, deduplicate and stop at recorded evidence');
