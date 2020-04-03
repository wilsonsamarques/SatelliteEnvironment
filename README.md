# SatelliteEnvironment

This is an implementation of a RL environment that represents a Satellite attitude dynamics. This simulation was created following OpenAI's Gym environments structure. As the attitude control problem of a satellite requires a continuos action space, the RL algorithms that can be used for the control task are for example DDPG and PPO. At the present time only the DDPG algotihm is available.

To test the algorithms with the gym Pendulum-v0 environment, just change the line env = gym.make('SatelliteEnvironment-v0') to env = gym.make('Pendulum-v0'). And in case you want to visualize the Pendulum simulation, uncomment the line env.render().

Requirements:

- Tensorflow version 1.14.0
- keras
- numpy
- gym
