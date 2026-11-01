# From Rutherford's nucleus to Bohr's atom

> **Why** does glowing hydrogen give off light of only a few colours, while a hot metal glows in all of them?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a darkened laboratory. On the left a thin glass tube on a stand glows with a soft pink-violet light. Its light passes through a narrow slit and a small glass grating on the bench. On a white screen on the right the light appears not as a rainbow but as four separate thin lines on each side of a dim central image: violet, blue, turquoise and red, with red bent farthest, and darkness between them." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="am-room" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#26313c"/><stop offset="1" stop-color="#1a222b"/></linearGradient><linearGradient id="am-bench" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7a5a32"/><stop offset="1" stop-color="#5a4024"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#am-room)"/>
  <rect x="0" y="470" width="1200" height="130" fill="url(#am-bench)"/>
  <line x1="0" y1="470" x2="1200" y2="470" stroke="#a07a46" stroke-width="4" stroke-linecap="butt"/>
  <defs><radialGradient id="am-glow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#f3d9fa" stop-opacity="0.9"/><stop offset="1" stop-color="#cc5de8" stop-opacity="0"/></radialGradient></defs>
  <ellipse cx="190" cy="270" rx="120" ry="210" fill="url(#am-glow)"/>
  <rect x="184" y="420" width="12" height="50" fill="#8a96a3"/>
  <rect x="140" y="460" width="100" height="12" rx="4" fill="#8a96a3"/>
  <rect x="170" y="70" width="40" height="34" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="170" y="404" width="40" height="34" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="176" y="104" width="28" height="300" rx="12" fill="#e599f7" stroke="#f8f0fc" stroke-width="3"/>
  <rect x="186" y="112" width="8" height="284" rx="4" fill="#fbe7ff"/>
  <line x1="190" y1="60" x2="190" y2="70" stroke="#8a96a3" stroke-width="4" stroke-linecap="butt"/>
  <path d="M210,250 L470,262 L470,278 L210,290 Z" fill="#e599f7" stroke-linejoin="round" fill-opacity="0.25"/>
  <rect x="462" y="214" width="16" height="110" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="466" y="262" width="8" height="16" fill="#e599f7"/>
  <rect x="466" y="324" width="8" height="146" fill="#8a96a3"/>
  <rect x="560" y="230" width="20" height="80" rx="3" fill="#eef5f9" stroke="#8a96a3" stroke-width="3"/>
  <rect x="566" y="310" width="8" height="160" fill="#8a96a3"/>
  <path d="M478,264 L560,262 L560,278 L478,276 Z" fill="#e599f7" stroke-linejoin="round" fill-opacity="0.3"/>
  <rect x="900" y="80" width="220" height="380" rx="4" fill="#f8f9fa" stroke="#1f2933" stroke-width="3"/>
  <rect x="1000" y="460" width="20" height="12" fill="#8a96a3"/>
  <path d="M580,268 L900,83 L900,89 L580,272 Z" fill="#e03131" stroke-linejoin="round" fill-opacity="0.2"/>
  <rect x="904" y="83.5" width="212" height="5" fill="#e03131"/>
  <path d="M580,268 L900,451 L900,457 L580,272 Z" fill="#e03131" stroke-linejoin="round" fill-opacity="0.2"/>
  <rect x="904" y="451.5" width="212" height="5" fill="#e03131"/>
  <path d="M580,268 L900,131 L900,137 L580,272 Z" fill="#15aabf" stroke-linejoin="round" fill-opacity="0.2"/>
  <rect x="904" y="131.5" width="212" height="5" fill="#15aabf"/>
  <path d="M580,268 L900,403 L900,409 L580,272 Z" fill="#15aabf" stroke-linejoin="round" fill-opacity="0.2"/>
  <rect x="904" y="403.5" width="212" height="5" fill="#15aabf"/>
  <path d="M580,268 L900,145.5 L900,151.5 L580,272 Z" fill="#3b5bdb" stroke-linejoin="round" fill-opacity="0.2"/>
  <rect x="904" y="146" width="212" height="5" fill="#3b5bdb"/>
  <path d="M580,268 L900,388.5 L900,394.5 L580,272 Z" fill="#3b5bdb" stroke-linejoin="round" fill-opacity="0.2"/>
  <rect x="904" y="389" width="212" height="5" fill="#3b5bdb"/>
  <path d="M580,268 L900,152 L900,158 L580,272 Z" fill="#7048e8" stroke-linejoin="round" fill-opacity="0.2"/>
  <rect x="904" y="152.5" width="212" height="5" fill="#7048e8"/>
  <path d="M580,268 L900,382 L900,388 L580,272 Z" fill="#7048e8" stroke-linejoin="round" fill-opacity="0.2"/>
  <rect x="904" y="382.5" width="212" height="5" fill="#7048e8"/>
  <path d="M580,268 L900,262 L900,274 L580,272 Z" fill="#e599f7" stroke-linejoin="round" fill-opacity="0.12"/>
</svg>

## The gold-foil evidence {Foil}

In 1909 Hans Geiger and the 20-year-old student Ernest Marsden worked in Ernest Rutherford's laboratory in Manchester. They shot **alpha particles**, fast and heavy positive particles from a radioactive source, at very thin metal foils. Each alpha particle that hit a zinc sulfide screen made a tiny flash of light. In a darkened room they counted the flashes through a microscope, for hours at a time.

Most alpha particles went through the foil and were turned aside by only a small angle. But a few bounced back: from a thin platinum foil, about one alpha particle in 8000 was turned through more than $90^\circ$. Nobody had expected this. Rutherford later said that it was "almost as incredible as if you fired a 15-inch shell at a piece of tissue paper and it came back and hit you".

In 1911 Rutherford explained the result. Almost all the mass and all the positive charge of an atom sit in a tiny **nucleus** at its centre. An alpha particle that passes far from a nucleus hardly feels it. Only the rare one that comes very close is pushed back by the strong electric repulsion. The figure shows such paths near one gold nucleus, to scale.

<figure class="unit-photo"><img src="units/fy14/pics/rutherford.jpg" alt="Black-and-white portrait photograph of Ernest Rutherford, a man with a moustache wearing a suit." width="1185" height="1600" loading="lazy"><figcaption>Ernest Rutherford (1871–1937) discovered the atomic nucleus in 1911 from the scattering of alpha particles by gold foil. <span class="photo-credit">Photo: Bain News Service, publisher, public domain, via Wikimedia Commons</span></figcaption></figure>

