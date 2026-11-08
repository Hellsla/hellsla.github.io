## Challenge

Design a holder that clips onto the edge of a table without screws and keeps a charger cable in place. The holder works if it goes onto the table edge when you press it by hand, stays in place and does not scratch the table. This only works if you measure accurately and leave the right clearance in your dimensions.

The work takes one session of about 75 minutes. The model is printed following the guide [Getting started with 3D printing](ahjo-3d-tulostus.html).

## Learning goals

After this work you can

- measure an object with a vernier calliper and record the dimensions with their units
- build a model from basic shapes by adding and subtracting solids
- explain what clearance means and why the dimensions of a printed part cannot be exactly the same as those of the part it fits
- save the model in a printable format (STL or 3MF)
- estimate the object's volume and mass before printing.

## Starting level and prior skills

You do not need any experience of 3D modelling. You need a Tinkercad account, given by your teacher or created as the school instructs. Calculating areas and volumes and the idea of density (the chapter [Density](fy1-7.html)) help you estimate the mass.

## Equipment and materials

You model in Tinkercad, which runs in a browser and needs no installation. Once you know the basics, you continue in Onshape, which also runs in a browser and lets you give dimensions as variables (extension 2). Fusion is an alternative for those who want an installed program. Ahjo's computers are still being acquired.

| Item | Quantity |
|---|---|
| Computer and a mouse with a scroll wheel | 1 |
| Tinkercad account (later an Onshape account) | 1 |
| Vernier calliper | 1 |
| Squared paper and a pencil for a sketch | 1 |
| A table or a board to make the holder for | 1 |

## Safety and induction

Modelling is screen work. Take a break about every half hour and adjust your chair and screen to a suitable height. The jaws of a calliper are sharp, so handle it with care. Ahjo's safety instructions are being prepared, and printing safety is covered in the topic [3D printing safety](ahjo-turvallisuus.html#3d-tulostus).

## Steps

1. Measure the thickness of the table top with the calliper at three different points and calculate the mean. Record the result to a tenth of a millimetre, for example $t = 18.0\,\text{mm}$.
2. Choose the clearance $v$. When two parts fit together they need a gap between them, because a printer does not make the dimensions exactly right and printed plastic is often slightly wider than designed. Try $v = 0.4\,\text{mm}$ first. If you want to make sure of a suitable clearance, print a fit test first (extension 1).
3. Calculate the gap between the holder's arms:
   $$\begin{aligned}&a = t + v\\ &= 18.0\,\text{mm} + 0.4\,\text{mm}\\ &= 18.4\,\text{mm}.\end{aligned}$$
