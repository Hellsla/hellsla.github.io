# Inside ITER: the machine and fusion gain

> **Why** is it so hard to get more energy out of a fusion plasma than you put into it?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a cut-away view of a huge doughnut-shaped machine in a dark hall. In the middle stands a tall stack of coils. On both sides, large D-shaped magnet coils surround a steel chamber with a double wall. Inside each half of the chamber a pink, glowing ring of plasma floats without touching the walls. A pale blue haze around the coils shows that they are extremely cold, while the plasma glows hot. A huge steel vessel with a domed lid encloses everything." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy14ii-h-bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2d3a46"/><stop offset="1" stop-color="#1f2933"/></linearGradient><radialGradient id="fy14ii-h-glow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#fff0f6"/><stop offset="0.55" stop-color="#e64980" stop-opacity="0.8"/><stop offset="1" stop-color="#e64980" stop-opacity="0"/></radialGradient><radialGradient id="fy14ii-h-cold" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#e7f5ff"/><stop offset="0.55" stop-color="#74c0fc" stop-opacity="0.8"/><stop offset="1" stop-color="#74c0fc" stop-opacity="0"/></radialGradient><linearGradient id="fy14ii-h-steel" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8a96a3"/><stop offset="0.3" stop-color="#ffffff"/><stop offset="0.65" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy14ii-h-bg)"/>
  <rect x="0" y="540" width="1200" height="60" fill="#3a4754"/>
  <path d="M140,540 L140,170 Q600,30 1060,170 L1060,540 Z" fill="#46525f" stroke="#8a96a3" stroke-width="5" stroke-linejoin="round"/>
  <path d="M164,540 L164,184 Q600,56 1036,184 L1036,540 Z" fill="#26323d" stroke-linejoin="round"/>
  <ellipse cx="380" cy="320" rx="230" ry="210" fill="url(#fy14ii-h-cold)" fill-opacity="0.35"/>
  <ellipse cx="820" cy="320" rx="230" ry="210" fill="url(#fy14ii-h-cold)" fill-opacity="0.35"/>
  <rect x="572" y="150" width="56" height="48" rx="3" fill="url(#fy14ii-h-steel)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="577" y1="174" x2="623" y2="174" stroke="#b8622d" stroke-width="3" stroke-linecap="butt"/>
  <rect x="572" y="202" width="56" height="48" rx="3" fill="url(#fy14ii-h-steel)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="577" y1="226" x2="623" y2="226" stroke="#b8622d" stroke-width="3" stroke-linecap="butt"/>
  <rect x="572" y="254" width="56" height="48" rx="3" fill="url(#fy14ii-h-steel)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="577" y1="278" x2="623" y2="278" stroke="#b8622d" stroke-width="3" stroke-linecap="butt"/>
  <rect x="572" y="306" width="56" height="48" rx="3" fill="url(#fy14ii-h-steel)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="577" y1="330" x2="623" y2="330" stroke="#b8622d" stroke-width="3" stroke-linecap="butt"/>
  <rect x="572" y="358" width="56" height="48" rx="3" fill="url(#fy14ii-h-steel)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="577" y1="382" x2="623" y2="382" stroke="#b8622d" stroke-width="3" stroke-linecap="butt"/>
  <rect x="572" y="410" width="56" height="48" rx="3" fill="url(#fy14ii-h-steel)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="577" y1="434" x2="623" y2="434" stroke="#b8622d" stroke-width="3" stroke-linecap="butt"/>
  <path d="M218,320 L219,307.5 L221.5,295 L225.5,282.5 L231,270.5 L238,258.5 L246,247 L255.5,236 L266,225 L277.5,214.5 L290,205 L302.5,195.5 L316,187 L329.5,179 L343,171.5 L356.5,165 L370,159 L383.5,154 L396,149.5 L408.5,146 L420.5,143.5 L432,142 L442.5,141 L452.5,141 L462,142 L470.5,143.5 L478.5,146 L486,149.5 L493,154 L499,159 L504.5,165 L509.5,171.5 L514,179 L518,187 L521.5,195.5 L525,205 L527.5,214.5 L530,225 L532,236 L533.5,247 L535,258.5 L536,270.5 L537,282.5 L537.5,295 L538,307.5 L538,320 L538,332.5 L537.5,345 L537,357.5 L536,369.5 L535,381.5 L533.5,393 L532,404 L530,415 L527.5,425.5 L525,435 L521.5,444.5 L518,453 L514,461 L509.5,468.5 L504.5,475 L499,481 L493,486 L486,490.5 L478.5,494 L470.5,496.5 L462,498 L452.5,499 L442.5,499 L432,498 L420.5,496.5 L408.5,494 L396,490.5 L383.5,486 L370,481 L356.5,475 L343,468.5 L329.5,461 L316,453 L302.5,444.5 L290,435 L277.5,425.5 L266,415 L255.5,404 L246,393 L238,381.5 L231,369.5 L225.5,357.5 L221.5,345 L219,332.5 Z" fill="none" stroke="#6c7a89" stroke-width="30" stroke-linejoin="round"/>
  <path d="M218,320 L219,307.5 L221.5,295 L225.5,282.5 L231,270.5 L238,258.5 L246,247 L255.5,236 L266,225 L277.5,214.5 L290,205 L302.5,195.5 L316,187 L329.5,179 L343,171.5 L356.5,165 L370,159 L383.5,154 L396,149.5 L408.5,146 L420.5,143.5 L432,142 L442.5,141 L452.5,141 L462,142 L470.5,143.5 L478.5,146 L486,149.5 L493,154 L499,159 L504.5,165 L509.5,171.5 L514,179 L518,187 L521.5,195.5 L525,205 L527.5,214.5 L530,225 L532,236 L533.5,247 L535,258.5 L536,270.5 L537,282.5 L537.5,295 L538,307.5 L538,320 L538,332.5 L537.5,345 L537,357.5 L536,369.5 L535,381.5 L533.5,393 L532,404 L530,415 L527.5,425.5 L525,435 L521.5,444.5 L518,453 L514,461 L509.5,468.5 L504.5,475 L499,481 L493,486 L486,490.5 L478.5,494 L470.5,496.5 L462,498 L452.5,499 L442.5,499 L432,498 L420.5,496.5 L408.5,494 L396,490.5 L383.5,486 L370,481 L356.5,475 L343,468.5 L329.5,461 L316,453 L302.5,444.5 L290,435 L277.5,425.5 L266,415 L255.5,404 L246,393 L238,381.5 L231,369.5 L225.5,357.5 L221.5,345 L219,332.5 Z" fill="none" stroke="#9aa7b4" stroke-width="9" stroke-linejoin="round"/>
  <path d="M258,326 L258.5,316 L260,305.5 L263,295.5 L266.5,286 L271.5,276 L277,267 L283.5,257.5 L290.5,249 L298,240.5 L306.5,232.5 L315,225 L324,218 L333.5,211.5 L343,205.5 L352,200 L361.5,195 L370.5,191 L379.5,187.5 L388,184.5 L396.5,182.5 L404.5,181 L412,180.5 L419,180.5 L426,181 L432,182.5 L438,184.5 L443.5,187.5 L448,191 L452.5,195 L457,200 L460.5,205.5 L464,211.5 L467,218 L469.5,225 L472,232.5 L474,240.5 L475.5,249 L477.5,257.5 L478.5,267 L479.5,276 L480.5,286 L481,295.5 L481.5,305.5 L482,316 L482,326 L482,336 L481.5,346.5 L481,356.5 L480.5,366 L479.5,376 L478.5,385 L477.5,394.5 L475.5,403 L474,411.5 L472,419.5 L469.5,427 L467,434 L464,440.5 L460.5,446.5 L457,452 L452.5,457 L448,461 L443.5,464.5 L438,467.5 L432,469.5 L426,471 L419,471.5 L412,471.5 L404.5,471 L396.5,469.5 L388,467.5 L379.5,464.5 L370.5,461 L361.5,457 L352,452 L343,446.5 L333.5,440.5 L324,434 L315,427 L306.5,419.5 L298,411.5 L290.5,403 L283.5,394.5 L277,385 L271.5,376 L266.5,366 L263,356.5 L260,346.5 L258.5,336 Z" fill="#3b4a59" stroke="#c4ccd4" stroke-width="8" stroke-linejoin="round"/>
  <path d="M274,326 L274.5,317.5 L276,308.5 L278,300 L281.5,291.5 L285.5,283.5 L290,275 L295.5,267.5 L302,260 L308.5,252.5 L315.5,246 L323,239.5 L331,233.5 L338.5,227.5 L346.5,222.5 L354.5,218 L362.5,214 L370.5,210.5 L378,207.5 L385.5,205 L392.5,203 L399.5,202 L406,201.5 L412,201.5 L418,202 L423.5,203 L428,205 L433,207.5 L437,210.5 L441,214 L444.5,218 L447.5,222.5 L450.5,227.5 L453,233.5 L455.5,239.5 L457.5,246 L459,252.5 L460.5,260 L462,267.5 L463,275 L464,283.5 L464.5,291.5 L465.5,300 L465.5,308.5 L466,317.5 L466,326 L466,334.5 L465.5,343.5 L465.5,352 L464.5,360.5 L464,368.5 L463,377 L462,384.5 L460.5,392 L459,399.5 L457.5,406 L455.5,412.5 L453,418.5 L450.5,424.5 L447.5,429.5 L444.5,434 L441,438 L437,441.5 L433,444.5 L428,447 L423.5,449 L418,450 L412,450.5 L406,450.5 L399.5,450 L392.5,449 L385.5,447 L378,444.5 L370.5,441.5 L362.5,438 L354.5,434 L346.5,429.5 L338.5,424.5 L331,418.5 L323,412.5 L315.5,406 L308.5,399.5 L302,392 L295.5,384.5 L290,377 L285.5,368.5 L281.5,360.5 L278,352 L276,343.5 L274.5,334.5 Z" fill="#1c252e" stroke="#c9a26b" stroke-width="9" stroke-linejoin="round"/>
  <path d="M300,318 L300.5,311 L301.5,304 L303,297.5 L305,290.5 L307.5,284 L311,277.5 L314.5,271.5 L318.5,265.5 L323,260 L328,254.5 L333,249 L338,244.5 L343.5,240 L349,236 L354.5,232.5 L360,229 L365,226 L370.5,224 L375.5,222 L380.5,220.5 L385,219.5 L389.5,219 L394,219 L398,219.5 L401.5,220.5 L405,222 L408,224 L411,226 L414,229 L416.5,232.5 L418.5,236 L421,240 L422.5,244.5 L424,249 L425.5,254.5 L427,260 L428,265.5 L429,271.5 L430,277.5 L430.5,284 L431,290.5 L431.5,297.5 L432,304 L432,311 L432,318 L432,325 L432,332 L431.5,338.5 L431,345.5 L430.5,352 L430,358.5 L429,364.5 L428,370.5 L427,376 L425.5,381.5 L424,387 L422.5,391.5 L421,396 L418.5,400 L416.5,403.5 L414,407 L411,410 L408,412 L405,414 L401.5,415.5 L398,416.5 L394,417 L389.5,417 L385,416.5 L380.5,415.5 L375.5,414 L370.5,412 L365,410 L360,407 L354.5,403.5 L349,400 L343.5,396 L338,391.5 L333,387 L328,381.5 L323,376 L318.5,370.5 L314.5,364.5 L311,358.5 L307.5,352 L305,345.5 L303,338.5 L301.5,332 L300.5,325 Z" fill="url(#fy14ii-h-glow)" stroke-linejoin="round"/>
  <path d="M326,318 L326,314 L327,309.5 L327.5,305.5 L329,301.5 L330.5,297.5 L332.5,293.5 L335,290 L337.5,286 L340,282.5 L343,279.5 L346,276.5 L349,273.5 L352.5,270.5 L355.5,268.5 L359,266 L362,264 L365.5,262.5 L368.5,261 L371.5,260 L374.5,259 L377.5,258.5 L380.5,258 L383,258 L385.5,258.5 L387.5,259 L389.5,260 L391.5,261 L393.5,262.5 L395,264 L396.5,266 L398,268.5 L399,270.5 L400.5,273.5 L401.5,276.5 L402,279.5 L403,282.5 L403.5,286 L404,290 L404.5,293.5 L405,297.5 L405.5,301.5 L405.5,305.5 L406,309.5 L406,314 L406,318 L406,322 L406,326.5 L405.5,330.5 L405.5,334.5 L405,338.5 L404.5,342.5 L404,346 L403.5,350 L403,353.5 L402,356.5 L401.5,359.5 L400.5,362.5 L399,365.5 L398,367.5 L396.5,370 L395,372 L393.5,373.5 L391.5,375 L389.5,376 L387.5,377 L385.5,377.5 L383,378 L380.5,378 L377.5,377.5 L374.5,377 L371.5,376 L368.5,375 L365.5,373.5 L362,372 L359,370 L355.5,367.5 L352.5,365.5 L349,362.5 L346,359.5 L343,356.5 L340,353.5 L337.5,350 L335,346 L332.5,342.5 L330.5,338.5 L329,334.5 L327.5,330.5 L327,326.5 L326,322 Z" fill="#fff0f6" stroke-linejoin="round" fill-opacity="0.55"/>
  <path d="M334,446 L356,424 L374,440 L392,424 L414,446 Z" fill="#868e96" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M982,320 L981,307.5 L978.5,295 L974.5,282.5 L969,270.5 L962,258.5 L954,247 L944.5,236 L934,225 L922.5,214.5 L910,205 L897.5,195.5 L884,187 L870.5,179 L857,171.5 L843.5,165 L830,159 L816.5,154 L804,149.5 L791.5,146 L779.5,143.5 L768,142 L757.5,141 L747.5,141 L738,142 L729.5,143.5 L721.5,146 L714,149.5 L707,154 L701,159 L695.5,165 L690.5,171.5 L686,179 L682,187 L678.5,195.5 L675,205 L672.5,214.5 L670,225 L668,236 L666.5,247 L665,258.5 L664,270.5 L663,282.5 L662.5,295 L662,307.5 L662,320 L662,332.5 L662.5,345 L663,357.5 L664,369.5 L665,381.5 L666.5,393 L668,404 L670,415 L672.5,425.5 L675,435 L678.5,444.5 L682,453 L686,461 L690.5,468.5 L695.5,475 L701,481 L707,486 L714,490.5 L721.5,494 L729.5,496.5 L738,498 L747.5,499 L757.5,499 L768,498 L779.5,496.5 L791.5,494 L804,490.5 L816.5,486 L830,481 L843.5,475 L857,468.5 L870.5,461 L884,453 L897.5,444.5 L910,435 L922.5,425.5 L934,415 L944.5,404 L954,393 L962,381.5 L969,369.5 L974.5,357.5 L978.5,345 L981,332.5 Z" fill="none" stroke="#6c7a89" stroke-width="30" stroke-linejoin="round"/>
  <path d="M982,320 L981,307.5 L978.5,295 L974.5,282.5 L969,270.5 L962,258.5 L954,247 L944.5,236 L934,225 L922.5,214.5 L910,205 L897.5,195.5 L884,187 L870.5,179 L857,171.5 L843.5,165 L830,159 L816.5,154 L804,149.5 L791.5,146 L779.5,143.5 L768,142 L757.5,141 L747.5,141 L738,142 L729.5,143.5 L721.5,146 L714,149.5 L707,154 L701,159 L695.5,165 L690.5,171.5 L686,179 L682,187 L678.5,195.5 L675,205 L672.5,214.5 L670,225 L668,236 L666.5,247 L665,258.5 L664,270.5 L663,282.5 L662.5,295 L662,307.5 L662,320 L662,332.5 L662.5,345 L663,357.5 L664,369.5 L665,381.5 L666.5,393 L668,404 L670,415 L672.5,425.5 L675,435 L678.5,444.5 L682,453 L686,461 L690.5,468.5 L695.5,475 L701,481 L707,486 L714,490.5 L721.5,494 L729.5,496.5 L738,498 L747.5,499 L757.5,499 L768,498 L779.5,496.5 L791.5,494 L804,490.5 L816.5,486 L830,481 L843.5,475 L857,468.5 L870.5,461 L884,453 L897.5,444.5 L910,435 L922.5,425.5 L934,415 L944.5,404 L954,393 L962,381.5 L969,369.5 L974.5,357.5 L978.5,345 L981,332.5 Z" fill="none" stroke="#9aa7b4" stroke-width="9" stroke-linejoin="round"/>
  <path d="M942,326 L941.5,316 L940,305.5 L937,295.5 L933.5,286 L928.5,276 L923,267 L916.5,257.5 L909.5,249 L902,240.5 L893.5,232.5 L885,225 L876,218 L866.5,211.5 L857,205.5 L848,200 L838.5,195 L829.5,191 L820.5,187.5 L812,184.5 L803.5,182.5 L795.5,181 L788,180.5 L781,180.5 L774,181 L768,182.5 L762,184.5 L756.5,187.5 L752,191 L747.5,195 L743,200 L739.5,205.5 L736,211.5 L733,218 L730.5,225 L728,232.5 L726,240.5 L724.5,249 L722.5,257.5 L721.5,267 L720.5,276 L719.5,286 L719,295.5 L718.5,305.5 L718,316 L718,326 L718,336 L718.5,346.5 L719,356.5 L719.5,366 L720.5,376 L721.5,385 L722.5,394.5 L724.5,403 L726,411.5 L728,419.5 L730.5,427 L733,434 L736,440.5 L739.5,446.5 L743,452 L747.5,457 L752,461 L756.5,464.5 L762,467.5 L768,469.5 L774,471 L781,471.5 L788,471.5 L795.5,471 L803.5,469.5 L812,467.5 L820.5,464.5 L829.5,461 L838.5,457 L848,452 L857,446.5 L866.5,440.5 L876,434 L885,427 L893.5,419.5 L902,411.5 L909.5,403 L916.5,394.5 L923,385 L928.5,376 L933.5,366 L937,356.5 L940,346.5 L941.5,336 Z" fill="#3b4a59" stroke="#c4ccd4" stroke-width="8" stroke-linejoin="round"/>
  <path d="M926,326 L925.5,317.5 L924,308.5 L922,300 L918.5,291.5 L914.5,283.5 L910,275 L904.5,267.5 L898,260 L891.5,252.5 L884.5,246 L877,239.5 L869,233.5 L861.5,227.5 L853.5,222.5 L845.5,218 L837.5,214 L829.5,210.5 L822,207.5 L814.5,205 L807.5,203 L800.5,202 L794,201.5 L788,201.5 L782,202 L776.5,203 L772,205 L767,207.5 L763,210.5 L759,214 L755.5,218 L752.5,222.5 L749.5,227.5 L747,233.5 L744.5,239.5 L742.5,246 L741,252.5 L739.5,260 L738,267.5 L737,275 L736,283.5 L735.5,291.5 L734.5,300 L734.5,308.5 L734,317.5 L734,326 L734,334.5 L734.5,343.5 L734.5,352 L735.5,360.5 L736,368.5 L737,377 L738,384.5 L739.5,392 L741,399.5 L742.5,406 L744.5,412.5 L747,418.5 L749.5,424.5 L752.5,429.5 L755.5,434 L759,438 L763,441.5 L767,444.5 L772,447 L776.5,449 L782,450 L788,450.5 L794,450.5 L800.5,450 L807.5,449 L814.5,447 L822,444.5 L829.5,441.5 L837.5,438 L845.5,434 L853.5,429.5 L861.5,424.5 L869,418.5 L877,412.5 L884.5,406 L891.5,399.5 L898,392 L904.5,384.5 L910,377 L914.5,368.5 L918.5,360.5 L922,352 L924,343.5 L925.5,334.5 Z" fill="#1c252e" stroke="#c9a26b" stroke-width="9" stroke-linejoin="round"/>
  <path d="M900,318 L899.5,311 L898.5,304 L897,297.5 L895,290.5 L892.5,284 L889,277.5 L885.5,271.5 L881.5,265.5 L877,260 L872,254.5 L867,249 L862,244.5 L856.5,240 L851,236 L845.5,232.5 L840,229 L835,226 L829.5,224 L824.5,222 L819.5,220.5 L815,219.5 L810.5,219 L806,219 L802,219.5 L798.5,220.5 L795,222 L792,224 L789,226 L786,229 L783.5,232.5 L781.5,236 L779,240 L777.5,244.5 L776,249 L774.5,254.5 L773,260 L772,265.5 L771,271.5 L770,277.5 L769.5,284 L769,290.5 L768.5,297.5 L768,304 L768,311 L768,318 L768,325 L768,332 L768.5,338.5 L769,345.5 L769.5,352 L770,358.5 L771,364.5 L772,370.5 L773,376 L774.5,381.5 L776,387 L777.5,391.5 L779,396 L781.5,400 L783.5,403.5 L786,407 L789,410 L792,412 L795,414 L798.5,415.5 L802,416.5 L806,417 L810.5,417 L815,416.5 L819.5,415.5 L824.5,414 L829.5,412 L835,410 L840,407 L845.5,403.5 L851,400 L856.5,396 L862,391.5 L867,387 L872,381.5 L877,376 L881.5,370.5 L885.5,364.5 L889,358.5 L892.5,352 L895,345.5 L897,338.5 L898.5,332 L899.5,325 Z" fill="url(#fy14ii-h-glow)" stroke-linejoin="round"/>
  <path d="M874,318 L874,314 L873,309.5 L872.5,305.5 L871,301.5 L869.5,297.5 L867.5,293.5 L865,290 L862.5,286 L860,282.5 L857,279.5 L854,276.5 L851,273.5 L847.5,270.5 L844.5,268.5 L841,266 L838,264 L834.5,262.5 L831.5,261 L828.5,260 L825.5,259 L822.5,258.5 L819.5,258 L817,258 L814.5,258.5 L812.5,259 L810.5,260 L808.5,261 L806.5,262.5 L805,264 L803.5,266 L802,268.5 L801,270.5 L799.5,273.5 L798.5,276.5 L798,279.5 L797,282.5 L796.5,286 L796,290 L795.5,293.5 L795,297.5 L794.5,301.5 L794.5,305.5 L794,309.5 L794,314 L794,318 L794,322 L794,326.5 L794.5,330.5 L794.5,334.5 L795,338.5 L795.5,342.5 L796,346 L796.5,350 L797,353.5 L798,356.5 L798.5,359.5 L799.5,362.5 L801,365.5 L802,367.5 L803.5,370 L805,372 L806.5,373.5 L808.5,375 L810.5,376 L812.5,377 L814.5,377.5 L817,378 L819.5,378 L822.5,377.5 L825.5,377 L828.5,376 L831.5,375 L834.5,373.5 L838,372 L841,370 L844.5,367.5 L847.5,365.5 L851,362.5 L854,359.5 L857,356.5 L860,353.5 L862.5,350 L865,346 L867.5,342.5 L869.5,338.5 L871,334.5 L872.5,330.5 L873,326.5 L874,322 Z" fill="#fff0f6" stroke-linejoin="round" fill-opacity="0.55"/>
  <path d="M786,446 L808,424 L826,440 L844,424 L866,446 Z" fill="#868e96" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <rect x="278" y="105" width="44" height="30" rx="4" fill="#4dabf7" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="878" y="105" width="44" height="30" rx="4" fill="#4dabf7" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="163" y="305" width="44" height="30" rx="4" fill="#4dabf7" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="993" y="305" width="44" height="30" rx="4" fill="#4dabf7" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="278" y="505" width="44" height="30" rx="4" fill="#4dabf7" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="878" y="505" width="44" height="30" rx="4" fill="#4dabf7" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="390" y="520" width="60" height="20" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="750" y="520" width="60" height="20" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
