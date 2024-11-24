"""
@Time:2023/7/9 18:50
@Emial:chen_wangyi666@163.com
"""
import os
import sys
import unittest
# 获取当前文件的绝对路径，并找到项目的根目录
current_file_path = os.path.abspath(__file__)
project_root_path = os.path.dirname(os.path.dirname(current_file_path))
# 将项目的根目录添加到sys.path中
sys.path.append(project_root_path)
from utils import my_logger, global_var

logger = my_logger.MyLogger(__name__).get_logger()
var = global_var.GlobalVar()


class TestDemo(unittest.TestCase):
    """
    说明
    """

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

    def setUp(self) -> None:
        logger.info("execute unittest class={}, function={}".format(type(self).__name__, self._testMethodName))

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()

    def tearDown(self) -> None:
        pass

    def test_demo1(self):
        """"""
        a = 1
        b = 2
        self.assertEqual(a, b)
