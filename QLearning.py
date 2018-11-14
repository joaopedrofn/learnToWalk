import numpy as np
import random

class QLearning:
    def __init__(self,env, max_steps):
        self.env = env
        self.max_steps = max_steps
        self.qTable = np.zeros((env.observation_space.n, env.action_space.n))
        self.state = 20
        self.score = 0
        self.total_rewards = 0
        self.rewards = []
    
    def train(self, episodes, learning_rate, gamma, epsilon, max_epsilon, min_epsilon, decay_rate):
        for episode in range(episodes):
            state = self.env.reset()
            step = 0
            done = False
            
            for step in range(self.max_steps):
                tradeoff = random.uniform(0,1)
                if tradeoff > epsilon:
                    action = np.argmax(self.qTable[state, :])
                else:
                    action = self.env.action_space.sample()
                test = self.env.step(action)
                new_state, reward, done, info = test
                self.qTable[state, action] = self.qTable[state, action] + learning_rate * (reward + gamma * np.max(self.qTable[new_state, :]) - self.qTable[state, action])
                state = new_state
                if done == True:
                    break
            episode += 1
            epsilon = min_epsilon + (max_epsilon - min_epsilon)*np.exp(-decay_rate*episode)
        print('Training Complete!')
        print(self.qTable)

    def execute(self, tests, show_renders = False):
        self.env.reset()
        rewards = []

        for episode in range(tests):
            state = self.env.reset()
            step = 0
            done = False
            total_rewards = 0
            
            for step in range(self.max_steps):
                if show_renders: print(self.env.render())
                action = np.argmax(self.qTable[state, :])
                new_state, reward, done, info = self.env.step(action)
                total_rewards += reward
                if done:
                    rewards.append(total_rewards)
                    break
                state = new_state
        print ("Score over time: " +  str(sum(rewards)/tests))
    
    def ai_step(self):
        action = np.argmax(self.qTable[self.state, :])
        new_state, reward, done, info = self.env.step(action)
        self.total_rewards += reward
        if done:
            self.rewards.append(self.total_rewards)
            break
        self.state = new_state
        return {
            'action': action,
            'state': self.env.render(),
            'rewards': self.rewards,
            'qTable': self.qTable,
            'done': done
        }

    def close(self):
        self.env.close()