<svg data-fig="scatter" viewBox="0 0 600 420" role="img" aria-label="Drawing to scale of alpha particles that move from left to right past one gold nucleus, a small red dot in the middle. Each path starts at a different distance b from the line through the centre of the nucleus. Paths that start far from the line bend only a little. Paths closer to the line bend more, and the closest ones turn back towards the left. A scale bar shows 50 femtometres. The whole atom would be about 600 times wider than this drawing." style="max-width:100%;font-size:24px">
  <polyline points="62,236 63.5,236 64.5,236 66,236 67.5,236 69,236 70,236 71.5,236 73,236 74,236 75.5,236 77,236 78.5,236 79.5,236 81,236 82.5,236 83.5,236 85,236 86.5,236 87.5,236 89,236 90.5,236 92,236 93,236 94.5,236 96,236 97,236 98.5,236 100,236 101,236 102.5,236 104,236 105,236 106.5,236 108,236 109,236 110.5,236 112,236 113,236 114.5,236 116,236 117,236 118.5,236 120,236 121,236 122.5,236 124,236 125,236 126.5,236 128,236 129,236 130.5,236 132,236 133,236 134.5,236 135.5,236 137,236 138.5,236 139.5,236 141,236 142.5,236 143.5,236 145,236 146,236 147.5,236 149,236 150,236 151.5,236 152.5,236 154,236 155.5,236 156.5,236 158,236 159,236 160.5,236 162,236 163,236 164.5,236 165.5,236 167,236 168,236 169.5,236 171,236 172,236 173.5,236 174.5,236 176,236 177,236 178.5,236 179.5,236 181,236 182,236 183.5,236 184.5,236 186,236 187,236 188.5,236 189.5,236 191,236 192,236 193.5,236 194.5,236 196,236 197,236 198.5,236 199.5,236 200.5,236 202,236 203,236 204.5,236 205.5,236 207,236 208,236 209,236 210.5,235.5 211.5,235.5 212.5,235.5 214,235.5 215,235.5 216.5,235.5 217.5,235.5 218.5,235.5 219.5,235.5 221,235.5 222,235.5 223,235.5 224.5,235.5 225.5,235.5 226.5,235.5 227.5,235.5 229,235.5 230,235.5 231,235.5 232,235.5 233,235.5 234.5,235.5 235.5,235.5 236.5,235.5 237.5,235.5 238.5,235.5 239.5,235.5 240.5,235.5 241.5,235.5 242.5,235.5 243.5,235.5 244.5,235.5 245.5,235.5 246.5,235.5 247.5,235.5 248.5,235.5 249.5,235.5 250.5,235.5 251.5,235.5 252,235 253,235 254,235 255,235 255.5,235 256.5,235 257.5,235 258,235 259,235 259.5,235 260.5,235 261,235 262,235 262.5,234.5 263,234.5 264,234.5 264.5,234.5 265,234.5 265.5,234.5 266,234.5 266.5,234.5 267,234 267.5,234 268,234 268.5,234 269,234 269,233.5 269.5,233.5 269.5,233.5 270,233.5 270,233 270.5,233 270.5,233 270.5,232.5 270.5,232.5 270.5,232.5 271,232 270.5,232 270.5,232 270.5,231.5 270.5,231.5 270.5,231 270,231 270,230.5 269.5,230.5 269.5,230 269,230 269,229.5 268.5,229.5 268,229 267.5,228.5 267,228.5 267,228 266.5,227.5 266,227.5 265.5,227 264.5,226.5 264,226 263.5,226 263,225.5 262.5,225 261.5,224.5 261,224 260.5,224 259.5,223.5 259,223 258,222.5 257.5,222 256.5,221.5 256,221 255,220.5 254.5,220.5 253.5,220 253,219.5 252,219 251,218.5 250.5,218 249.5,217.5 248.5,217 247.5,216.5 247,216 246,215.5 245,215 244,214.5 243,214 242.5,213.5 241.5,213 240.5,212.5 239.5,211.5 238.5,211 237.5,210.5 236.5,210 235.5,209.5 234.5,209 234,208.5 233,208 232,207.5 231,207 230,206.5 229,205.5 228,205 227,204.5 226,204 225,203.5 223.5,203 222.5,202.5 221.5,201.5 220.5,201 219.5,200.5 218.5,200 217.5,199.5 216.5,199 215.5,198.5 214.5,197.5 213.5,197 212.5,196.5 211,196 210,195.5 209,194.5 208,194 207,193.5 206,193 205,192.5 203.5,191.5 202.5,191 201.5,190.5 200.5,190 199.5,189.5 198.5,188.5 197,188 196,187.5 195,187 194,186.5 193,185.5 191.5,185 190.5,184.5 189.5,184 188.5,183 187,182.5 186,182 185,181.5 184,181 183,180 181.5,179.5 180.5,179 179.5,178.5 178.5,177.5 177,177 176,176.5 175,176 174,175 172.5,174.5 171.5,174 170.5,173.5 169,172.5 168,172 167,171.5 166,171 164.5,170 163.5,169.5 162.5,169 161,168.5 160,167.5 159,167 158,166.5 156.5,165.5 155.5,165 154.5,164.5 153,164 152,163 151,162.5 149.5,162 148.5,161.5 147.5,160.5 146.5,160 145,159.5 144,158.5 143,158 141.5,157.5 140.5,157 139.5,156 138,155.5 137,155 136,154 134.5,153.5 133.5,153 132.5,152.5 131,151.5 130,151 129,150.5 127.5,149.5 126.5,149 125.5,148.5 124,148 123,147 121.5,146.5 120.5,146 119.5,145 118,144.5 117,144 116,143 114.5,142.5 113.5,142 112.5,141.5 111,140.5 110,140 109,139.5 107.5,138.5 106.5,138 105,137.5 104,136.5 103,136 101.5,135.5 100.5,135 99.5,134 98,133.5 97,133 95.5,132 94.5,131.5 93.5,131 92,130 91,129.5 90,129 88.5,128 87.5,127.5 86,127 85,126 84,125.5 82.5,125 81.5,124.5 80,123.5 79,123 78,122.5 76.5,121.5 75.5,121 74.5,120.5 73,119.5 72,119 70.5,118.5 69.5,117.5 68.5,117 67,116.5 66,115.5 64.5,115 63.5,114.5 62.5,113.5 61,113 60,112.5 58.5,111.5 57.5,111 56,110.5 55,109.5 54,109 52.5,108.5 51.5,108 50,107 49,106.5 48,106 46.5,105 45.5,104.5" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linecap="round"/>
  <line x1="51.5" y1="108" x2="57" y2="110.5" stroke="#c92a2a" stroke-width="3" stroke-linecap="butt"/>
  <path d="M45.5,104.5 L60.5,105.5 L54.5,116.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <polyline points="62,250 63.5,250 64.5,250 66,250 67.5,250 69,250 70,250 71.5,250 73,250 74,250 75.5,250 77,250 78.5,250 79.5,250 81,250 82.5,250 83.5,250 85,250 86.5,250 87.5,250 89,250 90.5,250 92,250 93,250 94.5,250 96,250 97,250 98.5,250 100,250 101,250 102.5,250 104,250 105,250 106.5,250 108,250 109,250 110.5,250 112,250 113,250 114.5,250 116,250 117,250 118.5,250 120,250 121,250 122.5,250 124,250 125,250 126.5,250 128,250 129,250 130.5,250 132,250 133,250 134.5,250 135.5,250.5 137,250.5 138.5,250.5 139.5,250.5 141,250.5 142.5,250.5 143.5,250.5 145,250.5 146,250.5 147.5,250.5 149,250.5 150,250.5 151.5,250.5 152.5,250.5 154,250.5 155.5,250.5 156.5,250.5 158,250.5 159,250.5 160.5,250.5 162,250.5 163,250.5 164.5,250.5 165.5,250.5 167,250.5 168,250.5 169.5,250.5 171,250.5 172,250.5 173.5,250.5 174.5,250.5 176,250.5 177,250.5 178.5,250.5 179.5,250.5 181,250.5 182,250.5 183.5,250.5 184.5,250.5 186,250.5 187,250.5 188.5,250.5 189.5,250.5 191,250.5 192,250.5 193.5,250.5 194.5,250.5 196,250.5 197,250.5 198.5,250.5 199.5,250.5 201,250.5 202,250.5 203,250.5 204.5,250.5 205.5,250.5 207,250.5 208,250.5 209,250.5 210.5,250.5 211.5,250.5 213,250.5 214,250.5 215,250.5 216.5,250.5 217.5,250.5 218.5,250.5 220,251 221,251 222,251 223,251 224.5,251 225.5,251 226.5,251 228,251 229,251 230,251 231,251 232,251 233.5,251 234.5,251 235.5,251 236.5,251 237.5,251 238.5,251 239.5,251 240.5,251.5 241.5,251.5 243,251.5 244,251.5 245,251.5 246,251.5 246.5,251.5 247.5,251.5 248.5,251.5 249.5,251.5 250.5,251.5 251.5,252 252.5,252 253.5,252 254,252 255,252 256,252 257,252 257.5,252.5 258.5,252.5 259,252.5 260,252.5 261,252.5 261.5,253 262.5,253 263,253 263.5,253 264.5,253.5 265,253.5 265.5,253.5 266.5,254 267,254 267.5,254 268,254.5 268.5,254.5 269,254.5 269.5,255 270,255 270.5,255.5 270.5,255.5 271,256 271.5,256.5 272,256.5 272,257 272.5,257 272.5,257.5 273,258 273,258.5 273,258.5 273.5,259 273.5,259.5 273.5,260 273.5,260.5 273.5,261 273.5,261.5 273.5,262 273.5,262.5 273.5,263 273.5,263.5 273.5,264 273.5,265 273.5,265.5 273.5,266 273,266.5 273,267.5 273,268 272.5,268.5 272.5,269.5 272.5,270 272,271 272,271.5 271.5,272.5 271.5,273 271,274 271,275 270.5,275.5 270,276.5 270,277 269.5,278 269.5,279 269,280 268.5,280.5 268.5,281.5 268,282.5 267.5,283.5 267,284.5 267,285 266.5,286 266,287 265.5,288 265.5,289 265,290 264.5,291 264,292 263.5,293 263.5,294 263,295 262.5,296 262,297 261.5,298 261,299 260.5,300 260.5,301 260,302 259.5,303 259,304 258.5,305 258,306 257.5,307 257,308 256.5,309 256,310.5 255.5,311.5 255.5,312.5 255,313.5 254.5,314.5 254,315.5 253.5,317 253,318 252.5,319 252,320 251.5,321 251,322 250.5,323.5 250,324.5 249.5,325.5 249,326.5 248.5,328 248,329 247.5,330 247,331 246.5,332.5 246,333.5 245.5,334.5 245,335.5 244.5,337 244,338 243.5,339 243,340 242.5,341.5 242,342.5 241.5,343.5 241,345 240.5,346 240,347 239.5,348.5 239,349.5 238.5,350.5 237.5,351.5 237,353 236.5,354 236,355 235.5,356.5 235,357.5 234.5,358.5 234,360 233.5,361 233,362.5 232.5,363.5 232,364.5 231.5,366 231,367 230.5,368 230,369.5 229.5,370.5 228.5,371.5 228,373 227.5,374 227,375.5 226.5,376.5 226,377.5 225.5,379 225,380 224.5,381 224,382.5" fill="none" stroke="#e8590c" stroke-width="3" stroke-linecap="round"/>
  <line x1="226.5" y1="376.5" x2="229" y2="370.5" stroke="#e8590c" stroke-width="3" stroke-linecap="butt"/>
  <path d="M224,382.5 L224,367 L235.5,372.5 Z" fill="#e8590c" stroke-linejoin="round"/>
  <polyline points="62,219.5 63.5,219.5 64.5,219.5 66,219.5 67.5,219.5 69,219.5 70,219.5 71.5,219.5 73,219.5 74,219.5 75.5,219.5 77,219.5 78.5,219.5 79.5,219.5 81,219.5 82.5,219.5 83.5,219.5 85,219.5 86.5,219.5 87.5,219.5 89,219.5 90.5,219.5 92,219.5 93,219.5 94.5,219.5 96,219.5 97,219.5 98.5,219.5 100,219.5 101,219.5 102.5,219.5 104,219.5 105,219.5 106.5,219.5 108,219.5 109,219.5 110.5,219.5 112,219.5 113,219.5 114.5,219.5 116,219.5 117,219.5 118.5,219.5 120,219.5 121,219.5 122.5,219.5 124,219.5 125,219.5 126.5,219.5 128,219.5 129,219.5 130.5,219.5 132,219.5 133,219.5 134.5,219.5 135.5,219.5 137,219.5 138.5,219.5 139.5,219.5 141,219.5 142.5,219.5 143.5,219.5 145,219.5 146,219.5 147.5,219.5 149,219.5 150,219.5 151.5,219.5 153,219.5 154,219.5 155.5,219.5 156.5,219.5 158,219.5 159,219.5 160.5,219.5 162,219.5 163,219.5 164.5,219.5 165.5,219.5 167,219.5 168,219.5 169.5,219.5 171,219.5 172,219.5 173.5,219.5 174.5,219.5 176,219.5 177,219.5 178.5,219 179.5,219 181,219 182,219 183.5,219 184.5,219 186,219 187,219 188.5,219 189.5,219 191,219 192,219 193.5,219 194.5,219 196,219 197,219 198.5,219 199.5,219 201,219 202,219 203.5,219 204.5,219 205.5,219 207,219 208,219 209.5,219 210.5,219 211.5,218.5 213,218.5 214,218.5 215.5,218.5 216.5,218.5 217.5,218.5 219,218.5 220,218.5 221,218.5 222.5,218.5 223.5,218.5 224.5,218.5 225.5,218.5 227,218.5 228,218.5 229,218 230,218 231.5,218 232.5,218 233.5,218 234.5,218 235.5,218 237,218 238,218 239,217.5 240,217.5 241,217.5 242,217.5 243,217.5 244,217.5 245.5,217.5 246.5,217 247.5,217 248.5,217 249.5,217 250.5,217 251,216.5 252,216.5 253,216.5 254,216.5 255,216 256,216 257,216 258,216 258.5,215.5 259.5,215.5 260.5,215.5 261,215 262,215 263,215 263.5,214.5 264.5,214.5 265.5,214 266,214 267,214 267.5,213.5 268.5,213.5 269,213 269.5,212.5 270.5,212.5 271,212 272,212 272.5,211.5 273,211 273.5,210.5 274.5,210.5 275,210 275.5,209.5 276,209 276.5,208.5 277,208 277.5,208 278,207.5 278.5,206.5 279,206 279.5,205.5 280,205 280.5,204.5 281,204 281.5,203.5 282,202.5 282.5,202 283,201.5 283,200.5 283.5,200 284,199.5 284.5,198.5 285,198 285,197 285.5,196.5 286,195.5 286.5,195 286.5,194 287,193 287.5,192.5 288,191.5 288,190.5 288.5,189.5 289,189 289,188 289.5,187 290,186 290.5,185 290.5,184.5 291,183.5 291.5,182.5 291.5,181.5 292,180.5 292.5,179.5 292.5,178.5 293,177.5 293.5,176.5 293.5,175.5 294,174.5 294.5,173.5 294.5,172.5 295,171.5 295,170.5 295.5,169 296,168 296,167 296.5,166 297,165 297,164 297.5,163 298,161.5 298,160.5 298.5,159.5 299,158.5 299,157 299.5,156 300,155 300,154 300.5,152.5 301,151.5 301,150.5 301.5,149.5 301.5,148 302,147 302.5,146 302.5,144.5 303,143.5 303.5,142.5 303.5,141 304,140 304.5,139 304.5,137.5 305,136.5 305.5,135.5 305.5,134 306,133 306.5,131.5 306.5,130.5 307,129.5 307,128 307.5,127 308,125.5 308,124.5 308.5,123.5 309,122 309,121 309.5,119.5 310,118.5 310,117 310.5,116 311,115 311,113.5 311.5,112.5 312,111 312,110 312.5,108.5 313,107.5 313,106 313.5,105 314,103.5 314,102.5 314.5,101 315,100 315,98.5 315.5,97.5" fill="none" stroke="#7048e8" stroke-width="3" stroke-linecap="round"/>
  <line x1="314" y1="103.5" x2="312" y2="110" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M315.5,97.5 L318,112.5 L306,109.5 Z" fill="#7048e8" stroke-linejoin="round"/>
  <polyline points="62,281 63.5,281 64.5,281 66,281 67.5,281 69,281 70,281 71.5,281 73,281 74,281 75.5,281 77,281 78.5,281 79.5,281 81,281 82.5,281 83.5,281 85,281 86.5,281 87.5,281 89,281 90.5,281 92,281 93,281 94.5,281 96,281 97,281 98.5,281 100,281 101,281 102.5,281 104,281 105,281 106.5,281 108,281 109,281 110.5,281 112,281 113,281 114.5,281 116,281 117,281 118.5,281 120,281 121,281 122.5,281 124,281 125,281 126.5,281 128,281 129,281 130.5,281 132,281 133,281 134.5,281 136,281 137,281 138.5,281 139.5,281 141,281 142.5,281 143.5,281 145,281 146.5,281 147.5,281 149,281 150,281 151.5,281 153,281 154,281 155.5,281 156.5,281 158,281 159.5,281 160.5,281 162,281 163,281.5 164.5,281.5 166,281.5 167,281.5 168.5,281.5 169.5,281.5 171,281.5 172,281.5 173.5,281.5 175,281.5 176,281.5 177.5,281.5 178.5,281.5 180,281.5 181,281.5 182.5,281.5 183.5,281.5 185,281.5 186,281.5 187.5,281.5 188.5,281.5 190,281.5 191,281.5 192.5,282 193.5,282 195,282 196,282 197.5,282 198.5,282 200,282 201,282 202.5,282 203.5,282 205,282 206,282 207.5,282 208.5,282 210,282.5 211,282.5 212,282.5 213.5,282.5 214.5,282.5 216,282.5 217,282.5 218,282.5 219.5,282.5 220.5,283 222,283 223,283 224,283 225.5,283 226.5,283 227.5,283 229,283 230,283.5 231,283.5 232.5,283.5 233.5,283.5 234.5,283.5 235.5,283.5 237,284 238,284 239,284 240,284 241.5,284 242.5,284.5 243.5,284.5 244.5,284.5 245.5,284.5 247,285 248,285 249,285 250,285 251,285.5 252,285.5 253.5,285.5 254.5,286 255.5,286 256.5,286 257.5,286.5 258.5,286.5 259.5,286.5 260.5,287 261.5,287 262.5,287 263.5,287.5 264.5,287.5 265.5,288 266.5,288 267.5,288.5 268.5,288.5 269.5,289 270.5,289 271.5,289.5 272.5,289.5 273.5,290 274.5,290 275.5,290.5 276.5,291 277,291 278,291.5 279,292 280,292 281,292.5 282,293 283,293.5 283.5,293.5 284.5,294 285.5,294.5 286.5,295 287.5,295.5 288,296 289,296 290,296.5 291,297 292,297.5 292.5,298 293.5,298.5 294.5,299 295.5,299.5 296.5,300 297,300.5 298,301 299,302 300,302.5 300.5,303 301.5,303.5 302.5,304 303.5,304.5 304.5,305 305,306 306,306.5 307,307 308,307.5 308.5,308.5 309.5,309 310.5,309.5 311.5,310 312.5,311 313,311.5 314,312 315,313 316,313.5 317,314 317.5,315 318.5,315.5 319.5,316.5 320.5,317 321.5,317.5 322.5,318.5 323,319 324,320 325,320.5 326,321.5 327,322 328,322.5 328.5,323.5 329.5,324 330.5,325 331.5,325.5 332.5,326.5 333.5,327 334,328 335,329 336,329.5 337,330.5 338,331 339,332 340,332.5 340.5,333.5 341.5,334 342.5,335 343.5,336 344.5,336.5 345.5,337.5 346.5,338 347.5,339 348.5,340 349,340.5 350,341.5 351,342 352,343 353,344 354,344.5 355,345.5 356,346.5 357,347 358,348 358.5,349 359.5,349.5 360.5,350.5 361.5,351.5 362.5,352 363.5,353 364.5,354 365.5,354.5 366.5,355.5 367.5,356.5 368.5,357 369.5,358 370.5,359 371.5,359.5 372,360.5 373,361.5 374,362 375,363 376,364 377,365 378,365.5 379,366.5 380,367.5 381,368 382,369 383,370 384,371 385,371.5 386,372.5 387,373.5 388,374.5 389,375 390,376 391,377 392,378 393,378.5 393.5,379.5 394.5,380.5 395.5,381.5 396.5,382" fill="none" stroke="#1971c2" stroke-width="3" stroke-linecap="round"/>
  <line x1="392" y1="378" x2="387" y2="373.5" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <path d="M396.5,382 L382,377.5 L390.5,368 Z" fill="#1971c2" stroke-linejoin="round"/>
  <polyline points="62,158.5 63.5,158.5 64.5,158.5 66,158.5 67.5,158.5 69,158.5 70,158.5 71.5,158.5 73,158.5 74,158.5 75.5,158.5 77,158.5 78.5,158.5 79.5,158.5 81,158.5 82.5,158.5 83.5,158.5 85,158.5 86.5,158.5 87.5,158.5 89,158.5 90.5,158.5 92,158.5 93,158.5 94.5,158.5 96,158.5 97,158.5 98.5,158.5 100,158.5 101,158.5 102.5,158.5 104,158.5 105.5,158.5 106.5,158.5 108,158.5 109.5,158.5 110.5,158.5 112,158.5 113.5,158.5 114.5,158 116,158 117.5,158 118.5,158 120,158 121.5,158 122.5,158 124,158 125.5,158 126.5,158 128,158 129.5,158 130.5,158 132,158 133.5,158 134.5,158 136,158 137.5,158 138.5,158 140,158 141,158 142.5,158 144,158 145,158 146.5,158 148,158 149,158 150.5,158 152,158 153,158 154.5,158 155.5,158 157,158 158.5,157.5 159.5,157.5 161,157.5 162.5,157.5 163.5,157.5 165,157.5 166,157.5 167.5,157.5 169,157.5 170,157.5 171.5,157.5 172.5,157.5 174,157.5 175.5,157.5 176.5,157.5 178,157.5 179,157.5 180.5,157.5 181.5,157 183,157 184.5,157 185.5,157 187,157 188,157 189.5,157 190.5,157 192,157 193.5,157 194.5,157 196,157 197,156.5 198.5,156.5 199.5,156.5 201,156.5 202,156.5 203.5,156.5 204.5,156.5 206,156.5 207.5,156.5 208.5,156 210,156 211,156 212.5,156 213.5,156 215,156 216,156 217.5,156 218.5,155.5 220,155.5 221,155.5 222.5,155.5 223.5,155.5 225,155.5 226,155.5 227.5,155 228.5,155 229.5,155 231,155 232,155 233.5,154.5 234.5,154.5 236,154.5 237,154.5 238.5,154.5 239.5,154.5 241,154 242,154 243,154 244.5,154 245.5,153.5 247,153.5 248,153.5 249.5,153.5 250.5,153 251.5,153 253,153 254,153 255.5,152.5 256.5,152.5 257.5,152.5 259,152 260,152 261,152 262.5,152 263.5,151.5 265,151.5 266,151.5 267,151 268.5,151 269.5,151 270.5,150.5 272,150.5 273,150 274.5,150 275.5,150 276.5,149.5 278,149.5 279,149.5 280,149 281.5,149 282.5,148.5 283.5,148.5 285,148 286,148 287,148 288.5,147.5 289.5,147.5 290.5,147 292,147 293,146.5 294,146.5 295.5,146 296.5,146 297.5,145.5 299,145.5 300,145 301,144.5 302.5,144.5 303.5,144 305,144 306,143.5 307,143.5 308.5,143 309.5,143 310.5,142.5 312,142 313,142 314,141.5 315.5,141 316.5,141 317.5,140.5 319,140.5 320,140 321,139.5 322.5,139.5 323.5,139 324.5,138.5 326,138.5 327,138 328,137.5 329.5,137.5 330.5,137 332,136.5 333,136 334,136 335.5,135.5 336.5,135 337.5,135 339,134.5 340,134 341,133.5 342.5,133.5 343.5,133 345,132.5 346,132 347,132 348.5,131.5 349.5,131 351,130.5 352,130.5 353,130 354.5,129.5 355.5,129 356.5,128.5 358,128.5 359,128 360.5,127.5 361.5,127 362.5,126.5 364,126.5 365,126 366.5,125.5 367.5,125 369,124.5 370,124 371,124 372.5,123.5 373.5,123 375,122.5 376,122 377.5,121.5 378.5,121.5 379.5,121 381,120.5 382,120 383.5,119.5 384.5,119 386,118.5 387,118.5 388,118 389.5,117.5 390.5,117 392,116.5 393,116 394.5,115.5 395.5,115.5 397,115 398,114.5 399.5,114 400.5,113.5 401.5,113 403,112.5 404,112 405.5,111.5 406.5,111.5 408,111 409,110.5 410.5,110 411.5,109.5 413,109 414,108.5 415.5,108 416.5,107.5 418,107 419,106.5 420.5,106.5 421.5,106 422.5,105.5 424,105 425,104.5 426.5,104 427.5,103.5 429,103 430,102.5 431.5,102 432.5,101.5 434,101 435,100.5 436.5,100.5 437.5,100 439,99.5 440,99 441.5,98.5 442.5,98 444,97.5" fill="none" stroke="#2b8a3e" stroke-width="3" stroke-linecap="round"/>
  <line x1="437.5" y1="100" x2="432" y2="102" stroke="#2b8a3e" stroke-width="3" stroke-linecap="butt"/>
  <path d="M444,97.5 L433,108.5 L428.5,96.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <polyline points="62,362.5 63.5,362.5 64.5,362.5 66,362.5 67.5,362.5 69,362.5 70,362.5 71.5,362.5 73,362.5 74,362.5 75.5,362.5 77,362.5 78.5,362.5 79.5,362.5 81,362.5 82.5,362.5 83.5,362.5 85,362.5 86.5,362.5 88,362.5 89,362.5 90.5,362.5 92,362.5 93,362.5 94.5,362.5 96,362.5 97,362.5 98.5,362.5 100,362.5 101.5,362.5 102.5,362.5 104,362.5 105.5,362.5 106.5,362.5 108,362.5 109.5,362.5 110.5,362.5 112,362.5 113.5,362.5 114.5,362.5 116,362.5 117.5,362.5 118.5,362.5 120,362.5 121.5,362.5 123,362.5 124,362.5 125.5,362.5 127,362.5 128,362.5 129.5,362.5 131,362.5 132,363 133.5,363 135,363 136,363 137.5,363 139,363 140,363 141.5,363 143,363 144,363 145.5,363 147,363 148,363 149.5,363 150.5,363 152,363 153.5,363 154.5,363 156,363 157.5,363 158.5,363 160,363 161.5,363 162.5,363 164,363.5 165.5,363.5 166.5,363.5 168,363.5 169,363.5 170.5,363.5 172,363.5 173,363.5 174.5,363.5 176,363.5 177,363.5 178.5,363.5 180,363.5 181,363.5 182.5,363.5 183.5,364 185,364 186.5,364 187.5,364 189,364 190,364 191.5,364 193,364 194,364 195.5,364 196.5,364 198,364 199.5,364.5 200.5,364.5 202,364.5 203,364.5 204.5,364.5 206,364.5 207,364.5 208.5,364.5 209.5,364.5 211,365 212.5,365 213.5,365 215,365 216,365 217.5,365 218.5,365 220,365 221.5,365.5 222.5,365.5 224,365.5 225,365.5 226.5,365.5 227.5,365.5 229,365.5 230.5,366 231.5,366 233,366 234,366 235.5,366 236.5,366 238,366.5 239.5,366.5 240.5,366.5 242,366.5 243,366.5 244.5,366.5 245.5,367 247,367 248,367 249.5,367 250.5,367 252,367.5 253,367.5 254.5,367.5 256,367.5 257,367.5 258.5,368 259.5,368 261,368 262,368 263.5,368.5 264.5,368.5 266,368.5 267,368.5 268.5,368.5 269.5,369 271,369 272,369 273.5,369 274.5,369.5 276,369.5 277.5,369.5 278.5,370 280,370 281,370 282.5,370 283.5,370.5 285,370.5 286,370.5 287.5,371 288.5,371 290,371 291,371 292.5,371.5 293.5,371.5 295,371.5 296,372 297.5,372 298.5,372 300,372.5 301,372.5 302.5,372.5 303.5,373 305,373 306,373 307.5,373.5 308.5,373.5 310,374 311,374 312.5,374 314,374.5 315,374.5 316.5,374.5 317.5,375 319,375 320,375.5 321.5,375.5 322.5,375.5 324,376 325,376 326.5,376.5 327.5,376.5 329,376.5 330,377 331.5,377 332.5,377.5 334,377.5 335,377.5 336.5,378 337.5,378 339,378.5 340,378.5 341.5,379 343,379 344,379.5 345.5,379.5 346.5,379.5 348,380 349,380 350.5,380.5 351.5,380.5 353,381 354,381 355.5,381.5 356.5,381.5 358,382 359.5,382 360.5,382.5 362,382.5 363,383" fill="none" stroke="#6b7480" stroke-width="3" stroke-linecap="round"/>
  <line x1="356.5" y1="381.5" x2="350.5" y2="380.5" stroke="#6b7480" stroke-width="3" stroke-linecap="butt"/>
  <path d="M363,383 L348,386.5 L350.5,374 Z" fill="#6b7480" stroke-linejoin="round"/>
  <line x1="40" y1="240" x2="560" y2="240" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="300" cy="240" r="9.05839" fill="#c92a2a" stroke="#1f2933" stroke-width="1.5"/>
  <foreignObject x="314" y="247.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{nucleus}$</span></div></foreignObject>
  <line x1="48" y1="240" x2="48" y2="281" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="42" y1="240" x2="54" y2="240" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="42" y1="281" x2="54" y2="281" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="18" y="246" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$b$</div></foreignObject>
  <line x1="470" y1="40" x2="532" y2="40" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="470" y1="32" x2="470" y2="48" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="532" y1="32" x2="532" y2="48" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="470" y="3.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$50\ \text{fm}$</div></foreignObject>
