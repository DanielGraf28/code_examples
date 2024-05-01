import copy
import random

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)
  def draw(self, num):
    if num > len(self.contents):
      return self.contents
    else:
      balls = []
      for i in range(num):
        ball = random.choice(self.contents)
        balls.append(ball)
        self.contents.remove(ball)
      return balls
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    balls = hat_copy.draw(num_balls_drawn)
    success = True
    for key, value in expected_balls.items():
      if balls.count(key) < value:
        success = False
        break
    if success:
      count += 1
  return count / num_experiments
