## Quick start

You make a card whose picture lights up when you press a corner. The first light comes on in about ten minutes, and all you need is card, copper tape, a coin cell and an LED. No devices are used, so no device induction is needed.

1. Fold the card in half. With a pencil, draw two tracks on the inside of the opened card as in the drawing below.
2. Stick copper tape on the tracks. Put the coin cell on the end of the minus track with its plus side up and fold the corner of the card over it.
3. Bend the LED's legs out to the sides and tape them onto the tracks so that the long leg is on the plus track and the short one on the minus track.
4. Press the corner. The LED lights up.

### Try

Make the LED light up when you press the corner of the card.

### Modify

Draw or cut a picture on the cover that the light shines through: a star, a window, a lighthouse or a character of your own.

### Challenge yourself

Add a second LED in parallel with the first one and compare the brightness. The explanation is below in the Learn more part.

## Challenge

Make a card in which the light is part of the picture. You build an electric circuit on paper, in which the copper tape is the conductor, the coin cell the voltage source and the folded corner of the card the switch. When you understand a paper circuit, you understand the basic idea of every electric circuit: current flows only in a closed circuit.

The work takes about 30 minutes. You can spend as long as you like on the illustration.

## Learning goals

After the work you can

- build a closed circuit with a voltage source, a switch and an LED
- connect an LED the right way round and explain why it lights in one direction only
- make a switch from paper and copper tape
- connect two LEDs in parallel and explain what you see.

## Starting level and prior skills

You need no earlier experience. If you want to know more about electric circuits, read the chapter [Electric circuit, current and voltage](fy6-1.html). How an LED works is explained in the chapter [Semiconductors, the diode, the LED and the solar cell](fy6-14.html).

## Equipment and materials

| Item | Quantity |
|---|---|
| Card, A5 or A4 folded | 1 |
| Copper tape with conductive adhesive, about $5\,\text{mm}$ wide | about $40\,\text{cm}$ |
| Coin cell CR2032 ($3\,\text{V}$) | 1 |
| LED, red or yellow, $3\,\text{mm}$ or $5\,\text{mm}$ in diameter | 1–2 |
| Tape, scissors, pencil and colours | 1 set |

Red and yellow LEDs light most reliably with the $3\,\text{V}$ of a coin cell. White and blue LEDs need almost the whole voltage of the cell, so they may stay dim.

## Safety and induction

The work needs no device induction. Still, follow these precautions:

- A coin cell is dangerous if swallowed. Keep the cells in their box and give them back to your teacher at the end of the lesson.
- Do not join the terminals of the cell directly with copper tape. A short circuit drains the cell and makes it warm.
- Use only a coin cell in this work. A bigger battery gives so large a current that the LED needs a series resistor.

## Steps

1. Fold the card in half so that you get a card. Open it and turn the inside up.
2. Draw two tracks with a pencil as in the drawing. The minus track runs from the bottom corner of the card, where the cell goes, to the picture. The plus track runs from the picture to the corner that folds, so that its end lands on the cell when the corner is folded.
3. Cut pieces of copper tape and stick them on the tracks. Where a track turns, do not cut the tape but fold it at the corner. A folded tape conducts better than two overlapping pieces.
4. Put the coin cell at the start of the minus track with its plus side up. The plus terminal is the wide side of the cell marked $+$, and the rim of the cell belongs to the plus terminal too. The bottom of the cell is the minus terminal, and it touches the minus track. Fix the cell with tape so that the tape does not cover the top of the cell.
5. Fold the corner of the card over the cell. The end of the plus track in the corner must land on the top of the cell, and it must not touch the minus track. This is the switch.
6. Bend the LED's legs out to the sides. The long leg is the anode and goes on the plus track, the short leg is the cathode and goes on the minus track. Tape the legs firmly against the copper tape.
7. Press the corner. The LED should light up. If it does not, see the section If something does not work below.
8. Draw or cut a picture on the cover so that the LED is behind it.

## Diagrams and example code

The opened card from the inside. The copper tracks are orange, and the corner that folds is marked with a dashed line.

<svg data-fig="kortti"></svg>

There is no programming in this work. Later the same circuit can be connected to an Arduino, so that the light can blink.

## Test and measure

- How it works: when you press the corner, the plus track touches the plus terminal of the cell and the circuit closes. Current flows from the plus terminal of the cell along the plus track to the anode of the LED, through the LED and from the cathode along the minus track back to the minus terminal of the cell. When you let go, the circuit opens and the light goes out.
- An LED lets current through in one direction only, from the anode to the cathode. That is why an LED the wrong way round does not light.
- A coin cell has an internal resistance, typically about $10\text{–}20\,\Omega$. It limits the current, so no separate series resistor is needed in this work.
- Challenge yourself: connect a second LED in parallel, with its long leg on the plus track and its short leg on the minus track. Compare the brightness with a one-LED card. Because the internal resistance of the cell limits the total current, the current is shared by two LEDs, and each is usually a little dimmer. If the LEDs have different colours, the one with the lower threshold voltage (red) may take almost all the current.

## If something does not work

| Symptom | Likely cause | Fix |
|---|---|---|
| The LED does not light | The LED is the wrong way round | Turn the LED: the long leg goes on the plus track. |
| The LED does not light | A leg does not touch the tape | Tape the leg more firmly or press it with a fingernail. |
| The LED does not light | The tracks are made of joined pieces | Press the joint firmly or put more tape over it. A single folded tape is the most reliable. |
| The LED is on all the time | The plus track touches the cell without being pressed | Put a piece of card under the corner as a spacer, so that contact happens only when you press. |
| The LED is dim | A white or blue LED, or an old cell | Change to a red or yellow LED or a new cell. |
| The cell gets warm | Short circuit: the tracks touch each other, or the minus track touches the rim of the cell | Remove the cell at once and find the place where the tracks touch. The rim of the cell is the plus terminal, so the minus track must not reach past the cell. |

## Extension

1. Two switches. Make a card in which the light comes on only when you press two corners at the same time. Draw a circuit diagram first. The switches are in series.
2. Comparing brightness. Make two identical cards, one with one LED and the other with two LEDs in parallel. Photograph them with a phone in the same conditions and compare the pictures.
3. An Arduino card. Connect the LED of the card to an Arduino pin through a $330\,\Omega$ resistor, as in [First steps with Arduino](ahjo-arduino.html), and make it blink.

## Document your work

Record in your project diary

- a photo of the finished card open and closed
- your own circuit diagram: the cell, the switch and the LED
- one thing that did not work at first, and how you fixed it
- if you did the challenge, what you saw about the brightness of one and two LEDs.

## For the teacher: preparation

- This is a draft: the guide has not been tried in Ahjo. Make one card yourself before the lesson with the LEDs and copper tape you have chosen.
- Get copper tape with conductive adhesive. With ordinary copper tape the adhesive does not conduct, so joints do not work.
- Reserve red and yellow LEDs. They work most reliably with a CR2032 cell.
- Hand out the coin cells at the start of the lesson and collect them at the end. A swallowed coin cell is life-threatening, so keep them in a locked box.
- The work suits the first lesson of Ahjo 1 as an alternative task or an extra challenge. It links the work with visual arts and the physics chapter [Electric circuit, current and voltage](fy6-1.html).
- Paper circuits are a common makerspace technique. The text and figure of the guide were made for Ruukkilabra.
