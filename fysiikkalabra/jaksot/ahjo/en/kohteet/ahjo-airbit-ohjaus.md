## Quick start

The Air:bit 2 is controlled with a second micro:bit, which sends the commands by radio. You program the controller yourself in MakeCode. The drone's own program is ready-made, and you learn to read it.

1. Open MakeCode and make a new project.
2. Set your group's own number as the radio group.
3. Send the tilt, the throttle and the arm value by radio as named values.
4. Test on the desk with another micro:bit that the values arrive.

### Try

Program a controller that sends the tilt and the throttle. Show on the receiving micro:bit that the values change.

### Modify

Add an arming safeguard: A and B together toggle the arm value and reset the throttle to zero. Add a shake that stops the motors.

### Challenge yourself

Read from the drone's program how it shares the power between the four motors, and explain why the drone tilts forwards.

## Challenge

The controller and the drone do not know each other: they only send to and listen to the same radio group. If two groups use the same number, one group's controller controls the other group's drone. The goal is a controller that works reliably and whose state you can see at a single glance.

The manufacturer estimates three to four hours for programming the controller. If your own program is not finished, the manufacturer's ready-made controller program is available.

## Learning goals

After the work you can

- send and receive values with the micro:bit's radio
- program a controller that has a throttle, tilt, an arming safeguard and an emergency stop
- tell what the main parts of the drone's program do
- describe stabilisation as feedback.

## Starting level and prior skills

Block programming in MakeCode is enough. Variables and the conditional statement are revised in the lesson. The drone must be assembled according to the guide [Assembling the Air:bit 2 and functional tests](ahjo-airbit-kokoaminen.html) before the controller is tried with it.

## Equipment and materials

| Supply | Amount |
|---|---|
| micro:bit as the controller (V1 or V2) and a battery holder | 1 |
| micro:bit as the receiver for the desk test | 1 |
| Computer on which MakeCode works in the browser | 1 |
| USB cable | 1 |
| Assembled Air:bit 2 without propellers | 1 |

## Safety and induction

See the topic [propellers and motors](ahjo-turvallisuus.html#drone-potkurit). It is in preparation until the school has approved it.

- Every new or changed program is tested first on the desk and then with the drone **without propellers**.
- The arming safeguard and the shake stop are always kept in the program.
- Values in the drone's program that affect flight are not changed without the teacher's permission. The original program is saved before any changes.

## Steps

The controller sends five values. The manufacturer's mnemonic is PARTY.

| Letter | Value | Range | How on the controller |
|---|---|---|---|
| P | pitch, tilt forwards and backwards | $-45$ … $45$ | tilt the controller |
| A | arm, permission to start | 0 or 1 | A and B together |
| R | roll, tilt to the side | $-45$ … $45$ | tilt the controller |
| T | throttle | 0 … 100 | A decreases, B increases |
| Y | yaw, turning about the vertical axis | $-30$ … $30$ | extra task |

1. Make variables for the arm value, the throttle and the tilts.
2. Set the radio group at the start of the program and show the number on the display.
3. Button A decreases the throttle by five and button B increases it by five. When the throttle is over 40, the step is one: hovering is adjusted precisely.
4. A and B together toggle the arm value between 0 and 1 and reset the throttle to zero.
5. A shake sets the arm value and the throttle to zero. This is the emergency stop.
6. Read the tilts from the micro:bit's orientation sensor and limit them to the range in the table.
7. Send the values in a forever loop as named values, each with its own capital letter.
8. Show the state on the display: armed or disarmed, the throttle level and the tilt dot.
9. Test on the desk with the receiving micro:bit, then with the drone without propellers.

## Diagrams and example code

You get the starter program from the page of lesson 5. Here is its core. Paste the program into MakeCode's JavaScript view, and you will see it as blocks too.

```typescript
let radioGroup = 7      // change to your group's own number
let arm = 0
let throttle = 0

radio.setGroup(radioGroup)

input.onButtonPressed(Button.AB, function () {
    arm = arm == 0 ? 1 : 0
    throttle = 0
})

input.onGesture(Gesture.Shake, function () {
    arm = 0
    throttle = 0
})

basic.forever(function () {
    radio.sendValue("A", arm)
    radio.sendValue("T", throttle)
    radio.sendValue("P", Math.constrain(input.rotation(Rotation.Pitch), -45, 45))
    radio.sendValue("R", Math.constrain(input.rotation(Rotation.Roll), -45, 45))
})
```

### How the drone's program works

In the Air:bit 2 the stabilisation is calculated in the micro:bit, and the program is open MakeCode code. Its main loop repeats the same stages many times a second:

1. **Measure.** The program reads the controller board's gyroscope and accelerometer and calculates the drone's attitude from them.
2. **Compare.** The program compares the measured attitude with the attitude that the controller asks for. The difference is the error.
3. **Correct.** A controller algorithm calculates a correction for each axis from the error.
4. **Share the power.** The program calculates the power of each motor from the throttle and the corrections. When the drone tilts forwards, the two rear motors get more power and the two front motors less.
5. **Make sure.** The motors run only when the drone is armed and the sensors work.

This is feedback: the measurement affects the control, and the control changes what is measured next.

## Test and measure

- Desk test: do the values shown by the receiver change when you tilt the controller and press the buttons?
- Range: from how far does the message still arrive in the classroom? Measure the distance.
- Drone test without propellers: do the motors start only when armed, and do they stop from a shake every time out of ten?

## If something does not work

- **The values do not arrive:** check that both micro:bits have the same radio group.
- **The neighbouring group's controller affects your drone:** you have the same radio group. Change yours.
- **The drone reacts in the wrong direction:** change the sign of the tilt value in the controller's program and test again without propellers.
- **The throttle jumps:** check that the handlers of button A and button B do not also fire when you press both.
- **Your own program is not finished:** upload the manufacturer's ready-made controller program and continue your own program later.

## Extension

In the manufacturer's extra task the yaw (Y) is done with the touch buttons. Design your own way of giving the yaw command and test it on the desk. Another option: make a micro:bit into a receiver that plots the values sent by the controller as a graph in MakeCode's data view.

## Document your work

Attach to your project diary

- a screenshot of the controller program
- the number of your group's radio group
- the results of the desk test and the drone test
- a reading map of the stages of the drone's program.

## For the teacher: preparation

- The ready-made programs are on the manufacturer's page [Air:bit documents](https://www.makekit.no/en/docs/airbit-docs/): the controller's hex file and the drone's program. Open the drone's program in MakeCode on a school computer before the lesson.
- Give each group its own radio group in the range 0–255. The default of the ready-made program is 7.
- The manufacturer's instructions do not include changing the tuning values. Reading the drone's program and the stability tests are the school's own tasks: try them yourself and decide which values the students may change and by how much. The tuning values are not recorded in this guide, because they can change with the version of the program.
- The starter program is an untested draft. Try it without propellers and check the direction of the tilt.
- Python: for the Air:bit 2 the manufacturer offers a Python version of the controller only, not of the drone's program.
- The information was read from the manufacturer's instructions on 12 November 2026.
