# Muuntajan tutkiminen

> **Tutkimuskysymys:** Miten muuntajan toisiojännite riippuu käämien kierroslukujen suhteesta, kuinka hyvin ideaalisen muuntajan malli kuvaa mittauksia, ja kuinka suuri on muuntajan hyötysuhde?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: laboratorion työpöydällä on muuntaja. Suljetun rautasydämen kummassakin pystyhaarassa on käämi. Vasemmanpuoleinen käämi on kytketty johtimilla virtalähteeseen ja kahteen yleismittariin, oikeanpuoleinen kahteen yleismittariin ja kuormitusvastukseen. Mittarien näytöt ovat tyhjiä. Pöydällä on lisäksi kaksi irrallista käämiä ja vihko." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy10mh-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef5f9"/><stop offset="1" stop-color="#dfe9ef"/></linearGradient><linearGradient id="fy10mh-desk" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy10mh-wall)"/>
  <rect x="0" y="470" width="1200" height="130" fill="url(#fy10mh-desk)"/>
  <line x1="0" y1="492" x2="1200" y2="488" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="514" x2="1200" y2="510" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="536" x2="1200" y2="532" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="558" x2="1200" y2="554" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="580" x2="1200" y2="576" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="470" x2="1200" y2="470" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="40" y="330" width="200" height="140" rx="10" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <rect x="60" y="350" width="100" height="44" rx="4" fill="#2b3a42" stroke="#1f2933" stroke-width="2"/>
  <circle cx="200" cy="372" r="16" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="90" cy="435" r="9" fill="#1f2933" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="190" cy="435" r="9" fill="#1f2933" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M120,435 q7.5,-14 15,0 t15,0" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="470" y="420" width="300" height="40" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="470" y="460" width="300" height="10" rx="2" fill="#495057" stroke="#1f2933" stroke-width="2"/>
  <rect x="495" y="240" width="50" height="180" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="695" y="240" width="50" height="180" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="470" y="200" width="300" height="40" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <line x1="472" y1="208" x2="768" y2="208" stroke="#8a96a3" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="472" y1="428" x2="768" y2="428" stroke="#8a96a3" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="472" y1="216" x2="768" y2="216" stroke="#8a96a3" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="472" y1="436" x2="768" y2="436" stroke="#8a96a3" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="472" y1="224" x2="768" y2="224" stroke="#8a96a3" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="472" y1="444" x2="768" y2="444" stroke="#8a96a3" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="472" y1="232" x2="768" y2="232" stroke="#8a96a3" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="472" y1="452" x2="768" y2="452" stroke="#8a96a3" stroke-width="1.2" stroke-linecap="butt"/>
  <rect x="600" y="196" width="40" height="48" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="470" y="258" width="100" height="12" rx="3" fill="#495057" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="470" y="400" width="100" height="12" rx="3" fill="#495057" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="480" y="270" width="80" height="130" fill="#b8622d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="482" y1="284.5" x2="558" y2="284.5" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="482" y1="299" x2="558" y2="299" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="482" y1="313.5" x2="558" y2="313.5" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="482" y1="328" x2="558" y2="328" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="482" y1="342" x2="558" y2="342" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="482" y1="356.5" x2="558" y2="356.5" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="482" y1="371" x2="558" y2="371" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="482" y1="385.5" x2="558" y2="385.5" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <rect x="670" y="258" width="100" height="12" rx="3" fill="#495057" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="670" y="400" width="100" height="12" rx="3" fill="#495057" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="680" y="270" width="80" height="130" fill="#b8622d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="682" y1="278.5" x2="758" y2="278.5" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="682" y1="287.5" x2="758" y2="287.5" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="682" y1="296" x2="758" y2="296" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="682" y1="304.5" x2="758" y2="304.5" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="682" y1="313.5" x2="758" y2="313.5" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="682" y1="322" x2="758" y2="322" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="682" y1="330.5" x2="758" y2="330.5" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="682" y1="339.5" x2="758" y2="339.5" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="682" y1="348" x2="758" y2="348" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="682" y1="356.5" x2="758" y2="356.5" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="682" y1="365.5" x2="758" y2="365.5" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="682" y1="374" x2="758" y2="374" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="682" y1="382.5" x2="758" y2="382.5" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="682" y1="391.5" x2="758" y2="391.5" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="492" cy="264" r="6" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="548" cy="264" r="6" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="692" cy="264" r="6" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="748" cy="264" r="6" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="270" y="380" width="90" height="90" rx="10" fill="#f4c542" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="282" y="392" width="66" height="30.5" rx="4" fill="#2b3a42" stroke="#1f2933" stroke-width="2"/>
  <circle cx="315" cy="439.5" r="11.7" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="315" y1="439.5" x2="315" y2="429.5" stroke="#ffffff" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="297" cy="458" r="5" fill="#1f2933"/>
  <circle cx="333" cy="458" r="5" fill="#1f2933"/>
  <rect x="370" y="380" width="90" height="90" rx="10" fill="#f4c542" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="382" y="392" width="66" height="30.5" rx="4" fill="#2b3a42" stroke="#1f2933" stroke-width="2"/>
  <circle cx="415" cy="439.5" r="11.7" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="415" y1="439.5" x2="415" y2="429.5" stroke="#ffffff" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="397" cy="458" r="5" fill="#1f2933"/>
  <circle cx="433" cy="458" r="5" fill="#1f2933"/>
  <rect x="790" y="380" width="90" height="90" rx="10" fill="#f4c542" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="802" y="392" width="66" height="30.5" rx="4" fill="#2b3a42" stroke="#1f2933" stroke-width="2"/>
  <circle cx="835" cy="439.5" r="11.7" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="835" y1="439.5" x2="835" y2="429.5" stroke="#ffffff" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="817" cy="458" r="5" fill="#1f2933"/>
  <circle cx="853" cy="458" r="5" fill="#1f2933"/>
  <rect x="890" y="380" width="90" height="90" rx="10" fill="#f4c542" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="902" y="392" width="66" height="30.5" rx="4" fill="#2b3a42" stroke="#1f2933" stroke-width="2"/>
  <circle cx="935" cy="439.5" r="11.7" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="935" y1="439.5" x2="935" y2="429.5" stroke="#ffffff" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="917" cy="458" r="5" fill="#1f2933"/>
  <circle cx="953" cy="458" r="5" fill="#1f2933"/>
  <rect x="1010" y="440" width="160" height="30" rx="5" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="1030" y="395" width="120" height="45" rx="18" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="1060" y1="397" x2="1060" y2="438" stroke="#a97a35" stroke-width="4" stroke-linecap="butt"/>
  <line x1="1080" y1="397" x2="1080" y2="438" stroke="#a97a35" stroke-width="4" stroke-linecap="butt"/>
  <line x1="1100" y1="397" x2="1100" y2="438" stroke="#a97a35" stroke-width="4" stroke-linecap="butt"/>
  <line x1="1120" y1="397" x2="1120" y2="438" stroke="#a97a35" stroke-width="4" stroke-linecap="butt"/>
  <circle cx="1025" cy="455" r="6" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="1155" cy="455" r="6" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M90,435 C90,365 297,388 297,458" fill="none" stroke="#1f2933" stroke-width="3.5" stroke-linejoin="round"/>
  <path d="M333,458 C333,198 492,4 492,264" fill="none" stroke="#1f2933" stroke-width="3.5" stroke-linejoin="round"/>
  <path d="M548,264 C548,-66 190,105 190,435" fill="none" stroke="#2b8a3e" stroke-width="3.5" stroke-linejoin="round"/>
  <path d="M397,458 C397,258 492,64 492,264" fill="none" stroke="#1f2933" stroke-width="3.5" stroke-linejoin="round"/>
  <path d="M433,458 C433,218 548,24 548,264" fill="none" stroke="#2b8a3e" stroke-width="3.5" stroke-linejoin="round"/>
  <path d="M748,264 C748,34 817,228 817,458" fill="none" stroke="#1f2933" stroke-width="3.5" stroke-linejoin="round"/>
  <path d="M853,458 C853,368 1025,365 1025,455" fill="none" stroke="#1f2933" stroke-width="3.5" stroke-linejoin="round"/>
  <path d="M1155,455 C1155,95 692,-96 692,264" fill="none" stroke="#2b8a3e" stroke-width="3.5" stroke-linejoin="round"/>
  <path d="M917,458 C917,208 692,14 692,264" fill="none" stroke="#2b8a3e" stroke-width="3.5" stroke-linejoin="round"/>
  <path d="M953,458 C953,258 748,64 748,264" fill="none" stroke="#1f2933" stroke-width="3.5" stroke-linejoin="round"/>
  <rect x="300" y="520" width="110" height="50" fill="#b8622d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="290" y="516" width="12" height="58" rx="3" fill="#495057" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="408" y="516" width="12" height="58" rx="3" fill="#495057" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="314" y1="522" x2="314" y2="568" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="327.5" y1="522" x2="327.5" y2="568" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="341" y1="522" x2="341" y2="568" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="355" y1="522" x2="355" y2="568" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="369" y1="522" x2="369" y2="568" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="382.5" y1="522" x2="382.5" y2="568" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="396" y1="522" x2="396" y2="568" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <rect x="450" y="520" width="110" height="50" fill="#b8622d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="440" y="516" width="12" height="58" rx="3" fill="#495057" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="558" y="516" width="12" height="58" rx="3" fill="#495057" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="458.5" y1="522" x2="458.5" y2="568" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="467" y1="522" x2="467" y2="568" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="475.5" y1="522" x2="475.5" y2="568" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="484" y1="522" x2="484" y2="568" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="492.5" y1="522" x2="492.5" y2="568" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="501" y1="522" x2="501" y2="568" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="509" y1="522" x2="509" y2="568" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="517.5" y1="522" x2="517.5" y2="568" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="526" y1="522" x2="526" y2="568" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="534.5" y1="522" x2="534.5" y2="568" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="543" y1="522" x2="543" y2="568" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <line x1="551.5" y1="522" x2="551.5" y2="568" stroke="#8a4a20" stroke-width="2" stroke-linecap="butt"/>
  <g transform="translate(1000,535) rotate(-5)"><rect x="-90" y="-36" width="190" height="66" rx="4" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/><line x1="-74" y1="-20" x2="84" y2="-20" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.6"/><line x1="-74" y1="-8" x2="84" y2="-8" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.6"/><line x1="-74" y1="4" x2="84" y2="4" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.6"/><line x1="-74" y1="16" x2="84" y2="16" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.6"/><line x1="-74" y1="28" x2="84" y2="28" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.6"/></g>
