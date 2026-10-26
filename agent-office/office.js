'use strict';
(() => {
  const $ = id => document.getElementById(id);
  const i18n=window.OfficeI18n,t=i18n.t;
  const roles = [
    {id:'developer', name:'Developer', label:'THE MAKER', color:'#edba70', x:270, y:250, path:'.claude/agents/developer.md', description:'Writes and improves lesson text, exercises, figures and simulations. The existing developer workflow checks the lesson before it goes to independent review.'},
    {id:'science', name:'Science reviewer', label:'THE PHYSICS CHECK', color:'#8cb8e0', x:640, y:250, path:'.claude/agents/science-reviewer.md', description:'Independently checks physics, mathematics, units, numerical answers and simulation behaviour. Reviews the work without editing the lesson.'},
    {id:'pedagogy', name:'Pedagogy reviewer', label:'THE LEARNER’S VIEW', color:'#e9a1b4', x:270, y:430, path:'.claude/agents/pedagogy-reviewer.md', description:'Independently reviews the learning path, explanations, activities and usability on a phone and laptop. Reviews the work without editing the lesson.'},
    {id:'repository', name:'Publication decision', label:'THE HUMAN DECISION', color:'#9ccb9b', path:'Git history · not an agent definition', description:'The colleague at this desk represents the teacher’s publication decision. The teacher receives reviewed work and decides what to merge. The build includes lessons with two current passing reviews, or an eligible legacy marker; CI separately checks the site. A recorded merge does not prove who approved it or whether deployment succeeded.'}
  ];
  const history = window.OFFICE_HISTORY || {events:[]};
  const gatekeeper = {id:'gatekeeper',name:'Review coordinator',label:'THE REVIEW DESK',color:'#719b95',path:'fysiikkalabra/scripts/reviews.py',description:'An ordinary office colleague represents the review approval check. Both independent reports must say PASS for the lesson’s current content hash. The coordinator delivers the reviewed packet to the decision-maker, then returns to the review desk. Missing, failed, invalid or stale reports cannot clear this step. The character illustrates an automatic rule, not an additional running agent.'};
  const teacher = {id:'teacher',name:'Teacher',label:'THE HUMAN COORDINATOR',color:'#e5dfbd',path:'Human role · not an additional AI agent',description:'Sets the lesson brief, assigns development work and receives independently reviewed material. The same teacher makes the separate publication decision. The walking character explains this workflow; Git history does not record the teacher’s actual movements or private instructions.'};
  const checks = {id:'checks',name:'Automatic checks',label:'THE CHECK RUNNER',color:'#d7b474',path:'fysiikkalabra/scripts/ · .github/workflows/fysiikkalabra-ci.yml',description:'The lesson workflow builds the preview and checks content, mathematics, simulations and layout. Saved checks.txt results appear here, but have no content hash: their freshness and CI success remain unknown. The machine illustrates automation, not an additional agent.'};
  const website = {id:'site',name:'Website courier',label:'AFTER THE PUBLICATION DECISION',color:'#a69ac3',path:'fysiikkalabra/site/ · GitHub Pages',description:'Represents the publishing process, not an additional AI agent. The courier comes to the publication desk, waits for a recorded approval matching this lesson version, and collects only approved material. A merge or HTML file alone is not proof of that decision. Deployment remains unverified.'};
  const lounge={id:'lounge',name:'Coffee lounge',label:'A WELL-EARNED PAUSE',color:'#d7b474',path:'Illustrated break · no real agent is paused',description:'A coffee machine, a sofa and a little breathing room. An idle colleague occasionally takes a break and returns before their next handoff. Breaks and bubbles are illustrations; no real agent is paused and no lessons are changed.'};
  const officeRoles = [teacher,...roles.slice(0,3),checks,gatekeeper,roles[3],website,lounge];
  const days = [...new Set(history.events.map(e=>e.day))].sort().reverse();
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  let selected = [], minute = 0, playing = false, lastFrame = 0, lastPaint = 0, phase = 0;
  let lessonState = null, snapshotEvent = null, workflowKey = '';
  const canvas = $('office');
  const dayLabel = day => i18n.dateLabel(day);
  const time = m => `${String(Math.floor(m/60)%24).padStart(2,'0')}:${String(Math.floor(m)%60).padStart(2,'0')}`;
  const roleNames = ids => ids.map(id=>id==='repository'?'Repository changes':roles.find(r=>r.id===id)?.name || id).join(' · ');
  const activeRoles = () => new Set(selected.filter(e=>e.minute<=minute && minute-e.minute<8).flatMap(e=>e.roles));
  const scene = window.AgentOfficeScene.create(canvas,{state:()=>lessonState,event:()=>snapshotEvent,active:activeRoles,phase:()=>phase,still:()=>$('motion').checked,presentation:()=>document.body.classList.contains('office-only'),speechEnabled:()=>$('bubbles').checked});
  const allLessons = new Map((history.snapshots || []).flat().map(lesson=>[lesson.id,lesson.title]));
  for(const [id,title] of [...allLessons].sort()){
    const option=document.createElement('option');option.value=id;option.textContent=`${id.toUpperCase()} · ${title}`;$('lesson').append(option);
  }
  function workflow(event){
    const key=`${event?.id || ''}:${$('lesson').value}`;
    if(key===workflowKey)return;
    workflowKey=key;snapshotEvent=event;
    const states=history.snapshots?.[event?.snapshot] || [];
    const target=$('lesson').value==='auto'?(event?.changedLessons?.find(id=>states.some(s=>s.id===id)) || states[0]?.id):$('lesson').value;
    lessonState=states.find(s=>s.id===target) || null;
    const state=lessonState;
    $('lesson-title').textContent=state?`${state.id.toUpperCase()} · ${state.title}`:'No lesson snapshot at this point in the recorded history.';
    const labels={PASS:'PASS · current version',FAIL:'FAIL · revision needed',stale:'STALE · content changed',missing:'Waiting for review',invalid:'Invalid report · blocked'};
    for(const role of ['science','pedagogy']){
      const report=state?.[role];const status=report?.status || 'missing';
      $(role+'-status').textContent=state?(labels[status] || 'Not observed'):'Not observed';
      $(role+'-card').dataset.state=status;
      $(role+'-evidence').textContent=report?.hash?`Report: ${report.hash}${status==='stale'?' · no longer matches':''}`:state?'No valid matching report in this snapshot.':'';
    }
    $('stage-draft').dataset.state=state?'PASS':'missing';
    $('stage-checks').dataset.state=state?.checks.failed?'FAIL':'unknown';
    $('checks-status').textContent=state?.checks.failed?`${state.checks.failed} saved failures · freshness unknown`:state?.checks.passed?`${state.checks.passed} saved passes · freshness unknown`:'No check results observed';
    $('stage-reviews').dataset.state=state?.eligible?'PASS':state && [state.science.status,state.pedagogy.status].includes('FAIL')?'FAIL':'unknown';
    $('stage-gate').dataset.state=state?(state.eligible?'PASS':'FAIL'):'unknown';
    $('gate-status').textContent=state?(state.eligible?'OPEN · both PASS on current hash':'CLOSED · both current approvals required'):'No lesson selected';
    $('stage-publish').dataset.state='unknown';
    const statuses=state?[state.science.status,state.pedagogy.status]:[];
    $('handoff-status').textContent=!state?'Select an event or a different lesson to inspect the gate.':state.eligible?'Review gate cleared. Automated checks and the teacher’s publication decision remain separate.':statuses.includes('FAIL')?'Return to developer: a reviewer found a blocking issue. Fix it, run checks and request independent review again.':statuses.includes('stale')?'Return to review: the lesson changed after approval. Earlier PASS reports cannot open this gate.':'Waiting for both independent reviewers. A missing or invalid approval keeps the gate closed.';
    $('snapshot-evidence').textContent=event?`Commit ${event.id.slice(0,7)} · ${event.timestamp}. ${state?.hash?'Lesson content hash: '+state.hash+'.':''} This is the selected commit’s snapshot, including its branch context.`:'No commit at the current replay time.';
    $('files-evidence').textContent=state?`Lesson packet: ${state.files.join(', ')}. Reviewers return separate reports; they do not take ownership of or edit the lesson.`:'';
    $('site-evidence').textContent=state?(state.included?'This lesson has an HTML page in this commit’s site/ snapshot. That does not establish a fresh build or successful deployment.':'This lesson has no HTML page in this commit’s site/ snapshot.')+(state.legacy.status==='PASS'?'\nA current legacy marker allows the earlier prototype exception; it does not clear the two-review gate.':''):'';
  }
  function showRole(role) {
    $('role-name').textContent = role.name;
    $('role-label').textContent = role.label;
    $('role-description').textContent = i18n.roleDescription(role.id,role.description);
    $('role-path').textContent = role.path;
    $('role-dialog').querySelector('.subtle').textContent=role.id==='gatekeeper'?(lessonState?`${lessonState.id.toUpperCase()}: science ${lessonState.science.status}; pedagogy ${lessonState.pedagogy.status}. Recorded review eligibility ${lessonState.eligible?'cleared':'blocked'}. `:'No lesson snapshot selected. ')+'The walkthrough desk separately waits for both report deliveries. Passing review clears only the review requirement; automated checks and the teacher’s publication decision are separate.':'Room activity comes from recorded file changes. Couriers and handoffs illustrate the workflow; they are not records of running agents, actual conversations or human approvals.';
    if(!$('role-dialog').open)$('role-dialog').showModal();
    $('role-dialog').dataset.role=role.id;
  }
  officeRoles.forEach(role=>{
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
    $('play').setAttribute('aria-label',`${playing?'Pause':'Play'} ${$('replay-mode').value==='history'?'day history':'lesson journey'}`);
    $('play').setAttribute('aria-pressed',String(playing));
    $('presentation-play').textContent=playing?'Pause':'Play';
    $('presentation-play').setAttribute('aria-label',playing?'Pause':'Play');
  }
  function seek(value){minute=Math.max(0,Math.min(1439.999,Number(value)));update();draw();}
  function update(){
    $('timeline').value=minute;$('clock').textContent=time(minute);
    $('timeline').setAttribute('aria-valuetext',time(minute)+' Helsinki time');
    const active=activeRoles();
    for(const b of $('desks').children)b.classList.toggle('active',active.has(b.dataset.role));
    const seen=selected.filter(e=>e.minute<=minute);const current=seen.at(-1);
    const prior=current || history.events.filter(e=>e.day<$('day').value).at(-1);
    workflow(prior);
    $('current').textContent=active.size?`${roleNames([...active])} — changes recorded near ${time(current.minute)}.`:'The office is quiet between recorded changes.';
    for(const [i,li] of [...$('events').children].entries()){
      li.classList.toggle('future',selected[i].minute>minute);
      li.firstElementChild.classList.toggle('current',selected[i]===current);
      if(selected[i]===current)li.firstElementChild.setAttribute('aria-current','true');else li.firstElementChild.removeAttribute('aria-current');
    }
  }
  function chooseDay(){
    phase=0;
    selected=history.events.filter(e=>e.day===$('day').value).sort((a,b)=>a.minute-b.minute || a.id.localeCompare(b.id));
    setPlaying(false);$('events').replaceChildren();$('ticks').replaceChildren();
    $('office-date').textContent=selected.length?dayLabel($('day').value):'No history available';
    $('count-commits').textContent=selected.length;
    for(const [id,role] of [['count-lessons','developer'],['count-science','science'],['count-pedagogy','pedagogy']])$(id).textContent=selected.filter(e=>e.roles.includes(role)).length;
    $('log-count').textContent=`${selected.length} commits`;$('empty').hidden=selected.length>0;
    selected.forEach(event=>{
      const li=document.createElement('li'),b=document.createElement('button'),t=document.createElement('time'),text=document.createElement('span'),meta=document.createElement('small');
      b.type='button';t.textContent=time(event.minute);t.dateTime=event.timestamp;
      const title=document.createElement('span');title.dataset.noI18n='';title.textContent=event.title;
      meta.textContent=`${event.id.slice(0,7)} · ${event.files} changed files · ${roleNames(event.roles)}`;
      text.append(title,meta);b.append(t,text);li.append(b);$('events').append(li);
      b.addEventListener('click',()=>{setPlaying(false);seek(event.minute);});
      const tick=document.createElement('i');tick.style.left=`${event.minute/1440*100}%`;$('ticks').append(tick);
    });
    $('play').disabled=$('next').disabled=$('timeline').disabled=!selected.length;
    seek(selected.length?Math.max(0,selected[0].minute-5):0);
  }
  $('day').addEventListener('change',chooseDay);
  $('lesson').addEventListener('change',()=>{phase=0;workflowKey='';update();draw();});
  $('play').addEventListener('click',()=>{if($('replay-mode').value==='history' && minute>=1439.9)seek(0);setPlaying(!playing);});
  $('next').addEventListener('click',()=>{setPlaying(false);const event=selected.find(e=>e.minute>minute+0.001);seek(event?event.minute:1439.999);});
  $('next-handoff').addEventListener('click',()=>{setPlaying(false);phase=scene.nextHandoff();draw();});
  $('replay-mode').addEventListener('change',()=>{setPlaying(false);$('mode-label').textContent=$('replay-mode').value==='history'?'DAY HISTORY':'LESSON WALKTHROUGH';});
  $('timeline').addEventListener('input',e=>{setPlaying(false);seek(e.target.value);});
  $('motion').checked=reduced;
  $('motion').addEventListener('change',()=>draw());
  $('bubbles').addEventListener('change',()=>draw());
  $('zoom').addEventListener('change',()=>{canvas.style.width=`${Number($('zoom').value)*100}%`;});
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
  function point(event){const r=canvas.getBoundingClientRect();return{x:(event.clientX-r.left)*canvas.width/r.width,y:(event.clientY-r.top)*canvas.height/r.height};}
  function hit(p){
    const id=scene.hit(p);
    return officeRoles.find(role=>role.id===id);
  }
  canvas.addEventListener('click',e=>{const role=hit(point(e));if(role)showRole(role);});
  canvas.addEventListener('mousemove',e=>{canvas.style.cursor=hit(point(e))?'pointer':'default';});
  function draw(){
    const result=scene.draw();
    const caption=t('Workflow illustration: {caption}',{caption:result.caption});
    if($('scene-story').textContent!==caption)$('scene-story').textContent=caption;
    const speech=result.speech?`${t(officeRoles.find(role=>role.id===result.speech.speaker)?.name || result.speech.speaker)}: ${result.speech.text}`:'';
    if($('speech-caption').textContent!==speech)$('speech-caption').textContent=speech;
  }
  function frame(now){
    const dt=Math.min((now-lastFrame)/1000,0.1);lastFrame=now;
    if(playing && $('replay-mode').value==='history' && !document.hidden && !$('role-dialog').open && !$('about-dialog').open){
      const next=selected.find(e=>e.minute>minute),near=selected.some(e=>Math.abs(e.minute-minute)<9);
      let step=dt*Number($('speed').value)*(near?3:100);
      if(next && minute+step>next.minute)step=next.minute-minute;
      minute=Math.min(1439.999,minute+step);update();if(minute>=1439.999)setPlaying(false);
    }
    const animating=playing && !$('motion').checked && !document.hidden && !$('role-dialog').open && !$('about-dialog').open;
    if(animating)phase+=dt*Number($('speed').value);
    if(animating || now-lastPaint>250){draw();lastPaint=now;}
    requestAnimationFrame(frame);
  }
  $('data-source').textContent=`Git history · ${history.events.length} commits · Europe/Helsinki`;
  let controlsTimer;
  function revealControls(){
    if(!document.body.classList.contains('office-only'))return;
    $('presentation-controls').classList.add('controls-visible');clearTimeout(controlsTimer);
    controlsTimer=setTimeout(()=>$('presentation-controls').classList.remove('controls-visible'),2200);
  }
  function officeOnly(value){
    document.body.classList.toggle('office-only',value);$('presentation-controls').hidden=!value;
    $('office-only').setAttribute('aria-pressed',String(value));
    if(value){if(!lessonState && selected.length)seek(selected[0].minute);if(!$('motion').checked)setPlaying(true);canvas.focus({preventScroll:true});revealControls();}
    else{clearTimeout(controlsTimer);$('office-only').focus({preventScroll:true});}
    try{const url=new URL(location.href);if(value)url.searchParams.set('view','office');else url.searchParams.delete('view');window.history.replaceState(null,'',url);}catch{}
    draw();
  }
  function languageButtons(){
    for(const button of document.querySelectorAll('.language-toggle')){
      button.dataset.language=i18n.language;
      button.setAttribute('aria-label','Switch between Finnish and English');
    }
  }
  for(const button of document.querySelectorAll('.language-toggle'))button.addEventListener('click',event=>{i18n.setLanguage(i18n.language==='fi'?'en':'fi');if(event.detail>0 && document.body.classList.contains('office-only'))canvas.focus({preventScroll:true});});
  window.addEventListener('office-language-change',()=>{
    for(const option of $('day').options)option.textContent=dayLabel(option.value);
    $('office-date').textContent=selected.length?dayLabel($('day').value):'No history available';
    workflowKey='';update();setPlaying(playing);languageButtons();
    if($('role-dialog').open)showRole(officeRoles.find(role=>role.id===$('role-dialog').dataset.role));
    draw();i18n.apply();
  });
  $('office-only').addEventListener('click',()=>officeOnly(true));
  $('return-office').addEventListener('click',()=>officeOnly(false));
  $('presentation-play').addEventListener('click',event=>{setPlaying(!playing);if(event.detail>0)canvas.focus({preventScroll:true});});
  document.addEventListener('pointermove',revealControls,{passive:true});document.addEventListener('touchstart',revealControls,{passive:true});
  document.addEventListener('keydown',event=>{
    if(event.key==='Escape' && document.body.classList.contains('office-only') && !document.querySelector('dialog[open]'))officeOnly(false);
    if(document.body.classList.contains('office-only') && event.code==='Space' && event.target===canvas){event.preventDefault();setPlaying(!playing);revealControls();}
  });
  chooseDay();draw();languageButtons();i18n.start();
  if(new URLSearchParams(location.search).get('view')==='office')officeOnly(true);
  requestAnimationFrame(frame);
})();
