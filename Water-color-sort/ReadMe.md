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

## Experiment 1

**Initial State:** [2 3 3 1 1 3 2 1 2 0 0 0 0 0 0]

| Step  | Action | Reward     | Total Reward      | Current Reward                                |
|-------|--------|------------|-------------------|-----------------------------------------------|
| 0     | -      | -          | -                 | [2 3 3 1 1 3 2 1 2 0 0 0 0 0 0]               |
| 1     | 5      | -1         | -1                | [2 3 3 1 1 3 2 1 0 0 0 0 2 0 0]               |
| 2     | -      | -1         | -2                | [2 3 3 1 1 0 2 1 0 3 0 0 2 0 0]               |
| 3     | -      | 10         | 7                 | [2 3 3 1 1 1 2 0 0 3 0 0 2 0 0]               |
| 4     | 2      | -1         | 6                 | [2 3 3 1 1 1 2 0 0 3 0 0 2 0 0]               |
| 5     | 15     | -1         | 5                 | [2 3 3 1 1 1 2 0 0 3 0 0 2 0 0]               |
| 6     | -      | -1         | 4                 | [2 3 3 1 1 1 0 0 0 3 0 0 2 2 0]               |
| 7     | 7      | -1         | 3                 | [2 3 3 1 1 1 0 0 0 3 0 0 2 2 0]               |
| 8     | 11     | -1         | 2                 | [2 3 3 1 1 1 0 0 0 3 0 0 2 2 0]               |
| 9     | 1      | -1         | 1                 | [2 3 3 1 1 1 0 0 0 3 0 0 2 2 0]               |
| 10    | 11     | -1         | 0                 | [2 3 3 1 1 1 0 0 0 3 0 0 2 2 0]               |
| 11    | -      | -1         | -1                | [2 3 0 1 1 1 3 0 0 3 0 0 2 2 0]               |
| 12    | -      | -1         | -2                | [2 3 0 1 1 1 0 0 0 3 3 0 2 2 0]               |
| 13    | -      | -1         | -3                | [2 0 0 1 1 1 3 0 0 3 3 0 2 2 0]               |
| 14    | 10     | -1         | -4                | [2 0 0 1 1 1 3 0 0 3 3 0 2 2 0]               |
| 15    | 6      | 10         | 6                 | [0 0 0 1 1 1 3 0 0 3 3 0 2 2 2]               |
| 16    | 10     | -1         | -4                | [0 0 0 1 1 1 0 0 0 3 3 3 2 2 2]               |




### Experiment 2

## Initial State: [2 1 1 3 2 3 1 3 2 0 0 0 0 0 0]

| Step | Action | Reward | Total Reward | Current State                                |
|------|--------|--------|--------------|----------------------------------------------|
| 0    | -      | -      | -            | [2 1 1 3 2 3 1 3 0 2 0 0 0 0 0]              |
| 1    | 2      | -1     | -1           | [2 1 1 3 2 3 1 3 0 2 0 0 0 0 0]              |
| 2    | -      | -1     | -2           | [2 1 1 3 2 3 1 0 0 2 0 0 3 0 0]              |
| 3    | 19     | -1     | -3           | [2 1 1 3 2 3 1 0 0 2 0 0 3 0 0]              |
| 4    | 6      | -1     | -4           | [2 1 1 3 2 3 1 0 0 2 0 0 3 0 0]              |
| 5    | 1      | -1     | -5           | [2 1 1 3 2 3 1 0 0 2 0 0 3 0 0]              |
| 6    | 19     | -1     | -6           | [2 1 1 3 2 3 1 0 0 2 0 0 3 0 0]              |
| 7    | 19     | -1     | -7           | [2 1 1 3 2 3 1 0 0 2 0 0 3 0 0]              |
| 8    | -      | -1     | -8           | [2 1 1 3 2 3 1 0 0 2 0 0 3 0 0]              |
| 9    | 11     | -1     | -9           | [2 1 1 3 2 0 1 0 0 2 0 0 3 3 0]              |
| 10   | -      | -1     | -10          | [2 1 1 3 2 0 1 0 0 2 0 0 3 3 0]              |
| 11   | 10     | 10     | -1           | [2 1 1 0 0 0 1 0 0 2 2 0 3 3 3]              |
| 12   | -      | -1     | -2           | [2 1 0 0 0 0 1 1 0 2 2 0 3 3 3]              |
| 13   | 10     | -1     | -3           | [2 1 0 0 0 0 1 1 0 2 2 0 3 3 3]              |
| 14   | 7      | 10     | 7            | [2 0 0 0 0 0 1 1 1 2 2 0 3 3 3]              |
| 15   | 17     | 10     | 17           | [0 0 0 0 0 0 1 1 1 2 2 2 3 3 3]              |

