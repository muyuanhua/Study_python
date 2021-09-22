
import datetime
import time
import requests
import unittest
from datetime import *
import json
import HTMLTestRunner

list=[]

class Test_port(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("测试开始")

    def test_login(self):
        """

        登录接口测试
        :return:
        """
        url = "http://api.heartdub.cn:8080/login"
        form={
            "user_addr":"1127535539@qq.com",
            "user_pass":"myh123",
            "auth_code":"150be7d0a3d711eb81d2d1264cd620fb"
        }
        r=requests.post(url,data=form)

        self.assertEqual(r.json()["msg"],"success")
        ticket1 = r.json()["result"]["ticket"]
        list.append(ticket1)
        return ticket1
        print(list)

    @classmethod
    def tearDownClass(cls):
        print("测试结束")

    def test_pattern(self):
        global list
        ticket=list[0]

        url_pattern="http://one.heartdub.cn:8084/pattern_info_select"
        form={
            "ticket":ticket
        }
        res=requests.post(url_pattern,data=form)
        self.assertEqual(res.json()["code"],"00000")
class Test_monkey(unittest.TestCase):
    def test_n(self):
        url="http://one.heartdub.cn:8082/login"
        form={
            "user_addr":"1127535539@qq.com",
            "user_pass":"myh123"

        }
        res=requests.post(url,data=form)
        self.assertEqual(res.json()["code"],"00000")

def suite():

    loginTestCase=unittest.makeSuite(Test_port,"test")
    TestMonkey=unittest.makeSuite(Test_monkey,"test")
    testall=unittest.TestSuite(loginTestCase,TestMonkey)
    return testall
if __name__ == '__main__':

    html_file='D:\\PyApi_heartdub\\result.html'
    fp=open(html_file,"w",encoding="utf-8")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="测试报告",description="测试报告详情")
    runner.run(suite())
    fp.close()

