import os
from .conf_env import Conf

config = Conf()

def prepare_config(env_name):  

    file_config = os.environ.get(env_name)
    if not(file_config):
        print('value for environ ', env_name, ' not found')
        raise
    
    config.load(file_config)
