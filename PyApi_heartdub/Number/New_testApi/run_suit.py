from case.testcase import TestCase
from setting import REPORT_PATG  #倒入setting.py内的变量
from tools.HTMLTestRunner import HTMLTestRunner #网上下一个就行
import unittest



suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestCase))
with open(REPORT_PATG, "wb") as f:
    runner = HTMLTestRunner(f, title="测试报告", description="None")
    runner.run(suite)