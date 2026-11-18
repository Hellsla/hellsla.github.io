/* Registers the service worker (work queue 17a PR 1). Only on https and localhost: not file://, not preview/.
   After the first install the page tells the worker which files it has already loaded, so the page works offline at once. */
(function () {
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
