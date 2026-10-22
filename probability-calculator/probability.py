import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []

        for key, value in kwargs.items():
            self.contents.extend([key] * value)

    def draw(self, num_balls):

        drawn_balls = []

        for _ in range(min(num_balls, len(self.contents))):
            ball = self.contents.pop(random.randint(0, len(self.contents) - 1)) 

            drawn_balls.append(ball)  
        
        return drawn_balls

        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    successes = 0

    for _ in range(num_experiments):
        experiment_hat = copy.deepcopy(hat)
        drawn_balls = experiment_hat.draw(num_balls_drawn)

        for key, value in expected_balls.items():
            if drawn_balls.count(key) < value:
                break
        else: 
            successes += 1
    
    return successes / num_experiments