</svg>

## The parts of the machine {Machine}

ITER is a **tokamak**. Its plasma, about $830\ \text{m}^3$ of deuterium and tritium at about $150$ million $^\circ\text{C}$, is held by magnetic fields inside a ring-shaped steel chamber.

- **Magnets.** $18$ D-shaped **toroidal field coils** make the field that runs around the ring (up to $11.8\ \text{T}$). Six ring-shaped **poloidal field coils** shape the plasma and hold it in place. The **central solenoid**, a $13\ \text{m}$ tall stack of six modules, works like the primary coil of a transformer: a changing current in it drives a current of up to $15\ \text{MA}$ in the plasma. All the magnets are **superconducting** and are cooled with helium to about $4\ \text{K}$.
- **Vacuum vessel.** A double-walled steel chamber, $19.4\ \text{m}$ wide, keeps the vacuum and is the first barrier that keeps tritium in.
- **Blanket.** $440$ modules line the inside of the vessel. They take the heat and the fast neutrons and shield the vessel and the magnets.
- **Divertor.** At the bottom, $54$ cassettes with tungsten targets catch the heat and the helium "ash" that flow out along the edge of the plasma. The heat flow there is up to about $10\text{–}20\ \text{MW}$ on each square metre, the highest in the machine.
- **Heating.** Beams of fast neutral atoms and two kinds of radio waves heat the plasma with a planned $50\ \text{MW}$.
- **Cryostat.** A vacuum chamber about $30\ \text{m}$ tall around everything insulates the cold magnets from the warm building.

