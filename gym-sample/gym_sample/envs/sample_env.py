import gym
import json
from gym import error, spaces, utils
from gym.utils import seeding

class SampleEnv(gym.Env):
  metadata = {'render.modes': ['human']}
  def __init__(self):
      self.reset()
      self.action_space = gym.spaces.Discrete(4)
      self.observation_space = gym.spaces.Discrete(25)
    
  def step(self, action):
    for row, cols in enumerate(self.state):
        for col, val in enumerate(cols):
            if val == 1:
                if action == 0:
                    if row-1 < 0:
                        return (row)*5+col, -1, False, 'hi'
                    else: 
                        if self.state[row-1][col] == 0:
                            self.state[row-1][col] = 1
                            self.state[row][col] = 0
                            return (row-1)*5+col, 1, False, 'hi'
                        elif self.state[row-1][col] == -1:
                            return (row)*5+col, -1, False, 'hi'
                        elif self.state[row-1][col] == -2:
                            self.state[row-1][col] = 1
                            self.state[row][col] = 0
                            return (row-1)*5+col, -20, True, 'hi'
                        elif self.state[row-1][col] == 2:
                            self.state[row-1][col] = 1
                            self.state[row][col] = 0
                            return (row-1)*5+col, 20, True, 'hi'
                if action == 1:
                    if row+1 > 4:
                        return (row)*5+col, -1, False, 'hi'
                    else:
                        if self.state[row+1][col] == 0:
                            self.state[row+1][col] = 1
                            self.state[row][col] = 0
                            return (row+1)*5+col, 1, False, 'hi'
                        elif self.state[row+1][col] == -1:
                            return (row)*5+col, -1, False, 'hi'
                        elif self.state[row+1][col] == -2:
                            self.state[row+1][col] = 1
                            self.state[row][col] = 0
                            return (row+1)*5+col, -20, True, 'hi'
                        elif self.state[row+1][col] == 2:
                            self.state[row+1][col] = 1
                            self.state[row][col] = 0
                            return (row+1)*5+col, 20, True, 'hi'
                if action == 2:
                    if col-1 < 0:
                        return (row)*5+col, -1, False, 'hi'
                    else:
                        if self.state[row][col-1] == 0:
                            self.state[row][col-1] = 1
                            self.state[row][col] = 0
                            return (row)*5+col-1, 1, False, 'hi'
                        elif self.state[row][col-1] == -1:
                            return (row)*5+col, -1, False, 'hi'
                        elif self.state[row][col-1] == -2:
                            self.state[row][col-1] = 1
                            self.state[row][col] = 0
                            return (row)*5+col-1, -20, True, 'hi'
                        elif self.state[row][col-1] == 2:
                            self.state[row][col-1] = 1
                            self.state[row][col] = 0
                            return (row)*5+col-1, 20, True, 'hi'
                if action == 3:
                    if col+1 > 4:
                        return (row)*5+col, -1, False, 'hi'
                    else:
                        if self.state[row][col+1] == 0:
                            self.state[row][col+1] = 1
                            self.state[row][col] = 0
                            return (row)*5+col+1, 1, False, 'hi'
                        elif self.state[row][col+1] == -1:
                            return (row)*5+col, -1, False, 'hi'
                        elif self.state[row][col+1] == -2:
                            self.state[row][col+1] = 1
                            self.state[row][col] = 0
                            return (row)*5+col-1, -20, True, 'hi'
                        elif self.state[row][col+1] == 2:
                            self.state[row][col+1] = 1
                            self.state[row][col] = 0
                            return (row)*5+col+1, 20, True, 'hi'
                else:
                    return (row)*5+col, 0, True, 'hi'

  def reset(self):
      self.state = [
          [0,0,0,0,0],
          [0,-1,0,0,2],
          [0,-1,0,0,-2],
          [0,0,-1,0,0],
          [1,0,0,0,0],
        ]
      return 20
    
  def render(self, mode='human', close=False):
      return json.dumps(self.state)