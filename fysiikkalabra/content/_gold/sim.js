// Gold-standard simulation: block under net force. p5.js instance mode.
new p5((p) => {
  let m, F, f, v = 0, t = 0, hist = [];
  p.setup = () => { p.createCanvas(600, 400);
    m = p.createSlider(1, 20, 5, 0.5); F = p.createSlider(0, 50, 20, 1); f = p.createSlider(0, 20, 5, 1); };
  p.draw = () => {
    const a = Math.max(0, (F.value() - f.value()) / m.value()); // a = (F − f)/m, no backward motion
    v += a / 60; t += 1 / 60; hist.push([t, v]); if (hist.length > 600) hist.shift();
    window.simState = { m: m.value(), F: F.value(), f: f.value(), a, v, t };
    p.background(250); p.fill(0); p.text(`a = ${a.toFixed(2)} m/s²   v = ${v.toFixed(1)} m/s`, 20, 30);
    p.noFill(); p.beginShape(); hist.forEach(([tt, vv]) => p.vertex(300 + (tt % 10) * 28, 380 - vv * 4)); p.endShape();
  };
});
