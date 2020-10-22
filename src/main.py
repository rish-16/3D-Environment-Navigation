import numpy as np
import gym
import gym_maze

from membuffs import get_lstm

env = gym.make("maze-sample-3x3-v0")
n_actions = env.action_space.n
obv_dim = env.observation_space.sample().shape

mem_buff = get_lstm(obv_dim)

while True:
    env.render()
    
    random_action = np.random.randint(0, n_actions)
    obs, reward, done, info = env.step(random_action)
    
    if done:
        print ("done")
        break