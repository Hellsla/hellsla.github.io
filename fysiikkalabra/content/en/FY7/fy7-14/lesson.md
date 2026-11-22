# Thin-film interference

> **Why** do bright bands of colour appear on the surface of a soap bubble, even though soapy water is colourless?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: on a sunny day three soap bubbles float above a garden. The surface of the largest bubble has horizontal bands of colour: grey and white at the top, then yellow, orange, magenta, blue and green, and lower down yellow and magenta again. On a table there is a bowl of soapy water and a bubble wand. The colours are calculated from the thickness of the soap film, which increases from the top of the bubble to the bottom." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-14-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### Two reflections
In the chapter *Interference and diffraction of light* we saw that light is a wave motion and that two light waves can strengthen or weaken each other. A **thin film** is a transparent layer whose thickness is of the same order of magnitude as the wavelength of light, about $100$–$1000\,\text{nm}$: the wall of a soap bubble, an oil film on water or the coating of a lens. Of the light arriving at the film, a small part is reflected from the upper surface of the film and a small part from the lower surface. These two reflected waves travel in the same direction and **interfere**. In this chapter we consider only light that arrives at normal incidence on the film.

<svg data-fig="reflections" viewBox="0 0 600 360" role="img" aria-label="Schematic picture, not to scale: a soap film in cross-section, with air on both sides. The thickness d of the film is exaggerated, and the rays are drawn slanted so that they can be told apart; the chapter considers light at normal incidence. The ray arriving from above is partly reflected from the upper surface of the film: this is ray 1, and the wave reflected there gets a half-wavelength shift, because the light is reflected from a material of higher refractive index. Part of the light continues into the film, is reflected from the lower surface of the film against air without a shift, and returns through the upper surface into the air: this is ray 2. Ray 2 travels an extra distance in the film, twice the thickness of the film. A weak part of the light continues through the lower surface downwards." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-14-reflections.webp" x="-1.3" y="0" width="603" height="370.6" preserveAspectRatio="none"/>
  <foreignObject x="273" y="19.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <foreignObject x="320" y="19.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <foreignObject x="127" y="103.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\tfrac{1}{2}\lambda\ \text{shift}$</div></foreignObject>
  <foreignObject x="171" y="251.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{no shift}$</div></foreignObject>
  <foreignObject x="106" y="175.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$d$</div></foreignObject>
  <foreignObject x="447" y="69.5" width="137" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{air},\ n = 1.00$</div></foreignObject>
  <foreignObject x="385" y="175.5" width="199" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{soap film},\ n = 1.33$</div></foreignObject>
  <foreignObject x="447" y="285.5" width="137" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{air},\ n = 1.00$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy7/soap-bubble-reflection.webp" alt="A soap bubble in the air against a green background; an upside-down reflection of trees and sky shows on its surface, with violet and blue colours at the edges."><figcaption>A soap bubble reflects its surroundings like a convex mirror. Colours appear at its edges because light is reflected from both the outer and the inner surface of the film, and the reflected waves interfere.</figcaption></figure>

### Path difference in the film
Wave 2, reflected from the lower surface, travels through the film and back, so it travels an extra distance $2d$, where $d$ is the thickness of the film. In the film light travels at the speed $c : n$, but its frequency does not change. The wavelength in the film is therefore $n$ times shorter than in air: for example, in a soap film ($n = 1.33$) a wavelength of $550\,\text{nm}$ shortens to $413.5\,\text{nm}$, because $550\,\text{nm} : 1.33 = 413.5\,\text{nm}$. The extra distance $2d$ therefore holds as many wavelengths as the distance $2nd$ does in air. The ray reflected from the lower surface thus travels a geometric extra distance $2d$ in the film, and because light travels more slowly in the film than in air, the corresponding **optical path difference** is $2nd$. This is compared with the wavelength given in air.

### A half-wavelength shift on reflection
The path difference alone does not decide the interference. In the chapter *A wave meets an obstacle or a gap*, a pulse on a rope was inverted when it reflected from a fixed end but not from a free end. A similar rule holds for light: **when light is reflected at an interface beyond which there is a material of higher refractive index, the reflected wave is inverted**, that is, a crest returns as a trough. This corresponds to a half-wavelength shift. When the material beyond the interface has a lower refractive index, the reflected wave is not inverted. In a soap film the reflection from the upper surface occurs from air into the film ($1.00 \to 1.33$), so wave 1 is inverted. The reflection from the lower surface occurs from the film into air ($1.33 \to 1.00$), so wave 2 is not inverted.

```pysahdy
Light travels in glass ($n = 1.52$) and is reflected at the boundary between the glass and air ($1.52 \to 1.00$). Is the reflected wave inverted?
---
No, because behind the boundary there is air, which has a lower refractive index. The wave is inverted only when the material behind has a higher refractive index.
```

### A very thin film is black
When a soap film is much thinner than the wavelength, the path difference is almost zero. However, wave 1 has been inverted and wave 2 has not, so the waves are in opposite phase and cancel each other. In the ideal case a very thin soap film reflects only very little light, so in reflected light it looks dark or almost black. This is why a black spot appears at the top of a soap bubble just before it bursts. When the film is so thick that $2nd = \tfrac{1}{2}\lambda$, wave 2 lags half a wavelength behind, which corresponds to an inversion. The waves are then in phase and strengthen each other.