</svg>

Sähköverkon jakelumuuntajat, hitsauslaitteet ja monet sähkölaitteiden virtalähteet muuttavat vaihtojännitteen suuruutta muuntajalla. Muuntajassa ei ole liikkuvia osia, eikä sen kahden käämin välillä kulje sähkövirtaa, mutta silti energia siirtyy käämistä toiseen. Tässä tutkimuksessa kokoat muuntajan itse vaihdettavista käämeistä, mittaat sen jännitteet ja sähkövirrat ja vertaat tuloksia malliin. Mittaa, piirrä ja päättele itse: tämä sivu kertoo, mitä tutkitaan, ja tukee sinua niin paljon kuin valitsemasi työtapa lupaa.

## Tutkimustehtävä

**Selvitettävä:**

- miten toisiojännitteen ja ensiöjännitteen suhde riippuu käämien kierroslukujen suhteesta, kun toisiokäämin napoihin on kytketty vain jännitemittari (mittaukset usealla eri kierroslukujen suhteella)
- kuinka hyvin ideaalisen muuntajan malli kuvaa mittauksia, ja muuttuuko toisiojännite, kun toisiopiiriin kytketään kuormitusvastus (mittaus ainakin yhdellä käämiyhdistelmällä sekä ilman kuormaa että kuormitettuna)
- muuntajan hyötysuhde epävarmuuksineen ensiö- ja toisiopuolen sähkötehoista, ja mistä energiahäviöt johtuvat.

