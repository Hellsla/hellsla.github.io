// node agent-office/test-floor.cjs — routes, fixtures and conversations share one floor.
const assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const sandbox={window:{}};vm.createContext(sandbox);
for(const file of ['office-web-review.js','office-floor.js','office-scene.js'])vm.runInContext(fs.readFileSync(__dirname+'/'+file,'utf8'),sandbox);
const floor=sandbox.window.OfficeFloor;
const obstacles=[...floor.walls,[477,382,242,42],[400,664,186,32]];
const blocked=(x,y)=>obstacles.some(([left,top,width,height])=>x>left&&x<left+width&&y>top&&y<top+height);
for(const [name,path] of Object.entries(floor.paths)){
  for(let i=1;i<path.length;i++){
    const a=path[i-1],b=path[i],length=Math.ceil(Math.hypot(b[0]-a[0],b[1]-a[1]));
    for(let n=0;n<=length;n++){
      const t=n/Math.max(1,length),x=a[0]+(b[0]-a[0])*t,y=a[1]+(b[1]-a[1])*t;
      assert(!blocked(x,y),`${name} crosses a wall at ${x},${y}`);
    }
  }
}
const ctx={fillRect(...args){assert(args.every(Number.isFinite));},fillText(){},measureText(s){return {width:s.length*7};},save(){},restore(){},translate(){},scale(){}};
let phase=0,external=false;
const state={id:'test',hash:'abc',science:{status:'PASS'},pedagogy:{status:'PASS'},eligible:true,checks:{passed:2,failed:0}};
const scene=sandbox.window.AgentOfficeScene.create({getContext:()=>ctx},{state:()=>state,phase:()=>phase,still:()=>true,wholeWebReview:()=>external,speechEnabled:()=>true});
for(const status of ['PASS','FAIL','stale','missing']){
  state.science.status=status;state.eligible=status==='PASS';
  for(phase=0;phase<42;phase+=.25){
    const result=scene.draw();
    assert.equal(Object.keys(result.positions).length,9,'Nine human roles; inbox and display are fixtures');
    for(const [role,[x,y]] of Object.entries(result.positions))assert(!blocked(x,y),`${role} walks through a wall at ${phase}`);
  }
}
state.science.status='PASS';state.eligible=true;external=false;phase=13.99;
const delivery=scene.draw();
assert(Math.hypot(delivery.positions.developer[0]-delivery.positions.checks[0],delivery.positions.developer[1]-delivery.positions.checks[1])>80,'A visitor does not stand on the test operator');
phase=31.5;const coordinatorVisit=scene.draw();
assert.equal(coordinatorVisit.positions.orchestrator.facing[0],-1);
assert.equal(coordinatorVisit.positions.repository.facing[0],1);
phase=35;
const discussion=scene.draw();
assert.equal(discussion.positions.teacher.facing[0],1);
assert.equal(discussion.positions.repository.facing[0],-1,'The publisher faces Lauri during their discussion');
external=true;phase=14;
const meeting=scene.draw();
assert.equal(meeting.positions.teacher[0],floor.seats.meeting[0]);
assert.equal(meeting.positions.teacher.facing[0],-1,'Lauri faces the external reviewer');
assert(!('site' in meeting.positions));assert(!('gatekeeper' in meeting.positions));
assert.equal(scene.portrait('site'),false);assert.equal(scene.portrait('gatekeeper'),false);
assert.equal(scene.hit({x:700,y:450}),'gatekeeper');
assert.equal(scene.hit({x:1120,y:650}),'site');
console.log('PASS: all routes use open doors, nine people stay clear of walls, conversations face inward, inbox and website are inspectable fixtures');