4. Draw the holder's cross-section on squared paper and mark its dimensions: arm length $30\,\text{mm}$, wall thickness $4\,\text{mm}$, the gap between the arms $a$ and the holder's width $20\,\text{mm}$. The figure below shows what the cross-section looks like.
5. In the modelling program, make a solid box the size of the holder's outer dimensions: depth $30\,\text{mm}$, height $a + 2 \cdot 4\,\text{mm} = 26.4\,\text{mm}$ and width $20\,\text{mm}$.
6. Make a second box as high as the gap between the arms: height $a = 18.4\,\text{mm}$, depth $30\,\text{mm}$ and width $24\,\text{mm}$. It is wider than the holder so that it surely goes through the sides. Turn it into a hole, that is, a solid to be removed (in Tinkercad, choose Hole in the shape's settings).
7. Place the hole so that its bottom edge is $4\,\text{mm}$ above the bottom edge of the first box, it reaches $2\,\text{mm}$ past each side, and a $4\,\text{mm}$ thick wall is left behind its back edge. The front end of the hole is then outside the holder. Select both and group them (in Tinkercad, Group or Ctrl + G). Now you have a U-shaped holder.
8. Add a hook for the cable: a small cylinder on the holder's top, from which you remove a cylinder as thick as the cable and a narrow slot for pressing the cable in. Measure the cable's diameter and add clearance to it as well.
9. Round or chamfer the edges facing the table if the program has a tool for it. A sharp edge scratches the table.
10. Check the dimensions with the program's ruler tool and save the model as STL or 3MF. Name the file so that it shows the maker and the version, for example `holder_v1_smith.stl`.

## Diagrams and example code

In most modelling programs a hole is made as a solid that is subtracted from another. Make the hole solid slightly longer than the solid it is removed from. Then the hole surely goes through and no thin skin is left on the surface.

<svg data-fig="csg"></svg>

The holder's cross-section on the edge of the table. The clearance is drawn much larger than it really is.

<svg data-fig="pidike"></svg>

In a fit test, holes of several sizes are made in the same piece. A peg is tried in the holes, which shows what clearance works on this particular printer.

<svg data-fig="sovitekoe"></svg>

## Test and measure

- Estimate the holder's volume before printing. Divide the cross-section into rectangles: two arms ($30\,\text{mm} \cdot 4\,\text{mm}$) and the wall between them ($18.4\,\text{mm} \cdot 4\,\text{mm}$). Multiply the area of the cross-section by the holder's width. The volume comes to about $6.3\,\text{cm}^3$.
- Calculate how much a solid holder would weigh in PLA plastic, whose density is $\rho = 1.24\,\text{g/cm}^3$. Compare the result with the slicer's estimate when you print the holder. Why is the program's estimate smaller?
- When the holder has been printed, measure the gap between its arms with the calliper and compare it with your designed value $a$. Write down the difference. It tells you how accurately the printer makes dimensions.

## If something does not work

| Symptom | Likely cause | Fix |
|---|---|---|
| The hole does not show in the model | The solids are not grouped, or the hole solid is not a hole | Select both and group them. Check that the solid to be removed is marked as a hole. |
| A thin skin is left at the bottom of the hole | The hole is exactly as long as the solid | Make the hole solid longer so that it goes past both ends. |
| The holder does not fit on the table edge | The clearance is too small or the thickness was measured wrong | Measure again. Increase the clearance $0.2\,\text{mm}$ at a time. |
| The holder is loose | The clearance is too large | Reduce the clearance or add a small bump on the arms that presses on the board. |
| The model is the wrong size in the slicer | The unit changed when saving | Check that the program uses millimetres. |

## Extension

1. Fit test. Model a test piece with four holes of diameters $10.0\,\text{mm}$, $10.2\,\text{mm}$, $10.4\,\text{mm}$ and $10.6\,\text{mm}$, and a peg of diameter $10.0\,\text{mm}$. Print them and record which hole is tight, which is right and which is loose.
2. Parametric model in Onshape. Draw the holder's U-shaped cross-section as a sketch and extrude it to a width of $20\,\text{mm}$. Make the dimensions variables ($t$, $v$, wall thickness). Then you get the same holder for different tables by changing one number.
3. User-centred design. Ask a classmate what they would keep on the edge of a table: headphones, a bag or a phone. Change the holder to meet their need.

## Document your work

Record in your project diary

- the measured thicknesses, their mean and the clearance you chose, with your reasons
- your sketch with dimensions and a screenshot of the finished model
- your volume and mass estimates with the calculations
- the measured gap between the arms of the print and its difference from the design
- what you would change in the next version and why.

## For the teacher: preparation

- This is a draft: the guide has not yet been tried on Ahjo's computers. The chosen programs are Tinkercad to start with and Onshape to continue (both in a browser, no installation). Before the first session, check both programs' terms of use and age limits and how the students sign in (for example Tinkercad's teacher classroom).
- Reserve at least one calliper for every two students.
- If printing time is short, print the fit test in advance on one printer and give the students a suitable clearance ready-made.
- Estimating the mass links the work to the physics chapter [Density](fy1-7.html), and developing the object for a user leads into the design process of the Ahjo 2 course.
- The structure of the guide was influenced by the project template of Prusa's educational materials. The text and figures were made for Ruukkilabra.
