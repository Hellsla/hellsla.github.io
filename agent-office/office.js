'use strict';
(() => {
  const $ = id => document.getElementById(id);
  const i18n=window.OfficeI18n,t=i18n.t;
  const roles = [
    {id:'developer', name:'Developer', label:'THE MAKER', color:'#edba70', x:270, y:250, path:'.claude/agents/developer.md', description:'Writes and improves material text, exercises, figures and simulations. The existing developer workflow checks the material before it goes to independent review.'},
    {id:'science', name:'Science reviewer', label:'THE PHYSICS CHECK', color:'#8cb8e0', x:640, y:250, path:'.claude/agents/science-reviewer.md', description:'Independently checks physics, mathematics, units, numerical answers and simulation behaviour. Reviews the work without editing the material.'},
    {id:'pedagogy', name:'Pedagogy reviewer', label:'THE LEARNER’S VIEW', color:'#e9a1b4', x:270, y:430, path:'.claude/agents/pedagogy-reviewer.md', description:'Independently reviews the learning path, explanations, activities and usability on a phone and laptop. Reviews the work without editing the material.'},
    {id:'repository', name:'Publisher', label:'LAURI MAKES THE DECISION', color:'#9ccb9b', path:'Git history · not an agent definition', description:'The publisher prepares a publication proposal. Lauri visits this desk to discuss the reviewed work before making the publication decision. The build includes materials with two current passing reviews, or an eligible legacy marker; CI separately checks the site. A recorded merge does not prove who approved it or whether deployment succeeded.'}
  ];
  const history = window.OFFICE_HISTORY || {events:[]};
  const gatekeeper={id:'gatekeeper',name:'Review inbox',label:'AN AUTOMATED RULE',color:'#719b95',path:'fysiikkalabra/scripts/reviews.py',description:'Two report trays beside the coordination desk represent the automated approval rule. Both independent reviews must pass for the current version, directly or through recorded carry evidence. The orchestrator handles the packet; the rule is not another employee. Exact reports and CI limits are shown in the evidence panel.'};
  const teacher = {id:'teacher',name:'Lauri',label:'THE HUMAN COORDINATOR',color:'#e5dfbd',path:'Human role · not an additional AI agent',description:'Sets the material brief, assigns development work and receives independently reviewed material. Lauri makes the separate publication decision. The walking character explains this workflow; Git history does not record Lauri’s actual movements or private instructions.'};
  const checks = {id:'checks',name:'Automatic checks',label:'THE CHECK RUNNER',color:'#d7b474',path:'fysiikkalabra/scripts/ · .github/workflows/fysiikkalabra-ci.yml',description:'The material workflow builds the preview and checks content, mathematics, simulations and layout. Saved checks.txt results appear here, but have no content hash: their freshness and CI success remain unknown. The colleague at the computer illustrates automated testing, not an additional running agent.'};
  const website={id:'site',name:'Website display',label:'THE OUTPUT',color:'#a69ac3',path:'fysiikkalabra/site/ · GitHub Pages',description:'A wall display beside publishing represents the website preview. It is an output, not an employee or an additional AI agent. The publisher prepares material only after Lauri’s recorded approval; a preview, merge or HTML file does not establish successful deployment. The evidence panel keeps those distinctions.'};
  const lounge={id:'lounge',name:'Coffee lounge',label:'A WELL-EARNED PAUSE',color:'#d7b474',path:'Illustrated break · no real agent is paused',description:'A coffee machine, a sofa and a little breathing room. An idle colleague occasionally takes a break and returns before their next handoff. Breaks and bubbles are illustrations; no real agent is paused and no materials are changed.'};
  const chatgpt={id:'chatgpt',name:'External review',label:'THE WHOLE-WEBPAGE VIEW',color:'#82cbb6',path:'External review · requested by Lauri',description:'Lauri sometimes asks an external reviewer to review the whole webpage: structure, clarity, consistency and usability across pages. An external reviewer offers another perspective alongside Claude’s lesson workflow. Lauri selects suggestions and briefs development. This is a user-described workflow; no conversation or completed review is inferred from Git. It does not replace science or pedagogy approval.'};
  const wholeWebReview=()=>$('replay-mode').value==='website';
  const orchestrator={id:'orchestrator',name:'Orchestrator',label:'THE COORDINATION DESK',color:'#c2ad80',path:'.claude/commands/lesson.md · .claude/commands/exercises.md',description:'Coordinates packets, checks, parallel reviewers, correction rounds and review scope. Committed usage files record orchestrator entries. This is coordination work performed by the command session, not a fourth dedicated agent definition. No private conversations or exact working times are inferred.'};
  const support={id:'support',name:'General-purpose agent',label:'RECORDED SUPPORT WORK',color:'#a9b5db',path:'Committed review/usage.tsv · agent=general-purpose',description:'Committed usage files include additional general-purpose agent work. The log does not establish a permanent specialty or its exact brief, so this office shows recorded support work without inventing a reviewer or an approval role.'};
  const officeRoles = [orchestrator,support,chatgpt,teacher,...roles.slice(0,3),checks,gatekeeper,roles[3],website,lounge];
  const days = [...new Set(history.events.map(e=>e.day))].sort().reverse();
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  let selected = [], minute = 0, playing = false, lastFrame = 0, lastPaint = 0, phase = 0;
  let lessonState = null, snapshotEvent = null, workflowKey = '';
  let journey=[],journeyIndex=-1,selectedFrame=null;
  const roundInfo=()=>journeyIndex<0?null:{index:journeyIndex,total:journey.length,version:journey[journeyIndex].version,commit:journey[journeyIndex].event.id};
  const canvas = $('office');
  const dayLabel = day => i18n.dateLabel(day);
  const time = m => window.OfficeTime.replay(m);
  const roleNames = ids => ids.map(id=>id==='repository'?'Repository changes':roles.find(r=>r.id===id)?.name || id).join(' · ');
  const activeRoles = () => new Set(selected.filter(e=>e.minute<=minute && minute-e.minute<8).flatMap(e=>e.roles));
  const scene = window.AgentOfficeScene.create(canvas,{state:()=>lessonState,event:()=>snapshotEvent,active:activeRoles,phase:()=>phase,still:()=>$('motion').checked,presentation:()=>document.body.classList.contains('office-only'),round:roundInfo,wholeWebReview,speechEnabled:()=>$('bubbles').checked});
  const allMaterials = new Map((history.snapshots || []).flat().map(lesson=>[lesson.id,lesson.title]));
  for(const [id,title] of [...allMaterials].sort()){
    const option=document.createElement('option');option.value=id;option.textContent=`${id.toUpperCase()} · ${title}`;$('lesson').append(option);
  }
  function workflow(event){
    const key=`${event?.id || ''}:${$('lesson').value}`;
    if(key===workflowKey)return;
    workflowKey=key;snapshotEvent=event;
    const states=history.snapshots?.[event?.snapshot] || [];
    const target=$('lesson').value==='auto'?(event?.changedLessons?.find(id=>states.some(s=>s.id===id)) || states[0]?.id):$('lesson').value;
    lessonState=states.find(s=>s.id===target) || null;
    selectedFrame={state:lessonState,event};
    journey=window.OfficeJourney.build(history,window.OFFICE_LINEAGE,event,target);
    journeyIndex=-2;phase=0;
    syncJourney();
  }
  function updateClock(){
    const stage=$('replay-mode').value==='walkthrough';
    const label=t(stage?'Commit time · Helsinki':'Replay time · Helsinki');
    const value=stage?window.OfficeTime.commit(snapshotEvent?.timestamp):time(minute);
    const title=stage && snapshotEvent?`${snapshotEvent.day} · ${snapshotEvent.timestamp}`:t('Day timeline · Europe/Helsinki');
    if($('clock-label').textContent!==label)$('clock-label').textContent=label;
    if($('clock').textContent!==value)$('clock').textContent=value;
    if($('clock').title!==title)$('clock').title=title;
  }
  function syncJourney(){
    const index=$('replay-mode').value==='walkthrough' && journey.length?Math.min(Math.floor(phase/42),journey.length-1):-1;
    const frame=index<0?selectedFrame:journey[index];
    if(!frame)return;
    if(index===journeyIndex && lessonState===frame.state && snapshotEvent===frame.event)return;
    journeyIndex=index;lessonState=frame.state;snapshotEvent=frame.event;
    evidence(lessonState,snapshotEvent);
    updateClock();
  }
  function evidence(state,event){
    $('lesson-title').textContent=state?`${state.id.toUpperCase()} · ${state.title}`:'No material snapshot at this point in the recorded history.';
    const labels={PASS:'PASS · current version',FAIL:'FAIL · revision needed',stale:'STALE · content changed',missing:'Waiting for review',invalid:'Invalid report · blocked'};
    for(const role of ['science','pedagogy']){
      const report=state?.[role];const status=report?.status || 'missing';
      $(role+'-status').textContent=state?(report?.carried?'PASS · recorded carry':labels[status] || 'Not observed'):'Not observed';
      $(role+'-card').dataset.state=status;
      $(role+'-evidence').textContent=report?.hash?`Report: ${report.hash}${report.carried?' · recorded carry: '+report.carried.categories:status==='stale'?' · no longer matches':''}`:state?'No valid matching report in this snapshot.':'';
    }
    $('stage-draft').dataset.state=state?'PASS':'missing';
    $('stage-checks').dataset.state=state?.checks.failed?'FAIL':'unknown';
    $('checks-status').textContent=state?.checks.failed?`${state.checks.failed} saved failures · freshness unknown`:state?.checks.passed?`${state.checks.passed} saved passes · freshness unknown`:'No check results observed';
    $('stage-reviews').dataset.state=state?.eligible?'PASS':state && [state.science.status,state.pedagogy.status].includes('FAIL')?'FAIL':'unknown';
    $('stage-gate').dataset.state=state?(state.eligible?'PASS':'FAIL'):'unknown';
    $('gate-status').textContent=state?(state.eligible?'OPEN · current or recorded carried PASS':'CLOSED · both current approvals required'):'No material selected';
    $('stage-publish').dataset.state='unknown';
    const statuses=state?[state.science.status,state.pedagogy.status]:[];
    $('handoff-status').textContent=!state?'Select an event or a different material to inspect the gate.':state.eligible?'Review gate cleared. Automated checks and Lauri’s publication decision remain separate.':statuses.includes('FAIL')?'Return to developer: a reviewer found a blocking issue. Fix it, run checks and request independent review again.':statuses.includes('stale')?'Return to review: the material changed after approval. Earlier PASS reports cannot open this gate.':'Waiting for both independent reviewers. A missing or invalid approval keeps the gate closed.';
    const work=state?.work;
    $('work-stats').replaceChildren();
    for(const [key,label] of [['development','Development entries'],['fixes','Correction entries'],['science','Science review entries'],['pedagogy','Pedagogy review entries'],['full','Full review entries'],['delta','Partial review entries'],['orchestration','Coordination entries'],['support','Support entries']]){
      const item=document.createElement('div'),value=document.createElement('b'),name=document.createElement('span');
      value.textContent=work?.entries?String(work[key] || 0):'—';name.textContent=t(label);item.append(value,name);$('work-stats').append(item);
    }
    const exercises=state?.exercises;
    const describe=report=>report?.carried?'PASS · recorded carry':report?.status || 'missing';
    $('exercise-status').textContent=exercises?t('Exercise set: science {science}; pedagogy {pedagogy}. Separate content hash: {hash}.',{science:describe(exercises.science),pedagogy:describe(exercises.pedagogy),hash:exercises.hash}):t('This snapshot predates separate exercise approvals.');
    $('work-evidence').textContent=work?.entries?t('{count} recorded usage entries. Highest recorded round: {round}.',{count:work.entries,round:work.round || '—'}):t('No committed usage entries for this material in this snapshot.');
    $('usage-sources').replaceChildren();
    for(const path of work?.sources || []){
      const item=document.createElement('li'),link=document.createElement('a');
      link.textContent=path;link.href=`https://github.com/Hellsla/hellsla.github.io/blob/${event.id}/${path}`;
      link.target='_blank';link.rel='noopener noreferrer';item.append(link);$('usage-sources').append(item);
    }
    $('snapshot-evidence').textContent=event?`Commit ${event.id.slice(0,7)} · ${event.timestamp}. ${state?.hash?'Material content hash: '+state.hash+'.':''} This is the displayed stage’s committed snapshot, including its branch context.`:'No commit at the current replay time.';
    $('files-evidence').textContent=state?`Material packet: ${state.files.join(', ')}. Reviewers return separate reports; they do not take ownership of or edit the material.`:'';
    $('site-evidence').textContent=state?(state.included?'This material has an HTML page in this commit’s site/ snapshot. That does not establish a fresh build or successful deployment.':'This material has no HTML page in this commit’s site/ snapshot.')+(state.legacy.status==='PASS'?'\nA current legacy marker allows the earlier prototype exception; it does not clear the two-review gate.':''):'';
  }
  function showRole(role) {
    $('role-name').textContent = role.name;
    const hasPortrait=!['lounge','gatekeeper','site'].includes(role.id);
    $('role-portrait-frame').hidden=!hasPortrait;
    if(hasPortrait){
      window.AgentOfficeScene.create($('role-portrait'),{phase:()=>0,still:()=>true}).portrait(role.id);
      $('role-portrait-caption').textContent=role.name;
    }
    $('role-label').textContent = role.label;
    $('role-description').textContent = i18n.roleDescription(role.id,role.description);
    $('role-path').textContent = role.path;
    $('role-dialog').querySelector('.subtle').textContent=role.id==='chatgpt'?'The whole-webpage review is an optional workflow described by Lauri. It is not recorded agent activity and does not change the selected material’s evidence.':role.id==='gatekeeper'?(lessonState?`${lessonState.id.toUpperCase()}: science ${lessonState.science.status}; pedagogy ${lessonState.pedagogy.status}. Recorded review eligibility ${lessonState.eligible?'cleared':'blocked'}. `:'No material snapshot selected. ')+'The walkthrough desk separately waits for both report deliveries. Passing review clears only the review requirement; automated checks and Lauri’s publication decision are separate.':'Room activity comes from recorded file changes. Couriers and handoffs illustrate the workflow; they are not records of running agents, actual conversations or human approvals.';
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
    if(value && $('replay-mode').value==='walkthrough' && journey.length && phase>=journey.length*42-.001)phase=0;
    playing=value && (wholeWebReview() || selected.length>0);
    $('play').replaceChildren(document.createTextNode(playing?'Ⅱ ':'▶ '),Object.assign(document.createElement('span'),{textContent:playing?'Pause':'Play'}));
    $('play').setAttribute('aria-label',`${playing?'Pause':'Play'} ${wholeWebReview()?'whole webpage review':$('replay-mode').value==='history'?'day history':'material journey'}`);
    $('play').setAttribute('aria-pressed',String(playing));
    $('presentation-play').textContent=playing?'Pause':'Play';
    $('presentation-play').setAttribute('aria-label',playing?'Pause':'Play');
  }
  function seek(value){minute=Math.max(0,Math.min(1439.999,Number(value)));update();draw();}
  function update(){
    $('timeline').value=minute;updateClock();
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
      b.type='button';t.textContent=window.OfficeTime.commit(event.timestamp);t.dateTime=event.timestamp;t.title=event.timestamp;
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
  $('next-stage').addEventListener('click',()=>{setPlaying(false);if(journey.length){phase=Math.min(Math.floor(phase/42)+1,journey.length-1)*42;draw();}});
  $('next-handoff').addEventListener('click',()=>{setPlaying(false);const next=scene.nextHandoff();phase=Math.floor(phase/42)*42+next;if(next===0)phase+=42;if(!wholeWebReview() && journey.length && phase>=journey.length*42)phase=journey.length*42-.001;draw();});
  $('replay-mode').addEventListener('change',()=>{
    setPlaying(false);phase=0;journeyIndex=-2;syncJourney();
    document.body.classList.toggle('website-review',wholeWebReview());
    $('web-review').hidden=!wholeWebReview();
    $('play').disabled=!wholeWebReview() && !selected.length;
    $('data-source').textContent=wholeWebReview()?'Workflow described by Lauri · illustrative playback':`Git history · ${history.events.length} commits · Europe/Helsinki`;
    $('mode-label').textContent=wholeWebReview()?'WEBPAGE REVIEW MODEL':$('replay-mode').value==='history'?'DAY HISTORY':'MATERIAL WALKTHROUGH';
    draw();
  });
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
    syncJourney();
    updateClock();
    const result=scene.draw();
    if(wholeWebReview())for(const [index,item] of [...$('web-review').querySelectorAll('li')].entries()){
      if(index===result.step)item.setAttribute('aria-current','step');else item.removeAttribute('aria-current');
    }
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
    if(animating){phase+=dt*Number($('speed').value);if($('replay-mode').value==='walkthrough' && journey.length && phase>=journey.length*42){phase=journey.length*42-.001;setPlaying(false);}}
    if(animating || now-lastPaint>250){draw();lastPaint=now;}
    requestAnimationFrame(frame);
  }
  const latestEvent=history.events.at(-1);
  $('history-freshness').textContent=latestEvent?t('Recorded through {day} {time} · Helsinki. Static history snapshot.',{day:latestEvent.day,time:window.OfficeTime.commit(latestEvent.timestamp)}):t('No recorded history.');
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
