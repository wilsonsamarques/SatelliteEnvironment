from gym.envs.registration import register

register(
    id='SatelliteEnvironment-v0',
    entry_point='SatelliteEnvironment.envs:SatelliteEnv',
    max_episode_steps=200,
)