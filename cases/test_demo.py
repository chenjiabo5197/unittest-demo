"""
@Time:2023/7/9 18:50
@Emial:chen_wangyi666@163.com
"""

import sys
import unittest
sys.path.append("..")
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
