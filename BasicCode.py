from kaggle_environments.envs.hungry_geese.hungry_geese import Observation, Configuration, Action, row_col
from kaggle_environments import evaluate, make, utils
import random

# Cada agente precisa ter sua função
def agent1(obs_dict, config_dict):
    return Action.SOUTH.name

def agent2(obs_dict, config_dict):
    return Action.NORTH.name


env = make("hungry_geese", debug=True)
env.run([agent1, agent2]) # Aqui escolhe o numero de agentes e a função que cada um vai utilizar
env.render(mode="ipython", width=500, height=350)
