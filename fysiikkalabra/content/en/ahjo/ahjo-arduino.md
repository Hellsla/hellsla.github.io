## Challenge

Make an LED blink with an Arduino and know why it blinks. You connect an LED and a series resistor on a breadboard, size the resistor yourself, write the program and finally measure whether the current in the circuit is the one you calculated. The finished circuit is a first building block for many Ahjo projects: the same connection later drives indicator lights, buzzers and motor drivers.

The work takes about 75 minutes. The extension needs a second session.

## Learning goals

After this work you can

- connect an LED and a series resistor the right way round on a breadboard and explain why the board's columns join the components
- calculate the series resistance from Ohm's law and choose the nearest suitable standard value
- write, save and upload an Arduino program with `setup()`, `loop()`, `pinMode()`, `digitalWrite()` and `delay()`
- measure the current with a multimeter and compare the measurement with the calculated value
- find a fault systematically, one symptom at a time.

## Starting level and prior skills

You do not need any programming experience. You should know what voltage, current and resistance mean. If needed, revise the chapters [Circuit, electric current and voltage](fy6-1.html) and [Resistance and Ohm's law](fy6-3.html). The LED is explained in more detail in the chapter [Semiconductors, the diode, the LED and the solar cell](fy6-14.html).

## Equipment and materials

Ahjo's starter kits use the Arduino Uno board. The equipment is still being acquired, so the models of the other items will be confirmed later.

| Item | Quantity |
|---|---|
| Arduino Uno and USB cable | 1 |
| Breadboard (at least half size) | 1 |
| Red LED, diameter $5\,\text{mm}$ | 1 |
| Resistor $330\,\Omega$ (colour bands orange, orange, brown, gold) | 1 |
| Jumper wires (male–male) | 2–4 |
| Multimeter | 1 |
| Push button and a second LED (extension) | 1 + 1 |
| Computer with the Arduino IDE | 1 |

## Safety and induction

Ahjo's safety instructions are still being prepared. See the topic [Soldering and electronics work](ahjo-turvallisuus.html#elektroniikka) and follow your teacher's induction.

This work uses only the $5\,\text{V}$ of the USB connection, so there is no risk of electric shock. You can still damage the devices:

- Make and change connections only when the USB cable is unplugged.
- Never connect an LED without a series resistor. Too large a current burns the LED and can damage the board's pin.
- Never connect the $5\,\text{V}$ or $3.3\,\text{V}$ pin directly to a GND pin. That is a short circuit.
- If a component gets hot or smells, unplug the USB cable at once and tell your teacher.

Mains electricity safety is covered in the chapter [Electrical safety at home and at work](fy6-15.html).

## Steps

1. Size the series resistor before you connect anything. In the HIGH state the Arduino pin gives the voltage $U = 5.0\,\text{V}$. About $U_\text{LED} = 2.0\,\text{V}$ is left across a red LED, and a suitable current is $I = 10\,\text{mA}$. The rest of the voltage is across the resistor, so
   $$\begin{aligned}&R = \frac{U - U_\text{LED}}{I}\\ &= \frac{5.0\,\text{V} - 2.0\,\text{V}}{0.010\,\text{A}}\\ &= 300\,\Omega.\end{aligned}$$
   The nearest common standard value that is not smaller is $330\,\Omega$. A larger resistance makes the current smaller, so the LED is safe.
2. Calculate the current with the $330\,\Omega$ resistor: $I = \dfrac{3.0\,\text{V}}{330\,\Omega} \approx 9.1\,\text{mA}$. Write the value in your project diary. You check it by measuring in step 9.
3. Identify the LED's legs. The long leg is the anode and the short leg the cathode. The rim of the LED often also has a flat spot on the cathode side.
4. Unplug the USB cable. Put the LED on the breadboard with the cathode in hole a5 and the anode in hole a6.
5. Put the resistor between holes b6 and b10. A resistor has no direction.
6. Run a wire from the Arduino's pin 13 to hole e10 and another wire from a GND pin to hole e5. Compare your circuit with the drawing and the circuit diagram.
7. Open the Arduino IDE, type the program below and save it. Choose the right board and port from the menu, and upload the program with the Upload button.
8. Plug in the USB cable. The LED should be on for one second and off for one second in turn.
9. Measure the current. Unplug the USB cable, take the pin 13 wire out of hole e10 and connect the multimeter in series in its place: one lead to pin 13 and the other to hole e10. Choose the current range $\text{mA}$. Plug in the USB cable and read the value while the LED is on. Measuring is explained further in the chapter [Measurements in an electric circuit](fy6-2.html).

## Diagrams and example code

The circuit diagram shows the order in which the current flows from pin 13 through the resistor and the LED to ground.

<svg data-fig="kytkenta"></svg>

On a breadboard the five holes of the same column are joined inside the board. The columns 5, 6 and 10, marked yellow in the drawing, carry the current from one component to the next.

<svg data-fig="koekytkentalevy"></svg>

The example program. Two slashes start a comment, which the Arduino does not run.

```cpp
// Blinking LED: pin 13 -> 330 ohm resistor -> LED -> GND
const int LED_PIN = 13;        // the pin the resistor is connected to
const int ON_MS = 1000;        // how long the LED is on (ms)
const int OFF_MS = 1000;       // how long the LED is off (ms)

void setup() {
  pinMode(LED_PIN, OUTPUT);    // the pin works as an output
}

void loop() {
  digitalWrite(LED_PIN, HIGH); // 5 V to the pin: the LED lights up
  delay(ON_MS);
  digitalWrite(LED_PIN, LOW);  // 0 V to the pin: the LED goes out
  delay(OFF_MS);
}
```

`setup()` runs once when the board starts. `loop()` repeats for as long as the board has power.

## Test and measure

- Change the values of the constants `ON_MS` and `OFF_MS`. At what blinking frequency can you no longer see the blinking? Write down your observation and the values you used.
- Compare the current you measured with the value $9.1\,\text{mA}$ you calculated in step 2. Calculate the relative difference. Think about where the difference could come from: the resistor's tolerance is typically $\pm 5\,\%$, the LED's voltage is not exactly $2.0\,\text{V}$, and the pin's voltage is not exactly $5.0\,\text{V}$.
- Measure the voltage across the LED and across the resistor separately. Is their sum the same as the voltage between the pin and GND?

## If something does not work

| Symptom | Likely cause | Fix |
|---|---|---|
| The LED does not light at all | The LED is the wrong way round | Turn the LED: long leg in hole a6. |
| The LED does not light at all | A wire is in the wrong column | Compare every hole with the drawing. |
| The upload fails | Wrong board or port | Check the Tools menu. Try another USB cable, as some cables only carry power. |
| No port is shown at all | The cable or the USB port does not work | Try another USB port and cable. If the port still does not show, tell your teacher. |
| The LED is on all the time | The program did not upload or the wire is in the wrong pin | Upload the program again and check that the wire is in pin 13. |
| The LED is dim | The resistor is too large | Check the colour bands: $330\,\Omega$ is orange, orange, brown. |
| The meter shows zero | The meter is in parallel instead of in series, or its fuse has blown | Put the meter in the current's path and check the range. |

## Extension

1. SOS signal. Change the program so that the LED flashes the Morse signal SOS: three short, three long and three short flashes. Write a separate function for a short and a long flash.
2. Push button. Connect a push button between pin 2 and GND, and switch on the board's internal pull-up resistor with `pinMode(2, INPUT_PULLUP)`. Now `digitalRead(2)` gives LOW while the button is pressed. Make a program in which the LED is on only while the button is pressed.
3. Two LEDs. Add a second LED and resistor to pin 12 and make them alternate like traffic lights. Calculate the total current taken from the Arduino.

## Document your work

Record in your project diary

- a photo of the finished circuit and your own drawing of the circuit diagram
- your resistor calculation and the standard value you chose
- the measured current, the calculated current and their difference
- the program code or a link to it, one thing you changed and what followed from it
- one fault you came across and how you found it. A failure is good material to document when you tell what you learned from it.

## For the teacher: preparation

- This is a draft: the guide has not yet been tried on Ahjo's own devices. The chosen board is the Arduino Uno. Before the first session, check that the Arduino IDE is installed on the school computers and recognises the board.
- Reserve one board, cable and component kit per pair. Keep spare LEDs and resistors, because they get lost and broken.
- Check that the fuses of the multimeters' current ranges are intact.
- The most common sticking point is uploading the program. Try an upload on every computer in advance.
- The work suits the electronics part of the Ahjo 1 course and the start of competition robotics. For the physics theory, refer to the chapters FY6.1–FY6.3 and FY6.14.
- The structure of the guide was influenced by SparkFun's experiment guide (SIK) and Arduino's own examples. The text, figures and code were written for Ruukkilabra.
