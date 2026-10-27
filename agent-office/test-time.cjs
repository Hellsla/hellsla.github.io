// node agent-office/test-time.cjs
const assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const context={window:{}};vm.createContext(context);
vm.runInContext(fs.readFileSync(__dirname+'/office-time.js','utf8'),context);
const time=context.window.OfficeTime;
assert.equal(time.commit('2026-10-26T08:32:16+02:00'),'08:32:16');
assert.equal(time.commit('2026-10-26T08:32:17+02:00'),'08:32:17');
assert.equal(time.commit('2026-10-26T06:32:17Z'),'08:32:17');
assert.equal(time.commit('2026-10-25T00:30:00Z'),'03:30:00','Before Helsinki autumn clock change');
assert.equal(time.commit('2026-10-25T01:30:00Z'),'03:30:00','After autumn clock change: repeated local time is legitimate');
assert.equal(time.commit('2026-03-29T00:30:00Z'),'02:30:00');
assert.equal(time.commit('2026-03-29T01:30:00Z'),'04:30:00','Skip the missing spring hour');
assert.equal(time.commit('not recorded'),'--:--:--');
assert.equal(time.replay(448.23333333333335),'07:28:14');
assert.equal(time.replay(1439.999),'23:59:59');
assert.equal(time.replay(0),'00:00:00');
console.log('PASS: second precision, timeline rounding, UTC conversion and Helsinki daylight saving changes');