</svg>

## The spectrum of hydrogen {Lines}

A **gas discharge tube** contains a thin gas, and a high voltage between its ends makes the gas glow. When you look at the glow of hydrogen through a **diffraction grating** or a spectroscope, you do not see a rainbow. You see a **line spectrum**: four bright, thin lines of visible light, always at the same wavelengths.

<svg data-fig="lines" viewBox="0 0 600 250" role="img" aria-label="The visible spectrum of hydrogen gas as seen through a grating, on a wavelength scale from 380 to 720 nanometres. On a dark background there are only four thin bright lines: violet at 410 nanometres, blue at 434, turquoise at 486 and red at 656 nanometres. Between them there is no light." style="max-width:100%;font-size:24px">
  <rect x="40" y="60" width="520" height="90" fill="#15191e" stroke="#1f2933" stroke-width="2"/>
  <rect x="459.5" y="60" width="6" height="90" fill="#e03131"/>
  <rect x="199.5" y="60" width="6" height="90" fill="#15aabf"/>
  <rect x="119.5" y="60" width="6" height="90" fill="#3b5bdb"/>
  <rect x="83" y="60" width="6" height="90" fill="#7048e8"/>
  <foreignObject x="440" y="21.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$656$</div></foreignObject>
  <foreignObject x="180" y="21.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$486$</div></foreignObject>
  <foreignObject x="116.5" y="21.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$434$</div></foreignObject>
  <foreignObject x="47" y="21.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$410$</div></foreignObject>
  <line x1="70.5" y1="150" x2="70.5" y2="166" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="48" y="171.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$400$</div></foreignObject>
  <line x1="147" y1="150" x2="147" y2="160" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="223.5" y1="150" x2="223.5" y2="166" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="201" y="171.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$500$</div></foreignObject>
  <line x1="300" y1="150" x2="300" y2="160" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="376.5" y1="150" x2="376.5" y2="166" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="354" y="171.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$600$</div></foreignObject>
  <line x1="453" y1="150" x2="453" y2="160" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="529.5" y1="150" x2="529.5" y2="166" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="507" y="171.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$700$</div></foreignObject>
  <foreignObject x="486" y="209.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\lambda\ (\text{nm})$</div></foreignObject>
