'use strict';
window.OfficeTime = {
  // The timeline uses fractional minutes; round away floating-point residue.
  replay(minute) {
    const seconds=Math.max(0,Math.min(86399,Math.round(minute*60)));
    return [Math.floor(seconds/3600),Math.floor(seconds/60)%60,seconds%60]
      .map(value=>String(value).padStart(2,'0')).join(':');
  },
  commit(timestamp) {
    const date=new Date(timestamp);
    if(!Number.isFinite(date.getTime()))return '--:--:--';
    return new Intl.DateTimeFormat('en-GB',{
      timeZone:'Europe/Helsinki',hour:'2-digit',minute:'2-digit',second:'2-digit',hourCycle:'h23'
    }).format(date);
  }
};
