## Quick start

The results of the flight tests are processed with Python. The program reads the measurements from a file, calculates the mean and the standard deviation for each series and draws a graph. No flying is needed: this work can be done whenever the drones are in another group's use.

1. Download the program `lentoanalyysi.py` and the example data from the lesson's page.
2. Run the program with the example data.
3. Write your own measurements into a similar file.
4. Run the program with your own file and interpret the graph.

### Try

Calculate and plot the mean and the standard deviation of one of your own group's measurement series.

### Modify

Compare two series in the same graph and write one sentence on whether their difference is larger than the variation within a series.

### Challenge yourself

Measure the drone's position from a video and calculate its speed at different moments with Python.

## Challenge

Five numbers in a table do not yet tell which setting was better. A graph that shows all the measurements, the mean and the spread tells it at a single glance. The goal is a graph that another group understands without an explanation.

## Learning goals

After the work you can

- save measurements in a file that a program can read
- calculate the mean and the standard deviation with Python
- draw a graph that has axis labels and units
- justify a conclusion with a graph.

## Starting level and prior skills

You do not need to know Python beforehand: you start from a ready-made program and change it. The principles of drawing a graph are in the guide [Graph of measurement points](tvt-kuvaaja.html) and calculating speed in the guide [Speed and distance from measurement data](tvt-nopeus-datasta.html).

## Equipment and materials

| Supply | Note |
|---|---|
| Raspberry Pi 5 or another computer | You need Python and, for graphs, the matplotlib library. |
| Display, keyboard and mouse | For the Raspberry Pi. |
| The group's measurements | From the flight log. |
| Flight video | Only for the Challenge yourself task. |

Here the Raspberry Pi is a computer with which data is processed. It does not control the drone, and it is not attached to the drone.

## Safety and induction

There is no flying in this work. See the topic [filming and privacy](ahjo-turvallisuus.html#drone-yksityisyys). It is in preparation until the school has approved it.

- Handle videos only on the school's devices. Do not transfer them to your own phone and do not publish them.
- If people are visible in a video, tell the teacher before you use it.

## Steps

1. Open a terminal and go to the folder where the files are.
2. Run the program with the example data: `python lentoanalyysi.py lentodata-esimerkki.csv`.
3. Read the output: for each series the number of measurements, the mean, the standard deviation and the range.
4. Open the example data in a text editor and see how it is written: the column names on the first row, after that one measurement per row.
5. Make your own file with the same structure. Write the quantity and the unit in the heading of the third column, for example `ajautuminen_cm`.
6. Run the program with your own file.
7. Look at the graph: do the measurements of the series overlap, or are they clearly apart?
8. Write the conclusion in one sentence.

## Diagrams and example code

The measurement file is a text file in which the columns are separated by a semicolon. The numbers below are made-up practice data.

```
sarja;toisto;etaisyys_cm
lahto 2 m;1;12,5
lahto 2 m;2;18,0
lahto 4 m;1;21,0
lahto 4 m;2;30,5
```

The core of the program reads the rows and calculates the statistics:

```python
import csv
import statistics

sarjat = {}
with open("lentodata-esimerkki.csv", encoding="utf-8") as f:
    rivit = [r for r in csv.reader(f, delimiter=";") if r and not r[0].startswith("#")]
for sarja, toisto, arvo in rivit[1:]:
    sarjat.setdefault(sarja, []).append(float(arvo.replace(",", ".")))

for nimi, arvot in sarjat.items():
    print(nimi, statistics.mean(arvot), statistics.stdev(arvot))
```

The mean is $\bar{x} = \dfrac{x_1 + x_2 + \dots + x_n}{n}$. The standard deviation tells how far the measurements typically are from the mean.

Speed from a video is calculated with the help of two consecutive positions: $v = \dfrac{\Delta x}{\Delta t}$, where $\Delta x$ is the change in position and $\Delta t$ the time between the frames.

## Test and measure

- Calculate the mean of one series with a calculator and compare it with the program's result.
- Add one clearly deviating measurement to the file. How do the mean and the standard deviation change?
- Show the graph to another group without an explanation. Do they conclude the same as you?

## If something does not work

- **The program does not find the file:** check that you are in the same folder and that the file name is written correctly.
- **An error in converting a number:** some row has text in the place of a number, or there is the wrong number of columns.
- **The graph is not drawn:** the matplotlib library is missing. Ask the teacher to install it. The statistics are still printed.
- **The standard deviation cannot be calculated:** the series has only one measurement. You need at least two.

## Extension

Change the program so that it plots the measurements in order of repetition. Does the graph show learning: do the results improve towards the end of the series?

## Document your work

Attach to your project diary

- a graph that has axis labels and units
- the statistics as a table
- the conclusion in one sentence
- what you would measure differently next time.

## For the teacher: preparation

- Install Python and matplotlib and run the starter program with the example data before the lesson. The program has been tried with the example data without the graph library; drawing the graph is worth trying on a school computer.
- There are 10 Raspberry Pi 5 computers. The Raspberry Pi 5 needs a power supply, a memory card, a display, a keyboard and a mouse. If they are not available, the work can be done on any computer that has Python.
- A computer vision project needs a camera, which is a separate purchase.
- Collect the groups' measurement files in a shared folder so that the groups can compare results.
- A video that suits video analysis is one in which the camera stays still, the drone moves in the plane of the picture and a scale is visible in the picture.
