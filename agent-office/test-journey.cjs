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

const extra={events:['x','y','z'].map((id,snapshot)=>({id,snapshot})),snapshots:[
  [{...material('same-lesson','PASS','PASS'),work:{entries:1},exercises:{hash:'e1'}}],
  [{...material('same-lesson','PASS','PASS'),work:{entries:2},exercises:{hash:'e1'}}],
  [{...material('same-lesson','PASS','PASS'),work:{entries:2},exercises:{hash:'e2'}}]
]};
const independent=build(extra,{z:'y',y:'x'},extra.events[2],'sample');
assert.equal(independent.length,3,'Recorded work and exercise changes are not lost when the lesson hash stays fixed');
assert.deepEqual(Array.from(independent,f=>f.version),[1,1,1],'Exercise edits do not invent new lesson versions');
console.log('PASS: work records and independent exercise updates remain visible without changing the lesson version');

const branches={events:[{id:'root',snapshot:0},{id:'main',snapshot:1},{id:'review1',snapshot:2},{id:'review2',snapshot:3},{id:'merge',snapshot:3}],snapshots:[
  [material('initial','missing','missing')],[material('initial','missing','missing')],
  [material('revised','FAIL','PASS')],[material('revised','PASS','PASS')]
]};
const merged=build(branches,{merge:'main',main:'root',review2:'review1',review1:'root',_parents:{merge:['main','review2']}},branches.events.at(-1),'sample');
assert.deepEqual(Array.from(merged,f=>f.event.id),['root','review1','review2'],'A real merge follows the branch carrying this material, including its correction rounds');
console.log('PASS: merged material journeys retain review rounds from their actual source branch');
