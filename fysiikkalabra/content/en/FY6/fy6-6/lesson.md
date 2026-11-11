# Electric power and the heating of a resistor

> **Why** do the resistance wires of a toaster glow red while the toaster's cord stays cool, even though the same current flows through both?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration, a close-up: a toaster on a kitchen worktop seen from slightly above. In its two slots the heating wires glow red-orange, and hot air shimmers above them. In the foreground the toaster&#x27;s black cord runs over the worktop to the wall socket. The cord has its ordinary colour and does not glow." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy66h-top" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><linearGradient id="fy66h-steel" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8a96a3"/><stop offset="0.25" stop-color="#ffffff"/><stop offset="0.6" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient><linearGradient id="fy66h-topface" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#dfe4e9"/><stop offset="1" stop-color="#f4f6f8"/></linearGradient><radialGradient id="fy66h-glow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#ffc078"/><stop offset="0.55" stop-color="#e8590c" stop-opacity="0.8"/><stop offset="1" stop-color="#e8590c" stop-opacity="0"/></radialGradient></defs>
  <rect x="0" y="0" width="1200" height="380" fill="#f6f1e6"/>
  <line x1="0" y1="0" x2="0" y2="380" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="95" y1="0" x2="95" y2="380" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="190" y1="0" x2="190" y2="380" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="285" y1="0" x2="285" y2="380" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="380" y1="0" x2="380" y2="380" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="475" y1="0" x2="475" y2="380" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="570" y1="0" x2="570" y2="380" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="665" y1="0" x2="665" y2="380" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="760" y1="0" x2="760" y2="380" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="855" y1="0" x2="855" y2="380" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="950" y1="0" x2="950" y2="380" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1045" y1="0" x2="1045" y2="380" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1140" y1="0" x2="1140" y2="380" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="0" x2="1200" y2="0" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="95" x2="1200" y2="95" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="190" x2="1200" y2="190" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="285" x2="1200" y2="285" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="380" x2="1200" y2="380" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <rect x="-10" y="380" width="1220" height="230" rx="4" fill="url(#fy66h-top)" stroke="#1f2933" stroke-width="3"/>
  <path d="M0,437.5 q305,-14 610,0 t590,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.6"/>
  <path d="M0,495 q305,-14 610,0 t590,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.6"/>
  <path d="M0,552.5 q305,-14 610,0 t590,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.6"/>
  <line x1="0" y1="380" x2="1200" y2="380" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="972" y="150" width="132" height="132" rx="14" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <circle cx="1038" cy="216" r="46" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="1010" y="190" width="56" height="62" rx="12" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <path d="M130,330 L770,330 L770,600 L130,600 Z" fill="url(#fy66h-steel)" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M130,330 L770,330 L700.0,170 L200.0,170 Z" fill="url(#fy66h-topface)" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linejoin="round"/>
  <rect x="766" y="430" width="40" height="24" rx="6" fill="#1f2933"/>
  <circle cx="450" cy="500" r="34" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <line x1="450" y1="500" x2="472" y2="478" stroke="#1f2933" stroke-width="4" stroke-linecap="round"/>
  <ellipse cx="450" cy="230" rx="330" ry="120" fill="url(#fy66h-glow)" fill-opacity="0.85"/>
  <path d="M244.5,196 L655.5,196 L672,234 L228,234 Z" fill="#1f2933" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linejoin="round"/>
  <path d="M254,201 L238,229" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M254,203 L238,227" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M272.5,201 L258.5,229" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M272.5,203 L258.5,227" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M291.5,201 L278.5,229" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M291.5,203 L278.5,227" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M310,201 L298.5,229" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M310,203 L298.5,227" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M328.5,201 L319,229" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M328.5,203 L319,227" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M347.5,201 L339,229" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M347.5,203 L339,227" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M366,201 L359,229" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M366,203 L359,227" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M384.5,201 L379.5,229" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M384.5,203 L379.5,227" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M403.5,201 L399.5,229" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M403.5,203 L399.5,227" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M422,201 L419.5,229" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M422,203 L419.5,227" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M440.5,201 L440,229" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M440.5,203 L440,227" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M459.5,201 L460,229" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M459.5,203 L460,227" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M478,201 L480.5,229" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M478,203 L480.5,227" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M496.5,201 L500.5,229" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M496.5,203 L500.5,227" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M515.5,201 L520.5,229" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M515.5,203 L520.5,227" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M534,201 L541,229" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M534,203 L541,227" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M552.5,201 L561,229" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M552.5,203 L561,227" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M571.5,201 L581,229" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M571.5,203 L581,227" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M590,201 L601.5,229" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M590,203 L601.5,227" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M608.5,201 L621.5,229" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M608.5,203 L621.5,227" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M627.5,201 L641.5,229" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M627.5,203 L641.5,227" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M646,201 L662,229" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M646,203 L662,227" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M216,262 L684,262 L702.5,304 L197.5,304 Z" fill="#1f2933" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linejoin="round"/>
  <path d="M226.5,267 L209,299" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M226.5,269 L209,297" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M247.5,267 L232,299" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M247.5,269 L232,297" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M269,267 L255,299" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M269,269 L255,297" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M290.5,267 L278,299" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M290.5,269 L278,297" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M311.5,267 L300.5,299" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M311.5,269 L300.5,297" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M333,267 L323.5,299" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M333,269 L323.5,297" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M354,267 L346.5,299" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M354,269 L346.5,297" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M375.5,267 L369.5,299" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M375.5,269 L369.5,297" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M397,267 L392.5,299" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M397,269 L392.5,297" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M418,267 L415.5,299" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M418,269 L415.5,297" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M439.5,267 L438.5,299" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M439.5,269 L438.5,297" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M460.5,267 L461.5,299" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M460.5,269 L461.5,297" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M482,267 L484.5,299" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M482,269 L484.5,297" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M503,267 L507.5,299" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M503,269 L507.5,297" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M524.5,267 L530.5,299" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M524.5,269 L530.5,297" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M546,267 L553.5,299" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M546,269 L553.5,297" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M567,267 L576.5,299" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M567,269 L576.5,297" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M588.5,267 L599.5,299" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M588.5,269 L599.5,297" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M609.5,267 L622,299" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M609.5,269 L622,297" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M631,267 L645,299" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M631,269 L645,297" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M652.5,267 L668,299" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M652.5,269 L668,297" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M673.5,267 L691,299" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M673.5,269 L691,297" fill="none" stroke="#ffc078" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M270,162 q-12,-20 0,-40 t0,-40 t0,-40" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.75"/>
  <path d="M360,162 q-12,-20 0,-40 t0,-40 t0,-40" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.75"/>
  <path d="M450,162 q-12,-20 0,-40 t0,-40 t0,-40" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.75"/>
  <path d="M540,162 q-12,-20 0,-40 t0,-40 t0,-40" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.75"/>
  <path d="M630,162 q-12,-20 0,-40 t0,-40 t0,-40" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.75"/>
  <path d="M770,548 C880,580 880,470 960,468 C1040,466 1040,360 1038,252" fill="none" stroke="#1f2933" stroke-width="18" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M770,548 C880,580 880,470 960,468 C1040,466 1040,360 1038,252" fill="none" stroke="#6b7480" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.7"/>
</svg>

## Key idea

### Power: how fast electrical energy is transformed
Power tells how much energy is transformed from one form to another per second (chapter *Power: $P = \Delta E/\Delta t$*). In a circuit it can be found from the voltage and the current. Voltage tells how much energy one coulomb of charge gives up as it passes through a component: $12\,\text{V}$ means $12\,\text{J}$ per coulomb (chapter *Circuit, electric current and voltage*). Current tells how many coulombs pass through the component per second. Multiplying the two gives the electrical energy transformed in the component per second, the **electric power** $P = UI$.

In the resistor in the figure, $0.50\,\text{C}$ passes through every second, and each coulomb gives up $12\,\text{J}$ in it. So $6.0\,\text{J}$ of electrical energy is transformed per second, and the power of the resistor is $6.0\,\text{W}$. The unit of power is the watt: $1\,\text{W} = 1\,\text{J/s} = 1\,\text{V} \cdot 1\,\text{A}$.

<svg data-fig="energia" viewBox="0 0 600 340" role="img" aria-label="Circuit diagram, not to scale: a voltage source U = 12 V and a resistor R in the same loop. Purple arrows show the direction of the current I = 0.50 A from the positive terminal through the resistor to the negative terminal. An orange energy-flow arrow leaves the resistor, with 6.0 J per second marked beside it. Below is the calculation: 12 J per coulomb times 0.50 C per second is 6.0 J per second, that is 6.0 W." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy66-en-heat" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></linearGradient></defs>
  <polyline points="80,145 80,70 330,70 330,236 80,236 80,161" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="54" y1="145" x2="106" y2="145" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="67" y1="161" x2="93" y2="161" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <foreignObject x="34" y="120.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="34" y="160.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="114" y="138.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U = 12\,\text{V}$</div></foreignObject>
  <rect x="318" y="121" width="24" height="64" fill="#f2a69c" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="276" y="138.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$R$</div></foreignObject>
  <path d="M215,70 L195,62 L195,78 Z" fill="#7048e8" stroke-linejoin="round"/>
  <path d="M195,236 L215,228 L215,244 Z" fill="#7048e8" stroke-linejoin="round"/>
  <path d="M330,122 L322,102 L338,102 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="120" y="21.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I = 0.50\,\text{A}$</div></foreignObject>
  <path d="M354,164 L404,164 L404,175 L434,153 L404,131 L404,142 L354,142 Z" fill="url(#fy66-en-heat)" stroke-linejoin="round"/>
  <foreignObject x="446" y="118.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$6.0\,\text{J}$</div></foreignObject>
  <foreignObject x="446" y="156.5" width="136" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{per second}$</div></foreignObject>
  <foreignObject x="65" y="285.5" width="470" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$12\,\tfrac{\text{J}}{\text{C}} \cdot 0.50\,\tfrac{\text{C}}{\text{s}} = 6.0\,\tfrac{\text{J}}{\text{s}} = 6.0\,\text{W}$</div></foreignObject>
</svg>

### Joule's law: why a resistor heats up
In a resistor the electric field accelerates free electrons, but they keep colliding with the ions of the metal (chapter *Resistance and Ohm's law*). In the collisions the energy the electrons have gained is passed on to the vibrations of the ions: electrical energy is transformed into internal energy of the resistor, and the resistor warms up. From a warm resistor, energy is transferred as heat to the surroundings.

When Ohm's law $U = RI$ is substituted into the formula for power, the power of the resistor becomes $P = RI \cdot I = RI^2$. This is **Joule's law**: the power transformed into internal energy in a resistor is proportional to the resistance and to the square of the current. When the current through the same resistor doubles and its resistance stays the same, the heating power becomes four times larger.

### How power is shared in a circuit
The same current flows through resistors in series (chapter *Resistors in series and in parallel*), so by Joule's law $P = RI^2$ a larger resistance gets a larger power. Resistors in parallel have the same voltage. Then it is best to calculate the power from the voltage: when $I = U : R$, the power is $P = U^2 : R$, and a smaller resistance gets a larger power.

In the figure, the same $4\,\Omega$ and $8\,\Omega$ resistors are connected to a $12\,\text{V}$ source, first in series and then in parallel. In both connections the powers of the resistors add up to the power $UI$ given by the source, because energy is conserved. In the series connection $4.0\,\text{W} + 8.0\,\text{W} = 12\,\text{W}$, and the power of the source is $12\,\text{V} \cdot 1.0\,\text{A} = 12\,\text{W}$.

<svg data-fig="jako" viewBox="0 0 600 380" role="img" aria-label="Horizontal bar graph to scale: the powers P in watts of resistors of 4 ohms and 8 ohms connected to a 12 volt voltage source. At the top the series connection, where the same current 1.0 A flows through both: the power of the 4 ohm resistor is 4.0 W and that of the 8 ohm resistor 8.0 W, so the larger resistance gets the larger power. At the bottom the parallel connection, where the same voltage 12 V is across both: the power of the 4 ohm resistor is 36 W and that of the 8 ohm resistor 18 W, so the smaller resistance gets the larger power." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy66-jako-bar" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></linearGradient></defs>
  <line x1="247.5" y1="318" x2="247.5" y2="24" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="325" y1="318" x2="325" y2="24" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="402.5" y1="318" x2="402.5" y2="24" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="318" x2="480" y2="24" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="169" y1="318" x2="494" y2="318" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M506,318 L493,324 L493,312 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="170" y1="319" x2="170" y2="10" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M170,-2 L176,11 L164,11 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="247.5" y1="318" x2="247.5" y2="325" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="231" y="327.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="325" y1="318" x2="325" y2="325" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="308.5" y="327.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="402.5" y1="318" x2="402.5" y2="325" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="386" y="327.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="480" y1="318" x2="480" y2="325" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="463.5" y="327.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$40$</div></foreignObject>
  <foreignObject x="140" y="323.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="512" y="303.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$P\ (\text{W})$</div></foreignObject>
  <foreignObject x="178" y="31.5" width="360" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{series: same current } I = 1.0\,\text{A}$</span></div></foreignObject>
  <foreignObject x="28" y="73.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$R_1 = 4\,\Omega$</div></foreignObject>
  <rect x="170" y="75" width="31" height="26" rx="3" fill="url(#fy66-jako-bar)" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="211" y="73.5" width="86" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$4.0\,\text{W}$</div></foreignObject>
  <foreignObject x="28" y="115.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$R_2 = 8\,\Omega$</div></foreignObject>
  <rect x="170" y="117" width="62" height="26" rx="3" fill="url(#fy66-jako-bar)" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="242" y="115.5" width="86" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$8.0\,\text{W}$</div></foreignObject>
  <foreignObject x="178" y="169.5" width="360" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{parallel: same voltage } U = 12\,\text{V}$</span></div></foreignObject>
  <foreignObject x="28" y="211.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$R_1 = 4\,\Omega$</div></foreignObject>
  <rect x="170" y="213" width="279" height="26" rx="3" fill="url(#fy66-jako-bar)" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="459" y="211.5" width="86" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$36\,\text{W}$</div></foreignObject>
  <foreignObject x="28" y="253.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$R_2 = 8\,\Omega$</div></foreignObject>
  <rect x="170" y="255" width="139.5" height="26" rx="3" fill="url(#fy66-jako-bar)" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="319.5" y="253.5" width="86" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$18\,\text{W}$</div></foreignObject>
  <line x1="24" y1="157" x2="576" y2="157" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
</svg>

<figure class="unit-photo"><img src="pics/fy6/toaster-glowing.webp" alt="A toaster seen from above: orange glowing heating wires beneath and beside a slice of bread."><figcaption>The heating wires of a working toaster glow orange. Their resistance is large, so they receive almost all of the toaster's power, while the cord carrying the same current stays cool.</figcaption></figure>

### The toaster and its cord
The resistance wire of the toaster and the cord are in series, so the same current flows through them. The resistance of the wire is tens of ohms, that of the copper conductors of the cord only hundredths of an ohm. In a toaster with a power of $900\,\text{W}$, the resistance of the wire is about $59\,\Omega$ and the current about $3.9\,\text{A}$. If the resistance of the cord is $0.050\,\Omega$, the cord gets a power of $0.050\,\Omega \cdot (3.9\,\text{A})^2 \approx 0.8\,\text{W}$, which is spread over the whole length of the cord. By Joule's law the power in the cord is therefore more than a thousand times smaller than in the wire: the ratio of the resistances is $59\,\Omega : 0.050\,\Omega \approx 1200$. The resistance wire, on the other hand, glows.

### The heating of a resistor levels off
When the current is switched on, the resistor first warms up quickly, because almost all the electric power increases its internal energy. The warmer the resistor is compared with its surroundings, the more heat is transferred from it to the surroundings per second, so the heating slows down. The temperature levels off when heat is transferred from the resistor to the surroundings as fast as electrical energy arrives. That is why a resistor has a maximum permitted power, for example $0.25\,\text{W}$: at a larger power the final temperature would rise so high that the resistor would be damaged.

<svg data-fig="lampo" viewBox="0 0 600 340" role="img" aria-label="Schematic graph, not to scale: the temperature T of a resistor as a function of time t when the current is switched on at time zero. At the start the temperature is the ambient temperature T0 and rises quickly, because almost all the electric power increases the internal energy of the resistor. The warmer the resistor is, the more heat is transferred to the surroundings, so the rise slows down. Finally the temperature levels off at the value marked with a dashed line, where heat is transferred from the resistor to the surroundings as fast as electrical energy arrives." style="max-width:100%;font-size:24px">
  <line x1="79" y1="296" x2="504" y2="296" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M516,296 L503,302 L503,290 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="80" y1="297" x2="80" y2="52" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M80,40 L86,53 L74,53 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="522" y="281.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="70" y="9.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$T$</div></foreignObject>
  <line x1="80" y1="112" x2="490" y2="112" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <polyline points="80,264 83.5,258 87,252.5 90,247.5 93.5,242.5 97,237.5 100.5,233 104,228.5 107.5,224 111,220 114,216 117.5,212 121,208.5 124.5,205 128,201.5 131,198 134.5,195 138,191.5 141.5,189 145,186 148.5,183 152,180.5 155,178 158.5,175.5 162,173 165.5,171 169,168.5 172,166.5 175.5,164.5 179,162.5 182.5,160.5 186,159 189.5,157 193,155.5 196,154 199.5,152.5 203,151 206.5,149.5 210,148 213,146.5 216.5,145.5 220,144 223.5,143 227,142 230.5,140.5 234,139.5 237,138.5 240.5,137.5 244,136.5 247.5,135.5 251,135 254,134 257.5,133 261,132.5 264.5,131.5 268,131 271.5,130 275,129.5 278,129 281.5,128 285,127.5 288.5,127 292,126.5 295,126 298.5,125.5 302,125 305.5,124.5 309,124 312.5,123.5 316,123 319,122.5 322.5,122.5 326,122 329.5,121.5 333,121 336,121 339.5,120.5 343,120 346.5,120 350,119.5 353.5,119.5 357,119 360,119 363.5,118.5 367,118.5 370.5,118 374,118 377,117.5 380.5,117.5 384,117 387.5,117 391,117 394.5,116.5 398,116.5 401,116.5 404.5,116 408,116 411.5,116 415,115.5 418,115.5 421.5,115.5 425,115.5 428.5,115 432,115 435.5,115 439,115 442,114.5 445.5,114.5 449,114.5 452.5,114.5 456,114.5 459,114.5 462.5,114 466,114 469.5,114 473,114 476.5,114 480,114 483,113.5 486.5,113.5 490,113.5" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="28" y="249.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$T_0$</div></foreignObject>
  <foreignObject x="-2" y="97.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$T_\text{final}$</div></foreignObject>
  <foreignObject x="133.5" y="226.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{rises quickly}$</div></foreignObject>
  <foreignObject x="268.5" y="72" width="230" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$P_\text{in} = P_\text{out}$</div></foreignObject>
</svg>

## Formula: Electric power and Joule's law
The electric power is
```latex
P = UI
```
where $P$ is the power (W), $U$ the voltage of the component (V) and $I$ the current through the component (A). The formula holds for any component: a resistor, a lamp, a motor or a battery being charged.

For a resistor with resistance $R$, Ohm's law $U = RI$ gives the two forms of Joule's law:
```latex
P = RI^2 = \frac{U^2}{R}
```
where $R$ is the resistance of the resistor ($\Omega$). The form $RI^2$ is handy when the current is known, as in a series connection, and the form $U^2 : R$ when the voltage is known, as in a parallel connection.

The electrical energy transformed in a component in a time $t$ is
```latex
E = Pt
```
where $E$ is the energy (J) and $t$ the time (s). In a resistor this energy is transformed into internal energy and transferred as heat to the surroundings.

The power marked on a device, for example $230\,\text{V}$ and $900\,\text{W}$, is its power at the rated voltage. At a lower voltage the power of a resistive device is smaller, because $P = U^2 : R$ when the resistance stays approximately the same. In the graph the power of a resistor grows as the square of the current: when the current of a $4\,\Omega$ resistor grows from $1.0\,\text{A}$ to $2.0\,\text{A}$, the power grows from $4.0\,\text{W}$ to $16\,\text{W}$.

<svg data-fig="graph" viewBox="0 0 600 360" role="img" aria-label="Graph to scale: the power P of a resistor in watts as a function of the current I in amperes for two resistors. The parabola of the 8 ohm resistor passes through the points (1.0 A; 8.0 W) and (2.0 A; 32 W), and that of the 4 ohm resistor through the points (1.0 A; 4.0 W) and (2.0 A; 16 W). Dashed lines mark the points of the 4 ohm resistor: when the current doubles from one ampere to two, the power becomes four times larger, from 4.0 watts to 16 watts." style="max-width:100%;font-size:24px">
  <line x1="173" y1="304" x2="173" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="249.5" y1="304" x2="249.5" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="326.5" y1="304" x2="326.5" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="403" y1="304" x2="403" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="304" x2="480" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="244.5" x2="480" y2="244.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="185" x2="480" y2="185" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="125.5" x2="480" y2="125.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="66" x2="480" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="304" x2="494" y2="304" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M506,304 L493,310 L493,298 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="305" x2="96" y2="52" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,40 L102,53 L90,53 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="173" y1="304" x2="173" y2="311" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="150.5" y="313.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.5$</div></foreignObject>
  <line x1="249.5" y1="304" x2="249.5" y2="311" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="239.5" y="313.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="326.5" y1="304" x2="326.5" y2="311" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="304" y="313.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1.5$</div></foreignObject>
  <line x1="403" y1="304" x2="403" y2="311" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="393" y="313.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="480" y1="304" x2="480" y2="311" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="457.5" y="313.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2.5$</div></foreignObject>
  <line x1="89" y1="244.5" x2="96" y2="244.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="230" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="89" y1="185" x2="96" y2="185" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="170.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="89" y1="125.5" x2="96" y2="125.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="111" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="89" y1="66" x2="96" y2="66" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="51.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40$</div></foreignObject>
  <foreignObject x="66" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="512" y="289.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$I\ (\text{A})$</div></foreignObject>
  <foreignObject x="86" y="9.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$P\ (\text{W})$</div></foreignObject>
  <polyline points="96,304 99,304 101.5,304 104.5,304 107.5,303.5 110.5,303.5 113,303.5 116,303 119,303 122,302.5 124.5,302.5 127.5,302 130.5,301.5 133,301 136,301 139,300.5 142,300 144.5,299 147.5,298.5 150.5,298 153,297.5 156,296.5 159,296 162,295.5 164.5,294.5 167.5,293.5 170.5,293 173.5,292 176,291 179,290 182,289 184.5,288 187.5,287 190.5,286 193.5,285 196,284 199,282.5 202,281.5 205,280 207.5,279 210.5,277.5 213.5,276 216,275 219,273.5 222,272 225,270.5 227.5,269 230.5,267.5 233.5,266 236,264.5 239,262.5 242,261 245,259.5 247.5,257.5 250.5,256 253.5,254 256.5,252 259,250.5 262,248.5 265,246.5 267.5,244.5 270.5,242.5 273.5,240.5 276.5,238.5 279,236.5 282,234 285,232 288,230 290.5,227.5 293.5,225.5 296.5,223 299,220.5 302,218.5 305,216 308,213.5 310.5,211 313.5,208.5 316.5,206 319,203.5 322,201 325,198 328,195.5 330.5,193 333.5,190 336.5,187.5 339.5,184.5 342,182 345,179 348,176 350.5,173 353.5,170 356.5,167 359.5,164 362,161 365,158 368,155 371,151.5 373.5,148.5 376.5,145.5 379.5,142 382,138.5 385,135.5 388,132 391,128.5 393.5,125 396.5,122 399.5,118.5 402.5,115 405,111 408,107.5 411,104 413.5,100.5 416.5,96.5 419.5,93 422.5,89 425,85.5 428,81.5 431,78 433.5,74 436.5,70 439.5,66" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="96,304 99,304 102.5,304 105.5,304 109,304 112,303.5 115,303.5 118.5,303.5 121.5,303.5 125,303 128,303 131,303 134.5,302.5 137.5,302.5 141,302 144,301.5 147,301.5 150.5,301 153.5,300.5 157,300.5 160,300 163,299.5 166.5,299 169.5,298.5 173,298 176,297.5 179,297 182.5,296.5 185.5,296 189,295.5 192,294.5 195,294 198.5,293.5 201.5,293 205,292 208,291.5 211,290.5 214.5,290 217.5,289 221,288.5 224,287.5 227,286.5 230.5,286 233.5,285 237,284 240,283 243,282 246.5,281 249.5,280 253,279 256,278 259,277 262.5,276 265.5,275 269,274 272,273 275,271.5 278.5,270.5 281.5,269.5 285,268 288,267 291,265.5 294.5,264.5 297.5,263 301,261.5 304,260.5 307,259 310.5,257.5 313.5,256 317,255 320,253.5 323,252 326.5,250.5 329.5,249 333,247.5 336,246 339,244.5 342.5,243 345.5,241 349,239.5 352,238 355,236 358.5,234.5 361.5,233 365,231 368,229.5 371,227.5 374.5,226 377.5,224 381,222 384,220.5 387,218.5 390.5,216.5 393.5,214.5 397,212.5 400,211 403,209 406.5,207 409.5,205 413,203 416,200.5 419,198.5 422.5,196.5 425.5,194.5 429,192.5 432,190 435,188 438.5,185.5 441.5,183.5 445,181.5 448,179 451,176.5 454.5,174.5 457.5,172 461,170 464,167.5 467,165 470.5,162.5 473.5,160 477,157.5 480,155" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="249.5" y1="280" x2="249.5" y2="304" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="280" x2="249.5" y2="280" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="249.5" cy="280" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <line x1="403" y1="209" x2="403" y2="304" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="209" x2="403" y2="209" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="403" cy="209" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="249.5" cy="256.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="403" cy="113.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="315.5" y="55.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$R = 8\,\Omega$</div></foreignObject>
  <foreignObject x="488" y="141" width="96" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$R = 4\,\Omega$</div></foreignObject>
  <foreignObject x="261.5" y="247.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$4.0\,\text{W}$</div></foreignObject>
  <foreignObject x="417" y="210.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$16\,\text{W}$</div></foreignObject>
</svg>

## Worked example
A car's auxiliary heater has two heating resistors, $R_1 = 15\,\Omega$ and $R_2 = 30\,\Omega$, connected in parallel to a $12\,\text{V}$ battery. How large is the power of each resistor, and how much electrical energy is transformed into internal energy of the resistors in total in $5.0\,\text{min}$? The resistances of the battery and the wires are ignored.

<!-- vaihe -->

**Given and find.** $U = 12\,\text{V}$, $R_1 = 15\,\Omega$, $R_2 = 30\,\Omega$ and $t = 5.0\,\text{min}$. We are asked for the powers $P_1$ and $P_2$ and the energy $E$.

<!-- vaihe -->

**Principle.** Across each of the resistors in parallel is the full battery voltage $U$. When the voltage is known, the power is calculated from the form of Joule's law $P = U^2 : R$. The energy is the total power times the time, and the total power is the sum of the powers of the resistors.

<!-- vaihe -->

**Formula solved.**
```latex
\begin{aligned}
&P_1 = \frac{U^2}{R_1} \\
&P_2 = \frac{U^2}{R_2} \\
&E = (P_1 + P_2)\,t
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** $t = 5.0\,\text{min} = 5.0 \cdot 60\,\text{s} = 300\,\text{s}$. In addition $\text{V}^2 : \Omega = \text{V} \cdot \text{A} = \text{W}$ and $\text{W} \cdot \text{s} = \text{J}$.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
&P_1 = \frac{U^2}{R_1} \\
&\phantom{P_1} = \frac{(12\,\text{V})^2}{15\,\Omega} = 9.6\,\text{W} \\
&P_2 = \frac{(12\,\text{V})^2}{30\,\Omega} = 4.8\,\text{W} \\
&E = 14.4\,\text{W} \cdot 300\,\text{s} \\
&\phantom{E} = 4320\,\text{J}
\end{aligned}
```

<!-- vaihe -->

**Result.** The power of the resistor $R_1$ is $9.6\,\text{W}$ and that of the resistor $R_2$ is $4.8\,\text{W}$. In five minutes about $4.3\,\text{kJ}$ is transformed into internal energy. The results are given to two significant figures like the initial data.

<!-- vaihe -->

**Reasonableness.** The current from the battery is $12\,\text{V} : 15\,\Omega + 12\,\text{V} : 30\,\Omega = 0.80\,\text{A} + 0.40\,\text{A} = 1.2\,\text{A}$, so the power of the battery is $12\,\text{V} \cdot 1.2\,\text{A} = 14.4\,\text{W}$, the same as the powers of the resistors together. In a parallel connection the resistor with half the resistance gets twice the power, as it should.

## Common misconception
Many people think that a resistor with a larger resistance always heats up more, or, the other way round, that a smaller resistance always heats up more because a larger current flows through it. Neither is always true: it depends on the connection. In a series connection the current is the same, and a larger resistance gets a larger power $RI^2$. In a parallel connection the voltage is the same, and a smaller resistance gets a larger power $U^2 : R$.

Another common mistake is to calculate the power of a resistor in series with the voltage of the source. If a $4\,\Omega$ and an $8\,\Omega$ resistor are connected in series to a $12\,\text{V}$ source, the power of the $8\,\Omega$ resistor is not $(12\,\text{V})^2 : 8\,\Omega = 18\,\text{W}$, because across the resistor there is only a part of the source voltage, $8.0\,\text{V}$. In the formula $U^2 : R$ you always substitute the voltage of the very component whose power you are calculating.

## Summary
- The electric power $P = UI$ tells how many joules of electrical energy are transformed in a component per second. The unit is $1\,\text{W} = 1\,\text{V} \cdot 1\,\text{A}$.
- Joule's law: the power transformed into internal energy in a resistor is $P = RI^2 = U^2 : R$. When the current through the same resistor doubles and its resistance stays the same, the power becomes four times larger.
- In a series connection a larger resistance gets a larger power, in a parallel connection a smaller one. The powers of the components add up to the power of the source.
- The energy is $E = Pt$. A resistor warms up until heat is transferred from it to the surroundings as fast as electrical energy arrives.
