## Quick start

You get the Arduino playing a tune in about ten minutes, and you do not have to write any code yourself. Your teacher has installed the Arduino IDE and saved a ready-made program. Always make connections with the USB cable unplugged.

1. Connect the plus leg or the red wire of the piezo buzzer to the Arduino's pin 8 and the other leg to a GND pin.
2. Plug in the USB cable and open your teacher's ready-made program or copy the example code below.
3. Choose Arduino Uno as the board and the right port, and press Upload.
4. The buzzer plays the beginning of the folk song Ukko Nooa.

### Try

Make the buzzer play with the ready-made program.

### Modify

Change the notes and their lengths and make your own melody, jingle or alarm sound. Change the tempo.

### Challenge yourself

Work out the frequencies of a major scale with the formula and play the scale. The instructions are below in the Learn more part.

## Challenge

Program the Arduino to play a tune of your own. A piezo buzzer vibrates in time with the changing voltage of the pin, and you hear the frequency of the vibration as pitch. When you know how frequency and pitch are related, you can work out the frequency of any note.

The work takes about 30 minutes. You can spend as long as you like composing your own melody.

## Learning goals

After the work you can

- connect a buzzer to an Arduino and play a note with the `tone()` command
- store a melody in arrays and play it in a loop
- explain how frequency and pitch are related
- work out the frequency of a note with the formula of equal temperament.

## Starting level and prior skills

You have done [First steps with Arduino](ahjo-arduino.html) or you know how to upload a program to an Arduino. Sound and frequency are explained in the chapter [Sound as a wave: pitch, timbre and the Doppler effect](fy5-14.html).

## Equipment and materials

| Item | Quantity |
|---|---|
| Arduino Uno and USB cable | 1 |
| Passive piezo buzzer | 1 |
| Jumper wires (male–male) or a breadboard | 2 |
| Computer with the Arduino IDE | 1 |

Use a passive buzzer. An active buzzer only plays its own fixed sound and does not follow the frequency of the `tone()` command. You can often recognise a passive buzzer by the circuit board visible underneath it, and it only clicks when you connect it straight to $5\,\text{V}$.

## Safety and induction

Ahjo's safety instructions are still being prepared. See the topic [Soldering and electronics work](ahjo-turvallisuus.html#elektroniikka) and follow your teacher's induction.

- Make and change connections only when the USB cable is unplugged.
- Close to the ear the sound of a buzzer is loud. Keep the buzzer on the table and do not put it next to your ear.
- Agree with your group when to play. Ten buzzers at once make a harsh soundscape.

## Steps

1. Unplug the USB cable. Connect the plus leg or the red wire of the buzzer to pin 8 and the other leg to a GND pin. If the buzzer has no marking, you can connect it either way round.
2. Check the connection against the drawing and then plug in the USB cable.
3. Open the Arduino IDE and type or copy the program below.
4. Choose Arduino Uno as the board and the right port, and upload the program with the Upload button. The buzzer plays the melody, pauses for two seconds and starts again.
5. Change the value of the constant `TEMPO` and upload the program again. What happens?
6. Change the arrays `melodia` and `kestot` and make your own melody. Both arrays must contain the same number of numbers, and the constant `N` must be that same number.

## Diagrams and example code

Circuit diagram: the buzzer is between pin 8 and ground.

<svg data-fig="kytkenta"></svg>

The example program plays the beginning of the Finnish folk song Ukko Nooa. The frequencies are rounded to whole hertz. The names in the code are Finnish: `SUMMERI` is the buzzer, `melodia` the melody and `kestot` the lengths.

