## Quick start

You get an LED to light in about five minutes without a program. Here the Arduino is only a power supply: its 5V pin has a voltage whenever the USB cable is connected. Always make connections with the USB cable unplugged.

1. Place the LED and the $330\,\Omega$ resistor on the breadboard as in the diagram below. The LED's long leg goes to the resistor's side.
2. Run a wire from the Arduino's 5V pin to the free end of the resistor and another wire from the GND pin to the column of the LED's short leg.
3. Plug the USB cable into a computer or a USB charger. The LED lights at once.

### Try

Build the circuit as in the diagram and get the LED to light.

### Modify

Add a second LED, first in series and then in parallel. In the parallel circuit every LED gets its own $330\,\Omega$ resistor. Compare in which circuit the LEDs shine brighter.

### Challenge yourself

Size the series resistor with Ohm's law and measure the current with a multimeter. Compare the measured current with your calculation.

## Challenge

You build your first own circuit: an LED, a series resistor and a voltage source. When the circuit works, you add a second LED first in series and then in parallel and find out why the LEDs shine with different brightness. The same circuit later becomes the indicator light of many Ahjo projects, and in lesson 9 you control it with a program.

The work takes one 75-minute lesson.

## Learning goals

After the work you can

- connect an LED and a series resistor the right way round on a breadboard
- explain why an LED needs a series resistor
- recognise series and parallel circuits and explain why every LED in a parallel circuit needs its own resistor
- calculate a series resistor from Ohm's law and measure the current with a multimeter.

## Starting level and prior skills

You do not need earlier electronics experience. Voltage, current and resistance are explained in the chapters [Circuit, electric current and voltage](fy6-1.html) and [Resistance and Ohm's law](fy6-3.html).

## Equipment and materials

Ahjo's equipment is still being acquired, so the models of the supplies will be specified later.

| Supply | Amount |
|---|---|
| Arduino Uno and USB cable | 1 |
| Breadboard | 1 |
| Red LED, diameter $5\,\text{mm}$ | 2 |
| Resistor $330\,\Omega$ (orange, orange, brown, gold) | 2 |
| Jumper wires (male–male) | 4–6 |
| Multimeter (Challenge yourself) | 1 |

## Safety and induction

Ahjo's safety instructions are still being prepared. See the topic [Soldering and electronics work](ahjo-turvallisuus.html#elektroniikka), and follow the teacher's induction.

The circuit only has the USB bus's $5\,\text{V}$, so there is no risk of electric shock. You can still break components:

- Make and change connections only when the USB cable is unplugged.
- Do not connect an LED without a series resistor. Too large a current burns the LED.
- Do not connect the 5V pin straight to the GND pin. That is a short circuit.
- If something gets hot or smells, unplug the USB cable at once and tell the teacher.

## Steps

1. Identify the LED's legs. The long leg is the anode and the short leg the cathode. On the cathode's side the LED's rim often has a flat spot.
2. Unplug the USB cable. Place the LED on the breadboard so that its legs are in different columns.
3. Place the resistor so that one of its ends is in the same column as the LED's long leg. A resistor has no direction.
4. Run a wire from the Arduino's 5V pin to the other end of the resistor and a wire from the GND pin to the column of the LED's short leg.
5. Check the circuit against the diagram and plug in the USB cable. The LED lights.
6. Series circuit. Unplug the USB cable. Add the second LED after the first so that the current flows through both one after the other. There is still one resistor. Plug in the USB cable and look at the brightness.
7. Parallel circuit. Unplug the USB cable. Build a second branch: its own $330\,\Omega$ resistor and its own LED between the 5V wire and the GND wire. Plug in the USB cable and compare the brightness with the series circuit.

## Diagrams and example code

In the first diagram the current flows from the 5V pin through the resistor and the LED to ground. No program is needed.

<svg data-fig="kytkenta"></svg>

In a series circuit the current has one path. In a parallel circuit each LED has its own branch and its own resistor.

<svg data-fig="sarja-rinnan"></svg>

Why do LEDs in parallel need their own resistors? The voltages of two LEDs are never exactly the same. If the branches shared one resistor, most of the current would flow through the LED with the smaller voltage. That LED would shine brightly and the other dimly, and at worst the first LED would be damaged.

## Test and measure

- Calculate the current of one LED. About $2{,}0\,\text{V}$ is left over a red LED, so $3{,}0\,\text{V}$ is left over the resistor:
  $$I = \frac{3{,}0\,\text{V}}{330\,\Omega} \approx 9{,}1\,\text{mA}.$$
- Over two LEDs in series there is about $4{,}0\,\text{V}$ altogether, so only about $1{,}0\,\text{V}$ is left over the resistor and the current is about $3\,\text{mA}$. That is why LEDs in series are dimmer.
- In the parallel circuit about $9\,\text{mA}$ flows in each branch, and about $18\,\text{mA}$ altogether is taken from the Arduino.
- Challenge yourself: measure the current by connecting the multimeter in series in place of the 5V wire. Choose the current range $\text{mA}$. The measuring method is explained in the chapter [Measurements in a circuit](fy6-2.html).

## If something does not work

| Symptom | Likely cause | Fix |
|---|---|---|
| The LED does not light | The LED is the wrong way round | Turn the LED: long leg to the resistor's side. |
| The LED does not light | A wire is in the wrong column | Compare every connection with the diagram. |
| LEDs in series do not light | The LEDs' voltage is too large | Use red LEDs. Blue and white LEDs need about $3\,\text{V}$, and two of them do not light in series from $5\,\text{V}$. |
| Only one of the LEDs in parallel lights | The branches share a resistor or one LED is the wrong way round | Give each branch its own resistor and check the LEDs' direction. |
| The Arduino's light is off | The USB cable gives no power | Try another cable or USB port. |

## Extension

1. Try how the size of the resistor affects the brightness. Replace the $330\,\Omega$ resistor with a $1\,\text{k}\Omega$ resistor and compare.
2. Add a push button between the LED and the resistor. Now the LED lights only while the button is pressed.
3. Move the 5V wire to pin 13 and continue in lesson 9 with the guide [First steps with Arduino](ahjo-arduino.html). Then a program decides when the LED lights.

## Document your work

Record in your project diary

- a photo of the circuit and your own drawing of the circuit diagram
- an observation: in which circuit the LEDs were brighter, and why
- Challenge yourself: your calculated and measured current and their difference
- one fault you ran into, and how you found it.

## For the teacher: preparation

- This is a draft: the guide has not yet been tried with Ahjo's own equipment. The board chosen is the Arduino Uno.
- Here the Arduino is only a $5\,\text{V}$ power supply. A power module on a USB charger or a 3 × AA battery holder can be used instead.
- Reserve red LEDs, as the series circuit does not work with blue or white LEDs from $5\,\text{V}$.
- Keep spare LEDs and resistors. Check that the fuses of the multimeters' current ranges are intact.
- The text, diagrams and calculations were written for Ruukkilabra.
