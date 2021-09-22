import unittest
import  paramunittest
from Send_request import Send_request
from test_file.Test_casename import set_data
from Readexcel import Readexcel



test_case=Readexcel().get_excel("testcase1.xls","fabric")

@paramunittest.parametrized(*test_case)
class Test_Case(unittest.TestCase):
    def setParameters(self,test_case):


        """
        执行测试脚本
        :param data:
        :return:
        """
        self.date=set_data(test_case)
        # self.results=self.response.json()
        code=test_case["expected"]
        self.assertEqual(test_case.json()["code"],code)