</svg>

In 1885 the Swiss teacher Johann Balmer found a simple formula that gives these four wavelengths, but nobody could say *why* it worked. Every element has its own pattern of lines, like a fingerprint. At the Fotoni lab visit you will look at the spectra of lamps and gas tubes yourself, at the station on spectra (unit *Fotoni lab visit: modern physics experiments*).

## Key idea

Rutherford's atom has a tiny, heavy, positive nucleus. The nucleus of gold has a radius of about $7\ \text{fm}$ ($1\ \text{fm} = 10^{-15}\ \text{m}$), while the gold atom has a radius of about $144\ \text{pm} = 1.44 \cdot 10^{-10}\ \text{m}$, about $20\,000$ times more. The atom is almost empty space, and the light **electrons** move around the nucleus.

But this atom raised a new problem. An electron moving round the nucleus is always accelerating, and classical physics says that an accelerating charge sends out electromagnetic radiation. The electron should lose energy, spiral into the nucleus and send out a continuous spectrum on the way. Real atoms are stable and give sharp lines. Classical physics had failed again.

## Bohr's quantum atom {Bohr}

In 1913 the Danish physicist Niels Bohr, who had worked with Rutherford in Manchester, combined the nuclear atom with Planck's and Einstein's quanta. His model of hydrogen rests on three ideas:

