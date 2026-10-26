'use strict';
// A spatial explanation of the workflow. Recorded evidence is supplied by office.js.
window.AgentOfficeScene = {
  create(canvas, options) {
    const ctx = canvas.getContext('2d');
    const C = {ink:'#ece4ce',muted:'#b8b8a9',gold:'#edba70',blue:'#8cb8e0',pink:'#e9a1b4',green:'#9ccb9b',red:'#e89885',amber:'#d7b474'};
    const stations = [
      {id:'developer',x:18,y:18,w:398,h:270,title:'DEVELOPMENT WORKSHOP',sub:'Text · exercises · simulations',floor:'#4b5350',accent:C.gold},
      {id:'science',x:430,y:18,w:357,h:270,title:'SCIENCE REVIEW',sub:'Independent physics & mathematics',floor:'#415861',accent:C.blue},
      {id:'pedagogy',x:801,y:18,w:381,h:270,title:'PEDAGOGY REVIEW',sub:'Independent learning & usability',floor:'#5b4d5b',accent:C.pink},
      {id:'teacher',x:18,y:535,w:310,h:247,title:'THE TEACHER',sub:'A question worth exploring',floor:'#66543e',accent:C.gold},
      {id:'checks',x:342,y:535,w:306,h:247,title:'AUTOMATIC CHECKS',sub:'Build · tests · layout',floor:'#414f50',accent:C.amber},
      {id:'repository',x:662,y:535,w:240,h:247,title:'PUBLICATION DECISION',sub:'The teacher decides',floor:'#4d5947',accent:C.green},
      {id:'site',x:916,y:535,w:266,h:247,title:'THE WEBSITE',sub:'A separate deployment',floor:'#4e525e',accent:'#c0b5db'}
    ];
    const home = {teacher:[150,668],developer:[212,202],science:[605,202],pedagogy:[990,202],gatekeeper:[739,425]};
    const colors = {teacher:'#e5dfbd',developer:C.gold,science:C.blue,pedagogy:C.pink,gatekeeper:'#a9bec6'};
    let figurePositions=[];
    function box(x,y,w,h,color){ctx.fillStyle=color;ctx.fillRect(Math.round(x),Math.round(y),w,h);}
    function text(s,x,y,color=C.ink,size=13,align='left') {ctx.font=`${size}px monospace`;ctx.textAlign=align;ctx.fillStyle=color;ctx.fillText(s,x,y);}
    function pill(s,x,y,color=C.gold,w=120){box(x-w/2,y-14,w,22,'#222d31');text(s,x,y+1,color,11,'center');}
    function plant(x,y){box(x-11,y,22,19,'#ad8060');box(x-14,y-2,28,5,'#c49b70');box(x-2,y-36,4,36,'#7f9863');box(x-19,y-24,18,9,'#8aaa72');box(x+2,y-36,18,11,'#98b37a');box(x-12,y-46,12,12,'#6c8b58');}
    function shelf(x,y,w=105){box(x,y,w,54,'#806e53');for(let row=0;row<2;row++){box(x+5,y+5+row*23,w-10,19,'#2e3a39');for(let i=0;i<Math.floor((w-10)/9);i++)box(x+7+i*9,y+8+row*23+(i%2)*3,6,14-(i%2)*3,['#c6a16c','#8daaa0','#b8827d','#a5a6bd'][i%4]);box(x,y+23+row*23,w,4,'#a18a65');}}
    function room(s){
      box(s.x,s.y,s.w,s.h,'#243236');box(s.x+6,s.y+6,s.w-12,s.h-12,s.floor);
      for(let y=s.y+8;y<s.y+s.h-8;y+=24)for(let x=s.x+7;x<s.x+s.w-7;x+=48){box(x,y,46,1,'#ffffff09');box(x,y,1,23,'#00000012');}
      box(s.x+6,s.y+6,s.w-12,44,'#293638');box(s.x+6,s.y+6,4,44,s.accent);
      text(s.title,s.x+18,s.y+26,s.accent,13);text(s.sub,s.x+18,s.y+43,'#b9c4bc',10);
      // Every room opens onto the common corridor.
      const door=s.id==='developer'?230:s.id==='science'?610:s.id==='pedagogy'?990:s.x+s.w/2;
      const y=s.y<300?s.y+s.h-7:s.y;
      box(door-28,y,56,8,'#9e9274');box(door-23,y+2,46,3,'#c3b18a');
    }
    function desk(x,y,color,on=false){
      box(x-80,y+11,160,13,'#342f2b');box(x-76,y+23,7,26,'#5a5042');box(x+66,y+23,7,26,'#5a5042');
      box(x-83,y-17,166,34,'#9b8262');box(x-83,y+14,166,7,'#b9a07a');
      box(x-56,y-73,77,49,'#1c2c32');box(x-51,y-68,67,39,on?'#43665d':'#30494e');
      for(let i=0;i<4;i++){box(x-46,y-61+i*7,18+(i%3)*12,2,color);box(x-18+(i%2)*7,y-61+i*7,14,2,'#a1bca0');}
      box(x-25,y-23,9,6,'#28353a');box(x-36,y-18,32,4,'#29363a');box(x-48,y-6,62,11,'#485452');
      for(let i=0;i<7;i++)box(x-44+i*8,y-3,5,2,'#9ea79b');
      box(x+46,y-9,18,17,'#e6dabb');box(x+63,y-5,5,9,'#bba887');
      box(x-16,y+38,33,24,'#33484b');
    }
    function pagePacket(x,y,lid,color,kind='LESSON'){
      box(x-9,y-12,18,24,'#e9dfbe');box(x-5,y-7,11,3,color);box(x-5,y-1,10,2,'#86836e');box(x-5,y+4,8,2,'#86836e');
      pill(`${lid.toUpperCase()} · ${kind}`,x,y-24,color,Math.max(98,(lid.length+kind.length+3)*6.5));
    }
    function person(x,y,color,moving=false,seed=0){
      const step=moving?Math.sin(options.phase()*8+seed)*3:0;
      box(x-13,y+32,29,6,'#243033');box(x-9,y+22,7,13+Math.round(step),'#2c3c43');box(x+4,y+22,7,13-Math.round(step),'#2c3c43');
      box(x-14,y,29,25,color);box(x-12,y-23,24,25,'#d3b18d');box(x-14,y-26,28,9,seed%2?'#493c36':'#5c503e');box(x-14,y-17,5,11,'#493c36');
      box(x+2,y-10,3,3,'#303738');box(x+9,y-10,3,3,'#303738');box(x-19,y+7,7,15,color);box(x+15,y+8,7,14,color);
    }
    function position(points,fraction){
      const lengths=points.slice(1).map((p,i)=>Math.hypot(p[0]-points[i][0],p[1]-points[i][1]));
      let d=Math.max(0,Math.min(1,fraction))*lengths.reduce((a,b)=>a+b,0),i=0;
      while(i<lengths.length-1 && d>lengths[i])d-=lengths[i++];
      const t=lengths[i]?d/lengths[i]:0;
      return [points[i][0]+(points[i+1][0]-points[i][0])*t,points[i][1]+(points[i+1][1]-points[i][1])*t];
    }
    function lane(points,color,blocked=false){
      ctx.strokeStyle=color;ctx.lineWidth=3;ctx.setLineDash(blocked?[3,8]:[8,7]);ctx.beginPath();ctx.moveTo(...points[0]);for(const p of points.slice(1))ctx.lineTo(...p);ctx.stroke();ctx.setLineDash([]);
      const a=points.at(-2),b=points.at(-1),angle=Math.atan2(b[1]-a[1],b[0]-a[0]);
      ctx.beginPath();ctx.moveTo(...b);ctx.lineTo(b[0]-10*Math.cos(angle-.5),b[1]-10*Math.sin(angle-.5));ctx.lineTo(b[0]-10*Math.cos(angle+.5),b[1]-10*Math.sin(angle+.5));ctx.closePath();ctx.fillStyle=color;ctx.fill();
    }
    const journeys={
      brief:[[150,668],[173,535],[173,335],[230,335],[212,202]],
      checks:[[212,202],[230,335],[495,335],[495,654]],
      science:[[605,202],[610,318],[495,318],[495,654],[495,318],[610,318],[605,202]],
      pedagogy:[[990,202],[990,346],[522,346],[495,654],[522,346],[990,346],[990,202]],
      scienceReport:[[605,202],[610,325],[672,325],[716,425],[672,325],[610,325],[605,202]],
      pedagogyReport:[[990,202],[990,375],[830,375],[773,425],[830,375],[990,375],[990,202]],
      fix:[[212,202],[230,475],[682,475],[716,425],[682,475],[230,475],[212,202]],
      receive:[[150,668],[173,502],[736,502],[739,444],[789,502],[789,664]],
      home:[[789,664],[789,502],[173,502],[150,668]]
    };
    function actors(state){
      const cycle=options.phase()%42,step=Math.floor(cycle/7),f=(cycle%7)/7;
      const positions=Object.fromEntries(Object.entries(home).map(([id,p])=>[id,[...p]]));
      const packets={};const moving={};
      const walk=(id,points,t,kind,color)=>{positions[id]=position(points,t);moving[id]=!options.still();if(kind)packets[id]={kind,color:color||colors[id]};};
      if(state){
        if(step===0)walk('teacher',journeys.brief,f,'BRIEF');
        if(step===1){walk('teacher',[...journeys.brief].reverse(),f);walk('developer',journeys.checks,f,'LESSON');}
        if(step===2){walk('developer',[...journeys.checks].reverse(),f);for(const role of ['science','pedagogy'])walk(role,journeys[role],f,f>.5?'COPY':null);}
        if(step===3){for(const role of ['science','pedagogy'])if(state[role].status!=='missing')walk(role,journeys[role+'Report'],f,f<.5?'REPORT':null,state[role].status==='PASS'?C.green:C.red);}
        if(step===4){if(state.eligible)walk('teacher',journeys.receive,f,f>.78?'REVIEWED':null,C.green);else walk('developer',journeys.fix,f,f>.5?'REVISE':null,C.red);}
        if(step===5 && state.eligible)walk('teacher',journeys.home,f);
      }
      figurePositions=[];
      for(const [i,id] of ['developer','science','pedagogy','teacher'].entries()){
        const [x,y]=positions[id];person(x,y,colors[id],moving[id],i);
        figurePositions.push({id,x,y});
        if(moving[id])pill(id==='teacher'?'TEACHER':id.toUpperCase(),x,y+54,colors[id],id.length*8+24);
        if(packets[id])pagePacket(x+26,y+11,state.id,packets[id].color,packets[id].kind);
      }
      return step;
    }
    function checks(state){
      const x=495,y=650;
      box(x-67,y-57,134,96,'#243237');box(x-61,y-51,122,76,'#3b5051');
      text('CHECK RUNNER',x,y-32,C.ink,12,'center');
      for(const [i,label] of ['BUILD','SIM TESTS','LAYOUT'].entries()){
        box(x-51,y-20+i*14,6,6,C.amber);text(label,x-36,y-13+i*14,'#b7c5bb',10);
      }
      text(state?.checks.failed?`${state.checks.failed} SAVED FAILURES`:state?.checks.passed?`${state.checks.passed} SAVED PASSES`:'NO SAVED RESULTS',x,718,state?.checks.failed?C.red:C.amber,12,'center');
      text('Freshness / CI unknown',x,738,C.muted,10,'center');
      box(372,596,24,80,'#253239');for(let i=0;i<5;i++){box(376,602+i*13,15,8,'#556669');box(378,604+i*13,3,3,C.amber);}
    }
    function gate(state){
      const open=Boolean(state?.eligible),color=!state?C.muted:open?C.green:C.red;
      const approvals=state?['science','pedagogy'].filter(r=>state[r].status==='PASS').length:'–';
      box(695,397,137,79,'#29383b');box(695,397,137,4,color);
      person(724,426,'#a9bec6',false,4);box(709,399,28,6,'#324d59');box(707,405,33,3,'#617f8a');box(719,400,7,4,C.gold);
      box(701,427,17,24,'#ad946c');box(704,431,11,16,'#eee1bd');
      ['science','pedagogy'].forEach((r,i)=>box(706,434+i*6,6,3,state?.[r].status==='PASS'?C.green:C.red));
      text('REVIEW GATE',768,385,C.ink,13,'center');
      pill(!state?'WAITING':open?'OPEN':'CLOSED',796,430,color,70);text(`${approvals}/2 PASS`,793,452,color,11,'center');
      box(786,476,5,28,'#687b76');
      box(739,434,13,6,'#a9bec6');box(749,432,7,7,'#d3b18d');
      if(open)box(787,471,5,28,'#b9c8ad');else{box(752,427,3,11,'#a18d6b');box(747,416,13,12,C.red);box(750,420,7,3,'#f0e3c6');box(791,477,41,6,'#c99b87');for(let x=795;x<832;x+=11)box(x,477,4,6,'#eddec4');}
    }
    function site(state){
      box(953,596,191,116,'#26323a');box(959,602,179,102,'#e1dfce');box(959,602,179,17,'#607d77');
      for(let i=0;i<3;i++)box(965+i*7,607,4,4,'#cfdfbd');
      text('FYSIIKKALABRA',1048,640,'#40544d',13,'center');
      box(974,651,68,40,'#b8c7b1');box(1049,651,74,5,'#9da99e');box(1049,663,65,4,'#b1b5a4');box(1049,674,71,4,'#b1b5a4');
      text(state?.included?'HTML IN COMMIT':'NO HTML IN SNAPSHOT',1048,735,state?.included?C.green:C.muted,12,'center');
      text('Deployment unverified',1048,754,C.amber,11,'center');
    }
    function draw(){
      const state=options.state();const active=options.active();
      ctx.imageSmoothingEnabled=false;box(0,0,1200,800,'#202c30');
      box(18,301,1164,221,'#8a7356');
      for(let y=306;y<522;y+=22)for(let x=20;x<1182;x+=68){box(x+(y%44?-20:0),y,65,1,'#a58c69');box(x,y,1,21,'#716148');}
      stations.forEach(room);
      // Distinct rooms make the split into two independent reviewers visible.
      shelf(40,78,125);shelf(252,78,135);shelf(455,78,124);shelf(636,78,124);shelf(827,78,124);shelf(1022,78,130);
      desk(212,190,C.gold,active.has('developer'));desk(605,190,C.blue,active.has('science'));desk(990,190,C.pink,active.has('pedagogy'));
      pill('1 · DEVELOP',212,257,C.gold,150);
      for(const [id,x] of [['science',605],['pedagogy',990]]){
        const status=state?.[id].status || 'NOT OBSERVED';
        pill(status==='PASS'?'PASS · SAME VERSION':status.toUpperCase(),x,257,status==='PASS'?C.green:status==='FAIL'?C.red:C.amber,198);
      }
      plant(380,245);plant(753,245);plant(1148,245);
      // Teacher's planning room and the deliberately empty sign-off desk share one human.
      desk(150,656,C.gold);box(42,595,34,42,'#d9d3ba');text('?',59,624,'#60756a',24,'center');
      shelf(207,595,90);plant(53,745);text('BRIEF & ASSIGN',173,743,C.gold,12,'center');
      desk(789,656,C.green);box(732,711,116,28,'#243631');text(options.event()?.merge?'MERGE RECORDED':'DECISION UNKNOWN',790,730,C.amber,10,'center');
      if(options.event()?.merge)text('Approver unverified',790,757,C.muted,10,'center');
      // Lesson routes use the shared corridor, never walls or the other reviewer's desk.
      lane([[173,535],[173,325],[230,325],[230,288]],'#c6ad78');
      lane([[249,288],[249,357],[471,357],[471,535]],'#c6ad78');
      lane([[495,535],[495,320],[610,320],[610,288]],'#86acc2');
      lane([[522,535],[522,345],[990,345],[990,288]],'#bd93a7');
      lane([[632,288],[632,370],[714,397]],state?.science.status==='PASS'?'#8cb8e0':'#96877b');
      lane([[1020,288],[1020,370],[818,397]],state?.pedagogy.status==='PASS'?'#e9a1b4':'#96877b');
      if(state?.eligible)lane([[789,505],[789,535]],C.green);else if(state)lane([[695,455],[652,485],[272,485],[272,288]],'#cf957c');
      // The final link is a proposed route, not a claim of deployment.
      lane([[902,658],[953,658]],C.amber,true);pill('DEPLOY ?',927,704,C.amber,89);
      pill('2 · CHECK',484,508,C.amber,132);pill('3 · INDEPENDENT REVIEWS',779,318,C.ink,259);
      pill('5 · HUMAN DECISION',790,516,C.gold,197);text('4 · MATCH BOTH APPROVALS',770,363,'#e9dfc8',11,'center');
      box(28,398,314,52,'#2f3e3e');text('ONE LESSON. TWO INDEPENDENT REVIEWS.',185,419,C.ink,12,'center');
      text(state?`${state.id.toUpperCase()}  /  ${state.hash || 'HASH UNAVAILABLE'}`:'SELECT A RECORDED LESSON',185,438,C.gold,11,'center');
      checks(state);site(state);gate(state);const step=actors(state);
      box(22,786,1156,11,'#202c30');text('WORKFLOW ILLUSTRATION · COURIER MOVEMENT IS NOT A SESSION LOG',30,795,'#c1c5b7',9);
      return {step,caption:this.caption(step,state)};
    }
    function caption(step,state){
      if(!state)return 'Choose a recorded lesson to explore its route through the office.';
      return [
        'The teacher brings a brief to the developer.',
        'The developer brings the lesson packet to automatic checks.',
        'The two independent reviewers collect separate copies of the lesson.',
        ['science','pedagogy'].every(role=>state[role].status==='missing')?'The gate waits for both independent review reports.':'Available review reports go to the gate; missing or stale approvals cannot open it.',
        state.eligible?'Both current reviews pass. The teacher receives the lesson for a publication decision.':'The gate stays closed. The lesson returns to the developer for revision or renewed review.',
        'Publication is a human decision. Website deployment is a separate, unverified step.'
      ][step];
    }
    function hit(p){
      const figure=figurePositions.find(f=>Math.abs(p.x-f.x)<27 && p.y>f.y-32 && p.y<f.y+40);
      if(figure)return figure.id;
      if(p.x>=688 && p.x<=838 && p.y>=370 && p.y<=510)return 'gatekeeper';
      return stations.find(s=>p.x>=s.x && p.x<=s.x+s.w && p.y>=s.y && p.y<=s.y+s.h)?.id;
    }
    return {draw,hit,caption};
  }
};
