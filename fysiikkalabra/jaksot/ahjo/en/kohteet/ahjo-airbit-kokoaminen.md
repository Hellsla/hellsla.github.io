## Quick start

The Air:bit 2 is a construction kit from which you assemble a quadcopter that runs on a micro:bit. You assemble it according to the manufacturer's building instructions. This page tells you in which order the work is done in Dronelabra and what is checked before the battery is connected.

1. Sort the parts and check them against the parts list in the instructions.
2. Assemble the frame and attach the motors and the controller board according to the instructions.
3. **Leave the propellers off.** In the manufacturer's instructions the propellers come at the end of the assembly chapter, but they are fitted only in the flying lesson.
4. Ask the teacher for an inspection and connect the battery only after that.

### Try

Assemble the drone without propellers and start it on a level surface. Record which letters the display shows.

### Modify

Do a motor test without propellers and mark on your parts map which motor is in which corner and which way its propeller is meant to spin.

### Challenge yourself

Write a troubleshooting card for two start-up errors: what do you check first, and in which order?

## Challenge

The drone flies only if every part is in the right place: two propellers spin clockwise and two anticlockwise, and there is a good electrical connection between the controller board and the micro:bit. The goal is to assemble the drone so carefully that it starts the first time and passes the motor test.

The manufacturer estimates two to three hours for the assembly, so the work is spread over two lessons.

## Learning goals

After the work you can

- name the parts of the drone and tell what they do
- assemble the drone according to the instructions and inspect the work
- charge the battery under supervision
- start the drone and interpret the messages on the display.

## Starting level and prior skills

No earlier experience is needed. Before the battery is connected, you must have gone through the [Dronelabra safety induction](ahjo-drone-perehdytys.html).

## Equipment and materials

The information is from the manufacturer's building instructions. Check the contents of your own kit against the parts list in the instructions.

| Part | What it does |
|---|---|
| Frame, six-layer birch plywood | Holds the parts in place and withstands crashes. |
| Controller board (black) with a charging circuit | Measures the attitude with a gyroscope, controls the motors and charges the battery. |
| 4 motors, of two different types | Spin the propellers. Two spin clockwise and two anticlockwise. |
| 4 propellers and 4 spare propellers, diameter $65\,\text{mm}$ | Produce the lift. The direction is marked on the propeller's hub. |
| Lithium polymer battery, 1 cell, $3.7\,\text{V}$, $800\,\text{mAh}$ | Powers the motors and the board. |
| micro:bit in the drone (the manufacturer recommends version V2) | Calculates the stabilisation and receives the radio commands. |
| micro:bit in the controller and a battery holder | Sends the control commands by radio. |
| Small cross-head screwdriver and socket wrench | For the assembly. The socket wrench is in the kit. |

The micro:bits, the battery holder and the USB cable are usually sold separately.

## Safety and induction

See the topics [propellers and motors](ahjo-turvallisuus.html#drone-potkurit) and [batteries](ahjo-turvallisuus.html#drone-akut). They are in preparation until the school has approved them.

- Propellers are not fitted in the assembly lessons. Starting and stopping the motors is first tried without them.
- The battery is connected only after the teacher's inspection and is always disconnected when the drone is not in use. When connected, the battery can discharge too far.
- The battery is charged from the controller board's micro-USB connector, not from the micro:bit's connector. A red light means that the battery is charging, and a green one that charging is complete. Charging takes about an hour. The battery is not charged without supervision.
- Do not bend, press or open the battery. A damaged or swollen battery is taken to the teacher.

## Steps

1. Sort the parts and compare them with the parts list in the instructions. Tell the teacher if something is missing.
2. Assemble the frame and attach the motors according to the instructions. Check the type and place of every motor before attaching it.
3. Attach the controller board. The board's five nuts are tightened lightly: they carry the electrical signal between the boards, so a loose nut prevents the drone from working.
4. Fit the micro:bit in place.
5. Inspect the work with your partner with the help of the parts map. Ask the teacher for an inspection.
6. Place the drone on a level surface and connect the battery. Do not move the drone during start-up.
7. Read the display: the letters G, M and C tell you that the gyroscope was found, the motor controller was found and the calibration is complete.
8. Do a motor test with the controller without propellers: start the motors, add throttle and stop them by shaking the controller.
9. Disconnect the battery.

## Diagrams and example code

The pictures of the building instructions are in the manufacturer's instructions, which the teacher hands out. Draw your own parts map: the outline of the drone from above, the four motors and their directions of rotation, the controller board, the micro:bit and the battery, and arrows that show where the power and the control signals travel.

The drone's program is uploaded to the micro:bit ready-made. It is studied in the guide [Air:bit 2 radio controller and control program](ahjo-airbit-ohjaus.html).

## Test and measure

- Do the letters G, M and C appear at start-up?
- Do all four motors start, and do they stop when you shake the controller?
- Weigh the drone without the battery and with the battery. How large a part of the mass is battery?

Record the results. The drone's mass is needed when you calculate the lift needed for hovering.

## If something does not work

The advice is from the manufacturer's troubleshooting.

| Observation | Try |
|---|---|
| The display reports that the gyroscope is not found | Tighten the board's five nuts lightly, disconnect the battery and connect it again. |
| The display reports that the motor controller is not found | Unplug the USB cable and the battery and then connect only the battery. |
| The motors do not start | Check that the controller and the drone are on the same radio group and that the dots on the controller's display move when you tilt it. Try the manufacturer's ready-made controller program. |
| The micro:bit shows an error number | Open the program in MakeCode and upload it again from there. |
| The calibration does not succeed | The drone is not on a level surface or it was moved. Disconnect the battery and start again. |
| The controller board's light is red | The battery must be charged. Do not try to fly. |

## Extension

Calculate the battery's energy from its markings: $E = QU$, when the charge $Q$ is given in milliampere-hours and the voltage $U$ in volts. How many joules does the battery hold? Compare the result with your phone's battery.

## Document your work

Attach to your project diary

- the parts map
- a photo of the assembled drone without propellers
- the stages of the start-up and the result of the motor test
- one thing that you would do differently in the assembly.

## For the teacher: preparation

- Download the manufacturer's building and coding instructions (*Airbit 2 – Building and coding*) from the page [Air:bit documents](https://www.makekit.no/en/docs/airbit-docs/). Use the instructions for the black board (Air:bit 2), not for the blue board (Air:bit 1).
- The manufacturer's time estimate is 2–3 hours for the assembly and 3–4 hours for programming the controller.
- In the page order of the instructions the propellers are fitted before the programming, but the safety page of the instructions advises fitting them only when the building and programming are done and starting and stopping the motors has been tried. Keep the propellers yourself until the flying lessons.
- Upload the drone program to the micro:bits beforehand and number the kits, micro:bits and radio groups by group.
- The school's kits have propeller guards. They are fitted according to the manufacturer's guide in the flying lesson, together with the propellers.
- There are 10 kits and 20 micro:bits, two for each kit. Check that the ones used on the drone are version V2.
- Propellers and motors wear out the most. Have spare parts in reserve.
- The manufacturer does not state the drone's mass or flight time: they are measured yourself.
- The information was read from the manufacturer's instructions on 12 November 2026.