1. The electron can move only in certain allowed orbits, the **stationary states**. In them it does not radiate. Each state has its own **energy level** $E_n$, numbered by $n = 1, 2, 3, \ldots$
2. The electron can **jump** from a higher level to a lower one. The atom then sends out one photon that carries away the difference in energy.
3. A photon can be absorbed only if its energy is exactly the difference between two levels.

So a hot gas sends out only the photon energies that match jumps between its levels: a line spectrum. A *bigger* jump gives a photon of *higher* energy, so a higher frequency and a *shorter* wavelength. The four visible lines of hydrogen are the jumps that end at $n = 2$. The jumps that end at $n = 1$ are much bigger and give ultraviolet light.

<svg data-fig="levels" viewBox="0 0 600 560" role="img" aria-label="Energy-level diagram of the hydrogen atom, drawn to scale. Horizontal lines: n = 1 at minus 13.6 electronvolts at the bottom, n = 2 at minus 3.40, n = 3 at minus 1.51, n = 4 at minus 0.85, then n = 5 and n = 6 crowding just below zero, which is the energy of a free electron. Downward arrows show jumps to n = 2 from n = 3, 4, 5 and 6, coloured red, turquoise, blue and violet, with the wavelengths 656, 486, 434 and 410 nanometres. A grey arrow from n = 2 to n = 1 gives ultraviolet light of 122 nanometres." style="max-width:100%;font-size:24px">
  <line x1="120" y1="50" x2="470" y2="50" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <foreignObject x="478" y="25.5" width="49" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$0\ \text{eV}$</div></foreignObject>
  <foreignObject x="65" y="25.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$n = \infty$</div></foreignObject>
  <line x1="120" y1="512.5" x2="470" y2="512.5" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="120" y1="165.5" x2="470" y2="165.5" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="120" y1="101.5" x2="470" y2="101.5" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="120" y1="79" x2="470" y2="79" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="120" y1="68.5" x2="470" y2="68.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="120" y1="63" x2="470" y2="63" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="65" y="498" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$n = 1$</div></foreignObject>
  <foreignObject x="478" y="498" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-13.6\ \text{eV}$</div></foreignObject>
  <foreignObject x="65" y="151" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$n = 2$</div></foreignObject>
  <foreignObject x="478" y="151" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-3.40\ \text{eV}$</div></foreignObject>
  <line x1="112" y1="106.5" x2="120" y2="101.5" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="101.5" x2="476" y2="106.5" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="65" y="92" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$n = 3$</div></foreignObject>
  <foreignObject x="478" y="92" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-1.51\ \text{eV}$</div></foreignObject>
  <line x1="112" y1="74" x2="120" y2="79" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="79" x2="476" y2="74" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="65" y="59.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$n = 4$</div></foreignObject>
  <foreignObject x="478" y="59.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-0.85\ \text{eV}$</div></foreignObject>
  <line x1="250" y1="101.5" x2="250" y2="149.5" stroke="#e03131" stroke-width="4" stroke-linecap="butt"/>
  <path d="M250,164.5 L243,148.5 L257,148.5 Z" fill="#e03131" stroke-linejoin="round"/>
  <foreignObject x="227.5" y="181" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e03131">$656$</div></foreignObject>
  <line x1="310" y1="79" x2="310" y2="149.5" stroke="#15aabf" stroke-width="4" stroke-linecap="butt"/>
  <path d="M310,164.5 L303,148.5 L317,148.5 Z" fill="#15aabf" stroke-linejoin="round"/>
  <foreignObject x="287.5" y="181" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#15aabf">$486$</div></foreignObject>
  <line x1="370" y1="68.5" x2="370" y2="149.5" stroke="#3b5bdb" stroke-width="4" stroke-linecap="butt"/>
  <path d="M370,164.5 L363,148.5 L377,148.5 Z" fill="#3b5bdb" stroke-linejoin="round"/>
  <foreignObject x="347.5" y="181" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#3b5bdb">$434$</div></foreignObject>
  <line x1="430" y1="63" x2="430" y2="149.5" stroke="#7048e8" stroke-width="4" stroke-linecap="butt"/>
  <path d="M430,164.5 L423,148.5 L437,148.5 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="407.5" y="181" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$410$</div></foreignObject>
  <foreignObject x="303" y="213" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\lambda\ \text{in nm}$</div></foreignObject>
  <line x1="160" y1="165.5" x2="160" y2="496.5" stroke="#6b7480" stroke-width="4" stroke-linecap="butt"/>
  <path d="M160,511.5 L153,495.5 L167,495.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <foreignObject x="176" y="324.5" width="124" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$122\ \text{nm (UV)}$</div></foreignObject>