<figure class="unit-photo"><img src="units/fy14/pics/iter-magnet-coil.jpg" alt="Colour photograph of a very large ring-shaped magnet coil in a factory hall." width="1600" height="1067" loading="lazy"><figcaption>A poloidal field coil being built in the coil factory on the ITER site. These giant rings shape and position the plasma. <span class="photo-credit">Photo: Johannes Reimer, CC BY 4.0, via Wikimedia Commons</span></figcaption></figure>

<figure class="unit-photo"><img src="units/fy14/pics/iter-vacuum-vessel-hellsten.jpg" alt="Colour photograph looking up in the ITER assembly hall: a huge curved steel vacuum-vessel sector hangs in a grey tooling frame next to pink-wrapped D-shaped magnet coils, with yellow cranes overhead and workers on scaffolding." width="1200" height="1600" loading="lazy"><figcaption>A sector of the ITER vacuum vessel in its assembly tooling, 26 March 2024, next to D-shaped toroidal field coils wrapped in pink protective film. The workers on the scaffolding show the scale: one sector is about as tall as a four-storey building. <span class="photo-credit">Photo: Lauri Hellsten</span></figcaption></figure>

## Key idea

A fusion plasma loses energy all the time: hot particles escape across the magnetic field and the plasma radiates. To keep it hot, we heat it from outside. The **fusion gain** $Q$ compares the fusion power produced in the plasma with this heating power.