<svg data-fig="phase" viewBox="0 0 600 360" role="img" aria-label="Formula picture: the waves 1 and 2 reflected from the film and their sum in two cases. On the left the film is much thinner than the wavelength. Wave 1 is inverted in the reflection from the upper surface, wave 2 is not, and wave 2 has not lagged behind, so the waves are in opposite phase: a crest meets a trough, and the sum is a horizontal straight line, that is, there is no reflected light. On the right the film is so thick that wave 2 travels half a wavelength further. The waves are then in phase, and the sum is a wave of double amplitude, that is, the reflection is strong." style="max-width:100%;font-size:24px">
  <foreignObject x="82" y="21.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{very thin film}$</div></foreignObject>
  <line x1="95" y1="72" x2="95" y2="300" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <path d="M70,100 L72,102.5 L73.5,105 L75.5,107.5 L77,109.5 L79,111.5 L80.5,113.5 L82.5,115.5 L84.5,117 L86,118.5 L88,120 L89.5,121 L91.5,121.5 L93,122 L95,122 L97,122 L98.5,121.5 L100.5,121 L102,120 L104,118.5 L105.5,117 L107.5,115.5 L109,114 L111,112 L113,109.5 L114.5,107.5 L116.5,105 L118,102.5 L120,100 L121.5,97.5 L123.5,95 L125.5,93 L127,90.5 L129,88.5 L130.5,86.5 L132.5,84.5 L134,83 L136,81.5 L138,80 L139.5,79.5 L141.5,78.5 L143,78 L145,78 L146.5,78 L148.5,78.5 L150,79 L152,80 L154,81.5 L155.5,82.5 L157.5,84.5 L159,86 L161,88 L162.5,90.5 L164.5,92.5 L166.5,95 L168,97.5 L170,100 L171.5,102.5 L173.5,104.5 L175,107 L177,109.5 L179,111.5 L180.5,113.5 L182.5,115.5 L184,117 L186,118.5 L187.5,119.5 L189.5,120.5 L191.5,121.5 L193,122 L195,122 L196.5,122 L198.5,121.5 L200,121 L202,120 L204,119 L205.5,117.5 L207.5,115.5 L209,114 L211,112 L212.5,110 L214.5,107.5 L216,105 L218,102.5 L220,100.5 L221.5,98 L223.5,95.5 L225,93 L227,90.5 L228.5,88.5 L230.5,86.5 L232.5,84.5 L234,83 L236,81.5 L237.5,80.5 L239.5,79.5 L241,78.5 L243,78 L245,78 L246.5,78 L248.5,78.5 L250,79 L252,80 L253.5,81 L255.5,82.5 L257,84 L259,86 L261,88 L262.5,90 L264.5,92.5 L266,95 L268,97 L269.5,99.5 L271.5,102 L273.5,104.5 L275,107 L277,109 L278.5,111.5 L280.5,113.5 L282,115.5 L284,117" fill="none" stroke="#e64980" stroke-width="3" stroke-linejoin="round"/>
  <path d="M70,170 L72,167.5 L73.5,165 L75.5,162.5 L77,160.5 L79,158.5 L80.5,156.5 L82.5,154.5 L84.5,153 L86,151.5 L88,150 L89.5,149 L91.5,148.5 L93,148 L95,148 L97,148 L98.5,148.5 L100.5,149 L102,150 L104,151.5 L105.5,153 L107.5,154.5 L109,156 L111,158 L113,160.5 L114.5,162.5 L116.5,165 L118,167.5 L120,170 L121.5,172.5 L123.5,175 L125.5,177 L127,179.5 L129,181.5 L130.5,183.5 L132.5,185.5 L134,187 L136,188.5 L138,190 L139.5,190.5 L141.5,191.5 L143,192 L145,192 L146.5,192 L148.5,191.5 L150,191 L152,190 L154,188.5 L155.5,187.5 L157.5,185.5 L159,184 L161,182 L162.5,179.5 L164.5,177.5 L166.5,175 L168,172.5 L170,170 L171.5,167.5 L173.5,165.5 L175,163 L177,160.5 L179,158.5 L180.5,156.5 L182.5,154.5 L184,153 L186,151.5 L187.5,150.5 L189.5,149.5 L191.5,148.5 L193,148 L195,148 L196.5,148 L198.5,148.5 L200,149 L202,150 L204,151 L205.5,152.5 L207.5,154.5 L209,156 L211,158 L212.5,160 L214.5,162.5 L216,165 L218,167.5 L220,169.5 L221.5,172 L223.5,174.5 L225,177 L227,179.5 L228.5,181.5 L230.5,183.5 L232.5,185.5 L234,187 L236,188.5 L237.5,189.5 L239.5,190.5 L241,191.5 L243,192 L245,192 L246.5,192 L248.5,191.5 L250,191 L252,190 L253.5,189 L255.5,187.5 L257,186 L259,184 L261,182 L262.5,180 L264.5,177.5 L266,175 L268,173 L269.5,170.5 L271.5,168 L273.5,165.5 L275,163 L277,161 L278.5,158.5 L280.5,156.5 L282,154.5 L284,153" fill="none" stroke="#e64980" stroke-width="3" stroke-linejoin="round"/>
  <line x1="70" y1="250" x2="284" y2="250" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <foreignObject x="38" y="85.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <foreignObject x="38" y="155.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <foreignObject x="13" y="235.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1 + 2$</div></foreignObject>
  <foreignObject x="88.5" y="315.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{destructive}$</div></foreignObject>
  <foreignObject x="411.5" y="21.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2nd = \tfrac{1}{2}\lambda$</div></foreignObject>
  <line x1="387" y1="72" x2="387" y2="300" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <path d="M362,100 L364,102.5 L365.5,105 L367.5,107.5 L369,109.5 L371,111.5 L372.5,113.5 L374.5,115.5 L376.5,117 L378,118.5 L380,120 L381.5,121 L383.5,121.5 L385,122 L387,122 L389,122 L390.5,121.5 L392.5,121 L394,120 L396,118.5 L397.5,117 L399.5,115.5 L401,114 L403,112 L405,109.5 L406.5,107.5 L408.5,105 L410,102.5 L412,100 L413.5,97.5 L415.5,95 L417.5,93 L419,90.5 L421,88.5 L422.5,86.5 L424.5,84.5 L426,83 L428,81.5 L430,80 L431.5,79.5 L433.5,78.5 L435,78 L437,78 L438.5,78 L440.5,78.5 L442,79 L444,80 L446,81.5 L447.5,82.5 L449.5,84.5 L451,86 L453,88 L454.5,90.5 L456.5,92.5 L458.5,95 L460,97.5 L462,100 L463.5,102.5 L465.5,104.5 L467,107 L469,109.5 L471,111.5 L472.5,113.5 L474.5,115.5 L476,117 L478,118.5 L479.5,119.5 L481.5,120.5 L483.5,121.5 L485,122 L487,122 L488.5,122 L490.5,121.5 L492,121 L494,120 L496,119 L497.5,117.5 L499.5,115.5 L501,114 L503,112 L504.5,110 L506.5,107.5 L508,105 L510,102.5 L512,100.5 L513.5,98 L515.5,95.5 L517,93 L519,90.5 L520.5,88.5 L522.5,86.5 L524.5,84.5 L526,83 L528,81.5 L529.5,80.5 L531.5,79.5 L533,78.5 L535,78 L537,78 L538.5,78 L540.5,78.5 L542,79 L544,80 L545.5,81 L547.5,82.5 L549,84 L551,86 L553,88 L554.5,90 L556.5,92.5 L558,95 L560,97 L561.5,99.5 L563.5,102 L565.5,104.5 L567,107 L569,109 L570.5,111.5 L572.5,113.5 L574,115.5 L576,117" fill="none" stroke="#e64980" stroke-width="3" stroke-linejoin="round"/>
  <path d="M362,170 L364,172.5 L365.5,175 L367.5,177.5 L369,179.5 L371,181.5 L372.5,183.5 L374.5,185.5 L376.5,187 L378,188.5 L380,190 L381.5,191 L383.5,191.5 L385,192 L387,192 L389,192 L390.5,191.5 L392.5,191 L394,190 L396,188.5 L397.5,187 L399.5,185.5 L401,184 L403,182 L405,179.5 L406.5,177.5 L408.5,175 L410,172.5 L412,170 L413.5,167.5 L415.5,165 L417.5,163 L419,160.5 L421,158.5 L422.5,156.5 L424.5,154.5 L426,153 L428,151.5 L430,150 L431.5,149.5 L433.5,148.5 L435,148 L437,148 L438.5,148 L440.5,148.5 L442,149 L444,150 L446,151.5 L447.5,152.5 L449.5,154.5 L451,156 L453,158 L454.5,160.5 L456.5,162.5 L458.5,165 L460,167.5 L462,170 L463.5,172.5 L465.5,174.5 L467,177 L469,179.5 L471,181.5 L472.5,183.5 L474.5,185.5 L476,187 L478,188.5 L479.5,189.5 L481.5,190.5 L483.5,191.5 L485,192 L487,192 L488.5,192 L490.5,191.5 L492,191 L494,190 L496,189 L497.5,187.5 L499.5,185.5 L501,184 L503,182 L504.5,180 L506.5,177.5 L508,175 L510,172.5 L512,170.5 L513.5,168 L515.5,165.5 L517,163 L519,160.5 L520.5,158.5 L522.5,156.5 L524.5,154.5 L526,153 L528,151.5 L529.5,150.5 L531.5,149.5 L533,148.5 L535,148 L537,148 L538.5,148 L540.5,148.5 L542,149 L544,150 L545.5,151 L547.5,152.5 L549,154 L551,156 L553,158 L554.5,160 L556.5,162.5 L558,165 L560,167 L561.5,169.5 L563.5,172 L565.5,174.5 L567,177 L569,179 L570.5,181.5 L572.5,183.5 L574,185.5 L576,187" fill="none" stroke="#e64980" stroke-width="3" stroke-linejoin="round"/>
  <path d="M362,250 L364,255 L365.5,260 L367.5,264.5 L369,269 L371,273.5 L372.5,277.5 L374.5,281 L376.5,284.5 L378,287 L380,289.5 L381.5,291.5 L383.5,293 L385,293.5 L387,294 L389,293.5 L390.5,293 L392.5,291.5 L394,289.5 L396,287.5 L397.5,284.5 L399.5,281 L401,277.5 L403,273.5 L405,269 L406.5,264.5 L408.5,260 L410,255 L412,250 L413.5,245.5 L415.5,240.5 L417.5,235.5 L419,231 L421,227 L422.5,222.5 L424.5,219 L426,215.5 L428,213 L430,210.5 L431.5,208.5 L433.5,207 L435,206.5 L437,206 L438.5,206 L440.5,207 L442,208.5 L444,210 L446,212.5 L447.5,215.5 L449.5,218.5 L451,222.5 L453,226.5 L454.5,230.5 L456.5,235 L458.5,240 L460,244.5 L462,249.5 L463.5,254.5 L465.5,259.5 L467,264 L469,268.5 L471,273 L472.5,277 L474.5,281 L476,284 L478,287 L479.5,289.5 L481.5,291.5 L483.5,293 L485,293.5 L487,294 L488.5,294 L490.5,293 L492,291.5 L494,290 L496,287.5 L497.5,284.5 L499.5,281.5 L501,278 L503,274 L504.5,269.5 L506.5,265 L508,260.5 L510,255.5 L512,250.5 L513.5,245.5 L515.5,241 L517,236 L519,231.5 L520.5,227 L522.5,223 L524.5,219.5 L526,216 L528,213 L529.5,210.5 L531.5,208.5 L533,207 L535,206.5 L537,206 L538.5,206 L540.5,207 L542,208.5 L544,210 L545.5,212.5 L547.5,215 L549,218.5 L551,222 L553,226 L554.5,230.5 L556.5,235 L558,239.5 L560,244.5 L561.5,249.5 L563.5,254 L565.5,259 L567,264 L569,268.5 L570.5,273 L572.5,277 L574,280.5 L576,284" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <foreignObject x="330" y="85.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <foreignObject x="330" y="155.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <foreignObject x="305" y="235.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1 + 2$</div></foreignObject>
  <foreignObject x="374" y="315.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{constructive}$</div></foreignObject>
  <line x1="300" y1="20" x2="300" y2="340" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
