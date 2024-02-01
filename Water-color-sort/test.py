from stable_baselines3 import PPO
from gym_water_color_sort.envs import WaterColorPuzzleEnv


# load the model
model = PPO.load("water_color_sort_model_ppo_5_vials")



env = WaterColorPuzzleEnv(num_vials=5, num_colors=3, water_capacity=3, num_empty_vials=2)

obs = env.reset()
print('initial state', obs)

done = False
i=0
total_reward= 0
while not done:
    print(f'step{i}')
    
    action, _ = model.predict(obs)

    
    obs, reward, done, _ = env.step(action)
    print('reward:', reward)
    total_reward += reward
    print("total_reward:", total_reward)
    
    print("Current state:", obs)
    i += 1
