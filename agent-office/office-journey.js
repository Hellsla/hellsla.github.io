'use strict';
// Each edge is verified first-parent ancestry, never merely chronological proximity.
window.OfficeJourney = {
  build(history, lineage, event, materialId) {
    const events = new Map(history.events.map(item => [item.id,item]));
    const chain=[],seen=new Set();
    while(event && !seen.has(event.id)){
      seen.add(event.id);chain.push(event);event=events.get(lineage?.[event.id]);
    }
    const frames=[];let lastKey='',version=0,lastHash;
    for(const item of chain.reverse()){
      const state=history.snapshots?.[item.snapshot]?.find(material=>material.id===materialId);
      if(!state)continue;
      const key=JSON.stringify([state.hash,state.science,state.pedagogy,state.checks,state.eligible,state.included,state.legacy,state.publicationDecision || null]);
      if(key===lastKey)continue;
      if(state.hash!==lastHash){version++;lastHash=state.hash;}
      frames.push({state,event:item,version});lastKey=key;
    }
    return frames;
  }
};
