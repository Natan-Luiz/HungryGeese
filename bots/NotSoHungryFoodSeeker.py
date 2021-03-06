from kaggle_environments.envs.hungry_geese.hungry_geese import Observation, Configuration, Action, row_col
from kaggle_environments import evaluate, make, utils
import random
import math

nl = 7
nc = 11

direction = [None,None,None,None]
eaten = [40,40,40,40]

def Distance(l,c,l1,c1):
    ld = abs(l1 - l)
    cd = abs(c1 - c)
    return ld + cd
    

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

def getClosestObstacle(l,c,obs):
    close_l = 99 
    close_c = 99
    for goose in obs.geese:
        for pos in goose:
            l1 = int(pos /nc)
            c1 = pos%nc
            if(abs(close_l-l) > abs(l1 - l)):
                close_l = l1
            if(abs(close_c-c) > abs(c1 - c)):
                close_c = c1
      
    return close_l, close_c

# Agent
def agent(obs_dict, config_dict):
    observation = Observation(obs_dict)
    configuration = Configuration(config_dict)
    player_index = observation.index
    player_goose = observation.geese[player_index]
    player_head = player_goose[0]
    player_row, player_col = row_col(player_head, configuration.columns)
    
    food_row, food_column = row_col(observation.food[0], configuration.columns)
    food_row1, food_column1 = row_col(observation.food[1], configuration.columns)
    
    if(Distance(food_row,food_column,player_row,player_col) > Distance(food_row1,food_column1,player_row,player_col)):
        food_row = food_row1
        food_column = food_column1
    
    
    if(eaten[player_index] > 20):
        if food_row > player_row and isEmpty(player_row+1,player_col,observation) and direction[player_index] != Action.NORTH.name:
            direction[player_index] = Action.SOUTH.name
            if(Distance(player_row,player_col,food_row,food_column) < 2):
                eaten[player_index] = 0
        elif food_row < player_row and isEmpty(player_row-1,player_col,observation) and direction[player_index] != Action.SOUTH.name:
            direction[player_index] = Action.NORTH.name 
            if(Distance(player_row,player_col,food_row,food_column) < 2):
                eaten[player_index] = 0
        elif food_column > player_col and isEmpty(player_row,player_col+1,observation) and direction[player_index] != Action.WEST.name:
            direction[player_index] = Action.EAST.name
            if(Distance(player_row,player_col,food_row,food_column) < 2):
                eaten[player_index] = 0
        elif isEmpty(player_row,player_col-1,observation) and direction[player_index] != Action.EAST.name:
            direction[player_index] = Action.WEST.name
            if(Distance(player_row,player_col,food_row,food_column) < 2):
                eaten[player_index] = 0
        elif isEmpty(player_row+1,player_col,observation) and direction[player_index] != Action.NORTH.name:
            direction[player_index] = Action.SOUTH.name
        elif isEmpty(player_row-1,player_col,observation) and direction[player_index] != Action.SOUTH.name:
            direction[player_index] = Action.NORTH.name 
        else:
            direction[player_index] = Action.EAST.name
            
    else:
        enemy_row, enemy_col = getClosestObstacle(player_row,player_col,observation)
        if enemy_row < player_row and isEmpty(player_row+1,player_col,observation) and direction[player_index] != Action.NORTH.name:
            direction[player_index] = Action.SOUTH.name
        elif enemy_row > player_row and isEmpty(player_row-1,player_col,observation) and direction[player_index] != Action.SOUTH.name:
            direction[player_index] = Action.NORTH.name 
        elif enemy_col < player_col and isEmpty(player_row,player_col+1,observation) and direction[player_index] != Action.WEST.name:
            direction[player_index] = Action.EAST.name
        
        elif isEmpty(player_row,player_col-1,observation) and direction[player_index] != Action.EAST.name:
            direction[player_index] = Action.WEST.name
        elif isEmpty(player_row+1,player_col,observation) and direction[player_index] != Action.NORTH.name:
            direction[player_index] = Action.SOUTH.name
        elif isEmpty(player_row-1,player_col,observation) and direction[player_index] != Action.SOUTH.name:
            direction[player_index] = Action.NORTH.name 
        else:
            direction[player_index] = Action.EAST.name
    
    eaten[player_index] = eaten[player_index] + 1
    return direction[player_index]
###

# Setup a hungry_geese environment and run agent vs a random.
env = make("hungry_geese", debug=True) # Set debug to False if you don't want the printed statements (or just remove the prints in the agent)
env.reset(num_agents = 1)
env.run([agent,agent,agent,agent])
env.render(mode="ipython", width=500, height=450)