</svg>

Bohr's model gives the hydrogen lines very accurately, but it fails for atoms with more than one electron, and its electrons in neat circular orbits are not the whole truth. In the 1920s **quantum mechanics** replaced the orbits with waves and probabilities: the topic of the next unit. The idea of energy levels survived.

## Formula: Energy levels of hydrogen

The energy levels of the hydrogen atom are
```latex
E_n = -\frac{13.6\ \text{eV}}{n^2}, \qquad n = 1, 2, 3, \ldots
```
The energy is negative, because the electron is bound: $13.6\ \text{eV}$ is needed to free it from the lowest level $n = 1$, the **ground state**. In a jump from level $n_\text{u}$ (upper) to $n_\text{l}$ (lower), energy is conserved:
```latex
hf = \frac{hc}{\lambda} = E_{n_\text{u}} - E_{n_\text{l}}
```
A useful product for these calculations is $hc = 1240\ \text{eV} \cdot \text{nm}$.

## Worked example

Rutherford's reasoning showed how close an alpha particle can come to a nucleus. An alpha particle (charge $2e$, mass $6.64 \cdot 10^{-27}\ \text{kg}$) moves straight towards a gold nucleus (charge $79e$) at a speed of $2.0 \cdot 10^{7}\ \text{m/s}$. How close does it come before it turns back? Compare the distance with the size of the gold atom.

