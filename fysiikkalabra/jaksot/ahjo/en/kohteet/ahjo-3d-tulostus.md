## Quick start

In ten minutes you see how long your own model takes to print and how much plastic it uses. Anyone may use the slicer. The printer is used only after the device induction, and until then your teacher starts the print.

1. Open PrusaSlicer and choose the profile your teacher has prepared (the printer and PLA).
2. Import your own model, for example the key ring from the 3D modelling quick start, or the teacher's ready-made model.
3. Press Slice and write down the print time and mass the program estimates.
4. Set the infill first to $10\,\%$ and then to $50\,\%$. Slice again and see how the time and the mass change.

### Try

Slice a model and read its print time and mass.

### Modify

Change the orientation, the layer height or the infill so that the print takes less than 15 minutes and the object is still usable.

### Challenge yourself

Work out the material cost of the print. Print the object after the induction and test its strength as in the Learn more part below.

## Challenge

Print your model so that the first layer sticks to the bed, the object withstands use and you know what the print cost. Once you can choose the print orientation and check the first layer, most failed prints never happen.

As the example you print the holder designed in [Basics of 3D modelling](ahjo-3d-mallinnus.html). The preparation takes about 30 minutes. The printing itself takes from half an hour to several hours, depending on the size of the object.

## Learning goals

After this work you can

- bring a model into a slicer and check its scale
- choose the print orientation so that the object withstands its load
- choose the layer height, infill and supports and justify your choices
- watch the first layer and stop the print if it fails
- calculate the material cost of a print and test its strength.

## Starting level and prior skills

You have a finished model in STL or 3MF format. You have had your teacher's induction to the printer you use. Nobody uses a printer without the induction.

## Equipment and materials

Ahjo's printers are still being acquired. The guide is written for an ordinary FDM printer, which prints from melted plastic filament one layer at a time. Device-specific settings will be added once the printers have been acquired.

| Item | Quantity |
|---|---|
| A 3D printer you are allowed to use | 1 |
| PrusaSlicer slicer | 1 |
| PLA filament | about $10\,\text{g}$ |
| Spatula for removing the print | 1 |
| Vernier calliper | 1 |
| Masses and a hook for the strength test | 1 set |
| Safety glasses for the strength test | 1 |

## Safety and induction

Ahjo's 3D printing safety instructions are being prepared: see the topic [3D printing safety](ahjo-turvallisuus.html#3d-tulostus). Until they are approved, follow your teacher's induction and at least these precautions:

- In use the nozzle is about $200\,{}^\circ\text{C}$ and the bed about $60\,{}^\circ\text{C}$. Do not touch either, and wait for the bed to cool before you remove the print.
- Do not reach into the printer while it moves. Tie your hair back and take off jewellery.
- Melting plastic releases fine particles into the air. Print only in a space with working ventilation, and do not sit next to the printer for the whole print.
- Remove the print with a spatula, pushing away from yourself.
- In the strength test a breaking piece can fly off. Wear safety glasses and do not stand under the masses.

## Steps

1. Open the slicer PrusaSlicer and choose the right printer and material (PLA).
2. Import the model. Check its dimensions: if the holder looks a hundred times too small or too large, the model was saved in the wrong unit.
3. Choose the print orientation. A printed object is strongest when the load runs along the layers, and weakest when the load tries to tear the layers apart. Lay the holder on its side so that the U-shaped cross-section is parallel to the bed. Then the arms withstand bending. The figure below shows the difference.
4. Choose the layer height $0.2\,\text{mm}$ and the infill $20\,\%$. A thinner layer makes the surface smoother but the print takes longer. More infill makes the object stronger and heavier.
5. Check whether supports are needed. If some part of the object is over empty space or slopes more than about $45^\circ$ from the vertical, it needs support. The holder lying on its side does not need supports.
6. Slice the model. Write down the print time and mass the program estimates.
7. Preview the layers. Scroll through the layers from the start and check that the first layer touches the bed over the whole base of the object.
8. Make sure the bed is clean, and start the print as your teacher has shown.
9. Watch the whole first layer. Compare it with the figure below. If the filament does not stick or the nozzle scrapes the bed, stop the print at once and tell your teacher.
10. When the print is ready, wait for the bed to cool. Remove the print and carefully take off any brim or supports.

