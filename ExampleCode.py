from kaggle_environments.envs.hungry_geese.hungry_geese import Observation, Configuration, Action, row_col
from kaggle_environments import evaluate, make, utils

# Agent
def agent(obs_dict, config_dict):
    """This agent always moves toward observation.food[0] but does not take advantage of board wrapping"""
    #print("Config dict", config_dict) # Config is static
    print("Observation dict", obs_dict) # This changes over each timestep (your observations change over time poggers)
   # print(obs_dict['step']) # This and obs_dict.step are the exact same. No idea which one's better.
    print("config dict", config_dict)
    observation = Observation(obs_dict) # -> Why is obs_dict wrapped in Observation? What does that do vs just obs_dict?
   # print('ho', observation)
    
    configuration = Configuration(config_dict)
    player_index = observation.index
    player_goose = observation.geese[player_index]
    player_head = player_goose[0]
    player_row, player_column = row_col(player_head, configuration.columns)
    food = observation.food[0]
    food_row, food_column = row_col(food, configuration.columns)

    if food_row > player_row:
        return Action.SOUTH.name
    if food_row < player_row:
        return Action.NORTH.name
    if food_column > player_column:
        return Action.EAST.name
    return Action.WEST.name

###



# Setup a hungry_geese environment and run agent vs a random.
env = make("hungry_geese", debug=True) # Set debug to False if you don't want the printed statements (or just remove the prints in the agent)
env.run([agent, agent,agent,agent])
env.render(mode="ipython", width=500, height=350)
