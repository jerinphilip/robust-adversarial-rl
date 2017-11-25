from pprint import pprint
from gym import envs
#xs = envs.registry.all()
#for x in xs:
#    print(x)

#import logging
#logger = logging.getLogger(__name__)
#logger.setLevel(logging.INFO)

import gym
#from gym_recording.wrappers import TraceRecordingWrapper
env = gym.make('InvertedPendulumAdv-v1')
#env = gym.make('Phoenix-v0')

#env = TraceRecordingWrapper(env)
#env.directory = "./"
#print(env.directory)

for i_episode in range(20000):
    observation = env.reset()
    for t in range(10000):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break

#print(env.directory)
