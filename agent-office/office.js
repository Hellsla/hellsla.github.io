'use strict';
(() => {
  const $ = id => document.getElementById(id);
  const roles = [
    {id:'developer', name:'Developer', label:'THE MAKER', color:'#edba70', x:270, y:250, path:'fysiikkalabra/.claude/agents/developer.md', description:'Writes and improves lesson text, exercises, figures and simulations. The existing developer workflow checks the lesson before it goes to independent review.'},
    {id:'science', name:'Science reviewer', label:'THE PHYSICS CHECK', color:'#8cb8e0', x:640, y:250, path:'fysiikkalabra/.claude/agents/science-reviewer.md', description:'Independently checks physics, mathematics, units, numerical answers and simulation behaviour. Reviews the work without editing the lesson.'},
    {id:'pedagogy', name:'Pedagogy reviewer', label:'THE LEARNER’S VIEW', color:'#e9a1b4', x:270, y:430, path:'fysiikkalabra/.claude/agents/pedagogy-reviewer.md', description:'Independently reviews the learning path, explanations, activities and usability on a phone and laptop. Reviews the work without editing the lesson.'},
    {id:'repository', name:'Repository', label:'THE RECORD KEEPER', color:'#9ccb9b', x:640, y:430, path:'Git history · not an agent definition', description:'Represents recorded commits and merges, including changes outside the three lesson roles. A commit is a saved change, not evidence of a deployment, test pass or running agent.'}
  ];
  const history = window.OFFICE_HISTORY || {events:[]};
  const days = [...new Set(history.events.map(e=>e.day))].sort().reverse();
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  let selected = [], minute = 0, playing = false, lastFrame = 0, lastPaint = 0, phase = 0;
  const canvas = $('office'), ctx = canvas.getContext('2d');
  const dateFormat = new Intl.DateTimeFormat('en-GB', {weekday:'short',day:'numeric',month:'long',year:'numeric',timeZone:'Europe/Helsinki'});
  const dayLabel = day => dateFormat.format(new Date(day+'T12:00:00+02:00'));
  const time = m => `${String(Math.floor(m/60)%24).padStart(2,'0')}:${String(Math.floor(m)%60).padStart(2,'0')}`;
  const roleNames = ids => ids.map(id=>roles.find(r=>r.id===id)?.name || id).join(' · ');
  const activeRoles = () => new Set(selected.filter(e=>e.minute<=minute && minute-e.minute<8).flatMap(e=>e.roles));
  function showRole(role) {
    $('role-name').textContent = role.name;
    $('role-label').textContent = role.label;
    $('role-description').textContent = role.description;
    $('role-path').textContent = role.path;
    $('role-dialog').showModal();
  }
  roles.forEach(role=>{
    const button=document.createElement('button'); button.type='button';
    button.style.setProperty('--role-color',role.color);button.dataset.role=role.id;
    const dot=document.createElement('i');dot.setAttribute('aria-hidden','true');
    button.append(dot,document.createTextNode(role.name));button.addEventListener('click',()=>showRole(role));
    $('desks').append(button);
  });
  for(const day of days){const option=document.createElement('option');option.value=day;option.textContent=dayLabel(day);$('day').append(option);}
  function setPlaying(value){
    playing=value && selected.length>0;
    $('play').replaceChildren(document.createTextNode(playing?'Ⅱ ':'▶ '),Object.assign(document.createElement('span'),{textContent:playing?'Pause':'Play'}));
    $('play').setAttribute('aria-label',playing?'Pause replay':'Play replay');
    $('play').setAttribute('aria-pressed',String(playing));
  }
  function seek(value){minute=Math.max(0,Math.min(1439.999,Number(value)));update();draw();}
  function update(){
    $('timeline').value=minute;$('clock').textContent=time(minute);
    $('timeline').setAttribute('aria-valuetext',time(minute)+' Helsinki time');
    const active=activeRoles();
    for(const b of $('desks').children)b.classList.toggle('active',active.has(b.dataset.role));
    const seen=selected.filter(e=>e.minute<=minute);const current=seen.at(-1);
    $('current').textContent=active.size?`${roleNames([...active])} — changes recorded near ${time(current.minute)}.`:'The office is quiet between recorded changes.';
    for(const [i,li] of [...$('events').children].entries()){
      li.classList.toggle('future',selected[i].minute>minute);
      li.firstElementChild.classList.toggle('current',selected[i]===current);
      if(selected[i]===current)li.firstElementChild.setAttribute('aria-current','true');else li.firstElementChild.removeAttribute('aria-current');
    }
  }
  function chooseDay(){
    selected=history.events.filter(e=>e.day===$('day').value).sort((a,b)=>a.minute-b.minute || a.id.localeCompare(b.id));
    setPlaying(false);$('events').replaceChildren();$('ticks').replaceChildren();
    $('office-date').textContent=selected.length?dayLabel($('day').value):'No history available';
    $('count-commits').textContent=selected.length;
    for(const [id,role] of [['count-lessons','developer'],['count-science','science'],['count-pedagogy','pedagogy']])$(id).textContent=selected.filter(e=>e.roles.includes(role)).length;
    $('log-count').textContent=`${selected.length} commits`;$('empty').hidden=selected.length>0;
    selected.forEach(event=>{
      const li=document.createElement('li'),b=document.createElement('button'),t=document.createElement('time'),text=document.createElement('span'),meta=document.createElement('small');
      b.type='button';t.textContent=time(event.minute);t.dateTime=event.timestamp;
      text.textContent=event.title;meta.textContent=`${event.id.slice(0,7)} · ${event.files} changed files · ${roleNames(event.roles)}`;
      text.append(meta);b.append(t,text);li.append(b);$('events').append(li);
      b.addEventListener('click',()=>{setPlaying(false);seek(event.minute);});
      const tick=document.createElement('i');tick.style.left=`${event.minute/1440*100}%`;$('ticks').append(tick);
    });
    $('play').disabled=$('next').disabled=$('timeline').disabled=!selected.length;
    seek(selected.length?Math.max(0,selected[0].minute-5):0);
  }
  $('day').addEventListener('change',chooseDay);
  $('play').addEventListener('click',()=>{if(minute>=1439.9)seek(0);setPlaying(!playing);});
  $('next').addEventListener('click',()=>{setPlaying(false);const event=selected.find(e=>e.minute>minute+0.001);seek(event?event.minute:1439.999);});
  $('timeline').addEventListener('input',e=>{setPlaying(false);seek(e.target.value);});
  $('motion').checked=reduced;
  $('motion').addEventListener('change',()=>draw());
  $('about').addEventListener('click',()=>$('about-dialog').showModal());
  for(const dialog of document.querySelectorAll('dialog')){
    dialog.querySelector('.close').addEventListener('click',()=>dialog.close());
    dialog.addEventListener('click',e=>{if(e.target===dialog){const r=dialog.getBoundingClientRect();if(e.clientX<r.left || e.clientX>r.right || e.clientY<r.top || e.clientY>r.bottom)dialog.close();}});
  }
  $('fullscreen').addEventListener('click',async()=>{
    try{if(document.fullscreenElement)await document.exitFullscreen();else await $('app').requestFullscreen();}
    catch{ $('fullscreen').textContent='Unavailable';$('fullscreen').disabled=true; }
  });
  document.addEventListener('fullscreenchange',()=>$('fullscreen').setAttribute('aria-label',document.fullscreenElement?'Exit full screen':'Enter full screen'));
  function point(event){const r=canvas.getBoundingClientRect();return{x:(event.clientX-r.left)*960/r.width,y:(event.clientY-r.top)*560/r.height};}
  function hit(p){return roles.find(r=>Math.abs(p.x-r.x)<125 && p.y>r.y-90 && p.y<r.y+60);}
  canvas.addEventListener('click',e=>{const role=hit(point(e));if(role)showRole(role);});
  canvas.addEventListener('mousemove',e=>{canvas.style.cursor=hit(point(e))?'pointer':'default';});
  function rect(x,y,w,h,c){ctx.fillStyle=c;ctx.fillRect(Math.round(x),Math.round(y),w,h);}
  function text(s,x,y,c='#d6d6bd',size=12,align='left'){ctx.font=`${size}px monospace`;ctx.fillStyle=c;ctx.textAlign=align;ctx.fillText(s,x,y);}
  function plant(x,y){rect(x-11,y,22,22,'#a06e55');rect(x-14,y,28,5,'#c4946b');rect(x-2,y-30,4,30,'#778b53');rect(x-20,y-24,18,9,'#78915d');rect(x+2,y-38,19,10,'#90aa70');rect(x-15,y-47,15,12,'#617a50');rect(x+4,y-17,16,8,'#506b49');}
  function person(x,y,color,on,seed){
    const bob=on && !$('motion').checked?Math.floor(Math.sin(phase*5+seed)*1.5):0;
    rect(x-14,y+31,31,7,'#272a2d');rect(x-9,y+20,7,14,'#253440');rect(x+4,y+20,7,14,'#253440');
    rect(x-13,y-1+bob,27,27,color);rect(x-12,y-21+bob,24,24,'#cfac8b');rect(x-14,y-24+bob,27,9,seed%2?'#493b35':'#554a3b');rect(x-14,y-15+bob,5,10,'#493b35');
    rect(x+2,y-9+bob,3,3,'#2b3337');rect(x+9,y-9+bob,3,3,'#2b3337');rect(x-17,y+11+bob,7,12,color);rect(x+14,y+9+bob,7,12,color);
    if(on){rect(x+18,y+16+bob,8,5,'#cfac8b');}
  }
  function desk(role,index,active){
    const x=role.x,y=role.y;
    rect(x-105,y+13,216,18,'#252b2e');rect(x-102,y+22,9,35,'#554c43');rect(x+89,y+22,9,35,'#554c43');
    rect(x-107,y-24,216,45,'#826d57');rect(x-107,y+14,216,9,'#aa8d6b');rect(x-103,y-24,208,4,'#b09979');
    rect(x-72,y-83,84,56,'#17232c');rect(x-68,y-79,76,46,active?'#365f57':'#2a3d43');rect(x-37,y-27,11,6,'#1b242c');rect(x-48,y-22,34,4,'#28323a');
    const c=active?role.color:'#66818b';
    for(let line=0;line<4;line++){rect(x-60,y-70+line*8,18+(line%3)*15,3,c);rect(x-37+(line%2)*10,y-70+line*8,14,3,'#8fbc9a');}
    rect(x-65,y-10,67,13,'#3e484a');for(let k=0;k<8;k++)rect(x-61+k*7,y-7,4,2,'#8a9190');
    rect(x+47,y-15,22,20,'#e3d7b4');rect(x+51,y-18,14,4,'#aaa18a');rect(x+69,y-11,6,11,'#baa987');
    rect(x+80,y-8,17,14,role.color);rect(x+83,y-5,12,2,'#534e4a');
    rect(x-20,y+23,44,36,'#3f5054');rect(x-15,y+55,6,12,'#253137');rect(x+12,y+55,6,12,'#253137');
    person(x+8,y+13,role.color,active,index);
    rect(x-94,y-112,190,23,'#242f35');rect(x-94,y-112,3,23,role.color);text(role.name.toUpperCase(),x,y-96,role.color,12,'center');
    if(active){rect(x+35,y-74,111,29,'#efe4c5');rect(x+43,y-47,7,7,'#efe4c5');text('FILE CHANGES',x+90,y-56,'#3c4c48',10,'center');}
  }
  function draw(){
    const active=activeRoles();ctx.imageSmoothingEnabled=false;
    rect(0,0,960,560,'#2c3639');
    for(let y=125;y<560;y+=28)for(let x=0;x<960;x+=64){rect(x+(y%56?0:-32),y,63,27,(Math.floor(x/64)+Math.floor(y/28))%3?'#3a4140':'#404644');rect(x,y,63,1,'#4b5149');}
    rect(0,0,960,126,'#4d5b57');rect(0,113,960,14,'#293638');rect(0,109,960,4,'#718175');
    for(let x=0;x<960;x+=48)rect(x,0,1,109,'#586662');
    // Three evening windows, with a distant city in miniature.
    for(const x of [56,425,786]){
      rect(x,19,119,82,'#202f37');rect(x+5,24,109,72,'#627c84');rect(x+5,24,109,29,'#879b96');
      for(let i=0;i<6;i++){rect(x+7+i*18,65-(i%3)*7,14,31+(i%3)*7,'#3c535c');rect(x+11+i*18,73-(i%3)*7,3,4,'#d6b77c');}
      rect(x+57,22,5,77,'#c1b49b');rect(x+3,60,112,4,'#c1b49b');rect(x-5,99,130,7,'#ab9a7b');
    }
    rect(220,20,153,74,'#a58d67');rect(226,26,141,62,'#273e3d');text('ASK. TEST.',296,47,'#d6dbc2',15,'center');text('UNDERSTAND.',296,69,'#a7c4a2',15,'center');
    rect(599,22,120,70,'#a28c6c');rect(605,28,108,58,'#d8d1b6');text('F = ma',659,51,'#4d6159',16,'center');text('EVIDENCE FIRST',659,73,'#6d7768',9,'center');
    // A bookcase and reading nook frame the working desks.
    rect(25,159,71,207,'#655b4a');for(let row=0;row<4;row++){rect(29,165+row*48,63,38,'#343d37');for(let b=0;b<7;b++)rect(32+b*8,173+row*48+(b%2)*5,6,29-(b%2)*5,['#a6866b','#7c9e94','#b8ae79','#8795ac'][b%4]);rect(24,201+row*48,74,6,'#9b8667');}
    plant(58,433);plant(902,210);
    rect(828,302,84,93,'#243638');rect(820,309,93,58,'#6d8271');rect(826,316,80,40,'#8d9a7c');rect(819,365,96,21,'#566b5c');
    rect(842,412,60,9,'#998061');rect(848,421,6,32,'#74674f');rect(889,421,6,32,'#74674f');rect(860,401,17,11,'#c4b899');
    // A sleeping office cat. Ambient animation never represents an agent session.
    rect(848,474,45,10,'#242e30');rect(855,461,30,15,'#bd9a70');rect(878,454,14,17,'#cda87a');rect(878,450,5,7,'#cda87a');rect(888,450,5,7,'#cda87a');rect(881,462,3,2,'#4d4c43');rect(888,462,3,2,'#4d4c43');
    rect(110,507,639,3,'#75806d');text('THE BEST IDEAS GET A SECOND PAIR OF EYES.',428,535,'#b5bba8',12,'center');
    roles.forEach((r,i)=>desk(r,i,active.has(r.id)));
    text('FY',120,75,'#d6c49b',19,'center');
  }
  function frame(now){
    const dt=Math.min((now-lastFrame)/1000,0.1);lastFrame=now;
    if(playing && !document.hidden && !$('role-dialog').open && !$('about-dialog').open){
      const next=selected.find(e=>e.minute>minute),near=selected.some(e=>Math.abs(e.minute-minute)<9);
      let step=dt*Number($('speed').value)*(near?3:100);
      if(next && minute+step>next.minute)step=next.minute-minute;
      minute=Math.min(1439.999,minute+step);update();if(minute>=1439.999)setPlaying(false);
    }
    if(now-lastPaint>80){if(!$('motion').checked)phase+=0.08;draw();lastPaint=now;}
    requestAnimationFrame(frame);
  }
  $('data-source').textContent=`Git history · ${history.events.length} commits · Europe/Helsinki`;
  chooseDay();draw();requestAnimationFrame(frame);
})();