At $Q = 1$, called **scientific breakeven**, the plasma produces as much fusion power as it receives. No magnetic fusion experiment has reached it yet with real $\text{D–T}$ fuel: JET's record from 1997 was $16\ \text{MW}$ of fusion power from $24\ \text{MW}$ of heating, $Q \approx 0.67$. ITER's goal is $Q = 10$: $500\ \text{MW}$ of fusion power from $50\ \text{MW}$ of heating, in pulses of $400\text{–}600\ \text{s}$. In D–T fusion, $3.5\ \text{MeV}$ of the $17.6\ \text{MeV}$ goes to the helium nucleus, which is charged and stays in the plasma. At $Q = 10$ these helium nuclei heat the plasma about twice as much as the external heating does: a **burning plasma**.

## Formula: Fusion gain

```latex
Q = \frac{P_\text{fusion}}{P_\text{heating}}
```

Here $P_\text{fusion}$ is the fusion power produced in the plasma and $P_\text{heating}$ is the heating power that reaches the plasma from outside. Both are in watts, so $Q$ has no unit.

<svg data-fig="power" viewBox="0 0 560 500" role="img" aria-label="Bar chart to scale, power in megawatts. First bar: 50 MW of heating power delivered into the plasma. Second bar: 500 MW of fusion power made in the plasma, divided into about 400 MW carried by neutrons, which leave the plasma and heat the blanket, and about 100 MW carried by helium nuclei, which stay in the plasma and heat it. Third bar: the electricity that the whole ITER plant draws from the grid, at least 110 MW, drawn solid, and up to 620 MW in peaks of 30 seconds, drawn as a pale range with a dashed outline." style="max-width:100%;font-size:26px">
  <line x1="64" y1="400" x2="545" y2="400" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="64" y1="298.5" x2="545" y2="298.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="7" y="283" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$200$</div></foreignObject>
  <line x1="64" y1="197" x2="545" y2="197" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="7" y="181.5" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$400$</div></foreignObject>
  <line x1="64" y1="95.5" x2="545" y2="95.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="7" y="80" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$600$</div></foreignObject>
  <foreignObject x="34" y="384.5" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$0$</div></foreignObject>
  <foreignObject x="8" y="10.5" width="80" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$P\ (\text{MW})$</div></foreignObject>
  <rect x="80" y="374.5" width="90" height="25.5" fill="#e8590c" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="107.5" y="337" width="35" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$50$</div></foreignObject>
  <rect x="215" y="146" width="130" height="50.5" fill="#c92a2a" stroke="#1f2933" stroke-width="2"/>
  <rect x="215" y="196.5" width="130" height="203.5" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="242" y="156" width="76" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#ffffff">$\alpha\text{: }100$</div></foreignObject>
  <foreignObject x="242" y="283" width="76" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#ffffff">$\text{n: }400$</div></foreignObject>
  <foreignObject x="255.5" y="108.5" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$500$</div></foreignObject>
  <rect x="395" y="85" width="130" height="259" fill="#b2f2bb" fill-opacity="0.45"/>
  <path d="M395,344 L395,85 L525,85 L525,344" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round" stroke-dasharray="6 5"/>
  <rect x="395" y="344" width="130" height="56" fill="#b2f2bb" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="435.5" y="356.5" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$110$</div></foreignObject>
  <foreignObject x="435.5" y="47.5" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$620$</div></foreignObject>
  <foreignObject x="422" y="199" width="76" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$\text{peaks}$</div></foreignObject>
  <foreignObject x="73.5" y="410.5" width="103" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$\text{heating}$</div></foreignObject>
  <foreignObject x="53.5" y="444.5" width="143" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$\text{into plasma}$</div></foreignObject>
  <foreignObject x="235.5" y="410.5" width="89" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$\text{fusion}$</div></foreignObject>
  <foreignObject x="222" y="444.5" width="116" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$\text{in plasma}$</div></foreignObject>
  <foreignObject x="429" y="410.5" width="62" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$\text{grid}$</div></foreignObject>
  <foreignObject x="368" y="444.5" width="184" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$\text{electricity in}$</div></foreignObject>
