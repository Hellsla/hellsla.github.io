'use strict';
// Shared geometry keeps furniture, doorways, walking routes and hit targets aligned.
window.OfficeFloor = {
  width:1200,height:900,
  home:{developer:[180,225],support:[390,225],science:[740,220],pedagogy:[1030,220],orchestrator:[595,470],checks:[1040,500],teacher:[470,745],repository:[835,745],chatgpt:[140,470]},
  seats:{publication:[710,745],meeting:[300,470],coffee:[115,715]},
  zones:[
    {id:'developer',x:35,y:55,w:260,h:275},{id:'support',x:300,y:100,w:185,h:230},
    {id:'science',x:620,y:55,w:250,h:275},{id:'pedagogy',x:910,y:55,w:250,h:275},
    {id:'chatgpt',x:40,y:390,w:310,h:160},{id:'orchestrator',x:490,y:380,w:155,h:145},
    {id:'gatekeeper',x:650,y:440,w:85,h:70},{id:'checks',x:960,y:400,w:200,h:160},
    {id:'lounge',x:40,y:620,w:300,h:220},{id:'teacher',x:380,y:635,w:230,h:205},
    {id:'repository',x:710,y:635,w:245,h:205},{id:'site',x:980,y:625,w:185,h:160}
  ],
  // Door gaps are part of the walls, not painted-on symbols.
  walls:[
    [30,40,1140,10],[30,40,10,820],[1160,40,10,820],
    [30,850,465,10],[575,850,595,10],
    [480,50,8,290],[35,332,185,8],[300,332,188,8],
    [612,50,8,290],[872,50,8,290],[612,332,108,8],[780,332,100,8],
    [900,50,8,290],[900,332,100,8],[1080,332,90,8],
    [35,380,315,7],[35,548,315,7],[350,380,7,48],[350,510,7,45],
    [350,620,7,220]
  ],
  paths:{
    brief:[[470,745],[590,790],[640,790],[640,575],[450,575],[450,355],[260,355],[260,310],[230,255]],
    checks:[[180,225],[260,290],[260,355],[450,355],[450,575],[925,575],[925,525]],
    science:[[740,220],[750,290],[750,355],[750,575],[925,575],[925,525],[925,575],[750,575],[750,355],[750,290],[740,220]],
    pedagogy:[[1030,220],[1040,290],[1040,355],[1115,355],[1115,575],[925,575],[925,525],[925,575],[1115,575],[1115,355],[1040,355],[1040,290],[1030,220]],
    scienceReport:[[740,220],[750,290],[750,355],[750,410],[680,470],[750,410],[750,355],[750,290],[740,220]],
    pedagogyReport:[[1030,220],[1040,290],[1040,355],[800,355],[800,540],[680,540],[680,470],[680,540],[800,540],[800,355],[1040,355],[1040,290],[1030,220]],
    scienceFeedback:[[740,220],[750,290],[750,355],[260,355],[260,290],[230,255],[260,290],[260,355],[750,355],[750,290],[740,220]],
    pedagogyFeedback:[[1030,220],[1040,290],[1040,355],[260,355],[260,290],[230,255],[260,290],[260,355],[1040,355],[1040,290],[1030,220]],
    decision:[[595,470],[535,575],[835,575],[950,640],[950,745],[950,640],[835,575],[535,575],[595,470]],
    publicationVisit:[[470,745],[590,790],[640,790],[640,575],[710,575],[710,640],[710,745]],
    publish:[[835,745],[900,805],[1090,805],[1090,755]],
    request:[[470,745],[590,790],[640,790],[640,575],[390,575],[390,470],[300,470]],
    feedback:[[140,470],[140,525],[300,525],[300,500],[300,525],[140,525],[140,470]],
    revision:[[300,470],[390,470],[390,575],[450,575],[450,355],[260,355],[260,290],[230,255]]
  },
  draw(ctx,{review,approved,external}) {
    const ink='#e7e1cf',muted='#b7beb2',wall='#424d4b',wood='#b29974';
    const b=(x,y,w,h,c)=>{ctx.fillStyle=c;ctx.fillRect(x,y,w,h);};
    const t=(s,x,y,c=muted,size=12,align='left')=>{ctx.font=`${size}px monospace`;ctx.textAlign=align;ctx.fillStyle=c;ctx.fillText(window.OfficeI18n?.t(s) ?? s,x,y);};
    const plant=(x,y)=>{b(x-10,y,20,17,'#a77755');b(x-13,y-3,26,5,'#c49b73');b(x-2,y-31,4,31,'#6a855c');b(x-17,y-26,17,9,'#8fa77c');b(x+1,y-39,16,11,'#a6b98c');};
    const books=(x,y,w)=>{b(x,y,w,42,'#7a6550');for(let i=0;i<w/10-1;i++)b(x+5+i*10,y+6,7,28-i%3*3,['#c7a770','#8caead','#b17f7e','#a9a6bd'][i%4]);b(x,y+37,w,5,wood);};
    const paper=(x,y,w=23,h=30)=>{b(x+2,y+2,w,h,'#26363840');b(x,y,w,h,'#eee6ce');for(let i=0;i<3;i++)b(x+4,y+7+i*6,w-8-i*2,2,'#97a49a');};
    const chair=(x,y,c='#52656a')=>{b(x-18,y+27,36,27,'#283c40');b(x-14,y+30,28,16,c);b(x-2,y+52,4,8,'#263638');b(x-16,y+59,32,3,'#263638');};
    const desk=(x,y,c,wide=164,monitor=true)=>{
      b(x-wide/2+4,y+15,wide,29,'#26363835');b(x-wide/2+6,y+18,7,32,'#6c5b49');b(x+wide/2-13,y+18,7,32,'#6c5b49');
      b(x-wide/2,y-16,wide,38,wood);b(x-wide/2,y+18,wide,5,'#d0b58a');
      if(monitor){b(x-54,y-73,78,48,'#24383c');b(x-49,y-68,68,37,'#345052');for(let i=0;i<4;i++)b(x-43,y-61+i*7,23+i%2*20,2,c);b(x-22,y-25,7,8,'#263b3e');b(x-33,y-18,29,4,'#263b3e');b(x-45,y-5,59,10,'#53605b');}
      chair(x,y);paper(x+43,y-8,19,23);
    };
    const board=(x,y,w,h)=>{b(x-3,y-3,w+6,h+6,'#887a60');b(x,y,w,h,'#e1e4d4');};
    const windowAt=(x,y,w)=>{b(x-4,y-4,w+8,33,'#687d7c');b(x,y,w,25,'#a4c3c0');b(x+5,y+4,w-10,15,'#bcd4cd');b(x+w/2-2,y,4,25,'#6e8a89');b(x-7,y+25,w+14,7,'#bfbaa1');b(x+7,y+34,w-10,17,'#e5dfb80a');};
    b(0,0,1200,900,'#19282c');b(24,34,1152,832,'#9a8464');
    for(let y=43;y<855;y+=28)for(let x=30;x<1160;x+=94){b(x+(y%56?-32:0),y,91,1,'#bca48045');b(x,y,1,27,'#6f604c40');}
    // Quiet review rooms, an open workshop and shared communal space.
    b(40,50,440,282,'#66716b');b(620,50,252,282,'#5b7077');b(908,50,252,282,'#786572');
    b(40,387,310,161,'#687f76');b(40,620,310,220,'#737f6a');
    b(395,660,210,168,'#736c58');b(725,660,220,168,'#68745d');
    for(const [x,y,w,h] of this.walls){b(x+3,y+4,w,h,'#273b3c45');b(x,y,w,h,wall);b(x,y,w,2,'#74817a');}
    // Glazed meeting-room wall with a real opening to the shared corridor.
    b(350,387,7,41,'#9cb6aa');b(350,510,7,38,'#9cb6aa');
    for(const [x,y] of [[260,336],[750,336],[1040,336]]){b(x-32,y-2,64,6,'#c9b38b');b(x-27,y+4,54,2,'#756d55');}
    windowAt(75,45,130);windowAt(295,45,135);windowAt(660,45,160);windowAt(948,45,165);
    t('DEVELOPMENT WORKSHOP',58,101,'#f0d2a3',15);t('SCIENCE REVIEW',637,101,'#c3e0e9',14);t('PEDAGOGY REVIEW',925,101,'#f0d1de',14);
    // Each desk has the equipment its role actually uses.
    desk(180,213,'#edba70',182);desk(390,213,'#adb9dc',140);
    paper(80,242,34,26);b(90,251,20,3,'#bb956d');b(106,245,3,18,'#8eacb7');
    b(60,131,31,49,'#897b62');paper(63,134,25,42);t('?',74,157,'#647b74',17,'center');
    t('Draft & build',180,304,'#e2d9ba',11,'center');t('Flexible support',390,304,'#d2d9d7',10,'center');
    board(640,112,204,30);t('F = ma',656,133,'#56727c',17);t('m/s²',768,133,'#56727c',13);
    desk(740,208,'#9cc6dc',164);b(800,197,27,27,'#e7e1ca');b(805,201,2,18,'#738e95');b(805,217,17,2,'#738e95');for(let i=0;i<5;i++)b(808+i*3,213-i*2,3,3,'#6a9cad');
    desk(1030,208,'#e4a8be',170);board(930,119,211,37);
    for(let i=0;i<4;i++){b(939+i*49,126,38,22,['#e5b8ad','#afc3a4','#bccbd5','#d4c1a0'][i]);b(945+i*49,132,23,2,'#72827d');}
    b(1083,191,19,31,'#293f43');b(1086,195,13,20,'#c1d1c5');b(1089,200,7,3,'#8cae9b');
    for(const [role,x] of [['science',740],['pedagogy',1030]]){
      const r=review.roles[role];
      const action=external?'Lesson reviews stay separate':r.collecting?'Collecting material':r.delivering?(r.status==='PASS'?'Returning review':'Discussing corrections'):r.work==='REVIEWING COPY'?(role==='science'?'Checking calculations':'Reading the learning path'):r.work==='REPORT DELIVERED'?'Review returned':'Waiting for material';
      t(action,x,301,'#d5ddd1',10,'center');
    }
    plant(460,290);plant(844,290);plant(1137,290);
    // Central dispatch island: a person coordinates, an inbox checks the rule.
    board(477,382,242,42);for(let col=0;col<3;col++){b(484+col*78,388,70,3,'#98a897');for(let row=0;row<2;row++)b(488+col*78,398+row*9,27+(row%2)*12,6,['#d9ba86','#a6bfc1','#c1b3c8'][col]);}
    t('COORDINATION',480,368,ink,14);desk(595,458,'#c2ad80',200,false);
    paper(519,449,28,20);paper(555,447,30,23);b(605,452,24,4,'#b37f65');
    b(651,449,67,36,'#536963');b(655,453,59,27,'#334943');
    for(const [i,role] of ['science','pedagogy'].entries()){
      const r=review.roles[role];paper(659+i*26,455,21,24);
      b(663+i*26,459,13,4,!r.arrived?'#a4ada1':r.status==='PASS'?'#7d9f78':'#bf8a77');
    }
    t('Review inbox',685,512,'#d7dece',10,'center');
    // A meeting room, not another production cubicle.
    t('EXTERNAL REVIEW',55,409,'#cee3d7',13);b(56,426,52,34,'#2b4142');b(61,431,42,23,'#9fbcb0');
    b(173,440,107,61,'#7b6c53');b(179,435,95,61,'#c2ab85');b(173,447,107,43,'#c2ab85');
    b(207,446,35,22,'#344d4f');b(211,449,27,15,'#abc8be');paper(245,467,18,21);
    chair(140,458,'#547b73');chair(300,458,'#547b73');
    // The check runner operates recognisable testing equipment.
    t('TESTING STATION',970,406,'#e2d1a8',13);desk(1040,488,'#d8bc79',156);
    b(1135,432,20,96,'#30464a');for(let i=0;i<5;i++){b(1138,439+i*16,14,10,'#677c78');b(1140,442+i*16,3,3,'#b5c898');}
    // Coffee corner and informal shared table.
    t('COFFEE & CONVERSATION',57,644,'#e0dbc1',13);
    b(59,674,139,51,'#4c6861');b(54,681,13,53,'#5e7c70');b(190,681,13,53,'#5e7c70');
    for(let i=0;i<3;i++)b(69+i*40,686,35,30,'#9eae91');b(64,723,130,11,'#4d665a');
    b(227,682,83,14,'#b49c76');b(233,696,6,42,'#6d6550');b(298,696,6,42,'#6d6550');
    b(270,650,40,34,'#2b4141');b(275,655,29,14,'#82988a');b(285,665,9,13,'#d8d6bd');
    b(225,773,88,43,'#b39b77');paper(234,779,21,25);b(278,780,12,11,'#e8dfc3');
    books(60,786,125);plant(320,807);
    // Lauri's planning nook and the publishing desk face a shared discussion area.
    t('LAURI · PLANNING',395,644,'#edddbc',13);board(400,664,186,32);t('Why?  →  Explore  →  Learn',409,686,'#5c756b',10);
    desk(470,733,'#dfbd7a',172,false);paper(421,721,30,26);b(477,725,37,6,'#b27e63');
    t('PUBLISHING',730,644,'#d8e4c7',13);desk(835,733,'#b7c89a',165);chair(710,733,'#78836c');
    t(approved?'Ready to publish':review.ready?(review.cycle>=35?'Discuss proposal':'Waiting for Lauri'):'Waiting for reviewed work',835,818,'#d4ddc8',10,'center');
    b(984,637,165,111,'#31474b');b(991,644,151,97,'#e2e2d0');b(991,644,151,17,'#728f80');
    t('FYSIIKKALABRA',1066,681,'#4c6b62',12,'center');b(1004,693,48,32,'#b5c8b1');b(1063,693,61,4,'#9aada0');b(1063,704,53,4,'#a8b6a5');b(1063,715,59,4,'#a8b6a5');
    t(external?'Webpage to discuss':'Website preview',1066,774,'#d3dccc',11,'center');
    plant(1140,818);plant(590,808);
    // Main entrance and an unobstructed common circulation space.
    b(496,843,78,10,'#c5b08b');b(494,861,82,8,'#54635b');b(485,819,100,18,'#6f7460');t('WELCOME',535,832,'#e4deca',10,'center');
  }
};
