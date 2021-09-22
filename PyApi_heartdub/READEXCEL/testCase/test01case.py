import json
import unittest
from common.configHttp import RunMain
import paramunittest
import geturlParams
import urllib.parse
# import pythoncom
import readExcel
import readConfig

# pythoncom.CoInitialize()

url = geturlParams.geturlParams().get_url()  # 调用我们的geturlParams获取我们拼接的URL
heartdub_xls = readExcel.readExcel().get_xls('heartdub_api.xls', 'Sheet1')
# print(heartdub_xls)


@paramunittest.parametrized(*heartdub_xls)
class testlongin(unittest.TestCase):
    def setParameters(self, case_name, path, data, method, expected_result):
        """
        set params
        :param case_name:
        :param path
        :param data
        :param method
        :return
        """
        self.case_name = str(case_name)
        self.path = str(path)
        self.data = str(data)
        self.method = str(method)
        self.expected_result = str(expected_result)
    # def description(self):
    #     """
    #     test report description
    #     :return:
    #     """
    #     self.case_name

    def setUp(self):
        """
        :return:
        """
        print(self.case_name + "测试开始前准备")

    def testcaseassert(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self):  # 断言
        """
        check test result
        :return:
        """
        i=1
        for i in range(len(heartdub_xls)):

            # url1 = "http://one.heartdub.cn:8082/"
            url=readConfig.ReadConfig().get_http("scheme") + "://"+ readConfig.ReadConfig().get_http("baseurl")+":"+readConfig.ReadConfig().get_http("port")
            new_url=url+readExcel().get_xls("heartdub_api.xls","Sheet1")[i][1]
            # new_url = url[i]
            # print(new_url)
            data1 = dict(urllib.parse.parse_qs(urllib.parse.urlsplit(new_url).query))  # 将数据转换成字典格式
            # print(data1)
            info = RunMain().run_main(self.method, new_url, data1)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
            # ss = json.loads(info)  # 将响应转换为字典格式
            ss = info.json()  # 将响应转换为字典格式
            # print(ss)
            if ss ==None:
                result1 = ss["code"]
                self.assertEqual(result1, self.expected_result)
            else:
                print('接口返回结果异常')
            i=i+1

# if __name__ == '__main__':
#     print(testlongin().checkResult())