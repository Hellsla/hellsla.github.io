/* Registers the service worker (work queue 17a PR 1). Only on https and localhost: not file://, not preview/.
   After the first install the page tells the worker which files it has already loaded, so the page works offline at once. */
(function () {
  // Persistent storage (work queue 17a PR 2): once the student has made a first attempt (event fl:attempt, lesson.js) the page asks the
  // browser to keep the site's data. Only where the request shows no permission prompt (a prompt would be new interface): Chromium and
  // Safari decide silently; Firefox asks the user, so it is left out. Nothing is stored by this and nothing is shown.
  if (navigator.storage && navigator.storage.persist && !/Firefox\//.test(navigator.userAgent)) {
    document.addEventListener("fl:attempt", function ask() {
      document.removeEventListener("fl:attempt", ask);
      try { navigator.storage.persisted().then(function (p) { return p || navigator.storage.persist(); }).catch(function () {}); } catch (e) { /* none */ }
    });
  }
  var s = document.currentScript;
  if (!s || !("serviceWorker" in navigator)) return;
  var h = location.hostname;
  if (!(location.protocol === "https:" || h === "localhost" || h === "127.0.0.1" || h === "[::1]")) return;
  if (location.pathname.indexOf("/preview/") !== -1) return;
  var first = !navigator.serviceWorker.controller;
  var sw = new URL("sw.js", s.src).href;
  function warm(reg) {
    var w = reg.active || reg.waiting || reg.installing;
    if (!w) return;
    var urls = [location.href.split("#")[0]];
    performance.getEntriesByType("resource").forEach(function (r) { if (r.name.indexOf(location.origin) === 0) urls.push(r.name); });
    w.postMessage({ type: "fl-cache", urls: urls });
  }
  function go() {
    navigator.serviceWorker.register(sw).then(function () { return navigator.serviceWorker.ready; })
      .then(function (reg) { if (first) warm(reg); }).catch(function () {});
  }
  if (document.readyState === "complete") go(); else window.addEventListener("load", go);
})();
