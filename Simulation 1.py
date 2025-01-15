import random

#defining grid, resources, and scenario
GRID_SIZE = 4
NUM_RESOURCES = 5
NUM_SCENARIOS = 20

#agents' starting positions and movement directions
start_positions = [(0, 0), (0, 3), (3, 3), (3, 0)]
move_directions = [(0, 1), (1, 0), (-1, 1), (0, -1)]

#scatter resources randomly on the grid
def scatter_resources():
    #empty set to store UNIQUE resource positions
    positions = set()
    #loop and generate unique positions
    for _ in range(NUM_RESOURCES):
        x = random.randint(0, GRID_SIZE - 1)  #Random x-coordinate (row)
        y = random.randint(0, GRID_SIZE - 1)  #Random y-coordinate (column)
        positions.add((x, y))  # Add the (x, y) position to the set
    return positions  # Return the set of resource positions

#move agents and wrap around grid
def move_agents(agent_positions):
    new_positions = []  #list to store updated agent positions
    #iterate over the index of each agent
    for i in range(len(agent_positions)):
        x, y = agent_positions[i]  #get the current position of the agent
        dx, dy = move_directions[i]  #get the movement direction of the agent
        #calculate new position with wrapping around the grid
        new_x = (x + dx) % GRID_SIZE  #new wrapped x position
        new_y = (y + dy) % GRID_SIZE  #new wrapped y position
        new_positions.append((new_x, new_y))  #store new position
    return new_positions  #return the list of new positions






#running the 20 scenarios/simulations
total_resources, total_collisions = 0, 0
for _ in range(NUM_SCENARIOS):
    agent_positions = start_positions[:]
    resources = scatter_resources()
    collected, collisions = 0, 0

    for _ in range(GRID_SIZE):
        new_positions = move_agents(agent_positions)

        #check for collisions
        if len(new_positions) != len(set(new_positions)):
            collisions += 1
            new_positions = agent_positions  #stop movement on collision

        #collect resources
        collected += sum(1 for pos in new_positions if pos in resources)
        resources -= set(new_positions)

        agent_positions = new_positions

    total_resources += collected
    total_collisions += collisions


#print results
print(f"Total resources collected: {total_resources}")
print(f"Total collisions: {total_collisions}")
