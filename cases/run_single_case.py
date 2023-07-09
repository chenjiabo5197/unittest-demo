"""
@Time:2023/7/9 19:12
@Emial:chen_wangyi666@163.com
"""
import argparse
import sys
import unittest
from unittest import case, suite


def get_parameter():
    """获取传入的参数"""
    parser = argparse.ArgumentParser(description="ArgUtils")
    parser.add_argument('-f', type=str, default=None, help="unittest file")
    parser.add_argument('-m', type=str, default=None, help="unittest method")
    args = parser.parse_args()
    return args


def get_module_from_name(name):
    """导入文件"""
    __import__(name)
    return sys.modules[name]


def get_run_suite(class_name, args):
    """获取run case的suite"""
    for name in dir(class_name):
        obj = getattr(class_name, name)
        if isinstance(obj, type) and issubclass(obj, case.TestCase):
            if issubclass(obj, suite.TestSuite):
                raise TypeError("error")
            loaded_suite = suite.TestSuite(map(obj, [args.m]))
            suite1 = suite.TestSuite([loaded_suite])
            suite2 = suite.TestSuite([suite1])
            suite3 = unittest.TestSuite()
            suite3.addTest(suite2)
            return suite3


if __name__ == "__main__":
    args = get_parameter()
    class_name = get_module_from_name(args.f.split(".")[0])
    runner = unittest.TextTestRunner()
    case = get_run_suite(class_name, args)
    result = runner.run(case)

