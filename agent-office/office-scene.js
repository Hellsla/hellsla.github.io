'use strict';
// A spatial explanation of the workflow. Recorded evidence is supplied by office.js.
window.AgentOfficeScene = {
  create(canvas, options) {
    const ctx = canvas.getContext('2d');
    const tr=value=>window.OfficeI18n?.t(value) ?? value;
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
    const home = {teacher:[150,668],developer:[212,202],science:[605,202],pedagogy:[990,202],repository:[789,668],gatekeeper:[735,447],site:[1048,685]};
    const colors = {teacher:'#e5dfbd',developer:C.gold,science:C.blue,pedagogy:C.pink,repository:'#b6c79f',gatekeeper:'#719b95',site:'#a69ac3'};
    const looks = {
      teacher:{skin:'#d5b399',hair:'#b9c1ba',shirt:'#e2d8bd',jacket:'#647a72',pants:'#46575b',hairStyle:'parted',glasses:true,beard:'#a5aaa0',scale:1.04},
      developer:{skin:'#b9815a',hair:'#302d2b',shirt:'#d8ad61',pants:'#424b60',hairStyle:'crop',headphones:true,beard:'#4b332b',scale:1},
      science:{skin:'#916550',hair:'#c0bbb1',shirt:'#8fb3cb',jacket:'#667f92',pants:'#5d5850',hairStyle:'curls',glasses:true,scale:1.08},
      pedagogy:{skin:'#e1bda3',hair:'#69434a',shirt:'#e4d5c5',jacket:'#b77c91',pants:'#534c66',hairStyle:'braid',scale:.96},
      gatekeeper:{skin:'#d2aa82',hair:'#71523e',shirt:'#dcdcc9',jacket:'#719b95',pants:'#4d605d',hairStyle:'bun',glasses:true,scale:.99},
      repository:{skin:'#b38b69',hair:'#6d6050',shirt:'#e7ddc8',jacket:'#95a87a',pants:'#555d50',hairStyle:'bald',beard:'#8b7760',tie:true,scale:1.03},
      site:{skin:'#9b6d53',hair:'#bc8754',shirt:'#a69ac3',pants:'#4d5371',hairStyle:'swept',satchel:true,scale:.97}
    };
    let figurePositions=[];
    function box(x,y,w,h,color){ctx.fillStyle=color;ctx.fillRect(x,y,w,h);}
    function text(s,x,y,color=C.ink,size=13,align='left') {ctx.font=`${size}px monospace`;ctx.textAlign=align;ctx.fillStyle=color;ctx.fillText(tr(s),x,y);}
    function pill(s,x,y,color=C.gold,w=120){ctx.font='11px monospace';w=Math.max(w,(ctx.measureText?.(tr(s)).width || tr(s).length*6.6)+16);box(x-w/2,y-14,w,22,'#222d31');text(s,x,y+1,color,11,'center');}
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
      pill(`${lid.toUpperCase()} · ${kind}`,x,y-52,color,Math.max(98,(lid.length+kind.length+3)*6.5));
    }
    function person(x,y,id,moving=false,carrying=false,facing=[1,0]){
      const look=looks[id],seed=Object.keys(looks).indexOf(id);
      const gait=moving?Math.sin(options.phase()*6+seed)*2.1:0;
      const bob=moving?Math.cos(options.phase()*12+seed)*.55:0;
      const back=moving && facing[1]<-.65 && Math.abs(facing[1])>Math.abs(facing[0]);
      ctx.save();ctx.translate(x,y);ctx.scale(look.scale,look.scale);
      box(-14,34,31,4,'#263437');
      if(moving && facing[0]<-.1)ctx.scale(-1,1);
      box(-9,22+gait,7,12,look.pants);box(4,22-gait,7,12,look.pants);
      box(-11,31+gait,10,4,'#e0d8c6');box(3,31-gait,10,4,'#ddd8cb');
      ctx.translate(0,bob);
      const coat=look.jacket || look.shirt;
      box(-14,0,29,25,coat);box(-5,0,10,23,look.shirt);
      if(look.jacket){box(-6,0,2,22,'#ffffff20');box(5,0,2,22,'#00000020');}
      if(id==='developer'){box(-5,1,2,8,'#e8d4a4');box(5,1,2,8,'#e8d4a4');box(-9,16,19,5,'#c39850');}
      if(look.tie && !back){box(-1,1,4,15,'#795a68');box(-2,15,6,4,'#795a68');}
      box(-19,7-gait,7,14,coat);box(-19,19-gait,7,5,look.skin);
      box(15,carrying?5:7+gait,7,carrying?10:14,coat);box(15,carrying?13:19+gait,7,5,look.skin);
      box(-4,-3,10,7,look.skin);box(-12,-23,24,24,back?look.hair:look.skin);
      if(look.hairStyle==='curls'){
        for(let i=0;i<5;i++){box(-14+i*6,-27-(i%2)*3,8,9,look.hair);}
        box(-15,-20,5,10,look.hair);box(10,-20,5,10,look.hair);
      }else if(look.hairStyle==='bald'){
        box(-13,-19,4,12,look.hair);box(10,-19,4,12,look.hair);box(-8,-25,6,3,look.hair);
      }else{
        box(-14,-26,28,8,look.hair);box(-14,-19,5,12,look.hair);
        if(look.hairStyle==='parted'){box(-1,-27,3,8,'#d8dbd0');box(8,-19,6,5,look.hair);}
        if(look.hairStyle==='crop'){box(-10,-29,6,4,look.hair);box(-2,-30,5,5,look.hair);}
        if(look.hairStyle==='braid'){box(-17,-21,7,29,look.hair);box(-16,7,5,9,look.hair);box(-16,11,5,3,'#d7b786');}
        if(look.hairStyle==='bun'){box(-20,-27,10,10,look.hair);box(7,-20,7,9,look.hair);}
        if(look.hairStyle==='swept'){box(-8,-30,21,6,look.hair);box(7,-25,9,10,look.hair);}
      }
      if(!back){
        box(2,-12,3,3,'#313437');box(9,-12,3,3,'#313437');box(5,-4,5,2,'#8e6353');
        if(look.beard){box(-7,-6,18,6,look.beard);box(-4,-1,12,3,look.beard);box(4,-5,5,2,look.skin);}
        if(look.glasses){box(-2,-15,7,2,'#3e4b4b');box(7,-15,7,2,'#3e4b4b');box(-2,-14,2,6,'#3e4b4b');box(4,-14,2,6,'#3e4b4b');box(7,-14,2,6,'#3e4b4b');box(13,-14,2,6,'#3e4b4b');box(0,-9,5,2,'#3e4b4b');box(9,-9,5,2,'#3e4b4b');box(5,-13,3,2,'#3e4b4b');}
      }
      if(look.headphones){box(-16,-24,30,3,'#cd8054');box(-18,-20,6,13,'#d89558');box(12,-20,6,13,'#d89558');}
      if(look.satchel){for(let i=0;i<6;i++)box(-12+i*4,1+i*3,4,4,'#77644f');box(7,13,15,14,'#b59163');box(10,17,9,2,'#dbc29b');}
      ctx.restore();
    }
    const pathCache=new WeakMap();
    const ease=t=>t*t*(3-2*t);
    function preparedPath(points){
      if(pathCache.has(points))return pathCache.get(points);
      const rounded=[points[0]];
      for(let i=1;i<points.length-1;i++){
        const a=points[i-1],b=points[i],c=points[i+1];
        const incoming=Math.hypot(b[0]-a[0],b[1]-a[1]),outgoing=Math.hypot(c[0]-b[0],c[1]-b[1]);
        const u=[(b[0]-a[0])/incoming,(b[1]-a[1])/incoming],v=[(c[0]-b[0])/outgoing,(c[1]-b[1])/outgoing];
        if(!incoming || !outgoing || u[0]*v[0]+u[1]*v[1]<-.95){rounded.push(b);continue;}
        const radius=Math.min(18,incoming/3,outgoing/3);
        const entry=[b[0]-u[0]*radius,b[1]-u[1]*radius],exit=[b[0]+v[0]*radius,b[1]+v[1]*radius];
        rounded.push(entry);
        for(let sample=1;sample<=8;sample++){const t=sample/8,s=1-t;rounded.push([s*s*entry[0]+2*s*t*b[0]+t*t*exit[0],s*s*entry[1]+2*s*t*b[1]+t*t*exit[1]]);}
      }
      rounded.push(points.at(-1));
      const lengths=rounded.slice(1).map((p,i)=>Math.hypot(p[0]-rounded[i][0],p[1]-rounded[i][1]));
      const result={points:rounded,lengths,total:lengths.reduce((a,b)=>a+b,0),roundTrip:points[0][0]===points.at(-1)[0]&&points[0][1]===points.at(-1)[1]};pathCache.set(points,result);return result;
    }
    function position(points,fraction){
      const path=preparedPath(points),f=Math.max(0,Math.min(1,fraction));
      const progress=path.roundTrip?(f<.5?ease(f*2)/2:.5+ease((f-.5)*2)/2):ease(f);
      let d=progress*path.total,i=0;
      while(i<path.lengths.length-1 && d>path.lengths[i])d-=path.lengths[i++];
      const t=path.lengths[i]?d/path.lengths[i]:0,a=path.points[i],b=path.points[i+1];
      const result=[a[0]+(b[0]-a[0])*t,a[1]+(b[1]-a[1])*t];
      result.facing=[(b[0]-a[0])/(path.lengths[i]||1),(b[1]-a[1])/(path.lengths[i]||1)];return result;
    }
    const journeys={
      brief:[[150,668],[173,535],[370,505],[370,335],[230,335],[260,220]],
      checks:[[212,202],[230,335],[495,335],[495,654]],
      science:[[605,202],[610,318],[495,318],[495,654],[495,318],[610,318],[605,202]],
      pedagogy:[[990,202],[990,346],[522,346],[495,654],[522,346],[990,346],[990,202]],
      scienceReport:[[605,202],[610,325],[672,325],[716,425],[672,325],[610,325],[605,202]],
      pedagogyReport:[[990,202],[990,375],[830,375],[773,425],[830,375],[990,375],[990,202]],
      fix:[[212,202],[230,335],[380,335],[380,485],[682,485],[716,425],[682,485],[380,485],[380,335],[230,335],[212,202]],
      decision:[[735,447],[789,502],[789,580],[849,690],[789,580],[789,502],[735,447]],
      websitePickup:[[1048,685],[1048,502],[789,502],[789,580],[849,690]]
    };
    journeys.briefReturn=journeys.brief.slice().reverse();
    journeys.checksReturn=journeys.checks.slice().reverse();
    journeys.websiteReturn=journeys.websitePickup.slice().reverse();
    const coffeeSeat=[132,455];
    for(const role of ['teacher','developer','science','pedagogy']){
      const start=home[role],door=role==='science'?610:role==='pedagogy'?990:230;
      journeys[role+'Coffee']=role==='teacher'?[start,[173,535],[370,505],[370,465],[295,435],coffeeSeat]:[start,[door,335],[370,335],[370,465],[295,435],coffeeSeat];
      journeys[role+'CoffeeReturn']=journeys[role+'Coffee'].slice().reverse();
    }
    function coffeeBreak(state,review){
      const loop=Math.floor(options.phase()/42);
      if(!state || loop%2)return null;
      const first=Object.keys(review.roles).find(role=>review.roles[role].collectStart===14);
      const choice=(parseInt(state.hash?.slice(-1) || '0',16)+Math.floor(loop/2))%3;
      const role=['teacher','developer',first][choice];
      if(choice===2 && !review.roles[role].available)return null;
      const [start,end]=role==='teacher'?[15,21]:role==='developer'?[21.2,27.8]:[28,41];
      if(review.cycle<start || review.cycle>=end)return null;
      const f=(review.cycle-start)/(end-start),seated=f>=1/3 && f<2/3;
      return {role,start,end,f,seated,mug:seated || (f<1/3?f*3>.8:(f-2/3)*3<.2)};
    }
    function lounge(){
      box(26,370,336,145,'#2c393a');box(31,375,326,135,'#526660');
      box(31,375,326,25,'#334a46');text('COFFEE LOUNGE',45,393,'#dfce9c',13);
      box(48,426,157,39,'#738683');box(43,432,11,40,'#5e7370');box(199,432,11,40,'#5e7370');
      for(let i=0;i<3;i++)box(57+i*46,435,41,23,'#93a09a');box(51,465,153,11,'#4b625f');
      box(235,433,92,13,'#b59a74');box(241,446,6,30,'#73684f');box(314,446,6,30,'#73684f');
      box(274,400,49,35,'#29383d');box(280,405,35,18,'#596c69');box(288,410,19,3,'#d7bc80');
      mug(294,430);mug(252,429);box(214,477,111,8,'#a28c6b');
      text('COFFEE',278,492,'#e9d8b2',10,'center');text('A little pause, not a skipped check.',194,507,'#ccd0bd',9,'center');
    }
    function mug(x,y){box(x-6,y-5,12,10,'#e8dfc6');box(x+6,y-3,4,6,'#c6bb9c');box(x-4,y-5,8,2,'#75604c');}
    function reviewProgress(state){
      const cycle=options.phase()%42;
      // Timing illustrates independent work; it is not inferred from session durations.
      // Vary which role finishes first, deterministically for each lesson version.
      const first=parseInt(state?.hash?.slice(-1) || '0',16)%2?'pedagogy':'science';
      const roles={};
      for(const role of ['science','pedagogy']){
        const fast=role===first;
        const timing=fast?{collectStart:14,collectEnd:18.6,reportStart:21.3,reportEnd:25.5}:{collectStart:15.8,collectEnd:21,reportStart:24.3,reportEnd:28};
        const status=state?.[role].status || 'missing';
        const arrival=(timing.reportStart+timing.reportEnd)/2;
        const available=status!=='missing';
        const arrived=available && cycle>=arrival;
        const collecting=cycle>=timing.collectStart && cycle<timing.collectEnd;
        const delivering=available && cycle>=timing.reportStart && cycle<timing.reportEnd;
        const work=collecting?'COLLECTING COPY':delivering?(arrived?'RETURNING TO DESK':'DELIVERING REPORT'):cycle<timing.collectStart?'WAITING FOR COPY':!available?'REPORT NOT RECORDED':cycle<timing.reportStart?'REVIEWING COPY':'REPORT DELIVERED';
        roles[role]={...timing,status,arrival,available,arrived,collecting,delivering,work};
      }
      const received=Object.values(roles).filter(role=>role.arrived).length;
      const needsRevision=Object.values(roles).some(role=>role.arrived && ['FAIL','stale','invalid'].includes(role.status));
      return {cycle,roles,received,needsRevision,ready:Boolean(state?.eligible) && received===2};
    }
    function nextHandoff(){
      const review=reviewProgress(options.state());
      const moments=[0,7,14,21,28,31.5,32,34,35,38,39,40.5,...Object.values(review.roles).flatMap(role=>[role.collectStart,(role.collectStart+role.collectEnd)/2,role.collectEnd,...(role.available?[role.reportStart,role.arrival,role.reportEnd]:[])])];
      return [...new Set(moments)].sort((a,b)=>a-b).find(moment=>moment>review.cycle+.001) ?? 0;
    }
    function actors(state,review,coffee){
      const cycle=options.phase()%42,step=Math.floor(cycle/7),f=(cycle%7)/7;
      const positions=Object.fromEntries(Object.entries(home).map(([id,p])=>[id,[...p]]));
      const packets={};const moving={};const busy=new Set();
      const walk=(id,points,t,kind,color)=>{positions[id]=position(points,t);moving[id]=!options.still();busy.add(id);if(kind)packets[id]={kind,color:color||colors[id]};};
      const approved=publicationApproved(state,review);
      if(state){
        if(step===0)walk('teacher',journeys.brief,f,'BRIEF');
        if(step===1){walk('teacher',journeys.briefReturn,f);walk('developer',journeys.checks,f,'LESSON');}
        if(step===2)walk('developer',journeys.checksReturn,f);
        for(const role of ['science','pedagogy']){
          const r=review.roles[role];
          if(r.collecting){const progress=(cycle-r.collectStart)/(r.collectEnd-r.collectStart);walk(role,journeys[role],progress,progress>=.5?'COPY':null);}
          if(r.delivering){const progress=(cycle-r.reportStart)/(r.reportEnd-r.reportStart);walk(role,journeys[role+'Report'],progress,progress<.5?`${r.status.toUpperCase()} REPORT`:null,r.status==='PASS'?C.green:C.red);}
        }
        if(step===4){if(review.ready)walk('gatekeeper',journeys.decision,f,f<.5?'REVIEWED':null,C.green);else if(review.needsRevision)walk('developer',journeys.fix,f,f>=.5?'REVISE':null,C.red);}
        if(step===5 && review.ready){
          if(cycle<38)walk('site',journeys.websitePickup,(cycle-35)/3);
          else if(cycle<39)positions.site=[849,690];
          else walk('site',journeys.websiteReturn,(cycle-39)/3,approved?'APPROVED':null,C.green);
        }
      }
      if(coffee && !busy.has(coffee.role)){
        if(coffee.f<1/3)walk(coffee.role,journeys[coffee.role+'Coffee'],coffee.f*3);
        else if(coffee.seated)positions[coffee.role]=coffeeSeat;
        else walk(coffee.role,journeys[coffee.role+'CoffeeReturn'],(coffee.f-2/3)*3);
      }
      figurePositions=[];
      for(const id of ['developer','science','pedagogy','teacher','repository','gatekeeper','site']){
        const point=positions[id],[x,y]=point;person(x,y,id,moving[id],Boolean(packets[id]),point.facing || [1,0]);
        figurePositions.push({id,x,y});
        const awayFromDesk=Math.hypot(x-home[id][0],y-home[id][1])>28;
        if((moving[id] && awayFromDesk) || coffee?.role===id){const label=coffee?.role===id?'COFFEE BREAK':id==='gatekeeper'?'COORDINATOR':id==='site'?'WEB COURIER':id.toUpperCase();pill(label,x,y+54,colors[id],label.length*8+24);}
        if(packets[id])pagePacket(x+(moving[id] && point.facing?.[0]<-.1?-26:26),y+11,state.id,packets[id].color,packets[id].kind);
        if(coffee?.role===id && coffee.mug)mug(x+25,y+14);
      }
      return {step,positions,packets,coffee};
    }
    function speech(state,review,actors){
      if(!state || options.speechEnabled?.()===false || options.phase()%6>4.5)return null;
      const {step,coffee,positions,packets}=actors;let speaker,message;
      if(coffee?.seated){speaker=coffee.role;message=speaker==='developer'?'Refactoring my caffeine levels.':speaker==='teacher'?'A brief pause. The universe can wait.':'A peer review of this coffee is now in progress.';}
      else if(step===0){speaker='teacher';message="Let's turn ‘why?’ into a lesson.";}
      else if(step===1){speaker='developer';message='It worked in my head. Now for the tests.';}
      else if(step===2){speaker=Object.keys(review.roles).find(role=>review.roles[role].work==='REVIEWING COPY') || 'pedagogy';message=speaker==='science'?'SI units. Not vibes.':'Would a student understand this before coffee?';}
      else if(step===3){
        const bad=Object.keys(review.roles).find(role=>review.roles[role].delivering && ['FAIL','stale','invalid'].includes(review.roles[role].status));
        if(bad){speaker=bad;message=review.roles[bad].status==='stale'?'New version? My old PASS just expired.':'The universe would like one small correction.';}
        else{speaker='gatekeeper';message=review.ready?'Two matching passes. My favourite duet.':'One PASS is not a quorum.';}
      }else if(step===4){speaker=review.needsRevision?'developer':'gatekeeper';message=review.needsRevision?'Back to the drawing board. Literally.':review.ready?'Two matching passes. My favourite duet.':'One PASS is not a quorum.';}
      else{speaker=review.ready?'site':'repository';message=packets.site?'Approved cargo. Still not a deployment receipt.':review.ready?'I deliver pages, not assumptions.':'Coffee is approved. Publication is still pending.';}
      const point=positions[speaker],quote=tr(message),width=242;ctx.font='12px monospace';
      const lines=[];let line='';
      for(const word of quote.split(' ')){const next=line?line+' '+word:word;if((ctx.measureText?.(next).width || next.length*7.2)>width-22 && line){lines.push(line);line=word;}else line=next;}
      if(line)lines.push(line);
      const height=lines.length*15+18,x=Math.max(8,Math.min(1192-width,point[0]-width/2)),y=Math.max(7,point[1]-height-68);
      box(x+3,y+3,width,height,'#17222970');box(x,y,width,height,'#efe7cf');box(x,y,width,3,colors[speaker]);
      box(point[0]-4,y+height,8,4,'#efe7cf');box(point[0]-2,y+height+4,4,4,'#efe7cf');
      lines.forEach((line,i)=>text(line,x+11,y+22+i*15,'#344540',12));
      return {speaker,text:quote};
    }
    function publicationApproved(state,review){
      // A merge or HTML file alone does not establish the human decision.
      return review.ready && state?.publicationDecision?.status==='approved' && state.publicationDecision.contentHash===state.hash;
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
    function gate(state,review){
      const color=review.ready?C.green:review.needsRevision?C.red:C.amber;
      const approvals=state?['science','pedagogy'].filter(r=>state[r].status==='PASS').length:'–';
      // An ordinary office colleague at a paper-covered desk, not a guard.
      box(695,405,137,35,'#9b8262');box(695,435,137,7,'#b9a07a');
      box(700,442,7,31,'#5a5042');box(820,442,7,31,'#5a5042');box(710,474,33,24,'#33484b');
      box(701,419,17,24,'#ad946c');box(704,423,11,16,'#eee1bd');
      ['science','pedagogy'].forEach((r,i)=>box(706,426+i*6,6,3,!review.roles[r].arrived?C.muted:state?.[r].status==='PASS'?C.green:C.red));
      text('REVIEW DESK',768,385,C.ink,13,'center');
      pill(review.ready?'READY':review.needsRevision?'REVISE':'WAITING',796,424,color,70);
      text(`${review.received}/2 REPORTS`,793,454,color,10,'center');text(`Recorded: ${approvals}/2 PASS`,793,473,C.muted,8,'center');
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
      const state=options.state();const active=options.active();const review=reviewProgress(state);const coffee=coffeeBreak(state,review);
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
        pill(status==='NOT OBSERVED'?'NO SNAPSHOT':status==='missing'?'NO REPORT RECORDED':`RECORDED ${status.toUpperCase()}`,x,254,status==='PASS'?C.green:status==='FAIL'?C.red:C.amber,198);
        text(coffee?.role===id?'COFFEE BREAK':state?review.roles[id].work:'WAITING FOR LESSON',x,277,C.muted,9,'center');
      }
      plant(380,245);plant(753,245);plant(1148,245);
      // The publication role is represented by a seated colleague throughout the journey.
      desk(150,656,C.gold);box(42,595,34,42,'#d9d3ba');text('?',59,624,'#60756a',24,'center');
      shelf(207,595,90);plant(53,745);text('BRIEF & ASSIGN',173,743,C.gold,12,'center');
      desk(789,656,C.green);box(732,711,116,28,'#243631');text(publicationApproved(state,review)?'APPROVED':options.event()?.merge?'MERGE RECORDED':'DECISION UNKNOWN',790,730,publicationApproved(state,review)?C.green:C.amber,10,'center');
      if(options.event()?.merge)text('Approver unverified',790,757,C.muted,10,'center');
      pill('2 · CHECK',484,508,C.amber,132);pill('3 · INDEPENDENT REVIEWS',779,318,C.ink,259);
      pill('5 · HUMAN DECISION',790,516,C.gold,197);text('4 · MATCH BOTH APPROVALS',770,363,'#e9dfc8',11,'center');
      box(28,309,326,45,'#2f3e3e');text(options.presentation?.()?'TODAY’S LESSON':'ONE LESSON. TWO INDEPENDENT REVIEWS.',191,327,C.ink,10,'center');
      text(state?(options.presentation?.()?state.id.toUpperCase():`${state.id.toUpperCase()}  /  ${state.hash || 'HASH UNAVAILABLE'}`):'SELECT A RECORDED LESSON',191,344,C.gold,10,'center');
      lounge();checks(state);site(state);gate(state,review);const activity=actors(state,review,coffee);const quote=speech(state,review,activity);
      if(!options.presentation?.()){box(22,786,1156,11,'#202c30');text('WORKFLOW ILLUSTRATION · COURIER MOVEMENT IS NOT A SESSION LOG',30,795,'#c1c5b7',9);}
      return {step:activity.step,speech:quote,caption:this.caption(activity.step,state,review)};
    }
    function caption(step,state,review=reviewProgress(state)){
      if(!state)return 'Choose a recorded lesson to explore its route through the office.';
      const name=role=>role==='science'?'Science':'Pedagogy';
      const first=Object.keys(review.roles).find(role=>review.roles[role].arrived);
      const waiting=Object.keys(review.roles).filter(role=>!review.roles[role].arrived).map(name).join(' and ');
      const reportCaption=review.needsRevision?'A failed, stale or invalid review blocks approval. The lesson must return for revision or renewed review.':review.ready?'Both independent reports have arrived and PASS the current version. The review desk is ready.':review.received===1?`${name(first)} report received. Waiting for ${waiting.toLowerCase()} to finish independently.`:Object.values(review.roles).every(role=>!role.available)?'No review reports are recorded for this version. The desk keeps waiting.':'The reviewers work independently and return reports at different times.';
      return [
        'The teacher brings a brief to the developer.',
        'The developer brings the lesson packet to automatic checks.',
        'The reviewers collect separate copies at different times and review independently, in parallel.',
        reportCaption,
        review.ready?'The review coordinator delivers the reviewed lesson to the publication decision-maker, then returns to the review desk.':review.needsRevision?'Approval is blocked. The developer takes a REVISE packet back to development.':`Still waiting for ${waiting.toLowerCase()} review. Nothing proceeds to the publication desk.`,
        review.needsRevision?'After fixing the work, the developer must rerun checks and request new reviews of the changed version.':!review.ready?`The review desk keeps waiting for ${waiting.toLowerCase()}. No publication handoff is made.`:review.cycle<38?'The website courier comes to the publication desk to collect approved material.':review.cycle<39?(publicationApproved(state,review)?'Approval is recorded for this version. The website courier can collect the approved lesson.':'The website courier waits: publication approval is not recorded for this version.'):(publicationApproved(state,review)?'The website courier carries approved material to the website. Deployment itself remains unverified.':'No publication approval is recorded. The website courier returns without collecting material.')
      ][step];
    }
    function hit(p){
      const figure=figurePositions.find(f=>Math.abs(p.x-f.x)<27 && p.y>f.y-32 && p.y<f.y+40);
      if(figure)return figure.id;
      if(p.x>=26 && p.x<=362 && p.y>=370 && p.y<=518)return 'lounge';
      if(p.x>=688 && p.x<=838 && p.y>=370 && p.y<=510)return 'gatekeeper';
      return stations.find(s=>p.x>=s.x && p.x<=s.x+s.w && p.y>=s.y && p.y<=s.y+s.h)?.id;
    }
    return {draw,hit,caption,nextHandoff};
  }
};
