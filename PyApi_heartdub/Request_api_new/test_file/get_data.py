import unittest
import  paramunittest
from Send_request import Send_request
from test_file.Test_casename import set_data
from Readexcel import Readexcel
from read_data import excel_dict


file = 'D:\\PyApi_heartdub\\Request_api_new\\test_case\\testcase1.xls'
e = Readexcel().get_excel(file, "fabric")
n=excel_dict(e)
print(n)
# test_case=Readexcel().get_excel("testcase1.xls","fabric")

@paramunittest.parametrized(n)
class Test_Case(unittest.TestCase):
    def setParameters(self, n):
        """
        执行测试脚本
        :param data:
        :return:
        """



        results=self.date = set_data(n)
        # self.results=self.response.json()
        for i in range(n):
            code = n[i]["expected"]
        return code
        self.assertEqual(results.json()["code"], code)

if __name__ == '__main__':
    a=Test_Case()
    b=a.setParameters(n)