**Päätät itse** (osittain ohjattu ja itsenäinen työtapa): käytettävät käämiyhdistelmät ja niiden määrän opettajan hyväksymien joukosta, ensiöjännitteen opettajan antamissa rajoissa, mitä pidät vakiona ja kuinka monta kertaa toistat lukemat. Itsenäisessä työtavassa valitset lisäksi kuvaajan akselit perusteluineen ja tavan, jolla arvioit tulosten epävarmuuden. Ohjatussa työtavassa sivu kiinnittää nämä valinnat. Osittain ohjatussa työtavassa sivu antaa tueksi mallikuvaajan ja tavat arvioida epävarmuutta.

::: tuki I
**Itsenäinen työtapa.** Laajennus, hyötysuhteen mittaaminen eri kuormituksilla, kuuluu työhösi.
:::

## Ennusta

Kirjoita ennusteesi vihkoon tai työselostuksen hypoteesiksi ennen kuin luet eteenpäin ja ennen kuin mittaat:

1. Ensiökäämi ja ensiöjännite pysyvät samoina. Mitä toisiojännitteelle tapahtuu, kun toisiokäämin kierrosluku kaksinkertaistetaan? Entä jos ensiökäämin kierrosluku kaksinkertaistetaan ja toisiokäämi pysyy samana?
2. Muuttuuko toisiojännite, kun toisiokäämin napoihin kytketään pelkän jännitemittarin lisäksi kuormitusvastus? Jos muuttuu, mihin suuntaan?
3. Kuinka suuri osa ensiöpuolelle tuodusta sähkötehosta arvelet saatavan toisiopuolelta? Mihin loput energiasta joutuu?
4. Mikä mittauksessa on todennäköisesti suurin epävarmuuden lähde?

Perustele ennusteesi fysiikan avulla. Palaat siihen johtopäätöksissä.

## Teoriaa lyhyesti

**Muuntajan rakenne.** Muuntajassa on kaksi käämiä yhteisen rautasydämen ympärillä. **Ensiökäämi** kytketään vaihtojännitelähteeseen ja **toisiokäämi** kuormaan, esimerkiksi vastukseen. Käämit eivät ole sähköisesti yhteydessä toisiinsa: energia siirtyy niiden välillä magneettikentän välityksellä. Käämin kierrosluku $N$ kertoo, kuinka monta kertaa johdin kiertää sydämen ympäri.

**Induktio lyhyesti.** Kun ensiökäämissä kulkee vaihtovirta, se synnyttää rautasydämeen magneettikentän, jonka suuruus ja suunta muuttuvat jatkuvasti. Rautasydän ohjaa kentän kulkemaan myös toisiokäämin läpi. Kierroksen läpi kulkevaa magneettikentän "määrää" kutsutaan **magneettivuoksi**. Kun magneettivuo muuttuu, johdinkierrokseen syntyy eli **indusoituu** jännite, joka on sitä suurempi, mitä nopeammin vuo muuttuu. Käämin kierrokset ovat peräkkäin eli sarjassa, joten niiden jännitteet laskevat yhteen. Sama tapahtuu myös ensiökäämissä itsessään: sen omiin kierroksiin indusoituva jännite vastustaa sähkövirran muutosta. Tasajännitteellä muuntaja ei toimi, koska muuttumaton magneettikenttä ei indusoi jännitettä. Induktiota ja muuntajaa käsitellään tarkemmin moduulissa FY7.

**Ideaalinen muuntaja** on malli, jossa

- kaikki magneettivuo kulkee rautasydämessä, eli sama vuo kulkee molempien käämien jokaisen kierroksen läpi
- käämien johtimilla ei ole resistanssia
- rautasydämessä ei synny energiahäviöitä.

Todellinen muuntaja ei täytä näitä ehtoja täsmälleen. Tässä työssä selvität, kuinka paljon se poikkeaa mallista.

**Vaihtojännite ja tehollinen arvo.** Vaihtojännite ja vaihtovirta muuttavat suuntaansa ja suuruuttaan jatkuvasti. Vaihtosuureiden mittari näyttää **tehollisen arvon**: se on valittu niin, että vastuksen keskimääräinen teho on $P = UI$, kun $U$ ja $I$ ovat tehollisia arvoja. Kytke siis yleismittari vaihtojännitteen ja vaihtovirran asetukselle.