</svg>

### Why a film is colourful
Sunlight is white light, which contains all the wavelengths of visible light, about $400$–$700\,\text{nm}$. In a film of a given thickness the path difference $2nd$ is constructive for some wavelengths and destructive for others. Part of the colours is then missing from the reflected light, and the film looks colourful. For example, in a soap film $200\,\text{nm}$ thick the path difference is $532\,\text{nm}$. Green light with a wavelength of $532\,\text{nm}$ is cancelled, but red and violet light are reflected, so the film looks magenta.

A soap bubble is not equally thick everywhere. Gravity drains the soapy water downwards, so the film thins at the top and thickens at the bottom. Each band of colour is a place where the film has the same thickness, and the bands move as the film drains and evaporates. In an oil film ($n \approx 1.5$) on the surface of water, the reflection from the upper surface occurs from air into oil and inverts the wave, and the reflection from the lower surface, from oil into water ($n = 1.33$), does not. The conditions are therefore the same as in a soap film. In a thick layer, such as window glass, no colours are seen. In a soap film as thick as $5\,\mu\text{m}$ there are $14$ strengthened wavelengths in the visible range, and between them there are almost as many weakened ones, so the colours mix into white.

<svg data-fig="bands" viewBox="0 0 600 300" role="img" aria-label="Picture of calculated colours: the colour of the light reflected in white light from a soap film with a refractive index of 1.33 as a function of the film thickness, at normal incidence. Above, a wedge-shaped film in cross-section, whose thickness grows from left to right from zero to 1000 nanometres (thickness exaggerated). The colour strip starts on the left as black, turns grey-blue, white, yellow, orange and, at about 200 nanometres, magenta, then blue, green, yellow and magenta again. The thicker the film, the paler the colours become. The brightness of the colours has been enhanced: the real reflection is only a few per cent." style="max-width:100%;font-size:24px">
  <path d="M40,116 L500,60 L500,116 Z" fill="#eef5f9" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <rect x="40" y="130" width="4.5" height="60" fill="#0a0d12"/>
  <rect x="43.5" y="130" width="4.5" height="60" fill="#2d3542"/>
  <rect x="47.5" y="130" width="4.5" height="60" fill="#4c586b"/>
  <rect x="51" y="130" width="4.5" height="60" fill="#68778e"/>
  <rect x="54.5" y="130" width="4.5" height="60" fill="#8193ad"/>
  <rect x="58.5" y="130" width="4.5" height="60" fill="#98abc7"/>
  <rect x="62" y="130" width="4.5" height="60" fill="#adc1dc"/>
  <rect x="66" y="130" width="4.5" height="60" fill="#bfd3ec"/>
  <rect x="69.5" y="130" width="4.5" height="60" fill="#cfe2f7"/>
  <rect x="73" y="130" width="4.5" height="60" fill="#ddeefe"/>
  <rect x="77" y="130" width="4.5" height="60" fill="#e9f7ff"/>
  <rect x="80.5" y="130" width="4.5" height="60" fill="#f2fdfd"/>
  <rect x="84" y="130" width="4.5" height="60" fill="#f9fff5"/>
  <rect x="88" y="130" width="4.5" height="60" fill="#fdffe9"/>
  <rect x="91.5" y="130" width="4.5" height="60" fill="#fffbd7"/>
  <rect x="95" y="130" width="4.5" height="60" fill="#fff4c1"/>
  <rect x="99" y="130" width="4.5" height="60" fill="#feeaa5"/>
  <rect x="102.5" y="130" width="4.5" height="60" fill="#f9dd84"/>
  <rect x="106" y="130" width="4.5" height="60" fill="#f3cc5d"/>
  <rect x="110" y="130" width="4.5" height="60" fill="#e9b829"/>
  <rect x="113.5" y="130" width="4.5" height="60" fill="#dea000"/>
  <rect x="117.5" y="130" width="4.5" height="60" fill="#cf8400"/>
  <rect x="121" y="130" width="4.5" height="60" fill="#be6539"/>
  <rect x="124.5" y="130" width="4.5" height="60" fill="#aa3f68"/>
  <rect x="128.5" y="130" width="4.5" height="60" fill="#92008e"/>
  <rect x="132" y="130" width="4.5" height="60" fill="#7600ae"/>
  <rect x="135.5" y="130" width="4.5" height="60" fill="#5400c8"/>
  <rect x="139.5" y="130" width="4.5" height="60" fill="#1e3ede"/>
  <rect x="143" y="130" width="4.5" height="60" fill="#0064ee"/>
  <rect x="146.5" y="130" width="4.5" height="60" fill="#0084fa"/>
  <rect x="150.5" y="130" width="4.5" height="60" fill="#00a0ff"/>
  <rect x="154" y="130" width="4.5" height="60" fill="#00b8ff"/>
  <rect x="158" y="130" width="4.5" height="60" fill="#2ecdff"/>
  <rect x="161.5" y="130" width="4.5" height="60" fill="#5ddef9"/>
  <rect x="165" y="130" width="4.5" height="60" fill="#7eecec"/>
  <rect x="169" y="130" width="4.5" height="60" fill="#9af6db"/>
  <rect x="172.5" y="130" width="4.5" height="60" fill="#b3fdc6"/>
  <rect x="176" y="130" width="4.5" height="60" fill="#c8ffab"/>
  <rect x="180" y="130" width="4.5" height="60" fill="#daff8c"/>
  <rect x="183.5" y="130" width="4.5" height="60" fill="#eafe68"/>
  <rect x="187" y="130" width="4.5" height="60" fill="#f7f83b"/>
  <rect x="191" y="130" width="4.5" height="60" fill="#ffee00"/>
  <rect x="194.5" y="130" width="4.5" height="60" fill="#ffe000"/>
  <rect x="198" y="130" width="4.5" height="60" fill="#ffcf2b"/>
  <rect x="202" y="130" width="4.5" height="60" fill="#ffbb5b"/>
  <rect x="205.5" y="130" width="4.5" height="60" fill="#ffa481"/>
  <rect x="209.5" y="130" width="4.5" height="60" fill="#ff89a1"/>
  <rect x="213" y="130" width="4.5" height="60" fill="#ff6bbc"/>
  <rect x="216.5" y="130" width="4.5" height="60" fill="#f34bd2"/>
  <rect x="220.5" y="130" width="4.5" height="60" fill="#e327e4"/>
  <rect x="224" y="130" width="4.5" height="60" fill="#ce0af1"/>
  <rect x="227.5" y="130" width="4.5" height="60" fill="#b525fa"/>
  <rect x="231.5" y="130" width="4.5" height="60" fill="#9648fe"/>
  <rect x="235" y="130" width="4.5" height="60" fill="#6e68fd"/>
  <rect x="238.5" y="130" width="4.5" height="60" fill="#2d85f8"/>
  <rect x="242.5" y="130" width="4.5" height="60" fill="#009fef"/>
  <rect x="246" y="130" width="4.5" height="60" fill="#00b6e1"/>
  <rect x="250" y="130" width="4.5" height="60" fill="#00cad0"/>
  <rect x="253.5" y="130" width="4.5" height="60" fill="#00dabc"/>
  <rect x="257" y="130" width="4.5" height="60" fill="#00e7a4"/>
  <rect x="261" y="130" width="4.5" height="60" fill="#00f18b"/>
  <rect x="264.5" y="130" width="4.5" height="60" fill="#29f772"/>
  <rect x="268" y="130" width="4.5" height="60" fill="#6dfb5d"/>
  <rect x="272" y="130" width="4.5" height="60" fill="#95fa53"/>
  <rect x="275.5" y="130" width="4.5" height="60" fill="#b4f759"/>
  <rect x="279" y="130" width="4.5" height="60" fill="#cef16b"/>
  <rect x="283" y="130" width="4.5" height="60" fill="#e4e782"/>
  <rect x="286.5" y="130" width="4.5" height="60" fill="#f5db9a"/>
  <rect x="290" y="130" width="4.5" height="60" fill="#ffcdb0"/>
  <rect x="294" y="130" width="4.5" height="60" fill="#ffbcc3"/>
  <rect x="297.5" y="130" width="4.5" height="60" fill="#ffaad3"/>
  <rect x="301.5" y="130" width="4.5" height="60" fill="#ff97df"/>
  <rect x="305" y="130" width="4.5" height="60" fill="#ff85e8"/>
  <rect x="308.5" y="130" width="4.5" height="60" fill="#ff74ed"/>
  <rect x="312.5" y="130" width="4.5" height="60" fill="#ff68ee"/>
  <rect x="316" y="130" width="4.5" height="60" fill="#f863ec"/>
  <rect x="319.5" y="130" width="4.5" height="60" fill="#e867e6"/>
  <rect x="323.5" y="130" width="4.5" height="60" fill="#d472dd"/>
  <rect x="327" y="130" width="4.5" height="60" fill="#bc81d1"/>
  <rect x="330.5" y="130" width="4.5" height="60" fill="#a192c4"/>
  <rect x="334.5" y="130" width="4.5" height="60" fill="#80a3b5"/>
  <rect x="338" y="130" width="4.5" height="60" fill="#58b3a5"/>
  <rect x="342" y="130" width="4.5" height="60" fill="#03c298"/>
  <rect x="345.5" y="130" width="4.5" height="60" fill="#00ce8d"/>
  <rect x="349" y="130" width="4.5" height="60" fill="#00d887"/>
  <rect x="353" y="130" width="4.5" height="60" fill="#00e088"/>
  <rect x="356.5" y="130" width="4.5" height="60" fill="#00e58e"/>
  <rect x="360" y="130" width="4.5" height="60" fill="#00e898"/>
  <rect x="364" y="130" width="4.5" height="60" fill="#4ee9a4"/>
  <rect x="367.5" y="130" width="4.5" height="60" fill="#76e7b1"/>
  <rect x="371" y="130" width="4.5" height="60" fill="#95e4bd"/>
  <rect x="375" y="130" width="4.5" height="60" fill="#afdec8"/>
  <rect x="378.5" y="130" width="4.5" height="60" fill="#c5d7d0"/>
  <rect x="382" y="130" width="4.5" height="60" fill="#d7ced7"/>
  <rect x="386" y="130" width="4.5" height="60" fill="#e5c5da"/>
  <rect x="389.5" y="130" width="4.5" height="60" fill="#f0badc"/>
  <rect x="393.5" y="130" width="4.5" height="60" fill="#f9b0da"/>
  <rect x="397" y="130" width="4.5" height="60" fill="#fea6d6"/>
  <rect x="400.5" y="130" width="4.5" height="60" fill="#ff9ed0"/>
  <rect x="404.5" y="130" width="4.5" height="60" fill="#ff97c9"/>
  <rect x="408" y="130" width="4.5" height="60" fill="#fc93c1"/>
  <rect x="411.5" y="130" width="4.5" height="60" fill="#f691b8"/>
  <rect x="415.5" y="130" width="4.5" height="60" fill="#ed93b0"/>
  <rect x="419" y="130" width="4.5" height="60" fill="#e297a9"/>
  <rect x="422.5" y="130" width="4.5" height="60" fill="#d69da4"/>
  <rect x="426.5" y="130" width="4.5" height="60" fill="#c7a4a2"/>
  <rect x="430" y="130" width="4.5" height="60" fill="#b7aca2"/>
  <rect x="434" y="130" width="4.5" height="60" fill="#a6b4a6"/>
  <rect x="437.5" y="130" width="4.5" height="60" fill="#94bcab"/>
  <rect x="441" y="130" width="4.5" height="60" fill="#83c3b2"/>
  <rect x="445" y="130" width="4.5" height="60" fill="#74c9b9"/>
  <rect x="448.5" y="130" width="4.5" height="60" fill="#68cec0"/>
  <rect x="452" y="130" width="4.5" height="60" fill="#61d2c6"/>
  <rect x="456" y="130" width="4.5" height="60" fill="#62d5ca"/>
  <rect x="459.5" y="130" width="4.5" height="60" fill="#6ad7ce"/>
  <rect x="463" y="130" width="4.5" height="60" fill="#76d7cf"/>
  <rect x="467" y="130" width="4.5" height="60" fill="#84d6cf"/>
  <rect x="470.5" y="130" width="4.5" height="60" fill="#94d4ce"/>
  <rect x="474" y="130" width="4.5" height="60" fill="#a3d1ca"/>
  <rect x="478" y="130" width="4.5" height="60" fill="#b1cdc6"/>
  <rect x="481.5" y="130" width="4.5" height="60" fill="#bfc8c1"/>
  <rect x="485.5" y="130" width="4.5" height="60" fill="#cac2bc"/>
  <rect x="489" y="130" width="4.5" height="60" fill="#d4bdb7"/>
  <rect x="492.5" y="130" width="4.5" height="60" fill="#dcb7b2"/>
  <rect x="496.5" y="130" width="4.5" height="60" fill="#e2b2af"/>
  <rect x="40" y="130" width="460" height="60" fill="none" stroke="#1f2933" stroke-width="2"/>
  <line x1="40" y1="190" x2="40" y2="197" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="30" y="201.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="132" y1="190" x2="132" y2="197" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="109.5" y="201.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="224" y1="190" x2="224" y2="197" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="201.5" y="201.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$400$</div></foreignObject>
  <line x1="316" y1="190" x2="316" y2="197" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="293.5" y="201.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$600$</div></foreignObject>
  <line x1="408" y1="190" x2="408" y2="197" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="385.5" y="201.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$800$</div></foreignObject>
  <line x1="500" y1="190" x2="500" y2="197" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="471" y="201.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1000$</div></foreignObject>
  <line x1="86" y1="190" x2="86" y2="195" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="178" y1="190" x2="178" y2="195" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="270" y1="190" x2="270" y2="195" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="362" y1="190" x2="362" y2="195" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="454" y1="190" x2="454" y2="195" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="512" y="145.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$d\ (\text{nm})$</div></foreignObject>
  <foreignObject x="40" y="19.5" width="199" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{soap film},\ n = 1.33$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy7/soap-bubble-colours.webp" alt="A close-up of a soap film: orange, blue and violet swirls against a dark background."><figcaption>Interference colours in a soap film. The thickness of the film varies from place to place, and at each point the colour that is reinforced is the one for which the path difference of the two reflections is right.</figcaption></figure>

