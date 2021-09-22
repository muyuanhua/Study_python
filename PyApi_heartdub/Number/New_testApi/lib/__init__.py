import logging
from lib.log import init_logging

# 环境切换 loc,dev,uat
surroundings = 'loc' #用来代替get_test_url方法的参数

init_logging()
logging.info("测试日志信息|{}环境".format(surroundings))