**Sähköteho ja hyötysuhde.** Vastuksen teho on sen napojen välisen jännitteen ja vastuksen läpi kulkevan sähkövirran tulo, $P = UI$. Sama pätee muihinkin laitteisiin silloin, kun jännite ja sähkövirta vaihtelevat samassa tahdissa. Jännitteen yksikkö on voltti ($\text{V}$), sähkövirran ampeeri ($\text{A}$) ja tehon watti: $1\ \text{V} \cdot 1\ \text{A} = 1\ \text{W}$. Sähkötehoa käsitellään tarkemmin moduulissa FY6. [[apua:fy2-3|Teho]] Muuntajan **hyötysuhde** on toisiopuolelta saatavan tehon $P_2$ ja ensiöpuolelle tuodun tehon $P_1$ suhde:

```latex
\eta = \frac{P_2}{P_1}
```

[[apua:fy2-4|Hyötysuhde]] Kuormitusvastukselle teho on $P_2 = U_2 I_2$. Ensiökäämille tulo $U_1 I_1$ ei kuitenkaan ole aivan sama kuin käämiin tuleva teho: osa ensiövirrasta vain magnetoi rautasydäntä, ja sen kuljettama energia palaa jännitelähteeseen saman jakson aikana. Siksi $U_1 I_1$ on vähintään yhtä suuri kuin ensiöpuolelle todella tuleva teho. Kun lasket hyötysuhteen tulosta $\eta = \dfrac{U_2 I_2}{U_1 I_1}$, saat arvon, joka ei ole todellista hyötysuhdetta suurempi.

**Mittarien kytkeminen.** Virtamittari kytketään **sarjaan** sen käämin tai vastuksen kanssa, jonka läpi kulkeva sähkövirta mitataan. Jännitemittari kytketään **rinnan** käämin kanssa, sen kahden navan väliin. Virtamittaria ei koskaan kytketä yksin käämin napoihin, sillä se oikosulkisi käämin.

<svg data-fig="setup" viewBox="0 0 600 380" role="img" aria-label="Kaaviokuva. Suljetun rautasydämen vasemmassa haarassa on ensiökäämi, jossa on N yksi kierrosta, ja oikeassa haarassa toisiokäämi, jossa on N kaksi kierrosta. Ensiökäämi on kytketty vaihtojännitelähteeseen. Ensiöpiirissä virtamittari on sarjassa käämin kanssa ja mittaa sähkövirran I yksi, ja jännitemittari on kytketty käämin napoihin ja mittaa jännitteen U yksi. Toisiopiirissä virtamittari on sarjassa kuormitusvastuksen R kanssa ja mittaa sähkövirran I kaksi, ja jännitemittari on kytketty toisiokäämin napoihin ja mittaa jännitteen U kaksi." style="max-width:100%;font-size:24px">
  <rect x="210" y="90" width="180" height="210" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="240" y="120" width="120" height="150" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="244" y="52" width="112" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#6b7480">$\text{rautasydän}$</div></foreignObject>
  <line x1="202" y1="150" x2="248" y2="140" stroke="#b8622d" stroke-width="3.5" stroke-linecap="round"/>
  <line x1="202" y1="166.5" x2="248" y2="156.5" stroke="#b8622d" stroke-width="3.5" stroke-linecap="round"/>
  <line x1="202" y1="183.5" x2="248" y2="173.5" stroke="#b8622d" stroke-width="3.5" stroke-linecap="round"/>
  <line x1="202" y1="200" x2="248" y2="190" stroke="#b8622d" stroke-width="3.5" stroke-linecap="round"/>
  <line x1="202" y1="216.5" x2="248" y2="206.5" stroke="#b8622d" stroke-width="3.5" stroke-linecap="round"/>
  <line x1="202" y1="233.5" x2="248" y2="223.5" stroke="#b8622d" stroke-width="3.5" stroke-linecap="round"/>
  <line x1="202" y1="250" x2="248" y2="240" stroke="#b8622d" stroke-width="3.5" stroke-linecap="round"/>
  <line x1="352" y1="145" x2="398" y2="135" stroke="#b8622d" stroke-width="3.5" stroke-linecap="round"/>
  <line x1="352" y1="156" x2="398" y2="146" stroke="#b8622d" stroke-width="3.5" stroke-linecap="round"/>
  <line x1="352" y1="167" x2="398" y2="157" stroke="#b8622d" stroke-width="3.5" stroke-linecap="round"/>
  <line x1="352" y1="178" x2="398" y2="168" stroke="#b8622d" stroke-width="3.5" stroke-linecap="round"/>
  <line x1="352" y1="189" x2="398" y2="179" stroke="#b8622d" stroke-width="3.5" stroke-linecap="round"/>
  <line x1="352" y1="200" x2="398" y2="190" stroke="#b8622d" stroke-width="3.5" stroke-linecap="round"/>
  <line x1="352" y1="211" x2="398" y2="201" stroke="#b8622d" stroke-width="3.5" stroke-linecap="round"/>
  <line x1="352" y1="222" x2="398" y2="212" stroke="#b8622d" stroke-width="3.5" stroke-linecap="round"/>
  <line x1="352" y1="233" x2="398" y2="223" stroke="#b8622d" stroke-width="3.5" stroke-linecap="round"/>
  <line x1="352" y1="244" x2="398" y2="234" stroke="#b8622d" stroke-width="3.5" stroke-linecap="round"/>
  <line x1="352" y1="255" x2="398" y2="245" stroke="#b8622d" stroke-width="3.5" stroke-linecap="round"/>
  <line x1="202" y1="140" x2="60" y2="140" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="60" y1="140" x2="60" y2="171" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="202" y1="250" x2="60" y2="250" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="60" y1="250" x2="60" y2="219" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="202" y1="140" x2="202" y2="150" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="202" y1="240" x2="202" y2="250" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="60" cy="195" r="24" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="50" y="180.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\sim$</div></foreignObject>
  <circle cx="110" cy="140" r="20" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="100.5" y="127" width="19" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:22px">$\mathrm{A}$</div></foreignObject>
  <foreignObject x="93.5" y="89.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$I_1$</div></foreignObject>
  <circle cx="170" cy="140" r="5" fill="#1f2933"/>
  <circle cx="170" cy="250" r="5" fill="#1f2933"/>
  <line x1="170" y1="140" x2="170" y2="175" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="170" y1="215" x2="170" y2="250" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="170" cy="195" r="20" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="160.5" y="182" width="19" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:22px">$\mathrm{V}$</div></foreignObject>
  <foreignObject x="109" y="180.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$U_1$</div></foreignObject>
  <line x1="398" y1="140" x2="550" y2="140" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="550" y1="140" x2="550" y2="165" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="398" y1="250" x2="550" y2="250" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="550" y1="250" x2="550" y2="225" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="398" y1="140" x2="398" y2="145" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="398" y1="245" x2="398" y2="250" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <rect x="540" y="165" width="20" height="60" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="568" y="180.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$R$</div></foreignObject>
  <circle cx="490" cy="140" r="20" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="480.5" y="127" width="19" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:22px">$\mathrm{A}$</div></foreignObject>
  <foreignObject x="473.5" y="89.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$I_2$</div></foreignObject>
  <circle cx="430" cy="140" r="5" fill="#1f2933"/>
  <circle cx="430" cy="250" r="5" fill="#1f2933"/>
  <line x1="430" y1="140" x2="430" y2="175" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="430" y1="215" x2="430" y2="250" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="430" cy="195" r="20" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="420.5" y="182" width="19" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:22px">$\mathrm{V}$</div></foreignObject>
  <foreignObject x="458" y="180.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U_2$</div></foreignObject>
  <foreignObject x="208.5" y="307.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$N_1$</div></foreignObject>
  <foreignObject x="358.5" y="307.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$N_2$</div></foreignObject>
  <foreignObject x="166" y="342" width="112" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#6b7480">$\text{ensiökäämi}$</div></foreignObject>
  <foreignObject x="317" y="342" width="122" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#6b7480">$\text{toisiokäämi}$</div></foreignObject>