</svg>

**Gain is not electricity.** $Q$ describes the plasma only. ITER has no turbines and will not produce any electricity. During a pulse the whole plant (heating systems, cooling water, cryogenics, magnets) draws far more electricity than the $50\ \text{MW}$ that reaches the plasma. According to ITER, it needs $110\ \text{MW}$ at the least and up to $620\ \text{MW}$ in peaks of $30\ \text{s}$; the cooling water and the cryogenic systems take about $80\ \%$ of it. A power plant would turn the heat into electricity with steam turbines, typically about one third of it. Even then, $500\ \text{MW}$ of heat would give only about $170\ \text{MW}$ of electricity: far less than ITER's peak demand of $620\ \text{MW}$.

**Scientific gain is not commercial viability.** A power plant must also produce more electricity than the whole plant uses, run for months instead of minutes, breed its own tritium, survive years of neutron damage and sell its electricity at a price people will pay. ITER is built to test the physics and the technology for that, not to show that fusion electricity is cheap.

## Fuel, blankets and radiation {Fuel}

**Tritium fuel cycle.** Only a small fraction of the fuel, about one per cent according to ITER, fuses on its way through the plasma. Cryopumps pump the exhaust out of the vessel, and the tritium plant separates the hydrogen isotopes and sends deuterium and tritium back to the fuelling system. Tritium is radioactive (half-life $12.3$ years, a weak beta emitter), so detritiation systems take it out of air and water.

