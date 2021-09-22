import HTMLTestRunner
import get_data
from get_data import Test_Case
import readPath
import unittest

name = Test_Case()

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(name))


with open(readPath.path + "/result/report.html", "wb") as f:
    runner = HTMLTestRunner.HTMLTestRunner(f, title="测试报告", description='None')
    runner.run(suite)
