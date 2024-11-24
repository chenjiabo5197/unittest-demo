"""
@Time:2023/6/10 14:35
@Emial:chen_wangyi666@163.com
"""
import logging
import os.path
import threading
import time
import utils
from logging.handlers import RotatingFileHandler

log_path = "log/"


class MyLogger(object):

    _instance_lock = threading.Lock()
    _first_init = True  # 防止重复执行init函数

    def __init__(self, log):
        if not self._first_init:
            return
        self.file_log_level = self.get_log_level(self, utils.get_config_field("log", "file_log_level"))
        self.stream_log_level = self.get_log_level(self, utils.get_config_field("log", "stream_log_level"))
        # 创建logger对象
        self.logger = logging.getLogger(log)
        self.init_logger()
        self._first_init = False
    
    def init_logger(self):
        """初始化对象"""
        self.logger.setLevel(logging.DEBUG)
        # log输出格式
        formatter = logging.Formatter(fmt="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s",
                                      datefmt="%Y-%m-%d %H:%M:%S")
        # 输出日志的handler
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(self.stream_log_level)
        stream_handler.setFormatter(formatter)

        time_struct = time.localtime(int(time.time()))
        str_time = time.strftime("%Y%m%d%H%M%S", time_struct)
        # 文件日志handler
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        file_handler = RotatingFileHandler(log_path + "name" + str_time + ".log", maxBytes=1024 * 1024 * 10,
                                           backupCount=3, encoding="utf-8") # 一个文件10m大，最多同一名字3个文件
        file_handler.setLevel(self.file_log_level)
        file_handler.setFormatter(formatter)

        # 添加到logger
        self.logger.addHandler(stream_handler)
        self.logger.addHandler(file_handler)
        self.logger.info("logger init success, file_level={}, stream_level={}".
                         format(self.file_log_level, self.stream_log_level))

    def __new__(cls, *args, **kwargs):
        """单例"""
        if not hasattr(MyLogger, "_instance"):
            with MyLogger._instance_lock:
                if not hasattr(MyLogger, "_instance"):
                    MyLogger._instance = object.__new__(cls)
        return MyLogger._instance

    @staticmethod
    def get_log_level(self, level):
        if level == "debug":
            return logging.DEBUG
        elif level == "info":
            return logging.INFO
        elif level == "warning":
            return logging.WARNING
        elif level == "error":
            return logging.ERROR
        else:
            return logging.CRITICAL

    def get_logger(self):
        return self.logger
