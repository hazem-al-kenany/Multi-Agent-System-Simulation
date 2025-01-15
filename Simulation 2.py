import random

#grid size and energy
GRID_SIZE = 6
INITIAL_ENERGY = 2
ENERGY_LOSS_PER_STEP = 1
ENERGY_GAIN_FROM_FOOD = 2

#movement directions for the four agents (sheep)
move_directions = [
    (0, 1),   #sheep 1 moves right
    (1, 0),   #sheep 2 moves down
    (-1, 1),  #sheep 3 moves diagonally up-right
    (0, -1)   #sheep 4 moves left
]

#scatter food on the grid randomly
def scatter_food(num_food):
    food_positions = set()  #empty set to store UNIQUE food positions

    #loop to generate food positions based on the number of food items
    for _ in range(num_food):
        x = random.randint(0, GRID_SIZE - 1)  #random x (row) position
        y = random.randint(0, GRID_SIZE - 1)  #random y (column) position
        food_positions.add((x, y))  #add food position to the set

    return food_positions  #return the set of food positions

#move agents, check collisions, food, and energy
def move_agents(agents, food):
    new_positions = []
    collisions = 0

    #move each agent and check collisions
    for i in range(len(agents)):
        x, y = agents[i]['position']  #get current position of agent
        if agents[i]['energy'] > 0:  #check if agent has energy
            dx, dy = move_directions[i % len(move_directions)]  #get movement direction
            new_x = (x + dx) % GRID_SIZE  #calculate new x position (with wrapping)
            new_y = (y + dy) % GRID_SIZE  #calculate new y position (with wrapping)
        else:
            new_x, new_y = x, y  #agent stays in place if it has no energy
        new_positions.append((new_x, new_y))  #store either new or unchanged position


    #detect collisions
    if len(new_positions) != len(set(new_positions)):
        collisions += 1
        for i in range(len(new_positions)):
            if new_positions.count(new_positions[i]) > 1: #checks if there is more than 1 agent in the same position
                agents[i]['energy'] -= ENERGY_LOSS_PER_STEP
                new_positions[i] = agents[i]['position']  #no movement in case of collision

    #food consumption and energy loss loop
    for i in range(len(agents)):
        if agents[i]['energy'] > 0:  #check if the agent has energy
            agents[i]['position'] = new_positions[i]  #update the agent's position
            if new_positions[i] in food:  #check if the agent is on a food item
                agents[i]['energy'] += ENERGY_GAIN_FROM_FOOD  #agent gains energy from food
                food.remove(new_positions[i])  #remove the consumed food from the grid
            agents[i]['energy'] -= ENERGY_LOSS_PER_STEP  #agent loses energy after the move

    return food, collisions

#run
def run_simulation(num_agents, num_food):
    agents = [{'position': (0, 0), 'energy': INITIAL_ENERGY},
              {'position': (0, GRID_SIZE - 1), 'energy': INITIAL_ENERGY},
              {'position': (GRID_SIZE - 1, GRID_SIZE - 1), 'energy': INITIAL_ENERGY},
              {'position': (GRID_SIZE - 1, 0), 'energy': INITIAL_ENERGY}] * (num_agents // 4) #this is so number num_agents can be an easy variable to change - here the 4s cancel out

    food = scatter_food(num_food)
    total_steps = 0
    total_collisions = 0

    #run until all agents have no energy left
    while any(agent['energy'] > 0 for agent in agents):
        food, collisions = move_agents(agents, food)
        total_steps += 1
        total_collisions += collisions

    alive_agents = sum(agent['energy'] > 0 for agent in agents)
    return total_steps, alive_agents, total_collisions

#test 1: adding more agents
test1_steps, test1_alive, test1_collisions = run_simulation(num_agents=8, num_food=5)
print(f"Test 1 - More Agents (8 agents): Steps: {test1_steps}, Alive Agents: {test1_alive}, Collisions: {test1_collisions}")

#test 2: changing the food spawn rate
test2_steps, test2_alive, test2_collisions = run_simulation(num_agents=4, num_food=10)
print(f"Test 2 - Higher Food Spawn Rate (10 food): Steps: {test2_steps}, Alive Agents: {test2_alive}, Collisions: {test2_collisions}")

#test 3: modifying parameters (less energy loss per step)
ENERGY_LOSS_PER_STEP = 0.5  # Agents lose less energy per step
test3_steps, test3_alive, test3_collisions = run_simulation(num_agents=4, num_food=5)
print(f"Test 3 - Less Energy Loss (0.5 per step): Steps: {test3_steps}, Alive Agents: {test3_alive}, Collisions: {test3_collisions}")