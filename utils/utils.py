"""
@Time:2023/6/10 14:38
@Emial:chen_wangyi666@163.com
"""
from configparser import ConfigParser

config_path = "conf/config.ini"


def get_config_field(scope, field_name):
    """获取配置"""
    conf = ConfigParser()
    conf.read(config_path)
    return conf.get(scope, field_name)