```pysahdy
Why are no interference colours seen in window glass, although it also reflects light from two surfaces?
---
The glass is so thick that there are very many strengthened and weakened wavelengths in the visible range. The colours mix into white.
```

## Formula: Thin-film interference
When light arrives at normal incidence on a film, the optical path difference between the waves reflected from the two surfaces of the film is
```latex
\Delta s = 2nd
```
where $n$ is the refractive index of the film, $d$ the thickness of the film and $\lambda$ the wavelength of the light in air (almost the same as in vacuum). The conditions depend on how many of the reflections invert the wave. When there is a material of lower refractive index on both sides of the film, as with a soap film in air, only the reflection from the upper surface inverts the wave. Then
```latex
\begin{aligned}
&\text{constructive:} \\
&2nd = (k + \tfrac{1}{2})\lambda \\[6pt]
&\text{destructive:} \\
&2nd = k\lambda
\end{aligned}
```
where $k = 0, 1, 2, \ldots$ When both reflections invert the wave, as in the coating of a lens whose refractive index lies between those of air and glass, the inversions cancel each other. The conditions then swap places: $2nd = k\lambda$ is constructive and $2nd = (k + \tfrac{1}{2})\lambda$ is destructive. The same holds when neither reflection inverts the wave.

```pysahdy
A soap film ($n = 1.33$) is $125\,\text{nm}$ thick, and light arrives at normal incidence from air. Which wavelength is strengthened when $k = 0$?
---
The path difference is $2nd = 2 \cdot 1.33 \cdot 125\,\text{nm} = 332.5\,\text{nm}$. From $2nd = (k + \tfrac{1}{2})\lambda$ and $k = 0$ we get $\lambda = 665\,\text{nm}$, so red light is strengthened.
```

