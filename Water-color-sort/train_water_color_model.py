import gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from gym_water_color_sort.envs import WaterColorPuzzleEnv
from stable_baselines3.common.evaluation import evaluate_policy

# Create an instance of your custom environment
env = DummyVecEnv([lambda: WaterColorPuzzleEnv(num_vials=5, num_colors=3, water_capacity=3, num_empty_vials=2)])

# Initialize the PPO model with custom parameters
model = PPO("MlpPolicy", env, verbose=1)

# Train the model
model.learn(total_timesteps=200000)

# Save the trained model
model.save("water_color_sort_model_ppo_5_vials")