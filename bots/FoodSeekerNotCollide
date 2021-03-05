from kaggle_environments.envs.hungry_geese.hungry_geese import Observation, Configuration, Action, row_col
from kaggle_environments import evaluate, make, utils
import random

nl = 7
nc = 11

direction = [None,None,None,None]

#Checa se há algo na posição linha,coluna
def isEmpty(l, c, obs):
    #wrap vertical
    if l >= nl:
        l = 0
    if l < 0:
        l = nl-1   
    #wrap horizontal
    if c >= nc:
        c = 0
    if c < 0:
        c = nc-1
    for goose in obs.geese:
        for pos in goose:
            if (l * nc + c) == pos:
                return False
    return True

# Agent
def agent(obs_dict, config_dict):
    observation = Observation(obs_dict)
    configuration = Configuration(config_dict)
    player_index = observation.index
    player_goose = observation.geese[player_index]
    player_head = player_goose[0]
    player_row, player_col = row_col(player_head, configuration.columns)
    food = observation.food[0]
    food_row, food_column = row_col(food, configuration.columns)
    
    if food_row > player_row and isEmpty(player_row+1,player_col,observation) and direction[player_index] != Action.NORTH.name:
        direction[player_index] = Action.SOUTH.name
    elif food_row < player_row and isEmpty(player_row-1,player_col,observation) and direction[player_index] != Action.SOUTH.name:
        direction[player_index] = Action.NORTH.name 
    elif food_column > player_col and isEmpty(player_row,player_col+1,observation) and direction[player_index] != Action.WEST.name:
        direction[player_index] = Action.EAST.name
    elif isEmpty(player_row,player_col-1,observation) and direction[player_index] != Action.EAST.name:
        direction[player_index] = Action.WEST.name
    elif isEmpty(player_row+1,player_col,observation) and direction[player_index] != Action.NORTH.name:
        direction[player_index] = Action.SOUTH.name
    elif isEmpty(player_row-1,player_col,observation) and direction[player_index] != Action.SOUTH.name:
        direction[player_index] = Action.NORTH.name 
    else:
        direction[player_index] = Action.EAST.name
    
    return direction[player_index]
###

# Setup a hungry_geese environment and run agent vs a random.
env = make("hungry_geese", debug=True) # Set debug to False if you don't want the printed statements (or just remove the prints in the agent)
env.reset(num_agents = 1)
env.run([agent,agent])
env.render(mode="ipython", width=500, height=450)
