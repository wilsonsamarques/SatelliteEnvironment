import os
import gym
import SatelliteEnvironment

import numpy as np
from DDPG_satellite_tensorflow import Agent
from utility import plotLearning

# Uncomment the lines below to specify which gpu to run on
#os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
#os.environ["CUDA_VISIBLE_DEVICES"] = "0"

if __name__ == '__main__':
    
    env = gym.make('SatelliteEnvironment-v0')

    
    
    agent = Agent(alpha=0.00005, beta=0.0005, input_dims=[2], tau=0.001,
                  env=env, batch_size=64, layer1_size=800, layer2_size=600,
                  n_actions=1)
    np.random.seed(0)
    score_history = []
    for i in range(1000):
        obs = env.reset()
        done = False
        score = 0
        while not done:
            act = agent.choose_action(obs)
            new_state, reward, done, info = env.step(act)
            agent.remember(obs, act, reward, new_state, int(done))
            agent.learn()
            score += reward
            obs = new_state
            #env.render()
            #print(reward)
        score_history.append(score)
        print('episode ', i, 'score %.2f' % score,
              'trailing 100 games avg %.3f' % np.mean(score_history[-100:]))

    filename = 'Pendulum-alpha00005-beta0005-800-600-optimized.png'
    plotLearning(score_history, filename, window=100)