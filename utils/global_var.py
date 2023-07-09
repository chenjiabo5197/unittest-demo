"""
@Time:2023/6/10 15:01
@Emial:chen_wangyi666@163.com
"""
import threading
import utils
import my_logger

logger = my_logger.MyLogger(__name__).get_logger()


class GlobalVar(object):
    """全局变量类"""

    _instance_lock = threading.Lock()
    _first_init = True

    def __init__(self):
        if not self._first_init:
            return
        self._global_dict = {
            "service": utils.get_config_field("config", "service"),
            "port": utils.get_config_field("config", "port")
        }
        logger.name("init global var={}".format(self._global_dict))
        self._first_init = False

    def __new__(cls, *args, **kwargs):
        """单例"""
        if not hasattr(GlobalVar, "_instance"):
            with GlobalVar._instance_lock:
                if not hasattr(GlobalVar, "_instance"):
                    GlobalVar._instance = object.__new__(cls)
        return GlobalVar._instance

    def is_exist(self, key):
        """判断当前key是否在全局变量中"""
        if key in self._global_dict.keys():
            return True
        return False

    def get_value(self, key):
        """获取全局变量，若不存在，则返回error"""
        if self.is_exist(key):
            value = self._global_dict[key]
            logger.debug("get global var success, key={}, value={}".format(key, value))
            return value
        else:
            logger.error("get global var fail, key={}, global_var={}".format(key, self._global_dict))
            raise Exception("获取" + key + "失败，无此变量")

    def set_value(self, key, value):
        self._global_dict[key] = value
        logger.info("set global var success, key={}, value={}".format(key, value))
