import copy
import random
# Consider using the modules imported above.

class Hat(object):

    def __init__(self, **balls):
        
        self.contents = []
        for color, number in balls.items():
            for index in range(number):
                self.contents.append(color)
        
        
    """
    * The Hat class should have a draw method that accepts an argument indicating the number of balls to draw from the hat. This method should remove balls at random from contents and return those balls as a list of strings. The balls should not go back into the hat during the draw, similar to an urn experiment without replacement. If the number of balls to draw exceeds the available quantity, return all the balls.
    """
    def draw(self,turns):
        draws_queue = []
        if turns >= len(self.contents):
            draws_queue = copy.deepcopy(self.contents)
            random.shuffle(draws_queue)
            self.contents.clear
            
            return draws_queue
        else:
            for turn in range(turns):
                color = random.choice(self.contents)
                self.contents.remove(color)
                draws_queue.append(color)
        return draws_queue
    
       
            

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0
    
    for try_number in range(num_experiments):
        
        clone_hat = copy.deepcopy(hat)
        clone_expected = copy.deepcopy(expected_balls)
        lucky_draws = clone_hat.draw(num_balls_drawn)
        
        for color in lucky_draws:

            if color in clone_expected.keys():
                clone_expected[color] -= 1 
        
        for color in clone_expected:
            if clone_expected[color] == 0 :
                success_count += 1 
                
    return success_count / num_experiments
        
        
        
        
