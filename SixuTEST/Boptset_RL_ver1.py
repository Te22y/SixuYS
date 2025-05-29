import subprocess
import shutil
import os
import sys

# 删除目录（等价于 `rm -rf`）
try:
    shutil.rmtree('boptestGymService')
except FileNotFoundError:
    pass

# 克隆仓库（等价于 `git clone ...`）
subprocess.run([
    'git', 'clone', '-b', 'boptest-gym-service',
    'https://github.com/ibpsa/project1-boptest-gym.git',
    'boptestGymService'
], check=True)



sys.path.insert(0,'boptestGymService')
from boptestGymService.boptestGymEnv import BoptestGymEnv

# url for the BOPTEST service
url = 'https://api.boptest.net'

# Instantiate environment
env = BoptestGymEnv(url                   = url,
                    testcase              = 'bestest_hydronic_heat_pump',
                    actions               = ['oveHeaPumY_u'],
                    observations          = {'reaTZon_y':(280.,310.)},
                    random_start_time     = False,
                    start_time            = 31*24*3600,
                    max_episode_length    = 24*3600,
                    warmup_period         = 24*3600,
                    step_period           = 3600)

obs, _ = env.reset()
print('Zone temperature: {:.2f} degC'.format(obs[0]-273.15))
print('Episode starting day: {:.1f} (from beginning of the year)'.format(env.start_time/24/3600))