<!-- vaihe -->

**Given:** ${m = 6.64 \cdot 10^{-27}\ \text{kg}}$, ${v = 2.0 \cdot 10^{7}\ \text{m/s}}$, ${q_1 = 2e}$, ${q_2 = 79e}$, ${e = 1.602 \cdot 10^{-19}\ \text{C}}$, ${k = 8.988 \cdot 10^{9}\ \text{N} \cdot \text{m}^2/\text{C}^2}$. Find the closest distance $d$.

<!-- vaihe -->

**Principle:** Energy is conserved. Far from the nucleus the alpha particle has only kinetic energy. At the turning point it stops for a moment, and all its kinetic energy has become electric potential energy $E_\text{p} = kq_1q_2/r$. The heavy nucleus is assumed not to move.

<!-- vaihe -->

**Formula:** Solved in symbols:
```latex
\begin{aligned}
\tfrac{1}{2}mv^2 &= \frac{kq_1q_2}{d} \\
d &= \frac{kq_1q_2}{\tfrac{1}{2}mv^2}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions:** The charges in coulombs: $q_1 = 2 \cdot 1.602 \cdot 10^{-19}\ \text{C} = 3.204 \cdot 10^{-19}\ \text{C}$ and $q_2 = 79 \cdot 1.602 \cdot 10^{-19}\ \text{C} = 1.266 \cdot 10^{-17}\ \text{C}$. The answer is changed to femtometres with $1\ \text{fm} = 10^{-15}\ \text{m}$.

<!-- vaihe -->

**Substitution:**
```latex
\begin{aligned}
E_\text{k} &= \tfrac{1}{2} \cdot 6.64 \cdot 10^{-27}\ \text{kg} \\
&\quad \cdot (2.0 \cdot 10^{7}\ \text{m/s})^2 \\
&= 1.328 \cdot 10^{-12}\ \text{J} \\[6pt]
kq_1q_2 &= 8.988 \cdot 10^{9}\ \tfrac{\text{N} \cdot \text{m}^2}{\text{C}^2} \\
&\quad \cdot 3.204 \cdot 10^{-19}\ \text{C} \\
&\quad \cdot 1.266 \cdot 10^{-17}\ \text{C} \\
&= 3.645 \cdot 10^{-26}\ \text{J} \cdot \text{m} \\[6pt]
d &= \frac{3.645 \cdot 10^{-26}\ \text{J} \cdot \text{m}}{1.328 \cdot 10^{-12}\ \text{J}} \\
&= 2.74 \cdot 10^{-14}\ \text{m} = 27\ \text{fm}
\end{aligned}
```

<!-- vaihe -->

**Answer:** The alpha particle turns back at about $d \approx 2.7 \cdot 10^{-14}\ \text{m} = 27\ \text{fm}$ from the centre of the nucleus. Two significant figures, like the speed. The gold atom ($1.44 \cdot 10^{-10}\ \text{m}$) is about $5000$ times larger.

<!-- vaihe -->

**Reasonableness:** Rutherford found the same order of magnitude: the nucleus must be smaller than about $3 \cdot 10^{-14}\ \text{m}$. Today's value for the radius of the gold nucleus, about $7\ \text{fm}$, is indeed smaller than $27\ \text{fm}$, so the alpha particle never touches it: only the electric force acts. The kinetic energy is about $8.3\ \text{MeV}$ ($1.328 \cdot 10^{-12}\ \text{J}$ divided by $1.602 \cdot 10^{-19}\ \text{J/eV}$). This is within the range of alpha particles from radioactive decay, about $4\text{–}9\ \text{MeV}$.

## Common misconception

"The atom is a tiny solar system." Bohr's circular orbits look like planets around the Sun, but electrons do not have paths like planets. The model was a bridge: it got the energy levels of hydrogen right, but quantum mechanics describes the electron with a wave and probabilities, not with a track.

A second mistake is to think that the wavelength of a line comes from one level alone. A photon carries the *difference* between two levels, $hf = E_{n_\text{u}} - E_{n_\text{l}}$, so you always need two levels. A third is to think that the electric repulsion stops the alpha particles in Thomson's atom too: there the positive charge was spread out, so the force on an alpha particle was never strong enough to turn it back.

## People in this story {People}

### Ernest Marsden (1889–1970)

<!-- photo: ernest-marsden -->

Ernest Marsden was born in Lancashire, England. In 1909 he was a 20-year-old undergraduate at the University of Manchester when Rutherford asked him to check whether any alpha particles bounce back from a metal foil. With Hans Geiger he found that a few did, the observation that led to the nucleus. Later Marsden moved to New Zealand. From 1926 he led the country's new Department of Scientific and Industrial Research. His story shows how a careful student's measurement can change science.

### Niels Bohr (1885–1962)

<figure class="unit-photo"><img src="units/fy14/pics/bohr.jpg" alt="Black-and-white portrait photograph of Niels Bohr as a young man in a suit and tie." width="1138" height="1600" loading="lazy"><figcaption>Niels Bohr (1885–1962) proposed in 1913 that electrons in atoms occupy fixed energy levels. He received the Nobel Prize in Physics in 1922. <span class="photo-credit">Photo: AB Lagrelius &amp; Westphal, public domain, via Wikimedia Commons</span></figcaption></figure>

Niels Bohr was born and died in Copenhagen. After his doctorate he worked with Rutherford in Manchester in 1912, and back in Copenhagen he published his model of the atom in three papers in 1913. His institute in Copenhagen, opened in 1921, became a meeting place for the young physicists who built quantum mechanics. He received the Nobel Prize in Physics in 1922 "for his services in the investigation of the structure of atoms and of the radiation emanating from them". Bohr linked Rutherford's nucleus with Planck's quanta.

## Summary

- The Geiger–Marsden experiment (1909) showed that a few alpha particles bounce back from a thin foil. Rutherford (1911) explained this with a tiny, positive, heavy **nucleus**; the atom is mostly empty.
- Classical physics could not explain why such an atom is stable or why gases give **line spectra**.
- Bohr's model (1913): the electron has only certain **energy levels**, and a jump between two levels sends out one photon, $hf = E_{n_\text{u}} - E_{n_\text{l}}$.
- For hydrogen, $E_n = -13.6\ \text{eV}/n^2$. The visible lines are jumps to $n = 2$: $656$, $486$, $434$ and $410\ \text{nm}$.
- The nucleus is tiny and positive, so two nuclei repel each other strongly: this is the first obstacle to fusion.