### Anti-reflection coating
Ordinary glass ($n = 1.52$) reflects about $4\,\%$ of light arriving at normal incidence from each of its surfaces. A camera objective has many lenses, so the reflections weaken the image and cause ghost images in it. In spectacles the reflection is seen as glare. An **anti-reflection coating** is a thin film evaporated onto the surface of the glass, for example magnesium fluoride $\text{MgF}_2$, whose refractive index is $1.38$ at a wavelength of $550\,\text{nm}$ (Dodge, *Applied Optics*, 1984). Both reflections of the coating occur at a material of higher refractive index ($1.00 \to 1.38 \to 1.52$), so the destructive condition is $2nd = (k + \tfrac{1}{2})\lambda$. For the thinnest coating $k = 0$, and its thickness is a quarter of the wavelength in the coating:
```latex
d = \frac{\lambda}{4n}
```
The coating is usually designed for the middle of the visible range, to which the eye is most sensitive. When $\lambda = 550\,\text{nm}$, the thickness is $99.6\,\text{nm}$, and the reflection from a surface falls from about $4.3\,\%$ to about $1.3\,\%$.

Complete cancellation would require the two reflected waves to be equally strong. At normal incidence this happens when the refractive index of the coating is $\sqrt{n_\text{glass}}$, for glass $\sqrt{1.52} \approx 1.23$. Durable coating materials do not have such a small refractive index, and $\text{MgF}_2$ is one of the closest. Nor does the coating cancel all wavelengths equally well: more violet and red is reflected than green, so a coated lens shines purple. Light does not disappear: the less of it is reflected, the more of it passes through the glass. Modern objectives often have many layers on top of each other.

