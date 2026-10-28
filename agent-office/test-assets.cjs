// node agent-office/test-assets.cjs — catches missing or stale static asset versions.
const assert=require('node:assert/strict'),fs=require('node:fs'),crypto=require('node:crypto');
const html=fs.readFileSync(__dirname+'/index.html','utf8');
const assets=[...html.matchAll(/(?:src|href)="([^"?]+\.(?:js|css))(?:\?([^"]*))?"/g)];
assert(assets.length>0,'The office must load its static assets');
for(const [,name,query] of assets){
  const bytes=fs.readFileSync(__dirname+'/'+name);
  const digest=crypto.createHash('sha256').update(bytes).digest('hex').slice(0,12);
  assert.equal(query,'v='+digest,`${name}: run python3 agent-office/version_assets.py`);
}
console.log('PASS: all office scripts and styles have matching content-versioned URLs');