**Breeding.** Tritium is very rare; today it comes mainly from heavy-water fission reactors. A power plant must make its own from lithium: $^{6}_{3}\text{Li} + \text{n} \to {}^{4}_{2}\text{He} + {}^{3}_{1}\text{H} + 4.8\ \text{MeV}$. In ITER, a few **test blanket modules** will try out ways to do this.

**Radiation protection.** The fast neutrons make the vessel and the blanket radioactive (**activation**), so parts inside the vessel are changed by remote-handling robots. A thick concrete **bioshield** surrounds the machine. The fuel leaves no long-lived high-level waste, and the reaction stops by itself if anything fails, but tritium, activated parts, the strong magnets and the heat are real hazards. ITER obtained the licence of a French nuclear installation in 2012.

## Worked example

ITER's goal is a pulse with $P_\text{heating} = 50\ \text{MW}$ and $P_\text{fusion} = 500\ \text{MW}$. Calculate the fusion gain $Q$ and the power carried by the helium nuclei. Do the helium nuclei heat the plasma more than the external heating does?

<!-- vaihe -->

**Given:** heating power ${P_\text{heating} = 50\ \text{MW}}$, fusion power ${P_\text{fusion} = 500\ \text{MW}}$. In one $\text{D–T}$ reaction, ${E_\text{total} = 17.6\ \text{MeV}}$ is released and the helium nucleus carries ${E_\alpha = 3.5\ \text{MeV}}$. **Find:** $Q$ and the helium power $P_\alpha$.