<svg data-fig="graph" viewBox="0 0 600 340" role="img" aria-label="Graph to scale: the percentage R of light reflected at normal incidence as a function of wavelength from 400 to 700 nm. Uncoated glass with a refractive index of 1.52 reflects about 4.3 per cent at all wavelengths, a horizontal black line. When the glass is coated with a magnesium fluoride layer with a refractive index of 1.38 and a thickness of 99.6 nanometres, that is, a quarter of the wavelength 550 nanometres in the film, the green curve falls to its minimum of about 1.3 per cent at 550 nanometres and rises towards the edges: to about 2.2 per cent at 400 nanometres and about 1.6 per cent at 700 nanometres. The dependence of the refractive indices on wavelength is not taken into account." style="max-width:100%;font-size:24px">
  <line x1="158.5" y1="286" x2="158.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="220.5" y1="286" x2="220.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="283" y1="286" x2="283" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="345.5" y1="286" x2="345.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="407.5" y1="286" x2="407.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="286" x2="470" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="241.5" x2="470" y2="241.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="197" x2="470" y2="197" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="153" x2="470" y2="153" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="108.5" x2="470" y2="108.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="64" x2="470" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="286" x2="484" y2="286" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,286 L483,292 L483,280 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="287" x2="96" y2="50" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,38 L102,51 L90,51 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="158.5" y1="286" x2="158.5" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="220.5" y1="286" x2="220.5" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="198" y="295.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$500$</div></foreignObject>
  <line x1="283" y1="286" x2="283" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="345.5" y1="286" x2="345.5" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="323" y="295.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$600$</div></foreignObject>
  <line x1="407.5" y1="286" x2="407.5" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="470" y1="286" x2="470" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="447.5" y="295.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$700$</div></foreignObject>
  <line x1="89" y1="241.5" x2="96" y2="241.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="227" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="89" y1="197" x2="96" y2="197" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="182.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="89" y1="153" x2="96" y2="153" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="138.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="89" y1="108.5" x2="96" y2="108.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="94" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="89" y1="64" x2="96" y2="64" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="49.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$5$</div></foreignObject>
  <foreignObject x="502" y="271.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\lambda\ (\text{nm})$</div></foreignObject>
  <foreignObject x="86" y="7.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$R\ (\%)$</div></foreignObject>
  <foreignObject x="73.5" y="295.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$400$</div></foreignObject>
  <foreignObject x="60" y="265.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <polyline points="96,97 470,97" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="96,188 99,189.5 102,191.5 105.5,193 108.5,194.5 111.5,196 114.5,197.5 118,199 121,200.5 124,201.5 127,203 130.5,204 133.5,205.5 136.5,206.5 139.5,208 143,209 146,210 149,211 152,212 155,213 158.5,214 161.5,215 164.5,216 167.5,216.5 171,217.5 174,218.5 177,219 180,220 183.5,220.5 186.5,221 189.5,222 192.5,222.5 195.5,223 199,223.5 202,224 205,224.5 208,225 211.5,225.5 214.5,226 217.5,226.5 220.5,226.5 224,227 227,227.5 230,227.5 233,228 236,228 239.5,228.5 242.5,228.5 245.5,229 248.5,229 252,229.5 255,229.5 258,229.5 261,229.5 264.5,230 267.5,230 270.5,230 273.5,230 277,230 280,230 283,230 286,230 289,230 292.5,230 295.5,230 298.5,230 301.5,230 305,229.5 308,229.5 311,229.5 314,229.5 317.5,229.5 320.5,229 323.5,229 326.5,229 330,228.5 333,228.5 336,228.5 339,228 342,228 345.5,227.5 348.5,227.5 351.5,227.5 354.5,227 358,227 361,226.5 364,226.5 367,226 370.5,226 373.5,225.5 376.5,225 379.5,225 382.5,224.5 386,224.5 389,224 392,224 395,223.5 398.5,223 401.5,223 404.5,222.5 407.5,222 411,222 414,221.5 417,221 420,221 423,220.5 426.5,220 429.5,220 432.5,219.5 435.5,219 439,219 442,218.5 445,218 448,217.5 451.5,217.5 454.5,217 457.5,216.5 460.5,216 464,216 467,215.5 470,215" fill="none" stroke="#2b8a3e" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="283" y1="230" x2="283" y2="286" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="230" x2="283" y2="230" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="283" cy="230" r="6.5" fill="#2b8a3e" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="362" y="60.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{uncoated}$</span></div></foreignObject>
  <foreignObject x="322.5" y="245" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{MgF}_2\text{-coating}$</span></div></foreignObject>
