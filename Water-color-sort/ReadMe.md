# WaterSortPuzzleEnv Class

## Description

The Water Sort Puzzle Environment is designed for simulating the Water Sort Puzzle game. It provides an environment of five vials, each capable of holding water of different colors. The goal is to solve the puzzle by arranging the water so that all vials end up with the same color.

Here are the main points:

**Vials:**
There are a certain number of vials in the game (default is 5), and each vial can hold water of different colors.

**Colors:**
The water in each vial is shown using three unique colors.

**Action Space:**
Actions in this game are discrete, meaning each action represents pouring water from one vial to another.

**Observation Space:**
What you see in the game is represented by a box, showing the current order of colors in each vial.

**Rewards:**
* +10: for each bottle filled with the same color.
* -1: For invalid or ineffective actions.

**Episode Termination:**
The game is considered solved when all vials have the same color of water or when the maximum number of steps is reached.

**Initialization:**
When the game starts, you set some things like the number of vials, colors, water capacity, and empty vials. Other things like maximum steps, current step, state, reward, and whether the game is done are also set.

**Methods and Functions**
The WaterSortPuzzleEnv class has different methods to make the game work:

    * _generate_initial_state: It sets up how the vials look at the beginning.
    * _check_game_over: It checks if the game is finished by looking at how the colors are arranged in the vials.
    * _can_pour_to_vial and _can_pour_from_vial: These check if pouring water from one vial to another is possible.
    * _action_to_vials: It helps to figure out which vials are involved when you make a move.
    * observation_and_action_splitter: It creates a list of valid moves based on the current state.
    * _pour_color_action: This changes the state by moving water from one vial to another.
    * check_full_vial: It checks if a vial is full with the same color.
    * get_pour_parameters: It gets information needed when you pour water from one vial to another.
    * check_permutation_condition: It checks if the pour operation follows specific rules.
    * step: It makes a move in the game, changing the state, giving points, and checking if the game is over.
    * reset: It takes the game back to the beginning for a new state.



## Results

### Experiment 1
initial state [2 3 3 1 1 3 2 1 2 0 0 0 0 0 0]
step0
Invalid action: 5
reward: -1
total_reward: -1
Current state: [2 3 3 1 1 3 2 1 2 0 0 0 0 0 0]
step1
reward: -1
total_reward: -2
Current state: [2 3 3 1 1 3 2 1 0 0 0 0 2 0 0]
step2
reward: -1
total_reward: -3
Current state: [2 3 3 1 1 0 2 1 0 3 0 0 2 0 0]
step3
reward: 10
total_reward: 7
Current state: [2 3 3 1 1 1 2 0 0 3 0 0 2 0 0]
step4
Invalid action: 2
reward: -1
total_reward: 6
Current state: [2 3 3 1 1 1 2 0 0 3 0 0 2 0 0]
step5
Invalid action: 15
reward: -1
total_reward: 5
Current state: [2 3 3 1 1 1 2 0 0 3 0 0 2 0 0]
step6
reward: -1
total_reward: 4
Current state: [2 3 3 1 1 1 0 0 0 3 0 0 2 2 0]
step7
Invalid action: 7
reward: -1
total_reward: 3
Current state: [2 3 3 1 1 1 0 0 0 3 0 0 2 2 0]
step8
Invalid action: 11
reward: -1
total_reward: 2
Current state: [2 3 3 1 1 1 0 0 0 3 0 0 2 2 0]
step9
Invalid action: 1
reward: -1
total_reward: 1
Current state: [2 3 3 1 1 1 0 0 0 3 0 0 2 2 0]
step10
Invalid action: 11
reward: -1
total_reward: 0
Current state: [2 3 3 1 1 1 0 0 0 3 0 0 2 2 0]
step11
reward: -1
total_reward: -1
Current state: [2 3 0 1 1 1 3 0 0 3 0 0 2 2 0]
step12
reward: -1
total_reward: -2
Current state: [2 3 0 1 1 1 0 0 0 3 3 0 2 2 0]
step13
reward: -1
total_reward: -3
Current state: [2 0 0 1 1 1 3 0 0 3 3 0 2 2 0]
step14
Invalid action: 10
reward: -1
total_reward: -4
Current state: [2 0 0 1 1 1 3 0 0 3 3 0 2 2 0]
step15
reward: 10
total_reward: 6
Current state: [0 0 0 1 1 1 3 0 0 3 3 0 2 2 2]
step16
reward: 10
total_reward: 16
Current state: [0 0 0 1 1 1 0 0 0 3 3 3 2 2 2]

### Experiment 2

initial state [2 1 1 3 2 3 1 3 2 0 0 0 0 0 0]
step0
reward: -1
total_reward: -1
Current state: [2 1 1 3 2 3 1 3 0 2 0 0 0 0 0]
step1
Invalid action: 2
reward: -1
total_reward: -2
Current state: [2 1 1 3 2 3 1 3 0 2 0 0 0 0 0]
step2
reward: -1
total_reward: -3
Current state: [2 1 1 3 2 3 1 0 0 2 0 0 3 0 0]
step3
Invalid action: 19
reward: -1
total_reward: -4
Current state: [2 1 1 3 2 3 1 0 0 2 0 0 3 0 0]
step4
Invalid action: 6
reward: -1
total_reward: -5
Current state: [2 1 1 3 2 3 1 0 0 2 0 0 3 0 0]
step5
Invalid action: 1
reward: -1
total_reward: -6
Current state: [2 1 1 3 2 3 1 0 0 2 0 0 3 0 0]
step6
Invalid action: 19
reward: -1
total_reward: -7
Current state: [2 1 1 3 2 3 1 0 0 2 0 0 3 0 0]
step7
Invalid action: 19
reward: -1
total_reward: -8
Current state: [2 1 1 3 2 3 1 0 0 2 0 0 3 0 0]
step8
reward: -1
total_reward: -9
Current state: [2 1 1 3 2 0 1 0 0 2 0 0 3 3 0]
step9
Invalid action: 11
reward: -1
total_reward: -10
Current state: [2 1 1 3 2 0 1 0 0 2 0 0 3 3 0]
step10
reward: -1
total_reward: -11
Current state: [2 1 1 3 0 0 1 0 0 2 2 0 3 3 0]
step11
reward: 10
total_reward: -1
Current state: [2 1 1 0 0 0 1 0 0 2 2 0 3 3 3]
step12
reward: -1
total_reward: -2
Current state: [2 1 0 0 0 0 1 1 0 2 2 0 3 3 3]
step13
Invalid action: 10
reward: -1
total_reward: -3
Current state: [2 1 0 0 0 0 1 1 0 2 2 0 3 3 3]
step14
reward: 10
total_reward: 7
Current state: [2 0 0 0 0 0 1 1 1 2 2 0 3 3 3]
step15
reward: 10
total_reward: 17
Current state: [0 0 0 0 0 0 1 1 1 2 2 2 3 3 3]