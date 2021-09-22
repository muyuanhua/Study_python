import unittest
from unit_test.test_un import Test_Pattern_message
from util import HTMLTestRunner
from util.test_get_post import Runmain


class Runmain():

    def run_case(self):

        # TestCase=suite.addTests(map(Test_Pattern_message,[]))
        # return TestCase
        discover = unittest.defaultTestLoader.discover("D:\PyApi_heartdub\Heartdub", 'test*.py')
        suite = unittest.TestSuite(discover)
        path = "D:\\PyApi_heartdub\\Heartdub\\report\\report.html"
        rp = open(path,'wb')
        HTMLTestRunner.HTMLTestRunner(stream=rp, title="Fabric V1.0测试报告", description="测试详情").run(suite)
        rp.close()


if __name__ == '__main__':
    # runner=Runmain
    run=Runmain()
    run.run_case()
    # unittest.main()
    # print(run.run_case())