</svg>

## Tutkimuskysymyksestä mitattaviksi suureiksi

Ennen kuin luet eteenpäin, kirjaa:

1. Mitä ideaalisen muuntajan malli ennustaa: miten toisiojännite $U_2$ riippuu ensiöjännitteestä $U_1$ ja kierrosluvuista $N_1$ ja $N_2$? Perustele yllä olevien periaatteiden avulla.
2. Millaisen kuvaajan piirrät, jotta mallin ennuste näkyy suorana? Mikä sen kulmakertoimen pitäisi olla, jos malli pätee?
3. Mitä muutat, mitä mittaat jokaisella käämiyhdistelmällä ja mitä pidät vakiona?
4. Mitkä suureet mittaat hyötysuhdetta varten, ja mitkä niistä on luettava samaan aikaan?

::: tuki O OO
Tarkista kirjauksesi tästä. Ideaalisessa muuntajassa sama magneettivuo kulkee jokaisen kierroksen läpi, joten jokaiseen kierrokseen indusoituu yhtä suuri jännite kummassakin käämissä. Toisiokäämin jännite on silloin $N_2$ kertaa yhden kierroksen jännite. Ensiökäämiin indusoituva jännite on vastaavasti $N_1$ kertaa sama kierroksen jännite, ja koska käämin johtimella ei mallissa ole resistanssia, se on yhtä suuri kuin käämiin kytketty jännite $U_1$. Yhden kierroksen jännite on siis $\dfrac{U_1}{N_1} = \dfrac{U_2}{N_2}$, eli

```latex
\frac{U_2}{U_1} = \frac{N_2}{N_1}
```

Jännitteiden suhde on mallin mukaan sama kuin kierroslukujen suhde. Kuvaaja, jossa pystyakselilla on $\dfrac{U_2}{U_1}$ ja vaaka-akselilla $\dfrac{N_2}{N_1}$, on silloin origon kautta kulkeva suora, jonka kulmakerroin on $1$. Koska akseleilla on suhteita, pienet ensiöjännitteen vaihtelut mittausten välillä eivät hajota pisteitä.

<svg data-fig="model" viewBox="0 0 600 330" role="img" aria-label="Kuvaaja: jännitteiden suhde U kaksi per U yksi kierroslukujen suhteen N kaksi per N yksi funktiona ideaalisen muuntajan mallin mukaan. Akseleilla on sama mittakaava, ja kummallekin on merkitty arvot yksi ja kaksi. Kuvaaja on origon kautta kulkeva suora, jonka kulmakerroin on yksi. Kuvaajassa ei ole mittauspisteitä." style="max-width:100%;font-size:24px">
  <line x1="182" y1="280" x2="182" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="274" y1="280" x2="274" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="188" x2="320" y2="188" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="96" x2="320" y2="96" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="89" y1="280" x2="334" y2="280" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M346,280 L333,286 L333,274 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="281" x2="90" y2="36" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,24 L96,37 L84,37 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="182" y1="280" x2="182" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="172" y="289.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="274" y1="280" x2="274" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="264" y="289.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="83" y1="188" x2="90" y2="188" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="173.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="83" y1="96" x2="90" y2="96" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="81.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <foreignObject x="60" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="352" y="265.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$N_2/N_1$</div></foreignObject>
  <foreignObject x="80" y="-6.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U_2/U_1$</div></foreignObject>
  <polyline points="90,280 311,59" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="228" y="182.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{kulmakerroin } 1$</span></div></foreignObject>
