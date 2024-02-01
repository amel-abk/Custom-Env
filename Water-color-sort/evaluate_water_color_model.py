import gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy
from gym_water_color_sort.envs import WaterColorPuzzleEnv

# Load the trained model
model = PPO.load("water_color_sort_model_ppo_5_vials")

# Create an instance of the custom environment for evaluation
eval_env = DummyVecEnv([lambda: WaterColorPuzzleEnv(num_vials=5, num_colors=3, water_capacity=3)])

# Evaluate the model
mean_reward, std_reward = evaluate_policy(model, eval_env, n_eval_episodes=20)

# Print the evaluation results
print(f"Mean reward: {mean_reward}, Std reward: {std_reward}")