```cpp
// A tune on a piezo buzzer: pin 8 -> buzzer -> GND
const int SUMMERI = 8;   // the pin the buzzer is connected to
const int TEMPO = 350;   // the length of one beat in milliseconds

// frequencies of the notes in hertz (C4 = 262, D4 = 294, E4 = 330, F4 = 349)
int melodia[] = {262, 262, 262, 330, 294, 294, 294, 349, 330, 330, 294, 294, 262};
int kestot[]  = {1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   2};  // in beats
const int N = 13;        // the number of notes

void setup() {
}

void loop() {
  for (int i = 0; i < N; i++) {
    int ms = kestot[i] * TEMPO;
    tone(SUMMERI, melodia[i], ms * 9 / 10);  // the note sounds for 90 % of the time, so the notes stay apart
    delay(ms);                               // wait until the note has sounded
  }
  noTone(SUMMERI);
  delay(2000);                               // a pause before the next round
}
```

`tone(pin, frequency, duration)` makes the voltage of the pin alternate between $0\,\text{V}$ and $5\,\text{V}$ at the given frequency. The command does not wait for the note to end, so a `delay()` is needed after it.

## Test and measure

- How it works: when the voltage of the pin alternates, the piezoelectric disc of the buzzer bends back and forth at the same frequency. The disc makes the air vibrate, and the ear hears the vibration as sound. The higher the frequency, the higher the pitch.
- A note one octave higher has twice the frequency. Play $262\,\text{Hz}$ and $523\,\text{Hz}$ one after the other and listen whether they sound like the same note at different heights.
- Challenge yourself: in equal temperament the octave is divided into twelve equal semitones. The frequency of a note that is $n$ semitones above the note A4 is

$$f = 440\,\text{Hz} \cdot 2^{n/12}.$$

  For example, C4 is 9 semitones below A4, so $f = 440\,\text{Hz} \cdot 2^{-9/12} \approx 262\,\text{Hz}$. The steps of a major scale are whole, whole, half, whole, whole, whole and half, that is 2, 2, 1, 2, 2, 2 and 1 semitones. Work out the frequencies of the C major scale from C4 to C5 and play the scale.

## If something does not work

| Symptom | Likely cause | Fix |
|---|---|---|
| No sound | The wire is in the wrong pin | Check that the wire is in pin 8. |
| No sound | The program did not upload | Check the board and the port in the Tools menu and upload again. |
| Only one and the same sound | The buzzer is active | Change to a passive buzzer. |
| The sound is very quiet | The buzzer is connected the wrong way round or is broken | Turn the buzzer round. If the sound does not get louder, change the buzzer. |
| The program does not compile | The arrays have different numbers of values or a semicolon is missing | Count the values in the arrays and check the line in the error message. |
| The melody is muddled | `N` does not match the length of the arrays | Set `N` to the number of values in the arrays. |

## Extension

1. A calculated scale. Calculate the frequencies in the program: `440.0 * pow(2.0, n / 12.0)`. Play all 13 notes from C4 to C5 with a loop.
2. A button instrument. Connect two push buttons to pins 2 and 3 as in the extension of [First steps with Arduino](ahjo-arduino.html) and make an instrument in which each button plays a different note.
3. A light theremin. Read the value of a light-dependent resistor from an analogue pin and turn it into a frequency with the `map()` command. The pitch changes when you move your hand over the sensor. This suits lesson 10.

## Document your work

Record in your project diary

- a photo of the connection and your own circuit diagram
- the arrays of your melody and a short recording or video
- one thing that did not work at first, and how you fixed it
- if you did the challenge, the frequencies you worked out as a table.

## For the teacher: preparation

- This is a draft: the guide has not been tried on Ahjo's own devices. Test the program and the buzzer before the lesson.
- Get passive piezo buzzers. Active buzzers do not follow the frequency of the `tone()` command. Mark the passive ones if both kinds are in the same box.
- Save the example program on the school computers in advance, so that the quick start works without typing.
- The work suits lesson 9 of Ahjo 1 as an alternative task or an extra challenge. It links the work with music and the physics chapter [Sound as a wave: pitch, timbre and the Doppler effect](fy5-14.html).
- The folk song Ukko Nooa is free to use. The text, figure and code of the guide were written for Ruukkilabra.
