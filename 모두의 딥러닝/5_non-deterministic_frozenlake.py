import gym
import numpy as np
import matplotlib.pyplot as plt

"""
이번 파트 핵심은 learning rate과 Q learning의 변형
"""

env = gym.make("FrozenLake-v0")

# Initialize table with all zeros
Q = np.zeros([env.observation_space.n, env.action_space.n])

# Set learning rate
learning_rate = 0.85
dis = 0.99 #discount
num_episodes = 2000

rList = []
for i in range(num_episodes):
    # Reset environment and get first new observation
    state = env.reset()
    rAll = 0
    done = False

    # The Q-Table learning algorithm
    while not done:
        action = np.argmax(Q[state, :] + np.random.randn(1, env.action_space.n) / (i+1))

        # Get new state and reward from environment
        new_state, reward, done, _ = env.step(action)

        # Update Q-Table with new knowledge using learning rate
        Q[state, action] = (1-learning_rate) * Q[state,action] \
            + learning_rate * (reward + dis*np.max(Q[new_state, :]))

        rAll += reward
        state = new_state
    rList.append(rAll)

# Report results
print("score over time: " + str(sum(rList)/num_episodes))
print("Final Q-Table Values")
print(Q)
plt.bar(range(len(rList)), rList, color='blue')
plt.show()
