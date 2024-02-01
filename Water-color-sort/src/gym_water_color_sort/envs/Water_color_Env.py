import gym
from gym import spaces
import numpy as np
from tf_agents.trajectories import time_step as ts


class WaterColorPuzzleEnv(gym.Env):

    metadata = {'render.modes': ['human']}

    def __init__(self, num_vials = 5, num_colors= 3, water_capacity=3, num_empty_vials=2):
        super(WaterColorPuzzleEnv, self).__init__()
        self.num_vials = num_vials
        self.num_colors = num_colors
        self.water_capacity = water_capacity
        self.num_empty_vials = num_empty_vials
        

        # Define the action space
        self.action_space = spaces.Discrete(num_vials * (num_vials - 1))
        # Define the observation space
        self.observation_space = spaces.Box(low=0, high=num_colors, shape=(num_vials * water_capacity,), dtype=np.int32)
        # Initialize other variables
        self.max_steps = 200
        

    def _generate_initial_state(self):
        observation = []
        for i in range(1, (self.num_colors + 1)):
            for j in range(self.water_capacity):
                observation.append(i)

        np.random.shuffle(observation)
        observation = observation + [0] * (self.num_vials * self.water_capacity - len(observation))

        return np.array(observation)

    def _check_game_over(self):
        
        for color in range(1, self.num_colors + 1):
            pattern = [color] * self.water_capacity
            if not any(np.array_equal(self.state[i:i + self.water_capacity], pattern) for i in range(0, len(self.state), self.water_capacity)):
                return False
        return True

    def _can_pour_to_vial(self, vial):

        return any(color == 0 for color in self.state[vial:vial + self.num_colors])

    def _can_pour_from_vial(self, vial):
        vial_contents = self.state[vial:vial + self.num_colors]
        return any(color != 0 for color in vial_contents)

    def _action_to_vials(self, action):
        source_vial = action % self.num_vials
        destination_vial = ((action // self.num_vials) + 1 + source_vial) % self.num_vials
        return source_vial * 3, destination_vial * 3

    def observation_and_action_splitter(self, source_vial, destination_vial):
        action_mask = [0] * (self.num_vials * (self.num_vials - 1))

        for action in range(0, self.num_vials * (self.num_vials - 1)):
            source_vial, destination_vial = self._action_to_vials(action)

            if self._can_pour_from_vial(source_vial) and self._can_pour_to_vial(destination_vial)and self.check_permutation_condition(source_vial, destination_vial):
                action_mask[action] = 1  # valid action 

        return action_mask

    def _pour_color_action(self, source_vial, destination_vial, source_color, last_non_zero_index, destination_index):
        new_state = np.copy(self.state)
        new_state[source_vial + last_non_zero_index], new_state[destination_vial + destination_index] = new_state[destination_vial + destination_index], source_color
        return new_state

    def check_full_vial(self, vial):
        # Check if the vial is full with the same color
        vial_contents = [self.state[vial + i] for i in range(self.num_colors)]
        if all(color == vial_contents[0] for color in vial_contents) and vial_contents[0] != 0:
            return True
        return False

    def get_pour_parameters(self, source_vial, destination_vial):
        # Obtain the colors from the source and destination vials
        content_source_vial = [self.state[source_vial + i] for i in range(self.num_colors)]
        content_destination_vial = [self.state[destination_vial + i] for i in range(self.num_colors)]

        # Find the last non-zero index in the source vial
        last_non_zero_index = len(content_source_vial) - 1 - content_source_vial[::-1].index(next((color for color in content_source_vial[::-1] if color != 0), 0))

        # Get the source color
        source_color = content_source_vial[last_non_zero_index]

        # Find the color before zero in the destination vial
        color_before_zero = next((color for color in reversed(content_destination_vial) if color != 0), None)

        # Get the destination index where the color will be poured
        destination_index = content_destination_vial.index(0)

        return source_color, color_before_zero, last_non_zero_index, destination_index



    def check_permutation_condition(self, source_vial, destination_vial):
       
        source_color, color_before_zero, last_non_zero_index, destination_index = self.get_pour_parameters(source_vial, destination_vial)
        # Check if the condition is satisfied
        return (source_color == color_before_zero) or (color_before_zero == None)
    


    def step(self, action):
        
        source_vial, destination_vial = self._action_to_vials(action)
        # Use the observation_and_action_splitter function to obtain the action mask
        action_mask = self.observation_and_action_splitter(source_vial, destination_vial)

        # Filter out valid actions
        valid_actions = [i for i in range(len(action_mask)) if action_mask[i] == 1]

        # Check if the provided action is valid
        if action not in valid_actions or self.check_full_vial(source_vial):
            print("Invalid action:", action)
            self.reward = -1
        else:
                                    
            source_color, color_before_zero, last_non_zero_index, destination_index = self.get_pour_parameters(source_vial, destination_vial)
            new_state = self._pour_color_action(source_vial, destination_vial, source_color, last_non_zero_index, destination_index)
            self.state = new_state

            # Check if the source or destination vial is now full with the same color
            if self.check_full_vial(source_vial) or self.check_full_vial(destination_vial):
                self.reward = 10
            else:
                self.reward = -1          

        # Update the step counter
        self.current_step += 1

        # Check if the maximum number of steps has been reached
        if self.current_step >= self.max_steps or self._check_game_over():
            self.done = True

        episode_info = {'reward': self.reward, 'length': self.current_step}

        # Return the necessary information to the agent
        return self.state, self.reward, self.done, episode_info
        

    
    def reset(self):
        self.state = self._generate_initial_state()
        self.reward = 0
        self.current_step = 0
        self.done = False
        obs = np.array(self.state, dtype=np.int32)       
        return obs