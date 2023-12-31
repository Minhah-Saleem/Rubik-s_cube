from cubeEnv import CubeEnv


class CubeAgent:

    def __init__(self, number_of_cubes=3, batches=10):

        self.env = [[CubeEnv() for x in range(batches)] for y in range(number_of_cubes)]
        self.number_of_cubes = number_of_cubes
        self.batches = batches

    def scramble_cubes_for_data(self):

        for i in range(self.number_of_cubes):
            j = 1
            while j < self.batches:
                self.env[i][j].cube = self.env[i][j-1].cube.copy()
                self.env[i][j].scramble()
                j += 1

    def reset_envs(self, number_of_turns=None):
        if number_of_turns is None:
            number_of_turns = [0] * self.number_of_cubes
        i = 0
        while i < self.number_of_cubes:
            self.env[i].reset(number_of_turns[i])
            i += 1
            
    def take_actions(self, action_function):
        for i in range(self.number_of_cubes):
            for j in range(self.batches):
                action = action_function(self.env[i][j].get_one_hot_state())
                # Assuming action_function takes a state representation and returns an action
                self.env[i][j].step(action)
