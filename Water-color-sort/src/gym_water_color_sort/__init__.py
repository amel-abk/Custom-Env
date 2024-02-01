from gym.envs.registration import register


register(
    id='Water_color_sort-v0',
    entry_point = 'gym_water_color_sort.envs:WaterColorSortEnv',
    max_episode_steps= 200,
)