'use strict';
// Each edge follows verified Git ancestry, never merely chronological proximity.
window.OfficeJourney = {
  build(history, lineage, event, materialId) {
    const events = new Map(history.events.map(item => [item.id,item]));
    const chain=[],seen=new Set();
    while(event && !seen.has(event.id)){
      seen.add(event.id);chain.push(event);
      let parent=lineage?.[event.id];
      const candidates=lineage?._parents?.[event.id] || [];
      const stateAt=item=>history.snapshots?.[item?.snapshot]?.find(s=>s.id===materialId);
      const contentKey=state=>state?JSON.stringify([state.hash,state.science,state.pedagogy,state.exercises || null,state.work || null]):null;
      const currentKey=contentKey(stateAt(event));
      // Follow the actual merged branch when it carries this material's recorded
      // version; unrelated branches are never joined by their timestamps.
      if(currentKey && candidates.length>1){
        const matching=candidates.filter(id=>contentKey(stateAt(events.get(id)))===currentKey);
        if(matching.length===1)parent=matching[0];
      }
      event=events.get(parent);
    }
    const frames=[];let lastKey='',version=0,lastHash;
    for(const item of chain.reverse()){
      const state=history.snapshots?.[item.snapshot]?.find(material=>material.id===materialId);
      if(!state)continue;
      const key=JSON.stringify([state.hash,state.science,state.pedagogy,state.checks,state.eligible,state.included,state.legacy,state.publicationDecision || null,state.work || null,state.exercises || null]);
      if(key===lastKey)continue;
      if(state.hash!==lastHash){version++;lastHash=state.hash;}
      frames.push({state,event:item,version});lastKey=key;
    }
    return frames;
  }
};