<!-- vaihe -->

**Principle:** $Q$ is the ratio of the two powers. Every reaction gives the same share of its energy to the helium nucleus, so the helium nuclei carry the same share of the fusion power.

<!-- vaihe -->

**Formula:**
```latex
\begin{aligned}
Q &= \frac{P_\text{fusion}}{P_\text{heating}} \\
P_\alpha &= \frac{E_\alpha}{E_\text{total}} \cdot P_\text{fusion}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions:** None are needed. Both powers are in megawatts and both energies in megaelectronvolts, so the units cancel in each ratio.

<!-- vaihe -->

**Substitution:**
```latex
\begin{aligned}
Q &= \frac{500\ \text{MW}}{50\ \text{MW}} = 10 \\[6pt]
P_\alpha &= \frac{3.5\ \text{MeV}}{17.6\ \text{MeV}} \cdot 500\ \text{MW} \\
&= 0.1989 \cdot 500\ \text{MW} \\
&= 99.4\ \text{MW}
\end{aligned}
```

<!-- vaihe -->

**Answer:** $Q = 10$ and $P_\alpha \approx 99\ \text{MW}$, two significant figures as in $3.5\ \text{MeV}$. The helium nuclei heat the plasma with about $99\ \text{MW}$, about twice the external $50\ \text{MW}$: about two thirds of the heating comes from fusion itself.

<!-- vaihe -->

**Reasonableness:** The helium nucleus is about four times heavier than the neutron, so by conservation of momentum it gets about one fifth of the energy: one fifth of $500\ \text{MW}$ is $100\ \text{MW}$. The other, about $400\ \text{MW}$, leaves with the neutrons and heats the blanket. $Q = 10$ is far above JET's $0.67$, which is why ITER is so much larger.

## Common misconception

"$Q = 10$ means that ITER gives ten times more electricity than it uses." $Q$ compares two powers *in the plasma*: the fusion power and the heating that reaches the plasma. ITER produces no electricity at all, and the whole plant draws far more from the grid than the $50\ \text{MW}$ that reaches the plasma.

A second mistake is "the plasma is $150$ million degrees, so the machine must be extremely hot everywhere". The plasma is hundreds of thousands of times less dense than air, and the magnetic field holds it away from the walls. A few metres away, the magnets are at about $4\ \text{K}$.

## Summary

- ITER's superconducting magnets (toroidal field coils, poloidal field coils, central solenoid) hold and shape the plasma; the vacuum vessel, the blanket and the divertor surround it; beams and waves heat it.
- Fusion gain: $Q = P_\text{fusion} / P_\text{heating}$. $Q = 1$ is scientific breakeven; JET reached $0.67$ in 1997; ITER aims at $Q = 10$, $500\ \text{MW}$ from $50\ \text{MW}$.
- At $Q = 10$ the helium nuclei carry about $100\ \text{MW}$ and heat the plasma more than the external heating: a burning plasma.
- $Q$ is a plasma gain, not electricity. ITER produces no electricity, and a power plant needs much more than a high $Q$.
- Tritium is recycled in a closed loop and must later be bred from lithium; neutrons activate the structure, so ITER is a licensed nuclear installation.