</svg>

Hyötysuhdetta varten tarvitset samalla käämiyhdistelmällä ja samalla kuormalla ensiöjännitteen $U_1$, ensiövirran $I_1$, toisiojännitteen $U_2$ ja toisiovirran $I_2$, kaikki luettuina samaan aikaan, koska ne voivat muuttua, kun kuormitusta muutetaan. Mallin ehdot eivät ole itsestään selviä, ja mittaus näyttää, pysyvätkö pisteet mallin suoralla.
:::

## Suunnittele

Ennen mittaamista päätä ja kirjaa ylös, mitä muutat, mitä mittaat ja mitä pidät vakiona. Piirrä kytkentäkaavio ja näytä kytkentä opettajalle ennen kuin kytket virran.

::: tuki O
**Ohjattu.** Kokoa muuntaja niin, että rautasydän on suljettu. Tee mittaukset kahdessa osassa.

- **Osa A, jännitteiden suhde.** Kytke toisiokäämin napoihin vain jännitemittari. Kytke ensiökäämiin opettajan ilmoittama jännite ja mittaa ensiöjännite $U_1$ ja toisiojännite $U_2$. Toista mittaus kaikilla opettajan hyväksymillä käämiyhdistelmillä, ja vaihda myös käämien rooleja niin, että sama käämi on vuorollaan ensiö- ja toisiokäämi. Tavoite on vähintään viisi eri kierroslukujen suhdetta, sekä ykköstä pienempiä että suurempia. Kirjaa jokaisella kerralla molemmat kierrosluvut. Lue kullakin yhdistelmällä lukemat kerran: toistoja ei tarvita, koska kuvaajan useat pisteet tasoittavat yksittäisten lukemien satunnaisia virheitä.
- **Osa B, hyötysuhde.** Valitse opettajan neuvoma käämiyhdistelmä. Mittaa ensin toisiojännite ilman kuormaa. Kytke sitten toisiopiiriin kuormitusvastus ja sen kanssa sarjaan virtamittari sekä ensiöpiiriin virtamittari. Lue kaikki neljä mittaria $U_1$, $I_1$, $U_2$ ja $I_2$ samalla kuormituksella. Katkaise virta, kytke se uudelleen ja lue lukemat vielä kahdesti, niin että saat kolme lukemasarjaa.

Pidä sähkövirrat opettajan ilmoittamien rajojen alapuolella.
:::

::: tuki OO
**Osittain ohjattu.** Päätä itse, mitä käämiyhdistelmiä käytät ja kuinka monta, millä ensiöjännitteellä mittaat ja montako kertaa toistat lukemat. Hyötysuhdetta varten tarvitset kuormitusvastuksen ja virtamittarin kumpaankin piiriin. Kirjaa päätöksesi perusteluineen.
:::

::: tuki O OO
Mieti ainakin näitä:

- Pysyykö ensiöjännite samana, kun vaihdat käämejä? Kannattaako se mitata joka kerta vai luottaa virtalähteen asetukseen?
- Miten saat samoista käämeistä sekä ykköstä pienempiä että suurempia kierroslukujen suhteita?
- Mitä tapahtuu, jos rautasydän ei ole kunnolla suljettu, esimerkiksi jos sen osien väliin jää rako?
:::

## Mittaa

Kirjaa alkuperäiset mittaustulokset taulukkoon heti mittauksen aikana. Laskemasi suureet saavat omat sarakkeensa mitattujen oikealle puolelle. Mittaa toisiojännite jokaisella käämiyhdistelmällä ilman kuormaa, ja ainakin yhdellä yhdistelmällä myös kuormitettuna.

::: tuki O
Voit käyttää esimerkiksi tällaisia taulukoita:

**Osa A.**

| $N_1$ | $N_2$ | $U_1\ (\text{V})$ | $U_2\ (\text{V})$ | $N_2/N_1$ | $U_2/U_1$ |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |

**Osa B.** Kirjaa taulukon yläpuolelle käämien kierrosluvut ja toisiojännite ilman kuormaa.

| $U_1\ (\text{V})$ | $I_1\ (\text{A})$ | $U_2\ (\text{V})$ | $I_2\ (\text{A})$ | $P_1 = U_1 I_1\ (\text{W})$ | $P_2 = U_2 I_2\ (\text{W})$ | $\eta = P_2/P_1$ |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |

Jos mittarissa on usea mittausalue, aloita suurimmalta ja vaihda pienemmälle vasta, kun tiedät, että lukema mahtuu siihen.
:::

Muista mittausepävarmuus: selvitä mittarien tarkkuus mittarin ohjeesta tai opettajalta, ja kirjaa se taulukkoon. Kirjaa myös, ovatko käämeihin merkityt kierrosluvut tarkkoja vai likimääräisiä, jos tieto on saatavilla. [[apua:fy1-3|Mittausepävarmuuden arvioiminen]]

## Käsittele tulokset

