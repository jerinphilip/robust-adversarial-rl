from IPython import display
import gym
import matplotlib.pyplot as plt
%matplotlib inline

env = gym.make('Breakout-v0') # insert your favorite environment
render = lambda : plt.imshow(env.render(mode='rgb_array'))
env.reset()
render()
