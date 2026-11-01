// FY14 Light as particles: the photoelectric effect. A vacuum photocell: light of one wavelength λ falls on a metal
// plate (the cathode); each absorbed photon of energy E = hf can free one electron if E > W (the work function of the
// metal), and the electron leaves with a kinetic energy of at most E_k,max = hf − W. A retarding voltage U between the
// cathode and the collector (anode) slows the electrons: only those with E_k > eU reach the collector, so the current
// I falls to zero at the stopping voltage U_s = E_k,max / e. Model (Mallin oletukset in the unit): the electrons'
// kinetic energies are spread evenly between 0 and E_k,max, so I = I_sat · (1 − eU / E_k,max) for 0 ≤ eU ≤ E_k,max;
// the saturation current I_sat is proportional to the light intensity (the number of photons per second) and does not
// depend on the wavelength (one quantum efficiency for every wavelength, a simplification). Work functions are typical
// textbook values (they depend on the surface). Every canvas text goes through lab(), which pushes its ink box to
// simState.labels. simState.f is in units of 10^14 Hz (as the readout shows it), so an experiment table records
// readable values; photonE, W and Ekmax are in eV, Us and U in V, I in nA. The retarding voltage makes the cathode the
// positive plate (+) and the collector the negative one (−); its range 0–4.5 V can stop every electron of the model. p5.js 1.9 instance mode; texts from strings.json via __().
new p5((p) => {
  const H = 6.62607015e-34, E = 1.602176634e-19, C = 2.99792458e8;
  const METALS = { cs: 2.14, k: 2.29, na: 2.36, zn: 4.3 };                        // eV, typical values
  const ISAT = 20;                                                                // nA at 100 % intensity
  const CAT = 196, ANO = 430, TOP = 150, BOT = 290;                               // cathode and anode plates (x), plate ends (y)
  const INK = [31, 41, 51], ELEC = [25, 113, 194], MUTED = [107, 116, 128];
  let slL, slI, slU, selM, selSpeed, btn, readout, lL, lI, lU;
  let running = true, photons = [], electrons = [], acc = 0, labels = [];

  const state = () => {
    const lam = Number(slL.value()), f = C / (lam * 1e-9), Eph = H * f / E, W = METALS[selM.value()];
    const Ek = Math.max(0, Eph - W), U = Number(slU.value()), inten = Number(slI.value());
    const I = Ek > 0 ? ISAT * inten / 100 * Math.max(0, 1 - U / Ek) : 0;
    return { lam, f, Eph, W, Ek, U, inten, I, Us: Ek };
  };
  // visible colour of a wavelength (ultraviolet drawn violet-grey, labelled as UV)
  const rgb = (l) => {
    if (l < 380) return [150, 120, 190];
    const t = [[380, [130, 0, 200]], [440, [70, 0, 255]], [490, [0, 160, 255]], [510, [0, 200, 80]], [580, [235, 210, 0]], [645, [255, 60, 0]], [700, [200, 0, 0]]];
    for (let i = 1; i < t.length; i++) if (l <= t[i][0]) { const a = (l - t[i - 1][0]) / (t[i][0] - t[i - 1][0]); return t[i - 1][1].map((c, k) => c + a * (t[i][1][k] - c)); }
    return [200, 0, 0];
  };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('tauko')).parent(controls); btn.elt.addEventListener('click', () => { running = !running; });
    const l1 = p.createElement('label').parent(controls); lL = p.createSpan('').parent(l1); slL = p.createSlider(200, 650, 450, 5).parent(l1);
    const l2 = p.createElement('label').parent(controls); lI = p.createSpan('').parent(l2); slI = p.createSlider(0, 100, 60, 10).parent(l2);
    const l3 = p.createElement('label').parent(controls); lU = p.createSpan('').parent(l3); slU = p.createSlider(0, 4.5, 0, 0.02).parent(l3);
    const lm = p.createElement('label').parent(controls); p.createSpan(__('metalli')).parent(lm); selM = p.createSelect().parent(lm);
    for (const k of Object.keys(METALS)) selM.option(__('m_' + k), k);
    selM.selected('na');
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.5'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '2'); selSpeed.selected('1');
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { lambda: { input: slL.elt, unit: 'nm' }, intensity: { input: slI.elt, unit: '%' }, U: { input: slU.elt, unit: 'V' }, metal: { input: selM.elt, unit: '' } },
      reset: () => { slL.value(450); slI.value(60); slU.value(0); selM.selected('na'); photons = []; electrons = []; },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const s = state();
    const dt = running ? Math.min(p.deltaTime, 60) / 1000 * Number(selSpeed.value()) : 0;
    lL.html(__('aallonpituus', { l: tx(s.lam, 0) })); lI.html(__('intensiteetti', { i: tx(s.inten, 0) })); lU.html(__('jannite', { u: tx(s.U, 2) }));
    const bt = running ? __('tauko') : __('jatka'); if (btn.elt.textContent !== bt) btn.elt.textContent = bt;
    readout.html(__('lukemat', { f: tx(s.f / 1e14, 2), E: tx(s.Eph, 2), W: tx(s.W, 2) }) + '<br>'
      + (s.Ek > 0 ? __('lukemat_ek', { ek: tx(s.Ek, 2), I: tx(s.I, 1) }) : __('lukemat_ei', { I: tx(0, 1) })));
    window.simState = { lambda: s.lam, f: s.f / 1e14, metal: selM.value(), W: s.W, intensity: s.inten, U: s.U, photonE: s.Eph, Ekmax: s.Ek, Us: s.Us, I: s.I, running, labels: null };
    // photons from the lamp to the cathode: their number per second follows the intensity
    acc += dt * s.inten * 0.4;
    while (acc >= 1) { acc -= 1; photons.push({ t: 0, y: TOP + 12 + Math.random() * (BOT - TOP - 24) }); }
    photons.forEach((q) => { q.t += dt * 1.6; });
    photons = photons.filter((q) => {
      if (q.t < 1) return true;
      if (s.Ek > 0 && Math.random() < 0.7) electrons.push({ x: CAT + 6, y: q.y, v: Math.sqrt(Math.random() * s.Ek), back: false });
      return false;
    });
    // electrons: speed ∝ √E_k; the retarding field decelerates them evenly over the gap (E_k falls by eU over the gap)
    electrons.forEach((e) => {
      const gap = ANO - CAT, a = s.U / gap;                         // "energy per pixel" in eV
      const ek = Math.max(0, e.v * e.v - a * (e.x - CAT - 6));
      const sp = 120 * Math.sqrt(ek) + 6;
      if (!e.back && ek <= 0.0005) e.back = true;
      e.x += (e.back ? -1 : 1) * sp * dt * 0.9;
    });
    electrons = electrons.filter((e) => e.x < ANO - 4 && e.x > CAT + 2).slice(-160);

    const k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));
    const fh = Math.round(11 * k);
    labels = [];
    p.background(250);
    // the glass tube
    p.noStroke(); p.fill(238, 245, 249); p.rect(150, 118, 330, 205, 60);
    p.noFill(); p.stroke(170, 190, 205); p.strokeWeight(2); p.rect(150, 118, 330, 205, 60);
    // lamp and beam
    const col = rgb(s.lam);
    p.noStroke(); p.fill(60, 66, 76); p.rect(22, 40, 70, 46, 8); p.fill(...col, s.inten > 0 ? 255 : 60); p.circle(92, 63, 22);
    if (s.inten > 0) { p.fill(...col, 30 + s.inten * 0.6); p.quad(96, 52, CAT, TOP + 6, CAT, BOT - 6, 96, 74); }
    photons.forEach((q) => {                                       // a short wave packet travelling to the plate
      const dx = CAT - 96, dy = q.y - 63, L = Math.hypot(dx, dy), ux = dx / L, uy = dy / L;
      const x = 96 + dx * q.t, y = 63 + dy * q.t;
      p.stroke(...col); p.strokeWeight(2); p.noFill(); p.beginShape();
      for (let u = -9; u <= 9; u += 1.5) { const w = 3.5 * Math.sin(u * 0.9); p.vertex(x + ux * u - uy * w, y + uy * u + ux * w); }
      p.endShape();
    });
    // plates
    p.noStroke(); p.fill(150, 158, 168); p.rect(CAT - 6, TOP, 12, BOT - TOP, 2);
    p.fill(184, 98, 45); p.rect(ANO - 6, TOP, 12, BOT - TOP, 2);
    // electrons
    p.noStroke(); p.fill(...ELEC); electrons.forEach((e) => p.circle(e.x, e.y, 6));
    // circuit: from each plate down to the battery and the ammeter
    p.stroke(...INK); p.strokeWeight(2); p.noFill();
    p.line(CAT, BOT, CAT, 360); p.line(CAT, 360, 280, 360); p.line(330, 360, 367, 360); p.line(403, 360, ANO, 360); p.line(ANO, 360, ANO, BOT);
    p.line(280, 345, 280, 375); p.strokeWeight(4); p.line(292, 352, 292, 368); p.strokeWeight(2);   // battery: long + short
    p.line(292, 360, 330, 360);
    p.fill(255); p.circle(385, 360, 36); p.noFill();
    lab('$\\text{A}$', 385, 360 + fh * 0.36, 'c', fh * 1.2, INK);
    lab('$+$', CAT - 16, BOT + 18, 'c', fh * 1.3, INK); lab('$-$', ANO + 16, BOT + 18, 'c', fh * 1.3, INK);   // retarding: cathode +, collector −, below the beam
    lab(`$U = ${tx(s.U, 2)}\\,\\text{V}$`, 286, 340, 'c', fh, INK);
    lab(`$I = ${tx(s.I, 1)}\\,\\text{nA}$`, 407, 384 + fh * 0.4, 'l', fh, INK);   // beside the ammeter, under the wire
    lab(__('katodi'), CAT - 8, 345, 'r', fh, MUTED); lab(__('kerain'), ANO + 8, 345, 'l', fh, MUTED);   // under the tube, clear of the light beam
    lab(`$\\lambda = ${tx(s.lam, 0)}\\,\\text{nm}$` + (s.lam < 380 ? ' ' + __('uv') : ''), 22, 26, 'l', fh, INK);   // both readings on the top line, clear of the beam
    lab(`$E = hf = ${tx(s.Eph, 2)}\\,\\text{eV}$`, 578, 26, 'r', fh, INK);
    if (s.Ek <= 0) lab(__('ei_elektroneja'), 315, 220, 'c', fh, [138, 59, 26]);
    window.simState.labels = labels;
  };

  function lab(s, x, y, align, size, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(s), x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    p.noStroke(); p.fill(...(col || INK)); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * size, x1: x0 + w, y1: y + 0.25 * size });
  }
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '.'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
});