Piirrä jännitteiden mittaustuloksista kuvaaja, jonka avulla voit verrata mittauksia ideaalisen muuntajan malliin. Merkitse akseleille suureet ja yksiköt, jos niillä on yksikkö. Piirrä mittauspisteet, älä yhdistä niitä murtoviivalla, ja sovita pisteisiin mallin mukainen käyrä (suora, jos valitsit akselit niin, että malli on suora). [[apua:fy1-4|Suoran sovittaminen ja kulmakertoimen tulkinta]]

::: tuki O
Valitse pystyakselille jännitteiden suhde $U_2/U_1$ ja vaaka-akselille kierroslukujen suhde $N_2/N_1$.
:::

Kirjoita sovitetun suoran yhtälö ja vastaa:

1. Miksi valitsit juuri nämä akselit? Mitä mallin mukaan pitäisi näkyä kuvaajassa?
2. Ovatko pisteet suoralla koko mittausalueella? Jos eivät, millä kierroslukujen suhteilla ne poikkeavat?
3. Mikä on suoran kulmakerroin, ja poikkeaako se mallin arvosta enemmän kuin epävarmuus selittää? Kulkeeko suora origon kautta?
4. Muuttuiko toisiojännite, kun kytkit kuormitusvastuksen? Jos muuttui, kuinka paljon, suhteessa mittarin tarkkuuteen?
5. Laske hyötysuhde $\eta = \dfrac{U_2 I_2}{U_1 I_1}$ jokaisesta lukemasarjasta ja niiden keskiarvo $\bar{\eta}$.

::: tuki O OO
Tarkista vastauksesi tästä.

**Miksi juuri nämä akselit?** Kun pystyakselilla on $U_2/U_1$ ja vaaka-akselilla $N_2/N_1$, ideaalisen muuntajan malli on suora $y = x$. Silloin mallin testaaminen on yksinkertaista: kulmakertoimen pitäisi olla $1$ ja suoran kulkea origon kautta. Jos piirtäisit pelkän toisiojännitteen $U_2$ kierroslukujen suhteen funktiona, kulmakerroin olisi ensiöjännite, ja vaihteleva ensiöjännite hajottaisi pisteitä.
:::

Kuvaajan sovitukseen voit käyttää esimerkiksi Graphical Analysis -ohjelmaa tai taulukkolaskentaa. Ruukkilabran ohjeet: [[ohje:tvt-suoran-sovitus|Suoran sovittaminen]], [[ohje:tvt-kulmakerroin|Kulmakertoimen tulkinta]] ja [[ohje:tvt-taulukkolaskenta|Taulukkolaskenta]].

## Epävarmuus ja luotettavuus

Ilmoita kuvaajan kulmakerroin muodossa $a \pm \Delta a$ ja hyötysuhde muodossa $\eta \pm \Delta\eta$, ja perustele, miten arvioit epävarmuudet.

::: tuki O OO
**Kulmakertoimen epävarmuuden** $\Delta a$ voit arvioida jommallakummalla tavalla:

- **Sovitusohjelman keskivirhe.** Monet ohjelmat ilmoittavat kulmakertoimen keskivirheen. Käytä sitä epävarmuutena $\Delta a$.
- **Jyrkin ja loivin suora.** Piirrä jyrkin ja loivin suora, jotka vielä sopivat pisteisiin niiden epävarmuuksien rajoissa. Määritä niiden kulmakertoimet $a_\text{max}$ ja $a_\text{min}$ ja arvioi epävarmuus vaihteluvälin puolikkaana: $\Delta a = \dfrac{a_\text{max} - a_\text{min}}{2}$.

Yksittäisen pisteen epävarmuuden pystysuunnassa saat jännitemittarien tarkkuudesta: osamäärän suhteellinen epävarmuus on osoittajan ja nimittäjän suhteellisten epävarmuuksien summa, $\dfrac{\Delta(U_2/U_1)}{U_2/U_1} \approx \dfrac{\Delta U_1}{U_1} + \dfrac{\Delta U_2}{U_2}$.

**Hyötysuhteen epävarmuus.** Hyötysuhde lasketaan neljän lukeman tulosta ja osamäärästä, joten sen suhteellinen epävarmuus on niiden suhteellisten epävarmuuksien summa:

```latex
\begin{aligned}
\frac{\Delta \eta}{\eta} \approx {} & \frac{\Delta U_1}{U_1} + \frac{\Delta I_1}{I_1} \\
& + \frac{\Delta U_2}{U_2} + \frac{\Delta I_2}{I_2}
\end{aligned}
```

Vertaa tätä lukemasarjojen hajontaan (esimerkiksi puolet suurimman ja pienimmän arvon erotuksesta), ja käytä epävarmuutena suurempaa. Muista lisäksi, että tulo $U_1 I_1$ on vähintään yhtä suuri kuin ensiöpuolelle todella tuleva teho: tämä systemaattinen virhe voi vain pienentää laskemaasi hyötysuhdetta, ei kasvattaa sitä.

Pyöristä epävarmuus yhteen merkitsevään numeroon ja tulos samaan desimaaliin.
:::

Pohdi sitten luotettavuutta konkreettisesti: mitkä olivat suurimmat epävarmuuden lähteet, olivatko ne satunnaisia vai systemaattisia, ja mihin suuntaan ne olisivat muuttaneet tuloksia? Miten parantaisit mittausta?

## Johtopäätökset

Vastaa tutkimuskysymykseen mittaustesi perusteella. Viittaa kuvaajaan, esimerkiksi "kuvaajasta 1 nähdään, että …", ja vastaa ainakin näihin:

