## Acoustic Wave Propagation Simulation with Cellular AutomataAcoustic Wave Propagation Simulation with Cellular Automata

This project simulates the propagation of acoustic waves using Cellular Automata (CA). The model is based on local interaction rules between cells in a 2D grid, where each cell represents a point in space with state variables such as sound pressure and particle velocity. The main objective is to analyze the Insertion Loss (IL) caused by different configurations of acoustic barriers.

The project is organized into three main files:

* config.py: Contains global settings such as scale and the grid size.
simulation.py: Implements the simulation, including the updates for pressure and velocity of the cells, as well as the calculation of Insertion Loss (IL) for different frequencies and barriers.
* main.py: Runs the simulation, generates the wave propagation visualization, and calculates and plots the Insertion Loss for different types of barriers.


### How It Works
1. Acoustic Wave Propagation Simulation
The simulation uses a 2D grid of cells, where each cell has a state (pressure and velocity) that interacts with neighboring cells. The propagation of acoustic waves is modeled based on pressure differences between neighboring cells and energy dissipation (attenuation).

2. Calculation of Insertion Loss (IL)
For different types of acoustic barriers (straight, "simple Y", and "double Y"), Insertion Loss is calculated based on the Fresnel Number (N), which describes how waves interact with the barrier. The insertion loss is calculated for a range of frequencies.

3. Visualization and Results
The visualization shows the evolution of sound pressure over time, allowing observation of how the wave propagates through the grid. The Insertion Loss (IL) vs frequency plot is generated for different barrier types, comparing the impact of each configuration.

### How to Run

* Requirements
* Python 3.x
* Poetry

Activate environment
```bash
poetry shell
```
Install Dependencies
```bash
poetry install
```

Execute choosing the type of wall

```bash
poetry run python main.py type_wall
```

The type_wall can be: 1, 2 or 3

To save the executin in video, use option "save"

Example:

```bash
poetry run python main.py 1 save
```

The video will save in the current folder