## Diagrams and example code

The same beam in two print orientations. The thin lines are the print layers, and the red arrow is the force acting on the beam.

<svg data-fig="suunta"></svg>

The first layer in cross-section at three nozzle heights. In a good first layer the strands are slightly flattened and touch each other.

<svg data-fig="ensikerros"></svg>

## Test and measure

- Calculate the material cost. If the slicer estimates the mass as $m = 5\,\text{g}$ and filament costs $25\,\text{€}$ a kilogram, that is $0.025\,\text{€/g}$, the material costs $5\,\text{g} \cdot 0.025\,\text{€/g} \approx 0.13\,\text{€}$. Calculate the same for your own print.
- Weigh the print and compare its mass with the program's estimate.
- Strength test: print two identical straight beams, one lying down and one standing up. Clamp one end of the beam and hang masses on the other end, adding them gradually until the beam clearly bends or breaks. Record the largest mass each one held. Calculate the corresponding weight $G = mg$. For example, the weight of a $2.0\,\text{kg}$ mass is $G = 2.0\,\text{kg} \cdot 9.81\,\text{m/s}^2 \approx 20\,\text{N}$. Weight is explained in the chapter [Weight, friction and the inclined plane](fy4-6.html).

## If something does not work

| Symptom | Likely cause | Fix |
|---|---|---|
| The filament does not stick to the bed | The nozzle is too high or the bed is greasy | Stop the print. Ask your teacher to adjust the first layer height, and clean the bed. |
| The nozzle scrapes and the filament is thin and ridged | The nozzle is too low | Stop the print and ask your teacher to adjust the height. |
| The corners of the object lift off | The object shrinks as it cools | Add a brim and avoid draughts around the printer. |
| A part printed in mid-air sags | A support is missing | Add supports or turn the object. |
| The print has strings | The nozzle oozes during travel moves | Small strings can be removed when finishing. If there are many, tell your teacher. |
| The printer stops in the middle | The filament ran out or jammed | Do not try to open the printer yourself. Tell your teacher. |

## Extension

1. The effect of infill. Print the same beam with infills $10\,\%$, $20\,\%$ and $40\,\%$. Do the strength test and draw a graph of the largest mass held as a function of the infill. Is the dependence linear?
2. Trading time for quality. Slice the same model with layer heights $0.1\,\text{mm}$, $0.2\,\text{mm}$ and $0.3\,\text{mm}$, and record the print times. When is a slower print worth it?
3. A sustainable choice. Find out what is done with failed prints in Ahjo. Calculate how much material your class uses on failed prints during the course.

## Document your work

Record in your project diary

- the print orientation, layer height, infill and supports you chose and your reasons for them
- the estimated and weighed mass, the print time and the material cost
- a photo of the first layer and of the finished print
- the results of the strength test as a table
- if the print failed: a photo, the likely cause and what you changed. A well-documented failure is a valuable result.

## For the teacher: preparation

- This is a draft: Ahjo's printers have not been chosen yet, and the guide has not been tried on them. PrusaSlicer is used for slicing. Add the printer-specific profiles and settings and the print queue practice once the devices have been acquired.
- The safety points of the guide are general precautions. They do not replace the school's approved 3D printing safety instructions, which are still being prepared.
- Check the ventilation where the printers are placed, and whether a printer may be left running unsupervised.
- Print the beams for the strength test in advance if printing time is short. Reserve masses with a total of at least $3\,\text{kg}$.
- The strength test and the cost calculation link the work to physics (weight, the chapter [Weight, friction and the inclined plane](fy4-6.html)) and to entrepreneurship (the price of a product in Ahjo 2 projects).
- The structure of the guide was influenced by the project template of Prusa's educational materials. The text and figures were made for Ruukkilabra.
