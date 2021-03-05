from kaggle_environments.envs.hungry_geese.hungry_geese import Observation, Configuration, Action, row_col
from kaggle_environments import evaluate, make, utils

# Cada agente precisa ter sua função, é aqui dentro que temos que encapsular todo o bot
def agent(obs_dict, config_dict):
    return Action.EAST.name

#Funções que rodam o jogo
env = make("hungry_geese", debug=True)
env.run([agent, agent]) # Aqui escolhe o numero de agentes e a função que cada um vai utilizar
env.render(mode="ipython", width=500, height=350)