- Kuinka hyvin ideaalisen muuntajan malli kuvaa mittauksiasi? Mikä mallin ehdoista täyttyi todennäköisesti huonoiten, ja mihin mittaustulokseen perustat päätelmäsi?
- Mistä muuntajan energiahäviöt johtuvat? Perustele sillä, mitä mittasit, esimerkiksi hyötysuhteella ja toisiojännitteen muutoksella kuormitettaessa.
- Mitä hyötysuhteesi kertoo juuri tästä muuntajasta ja tästä kuormituksesta, ja mitä se ei kerro muuntajista yleensä?

Vertaa tuloksia ennusteisiisi: mikä osui oikeaan ja mikä ei?

::: tuki O OO
Tarkista vastauksesi tästä, kun olet kirjoittanut ne.

**Jos tulos poikkeaa mallista.** Mieti, mikä ideaalisen mallin ehdoista ei täyty. Jos osa magneettivuosta kulkee ilmassa eikä toisiokäämin läpi, toisiokäämiin indusoituu vähemmän jännitettä kuin malli ennustaa. Ensiökäämin johtimen resistanssi vie osan ensiöjännitteestä, joten käämiin indusoituva jännite on hieman pienempi kuin $U_1$. Kun toisiopiirissä kulkee sähkövirta, myös toisiokäämin oma resistanssi vie osan indusoituneesta jännitteestä ennen kuin se ehtii kuormaan.

**Mihin energia häviää?** Käämien johtimet lämpenevät, kun niissä kulkee sähkövirta. Rautasydämeen indusoituu pyörrevirtoja, jotka lämmittävät sitä, ja sydämen magnetoinnin suunnan jatkuva kääntäminen kuluttaa energiaa.
:::

## Raportoi

Kirjoita työstä työselostus FY10:n työselostuspohjalla (kuvaajista ja tuloksista ohje [[ohje:tvt-tyoselostus|Kuvaajat ja tulokset työselostukseen]]) ja käy läpi sen kaikki osat. Tässä tutkimuksessa erityisen tärkeitä ovat nämä:

- **Tausta ja teoria:** ideaalisen muuntajan malli ja sen ehdot, miksi kuvaajan akselit valittiin niin kuin valittiin, sekä miten hyötysuhde lasketaan.
- **Koejärjestely ja menetelmä:** kytkentäkaavio, jossa näkyy, miten mittarit on kytketty kumpaankin piiriin, sekä työturvallisuus.
- **Mittaustulokset:** kierrosluvut ja alkuperäiset lukemat omissa sarakkeissaan ja lasketut suhteet ja tehot niiden oikealla puolella.
- **Tulos:** kulmakerroin $a \pm \Delta a$ ja hyötysuhde $\eta \pm \Delta\eta$ oikein pyöristettyinä, sekä kuormituksen vaikutus toisiojännitteeseen.
- **Luotettavuus:** konkreettiset epävarmuuden lähteet ja niiden vaikutuksen suunta, myös se, miksi tulosta $U_1 I_1$ käyttämällä saatu hyötysuhde ei voi olla todellista suurempi.

## Laajennus: hyötysuhde eri kuormituksilla

Muuntajan hyötysuhde ei välttämättä ole sama kaikilla kuormituksilla. Tutki samalla käämiyhdistelmällä, miten hyötysuhde riippuu siitä, kuinka paljon tehoa toisiopuolelta otetaan: vaihda kuormitusvastusta opettajan antamien vastusten joukosta ja määritä jokaisella kuormalla $U_1$, $I_1$, $U_2$ ja $I_2$. Pidä sähkövirrat koko ajan opettajan ilmoittamien rajojen alapuolella.

Piirrä hyötysuhde toisiopuolen tehon $P_2$ funktiona ja vastaa:

1. Millä kuormituksella hyötysuhde oli suurin ja millä pienin?
2. Miten toisiojännite muuttui, kun toisiovirta kasvoi?
3. Miten selität havaitsemasi muutokset muuntajan energiahäviöillä?

::: tuki O OO
**Vihjeitä.** Muuta vain kuormaa: pidä käämiyhdistelmä ja virtalähteen asetus samoina, ja anna käämien jäähtyä mittausten välillä, jos ne lämpenevät. Mieti vastatessasi, mitkä häviöt ovat suunnilleen samat kuormasta riippumatta (rautasydämen magnetointi) ja mitkä kasvavat sähkövirran kasvaessa (käämien johtimien lämpeneminen). Muista myös, että tulo $U_1 I_1$ yliarvioi ensiöpuolen tehoa eniten silloin, kun kuormitus on pieni.
:::

## Arvioi omaa työtäsi

Arvioi työtäsi työselostuspohjan muistilistalla ja vastaa lisäksi:

- Pystyisikö toinen ryhmä toistamaan mittauksesi kuvauksesi perusteella?
- Perustuuko johtopäätöksesi kuvaajaan ja mittaustuloksiin vai siihen, mitä odotit?
- Mitä tekisit toisin, jos aloittaisit alusta?

**Sovella:** Sähköenergia siirretään voimalaitoksilta pitkiä matkoja suurjännitteellä, ja muuntajat laskevat jännitteen ennen kuin sähkö tulee koteihin. Pohdi tehon $P = UI$ avulla, miksi sama teho kannattaa siirtää suurella jännitteellä: miten se vaikuttaa siirtojohtojen sähkövirtaan ja johtojen lämpenemiseen? Pohdi tätä ajatuksen tasolla: verkkojännitteeseen kytkettyjä laitteita ja muuntajia ei tutkita itse.
