from gym.envs.registration import register

register(
    id='sample-v0',
    entry_point='gym_sample.envs:SampleEnv',
)