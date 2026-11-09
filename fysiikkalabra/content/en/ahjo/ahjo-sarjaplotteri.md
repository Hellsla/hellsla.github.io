## Quick start

You get the sensor's readings as a curve in about ten minutes. The program is ready as a [starter file](ahjo-aloitus/sarjaplotteri.ino), and the same code is below in this guide. Always make connections with the USB cable unplugged.

1. Connect the light-dependent resistor and the $10\,\text{k}\Omega$ resistor in series between the Arduino's 5V and GND pins as in the diagram below.
2. Run a wire from between the light-dependent resistor and the $10\,\text{k}\Omega$ resistor to the Arduino's A0 input.
3. Plug in the USB cable, open the program in the Arduino IDE and upload it with the Upload button.
4. Open Tools → Serial Plotter and choose the speed 9600 baud. Cover the sensor with your hand: the curve drops.

### Try

Get the sensor's readings to show in the serial plotter and save them.

### Modify

Make the sensor into an instrument or a light that reacts to its surroundings. For example, a buzzer's pitch can rise when there is more light. The code is below in the Extension section.

### Challenge yourself

Convert the readings to voltages, collect a measurement series and draw a graph with units.

## Challenge

You make a measuring device that draws. A light-dependent resistor changes its resistance with light, and the Arduino measures it as a voltage. The serial plotter shows the readings as a curve as soon as the surroundings change. Many other sensors are read the same way, for example temperature, humidity and force sensors.

The work takes one 75-minute lesson.

## Learning goals

After the work you can

- connect a sensor to a voltage divider and an analogue input
- read the sensor's value with `analogRead()` and send it to the computer with `Serial.println()`
- open the serial plotter and interpret its curve
- convert a reading to a voltage and save a measurement series.

## Starting level and prior skills

You should know how to upload a program to the Arduino. Revise [First steps with Arduino](ahjo-arduino.html) if needed. The voltage divider and resistance are explained in the chapter [Resistance and Ohm's law](fy6-3.html).

## Equipment and materials

Ahjo's equipment is still being acquired, so the models of the supplies will be specified later.

| Supply | Amount |
|---|---|
| Arduino Uno and USB cable | 1 |
| Breadboard and jumper wires | 1 + 4 |
| Light-dependent resistor (LDR) | 1 |
| Resistor $10\,\text{k}\Omega$ (brown, black, orange, gold) | 1 |
| Passive buzzer, or an LED and a $330\,\Omega$ resistor (Modify) | 1 |
| Computer with the Arduino IDE | 1 |

## Safety and induction

Ahjo's safety instructions are still being prepared. See the topic [Soldering and electronics work](ahjo-turvallisuus.html#elektroniikka), and follow the teacher's induction.

- Make and change connections only when the USB cable is unplugged.
- Do not connect the 5V pin straight to the GND pin. The light-dependent resistor and the $10\,\text{k}\Omega$ resistor are always in series between them.
- If something gets hot or smells, unplug the USB cable at once and tell the teacher.

## Steps

1. Unplug the USB cable. Place the light-dependent resistor and the $10\,\text{k}\Omega$ resistor on the breadboard so that they share one column. That is the divider's middle point.
2. Run a wire from the 5V pin to the free end of the light-dependent resistor and a wire from the GND pin to the free end of the $10\,\text{k}\Omega$ resistor.
3. Run a wire from the middle point's column to the A0 input.
4. Plug in the USB cable. Open the program, choose the Arduino Uno as the board and the right port, and upload the program.
5. Open Tools → Serial Plotter and choose 9600 baud. The curve should move when you cover the sensor or point a phone's light at it.
6. Save a measurement series. Open Tools → Serial Monitor, cover the sensor now and then, and copy the readings into a spreadsheet.

## Diagrams and example code

The light-dependent resistor and the $10\,\text{k}\Omega$ resistor form a voltage divider. The more light, the smaller the light-dependent resistor's resistance and the larger the voltage at the A0 input.

<svg data-fig="kytkenta"></svg>

The example program reads the A0 input 20 times a second and sends the reading to the computer. The text `valo:` names the curve in the serial plotter.

```cpp
const int SENSOR_PIN = A0;      // the divider's middle point

void setup() {
  Serial.begin(9600);           // the same speed as in the serial plotter
}

void loop() {
  int value = analogRead(SENSOR_PIN);   // 0...1023 means 0...5 V
  Serial.print("valo:");
  Serial.println(value);
  delay(50);                            // 20 readings a second
}
```

The reading is a whole number 0–1023. It can be converted to a voltage:
$$U = \frac{\text{reading}}{1023} \cdot 5{,}0\,\text{V}.$$

## Test and measure

- Look at the reading in room light, covered with your hand and in a phone's light. Record three readings and convert them to voltages.
- Also measure the voltage at the A0 input with a multimeter. Does it match the voltage you calculated from the reading?
- Challenge yourself: compare the readings with the lux readings of a phone's light meter app in the same place and draw a graph. The app's reading is only indicative.

## If something does not work

| Symptom | Likely cause | Fix |
|---|---|---|
| The serial plotter is empty | Wrong speed | Choose 9600 baud in the plotter. |
| The serial plotter is empty | The program did not upload | Upload the program again and check the board and port. |
| The reading is always 0 or 1023 | The A0 wire is in the wrong column | Move the A0 wire to the middle point, between the light-dependent resistor and the resistor. |
| The reading jumps randomly | The A0 wire is loose | Press the wire firmly into the hole. |
| The curve rises when the sensor is covered | The light-dependent resistor and the resistor have swapped places | The circuit still works. Just note that the direction is reversed. |
| Uploading fails | The serial monitor or plotter holds the port | Close them and upload again. |

## Extension

1. Light instrument. Connect a passive buzzer between pin 8 and GND and add a line to the program's `loop()` that turns the reading into a pitch:
   ```cpp
   tone(8, map(value, 0, 1023, 200, 2000));   // more light, higher pitch
   ```
2. Night light. Connect an LED and a $330\,\Omega$ resistor to pin 13. Light the LED when the reading is smaller than a limit you choose. Choose the limit from your measurements.
3. Another sensor. Try the same program with another sensor, for example a potentiometer or a temperature sensor, if one is available.

## Document your work

Record in your project diary

- a photo of the circuit and a screenshot of the serial plotter's curve
- three readings in different lighting and the matching voltages
- how you made the sensor into an instrument, a light or another device
- one fault you ran into, and how you found it.

## For the teacher: preparation

- This is a draft: the guide and the starter program have not yet been tried with Ahjo's own equipment. Try the program on the teacher's computer before the lesson.
- The serial plotter is in the Arduino IDE from version 1.6.6. In the Arduino IDE 2 it also opens from the button in the window's top right corner.
- The resistance of light-dependent resistors varies by model. If the readings stay in a narrow range, try a $4{,}7\,\text{k}\Omega$ or $47\,\text{k}\Omega$ resistor in place of the $10\,\text{k}\Omega$ one.
- At the Modify level of lesson 10 a distance sensor can also be used, if one has been acquired. It needs its own program, which this guide does not have.
- The text, diagrams and code were written for Ruukkilabra.
