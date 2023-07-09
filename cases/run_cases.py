"""
@Time:2023/7/9 18:54
@Emial:chen_wangyi666@163.com
"""
import os.path
import time
import unittest
import sys
sys.path.append("..")
from utils import my_logger, my_html_test_runner

logger = my_logger.MyLogger(__name__).get_logger()

cases_path = "./"
report_path = "../report/"


def get_all_cases():
    """获取所有测试用例"""
    discover = unittest.defaultTestLoader.discover(cases_path, pattern="test*.py")
    suite = unittest.TestSuite()
    suite.addTest(discover)
    return suite


def set_html_report():
    """设置生成的HTML测试报告"""
    if not os.path.exists(report_path):
        os.makedirs(report_path)
    time_struct = time.localtime(int(time.time()))
    str_time = time.strftime("%Y%m%d%H%M%S", time_struct)
    report_abspath = os.path.join(report_path, "demo_"+str_time+".html")
    logger.info("save report path={}".format(report_abspath))
    return report_abspath


def get_result_data(result):
    data = {"demo": {"all_case":0, "pass": 0, "fail": 0}, "test": {"all_case":0, "pass": 0, "fail": 0}}
    rmap = {}
    classes = []
    for n, t, o, e in result:
        cls = t.__class__
        if not cls in rmap:
            rmap[cls] = []
            classes.append(cls)
        rmap[cls].append((n, t, o, e))
    r = [(cls, rmap[cls]) for cls in classes]
    for cid, (cls, cls_results) in enumerate(r):
        # subtotal for a class
        np = nf = ne = 0
        for n, t, o, e in cls_results:
            if n == 0:
                np += 1
            elif n == 1:
                nf += 1
            else:
                ne += 1

        # format class description
        if cls.__module__ == "__main__":
            name = cls.__name__
        else:
            name = "%s.%s" % (cls.__module__, cls.__name__)
        for key in data.keys():
            if key in name:
                data[key]["all_case"] = np + nf + ne
                data[key]["pass"] = np
                data[key]["fail"] = nf + ne
        logger.info("get report data")
    return data


if __name__ == "__main__":
    fp = open(set_html_report(), "wb")
    runner = my_html_test_runner.HTMLTestRunner(stream=fp,
                                                title=u'demo 自动化测试报告，测试结果如下:',
                                                description=u'用例执行情况:')
    case_result = runner.run(get_all_cases())
    result_table = get_result_data(case_result)
    logger.info("result_table={}".format(result_table))

    fp.close()
    logger.info("execute all case, close")

