import logging
from logging import handlers
import setting
import os

PROJECT_ROOT=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
LOG_PATH=os.path.join(PROJECT_ROOT,"log","api_test.log")
def init_logging():
    # 1 初始化日志器
    logger=logging.getLogger()

    # 2 设置日志等级
    logger.setLevel(logging.INFO)
    # 3创建控制处理器
    sh=logging.StreamHandler()
    # 4 创建文件处理器 - LOG_PATH为setting.py内的变量
    file=LOG_PATH
    fh = logging.handlers.TimedRotatingFileHandler(filename=LOG_PATH,when='D',interval=1,backupCount=7,encoding="utf-8")
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s %(funcName)s:%(lineno)d] - [%(message)s]"
    formatter=logging.Formatter(fmt)
    # 6 将格式化器，添加到处理器
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 7 将处理器添加到日志
    logger.addHandler(sh)
    logger.addHandler(fh)

if __name__ == '__main__':
    init_logging()
    logging.info('——————————————我2021必暴富——————————————————')