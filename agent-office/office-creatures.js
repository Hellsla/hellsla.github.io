'use strict';
// Original pixel familiars. Roles and evidence remain the controller's responsibility.
window.OfficeCreatures = {
  names: {
    developer:'Ember tinkerer', science:'Crystal owl', pedagogy:'Bloom newt',
    checks:'Circuit beetle', gatekeeper:'Ledger tortoise', site:'Parcel moth', chatgpt:'Mint wisp'
  },
  draw(ctx,x,y,id,{phase=0,moving=false,working=false,carrying=false,facing=[1,0],still=false,scale=1}={}) {
    if(!this.names[id])return false;
    const ink='#243438',cream='#fff0cc';
    const palettes={
      developer:['#e9a45d','#b85f49','#ffe0a0'],science:['#90c5dc','#547d9d','#d3edf0'],
      pedagogy:['#e7a6bb','#ae667f','#ffe0cf'],checks:['#d7bb70','#8c7950','#f4e7aa'],
      gatekeeper:['#84b5a0','#4d7e72','#cee2b2'],site:['#b6a2d4','#73658f','#e0d2ee'],
      chatgpt:['#85d2b7','#468e7e','#d0f5d6']
    };
    const [base,shade,light]=palettes[id];
    const seed=Object.keys(this.names).indexOf(id);
    const beat=still?0:Math.sin(phase*(moving?9:2.5)+seed);
    const feet=moving?beat*2:0,bob=still?0:beat*(moving?1.5:.55);
    const back=working || (moving && facing[1]<-.65 && Math.abs(facing[1])>Math.abs(facing[0]));
    const rect=(a,b,w,h,c)=>{ctx.fillStyle=c;ctx.fillRect(a,b,w,h);};
    // Stepped corners keep even the larger portraits crisp and sprite-like.
    const blob=(a,b,w,h,c)=>{
      rect(a+4,b,w-8,h,ink);rect(a,b+4,w,h-8,ink);
      rect(a+5,b+3,w-10,h-6,c);rect(a+3,b+5,w-6,h-10,c);
    };
    const eye=(a,b)=>{
      rect(a,b,8,10,cream);rect(a+3,b+2,4,7,ink);rect(a+4,b+2,2,2,'#ffffff');
    };
    ctx.save();ctx.translate(x,y);ctx.scale(scale,scale);
    rect(-22,34,44,4,'#15262d70');rect(-16,37,32,2,'#15262d40');
    if(moving && facing[0]<-.1)ctx.scale(-1,1);
    ctx.translate(0,bob);
    if(id==='developer'){
      // A stocky salamander with a solder-flame tail and oversized ear fins.
      blob(12,9,20,12,shade);blob(26,0,11,16,base);rect(30,-5,5,12,light);
      blob(-21,-27,13,20,base);blob(8,-27,13,20,base);
      rect(-16,-22,4,9,shade);rect(13,-22,4,9,shade);
      blob(-20,-17,40,45,base);blob(-12,6,24,20,light);
      rect(-17,27+feet,14,8,shade);rect(4,27-feet,14,8,shade);
      if(back){rect(-5,-15,10,5,shade);rect(-4,-5,8,5,shade);}
    }else if(id==='science'){
      // Angular crown, wide owl wings and a crystalline breastplate.
      blob(-20,-23,13,18,light);blob(7,-23,13,18,light);rect(-15,-31,5,14,base);rect(11,-31,5,14,base);
      blob(-25,-9,50,39,base);blob(-31,2,12,24,shade);blob(19,2,12,24,shade);
      blob(-12,9,24,18,light);rect(-13,28+feet,10,7,shade);rect(5,28-feet,10,7,shade);
      if(back){rect(-3,-16,6,27,light);rect(-11,-4,22,6,shade);}
    }else if(id==='pedagogy'){
      // A wide, soft newt: branching leaf gills and a curled tail.
      blob(15,16,17,12,shade);blob(25,7,10,15,base);
      for(const sign of [-1,1]){
        rect(sign<0?-29:20,-16,9,6,shade);rect(sign<0?-32:25,-22,7,6,light);
        rect(sign<0?-30:22,-4,9,6,shade);rect(sign<0?-34:28,-8,6,6,light);
      }
      blob(-23,-16,46,32,base);blob(-15,7,30,24,base);blob(-9,14,18,12,light);
      rect(-18,27+feet,13,8,shade);rect(6,27-feet,13,8,shade);
      if(back){rect(-6,-10,4,5,shade);rect(4,-7,4,5,shade);rect(-2,4,4,5,shade);}
    }else if(id==='checks'){
      // Squat beetle with four tool arms and a circuit-pattern carapace.
      rect(-14,-27,3,13,shade);rect(11,-27,3,13,shade);rect(-17,-30,9,5,light);rect(8,-30,9,5,light);
      for(const side of [-1,1])for(const row of [0,13])blob(side<0?-29:17,row,12,9,shade);
      blob(-21,-16,42,46,base);blob(-14,1,28,25,shade);
      rect(-3,1,5,22,light);rect(-11,7,24,4,light);rect(9,2,4,11,light);
      rect(-18,28+feet,13,7,shade);rect(5,28-feet,13,7,shade);
    }else if(id==='gatekeeper'){
      // A broad tortoise whose shell resembles a pair of review ledgers.
      blob(-27,0,54,32,shade);blob(-22,3,44,23,base);
      rect(-2,5,4,19,light);rect(-15,10,9,3,light);rect(6,10,9,3,light);
      rect(-15,17,9,3,light);rect(6,17,9,3,light);
      blob(-16,-18,32,28,base);rect(-22,27+feet,14,8,shade);rect(9,27-feet,14,8,shade);
    }else if(id==='site'){
      // A courier moth, with paper-fold wings and a tiny mail pouch.
      const flap=still?0:Math.round(beat*2);
      blob(-34,-19+flap,24,40,base);blob(10,-19-flap,24,40,base);
      blob(-29,-13+flap,13,23,light);blob(16,-13-flap,13,23,light);
      rect(-10,-28,3,15,shade);rect(8,-28,3,15,shade);rect(-14,-31,8,6,light);rect(7,-31,8,6,light);
      blob(-13,-16,26,43,shade);blob(-10,-12,20,21,base);
      rect(-10,27+feet,8,7,shade);rect(4,27-feet,8,7,shade);
      blob(7,13,17,15,'#b58c5f');rect(11,17,9,3,cream);
    }else if(id==='chatgpt'){
      // A mint jelly-wisp with asymmetrical antennae and a scalloped skirt.
      blob(-17,-27,9,15,base);blob(7,-31,10,19,base);rect(-15,-31,5,5,light);rect(10,-35,5,5,light);
      blob(-24,-17,48,42,base);blob(-17,-12,34,23,light);
      for(const [i,offset] of [-16,-5,7,17].entries())blob(offset-4,18,9,12+(i%2)*4,base);
      blob(-30,2,11,12,base);blob(19,2,11,12,base);
      if(back){rect(-10,-5,7,6,shade);rect(3,-8,7,6,shade);rect(-3,4,7,5,shade);}
    }
    if(!back){
      eye(-13,-8);eye(5,-8);
      rect(-3,6,6,3,ink);rect(-19,4,5,3,light);rect(15,4,5,3,light);
    }else{
      // A little profile eye remains visible while they face their monitors.
      rect(13,-5,5,7,cream);rect(16,-3,2,4,ink);
    }
    if(working){
      const tap=still?0:Math.sin(phase*9+seed);
      blob(-25,-1+tap,10,8,base);blob(16,-1-tap,10,8,base);
    }else if(carrying){blob(17,7,10,9,base);}
    ctx.restore();return true;
  }
};
