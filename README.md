# Grid-Based Multi-Agent Resource Collection and Movement Simulation

This project simulates multi-agent interactions on a grid. Agents move according to predefined patterns, collect resources, and handle collisions. Two variations of simulations are implemented:

1. **Energy-Based Simulation**:
   - Agents consume energy to move and gain energy from resources (food).
   - Tracks agent survival and collision dynamics.
2. **Scenario-Based Resource Collection**:
   - Agents collect resources over multiple scenarios.
   - Tracks resource collection and collisions across iterations.

---

## Features

### Energy-Based Simulation
- **Grid Environment**:
  - A `6x6` toroidal grid with wrapping boundaries.
  - Food (resources) is scattered randomly on the grid.
- **Agent Dynamics**:
  - Four agents with distinct movement directions:
    - Right, Down, Diagonal Up-Right, Left.
  - Energy management:
    - Initial energy: `2` units.
    - Energy loss per step: `1` (configurable).
    - Energy gain from food: `2` units.
- **Collision Handling**:
  - Agents lose energy upon collision and stop moving.
- **Simulation Metrics**:
  - Tracks steps, surviving agents, and total collisions.

### Scenario-Based Resource Collection
- **Grid Environment**:
  - A `4x4` toroidal grid.
  - Five resources randomly scattered in each scenario.
- **Agent Dynamics**:
  - Four agents with predefined starting positions and movement patterns.
  - Wrapping boundaries ensure continuous movement.
- **Collisions**:
  - Movement halts upon collision.
- **Simulation Metrics**:
  - Tracks total resources collected and collisions over 20 scenarios.

---

## Code Structure

### Energy-Based Simulation
1. **Food Scattering**:
   - Function: `scatter_food(num_food)`
   - Randomly places food on the grid, ensuring unique positions.
2. **Agent Movement**:
   - Function: `move_agents(agents, food)`
   - Updates positions, detects collisions, and manages energy.
3. **Simulation Loop**:
   - Function: `run_simulation(num_agents, num_food)`
   - Runs until all agents deplete their energy.

### Scenario-Based Simulation
1. **Resource Scattering**:
   - Function: `scatter_resources()`
   - Randomly places resources on the grid for each scenario.
2. **Agent Movement**:
   - Function: `move_agents(agent_positions)`
   - Moves agents and wraps their positions around the grid.
3. **Simulation Loop**:
   - Simulates 20 scenarios, tracking resource collection and collisions.

---

## How to Run

### Prerequisites
- Python 3.7 or higher.

### Running the Simulation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <project-folder>
