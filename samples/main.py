import os

from envconf.set_env import prepare_config, config

env_name = 'PEMP_ENV'
file_config = os.environ.get(env_name)
if not(file_config):
	print('value for environ ', env_name, ' not found')
	raise

print('file_config :', file_config)

prepare_config(env_name)

print('var1 :' + config.value['var1'])
print('var2 :' + config.value['var2'])

print('sub :', config.value['sub'])
