## Quick start

You get the servo to turn with a potentiometer in about ten minutes. The Arduino IDE has a ready example program File → Examples → Servo → Knob, and below is the same thing as a shorter program. Always make connections with the USB cable unplugged.

1. Connect the potentiometer's outer legs to the Arduino's 5V and GND pins and the middle leg to the A0 input as in the diagram below.
2. Connect the servo's red wire to 5V, the brown or black wire to GND and the orange or yellow wire to pin 9.
3. Plug in the USB cable, open the program and upload it with the Upload button.
4. Turn the potentiometer. The servo's arm turns along with it.

### Try

Get the servo to turn with the potentiometer.

### Modify

Limit the servo's movement to what you need, for example to 30–150 degrees, or make the servo into a pointer with your own scale drawn behind it.

### Challenge yourself

Attach the servo to your own construction, for example a gate, a fan or a moving figure, and test whether the attachment survives a hundred back-and-forth movements.

## Challenge

You make your first movement with a program. A potentiometer is an adjustable resistor whose position the Arduino reads as a voltage. The program turns the reading into an angle, and the servo turns to that angle. Many robot parts move on the same principle, for example grippers and steered wheels.

The work takes one 75-minute lesson.

## Learning goals

After the work you can

- connect a potentiometer as a voltage divider and a servo to the Arduino
- turn a reading into an angle with `map()` and turn a servo with `write()`
- limit the servo's movement in the program
- attach a servo to a construction so that the arm is not forced.

## Starting level and prior skills

You should know how to upload a program to the Arduino. Revise [First steps with Arduino](ahjo-arduino.html) if needed. Reading an analogue value is practised in the guide [Light sensor and the serial plotter](ahjo-sarjaplotteri.html).

## Equipment and materials

Ahjo's equipment is still being acquired, so the models of the supplies will be specified later.

| Supply | Amount |
|---|---|
| Arduino Uno and USB cable | 1 |
| Breadboard and jumper wires | 1 + 6 |
| Potentiometer, for example $10\,\text{k}\Omega$ | 1 |
| Small hobby servo, for example SG90 size | 1 |
| Servo arm and screw (come with the servo) | 1 |
| Cardboard, tape or hot glue for the construction (Challenge yourself) | as needed |
| Computer with the Arduino IDE | 1 |

## Safety and induction

Ahjo's safety instructions are still being prepared. See the topic [Soldering and electronics work](ahjo-turvallisuus.html#elektroniikka), and follow the teacher's induction. The hot glue gun is used only with the teacher's permission.

- Make and change connections only when the USB cable is unplugged.
- Keep your fingers out of the servo arm's way while the program runs.
- Do not force the servo arm by hand. The gears inside the servo can break.
- A small servo works from the USB cable's 5 V. A bigger servo or several servos need their own power supply. Ask the teacher, and then remember to join the GND pins of the power supply and the Arduino.
- If the servo buzzes in place for a long time, gets hot or smells, unplug the USB cable at once and tell the teacher.

## Steps

1. Unplug the USB cable. Place the potentiometer on the breadboard so that its three legs are in different columns.
2. Run a wire from the 5V pin to one outer leg of the potentiometer and a wire from the GND pin to the other outer leg.
3. Run a wire from the potentiometer's middle leg to the A0 input.
4. Connect the servo's red wire to the same 5V row, the brown or black wire to the GND row and the orange or yellow wire to pin 9.
5. Fit the servo arm, but do not screw it to the construction yet. First see the movement free.
6. Plug in the USB cable, choose the Arduino Uno as the board and the right port, and upload the program.
7. Turn the potentiometer from one end to the other. See at which angles the arm stops, and record them.

## Diagrams and example code

The potentiometer is a voltage divider whose middle point the wiper moves. The servo has three wires: two for power and one for control.

<svg data-fig="kytkenta"></svg>

The program reads the potentiometer, turns the reading 0–1023 into an angle of 0–180 degrees and turns the servo to it.

```cpp
#include <Servo.h>

const int POT_PIN = A0;     // the potentiometer's middle leg
const int SERVO_PIN = 9;    // the servo's control wire

Servo servo;

void setup() {
  servo.attach(SERVO_PIN);
}

void loop() {
  int value = analogRead(POT_PIN);          // 0...1023
  int angle = map(value, 0, 1023, 0, 180);  // 0...180 degrees
  servo.write(angle);
  delay(15);                                 // the servo has time to turn
}
```

At the Modify level the movement is limited by changing the last two numbers of the `map()` line, for example `map(value, 0, 1023, 30, 150)`.

## Test and measure

- Record at which angles the arm stops at the potentiometer's end positions. Do they match the program's numbers 0 and 180?
- When the servo is attached to the construction, turn the potentiometer slowly and see where the movement starts to stick. Limit the movement in the program to inside that point.
- Challenge yourself: write a program that moves the servo back and forth a hundred times, and then check the attachment. Did it hold? What came loose?

## If something does not work

| Symptom | Likely cause | Fix |
|---|---|---|
| The servo does not move at all | The control wire is in the wrong pin | Move the orange or yellow wire to pin 9. |
| The servo does not move at all | The program did not upload | Upload the program again and check the board and port. |
| The servo jerks or the Arduino restarts | The servo takes too much current from the USB cable | Try a smaller servo or ask the teacher for a separate power supply. |
| The servo turns only a little | The potentiometer's wire is loose or on the wrong leg | Check that the middle leg goes to the A0 input. |
| The arm buzzes at an end position | The construction blocks the movement | Limit the movement in the program on the `map()` line. |
| The movement goes the wrong way | The potentiometer's outer legs are the other way round | Swap the 5V and GND wires or swap the numbers 0 and 180. |

## Extension

1. Pointer meter. Combine this guide with the [light sensor](ahjo-sarjaplotteri.html): the servo arm shows the amount of light on your own scale.
2. Two positions. Replace the potentiometer with a push button. When the button is pressed, the servo turns to its other position.
3. Moving figure. Make a cardboard figure or mechanism that the servo moves, and show it to the other groups.

## Document your work

Record in your project diary

- a photo or a short video of the circuit and the movement
- the servo's end positions and how you limited the movement
- how you attached the servo and whether the attachment held
- one fault you ran into, and how you found it.

## For the teacher: preparation

- This is a draft: the guide and the program have not yet been tried with Ahjo's own equipment. Try the circuit before the lesson with the same servo model the students use.
- The Servo library comes with the Arduino IDE. The example program Knob is in the menu File → Examples → Servo.
- A small hobby servo usually works from the USB cable's voltage, but the current varies by model. If the Arduino restarts, give the servo its own power supply and a shared GND.
- The use of hot glue is decided in Ahjo's safety instructions, which are still being prepared.
- The text, diagrams and code were written for Ruukkilabra.