</svg>

## Worked example
The wall of a soap bubble is $380\,\text{nm}$ thick at one point, and the refractive index of soapy water is $1.33$. White light arrives at normal incidence on the film. Which wavelengths of visible light ($400$–$700\,\text{nm}$) are reflected most strongly?

<!-- vaihe -->

**Given and find.** The thickness of the film is $d = 380\,\text{nm}$ and the refractive index is $n = 1.33$, with air on both sides of the film. We are asked for the wavelengths $\lambda$ between $400$ and $700\,\text{nm}$ at which the interference is constructive.

<!-- vaihe -->

**Principle.** The reflection from the upper surface, from air into the film, inverts the wave; the reflection from the lower surface, from the film into air, does not. The reflections thus contain one half-wavelength shift, so the condition for constructive interference is $2nd = (k + \tfrac{1}{2})\lambda$. We calculate the wavelength for different values of $k$ and choose those in the visible range.

<!-- vaihe -->

**Formula solved.**
```latex
\begin{aligned}
&2nd = (k + \tfrac{1}{2})\lambda \\[6pt]
&\lambda = \frac{2nd}{k + \frac{1}{2}}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** Not needed: the thickness and the wavelength are both in nanometres, and the refractive index has no unit.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
&\lambda = \frac{2nd}{k + \frac{1}{2}} \\[6pt]
&k = 1:\ \lambda = \frac{2 \cdot 1.33 \cdot 380\,\text{nm}}{1.5} \\
&= 673.9\,\text{nm} \\[6pt]
&k = 2:\ \lambda = \frac{2 \cdot 1.33 \cdot 380\,\text{nm}}{2.5} \\
&= 404.3\,\text{nm}
\end{aligned}
```
The path difference is $2nd = 1010.8\,\text{nm}$. For $k = 0$ we get $2021.6\,\text{nm}$ (infrared) and for $k = 3$ we get $288.8\,\text{nm}$ (ultraviolet), so these are not visible light.

