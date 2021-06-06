import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **arguments):
        self.contents = list()
        for argument_name, argument_no in arguments.items():
            for i in range(argument_no):
                self.contents.append(argument_name)

    def draw(self, no_of_balls):
        list_balls_draw_return = list()
        for i in range(no_of_balls):
            random_item_from_list = random.choice(self.contents)
            list_balls_draw_return.append(random_item_from_list)
            self.contents.remove(random_item_from_list)
        return list_balls_draw_return


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    if num_balls_drawn >= len(hat.contents):
        return 1
    expected_contents = list()
    for argument_name, argument_no in expected_balls.items():
        for i in range(argument_no):
            expected_contents.append(argument_name)
    no_of_found = 0
    for j in range(num_experiments):
        len_balls = 0
        hat1 = copy.deepcopy(hat)
        expected_contents_copy = copy.deepcopy(expected_contents)
        for ball in hat1.draw(num_balls_drawn):
            if ball in expected_contents_copy:
                expected_contents_copy.remove(ball)
                len_balls += 1
                if len_balls >= len(expected_contents):
                    no_of_found += 1
                    break
    return no_of_found / num_experiments
