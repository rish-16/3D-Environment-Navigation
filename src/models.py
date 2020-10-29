from stable_baselines.ppo2 import PPO2
from stable_baselines.common import make_vec_env
from stable_baselines.common.policies import CnnLstmPolicy

def get_PPO(env_name, ckpt_name="ppo_default_bin"):
    new_env = make_vec_env(env_name, n_envs=1)
    model = PPO2(CnnLstmPolicy, new_env, verbose=1)
    
    return new_env, model