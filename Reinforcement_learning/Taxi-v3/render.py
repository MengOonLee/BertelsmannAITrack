import gym
import sys

env = gym.make('Taxi-v3')
env.seed(505)
state = env.reset()
score = 0
for _ in range(200):
    env.render()
    action = env.action_space.sample()
    state, reward, done, info = env.step(action)
    score += reward
    if done:
        break
        
print('Final score:', score)
env.close()