<!-- vaihe -->

**Result.** The most strongly reflected light is red light with a wavelength of $674\,\text{nm}$ and violet light with a wavelength of $404\,\text{nm}$. The answers are given to three significant figures like the refractive index and the thickness. Between them the destructive condition $2nd = 2\lambda$ cancels blue-green light, $1010.8\,\text{nm} : 2 = 505\,\text{nm}$, so the film looks reddish purple at this point.

<!-- vaihe -->

**Reasonableness.** Check: $(1 + \tfrac{1}{2}) \cdot 673.9\,\text{nm} = 1010.8\,\text{nm}$ and $(2 + \tfrac{1}{2}) \cdot 404.3\,\text{nm} = 1010.8\,\text{nm}$. The two strengthened wavelengths are of consecutive orders, so exactly one weakened wavelength lies between them, as it should. In a thinner film there would be fewer strengthened wavelengths in the visible range, and in a thicker film more.

## Common misconception
Many people think that the colours of a soap bubble arise in the same way as the colours of a prism or a rainbow, by refraction in different directions. The colours of a bubble, however, arise from interference: a film of a given thickness strengthens some wavelengths and weakens others, and the colour depends on the thickness of the film. Another mistake is to forget the half-wavelength shift on reflection and conclude that a very thin film reflects strongly because the path difference is zero. A third mistake is to believe that an anti-reflection coating absorbs the reflected light. The coating is transparent: in destructive interference less light is reflected and more of it passes through the glass.

## Summary
- The waves reflected from the two surfaces of a thin film interfere. When the light arrives at normal incidence, their optical path difference is $2nd$, because the wavelength in the film is $\lambda : n$.
- A reflected wave is inverted, that is, it gets a half-wavelength shift, when the light is reflected at a material of higher refractive index.
- A soap film in air has one shift: constructive $2nd = (k + \tfrac{1}{2})\lambda$, destructive $2nd = k\lambda$. In reflected light a very thin film therefore looks almost black.
- In white light a film looks colourful because some wavelengths cancel, and the colour changes with the thickness of the film.
- An anti-reflection coating has two shifts, and the thinnest destructive coating is $d = \lambda : (4n)$, for example $99.6\,\text{nm}$ for $\text{MgF}_2$ at a wavelength of $550\,\text{nm}$.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Illustration: after rain there is a puddle on the asphalt, with a thin film of oil on its surface. The film shows winding rings of blue, green, yellow and magenta, because the film is thicker in the middle than at the edges. The colours are calculated for an oil film on water." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-14-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
