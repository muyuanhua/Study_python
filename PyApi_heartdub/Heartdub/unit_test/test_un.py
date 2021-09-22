# import sys
# sys.path.append("../Heartdub")
import unittest
from util.test_get_post import Runmain
from util.ticket_request import ticket, user_code, info_code


class Test_Pattern_message(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ticket=ticket()
        cls.user_code=user_code()
        cls.info_code=info_code()


    @classmethod
    def tearDownClass(cls):
       pass



    def setUp(self):
        self.run=Runmain()
    def tearDown(self):
        pass


    def pattern_info_select(self):
        url = "http://one.heartdub.cn:8082/pattern_info_select"
        form = {"user_code":self.user_code}
        res=self.run.run_main(url,form,None,'post')
        print(res)
        self.assertEqual(res.json()["code"],"00000")


    def test_pattern_info_select2(self):
        """
        查询我的花型列表：参数组合,按时间倒序
        :return:
        """


        url = "http://one.heartdub.cn:8082/pattern_info_select"
        form = {
            "user_code": self.user_code,
            "order_by":"time_des"
        }
        res=self.run.run_main(url,form,None,"post")
        self.assertEqual(res.json()["code"], "00000")

    def test_pattern_info_select3(self):
        """
        查询我的花型列表：参数组合，按热度倒序
        :return:
        """


        url = "http://one.heartdub.cn:8082/pattern_info_select"
        form = {
            "user_code": self.user_code,
            "order_by": "hot_des"
        }
        res = self.run.run_main(url,form,None,'post')
        self.assertEqual(res.json()["code"], "00000")


    def test_pattern_info_insert(self):
        """
        新建花型：传入refer和fabric_code
        :return:
        """


        url = "http://one.heartdub.cn:8082/pattern_info_insert"

        form = {
            "ticket":self.ticket,
            "refer": "1624869733661_bc50fcd0d7ec11eb8736a183c91b4699",
            # "info_name": '["001.png"]',
            "fabric_code":'1629972256535_f8f33270065411ecad9fffff3cffe6a8'
        }
        res = self.run.run_main(url,form,None,'post')
        self.assertEqual(res.json()["code"], "00000")


    def test_pattern_info_insert1(self):
        """
        新建花型：传入ticket、refer。info_name、fabric_code
        :return:
        """


        url = "http://one.heartdub.cn:8082/pattern_info_insert"

        form = {
            "ticket":self.ticket,
            "refer": "1624869733661_bc50fcd0d7ec11eb8736a183c91b4699",
            "info_name": '["001.png"]',
            "fabric_code":'1629972256535_f8f33270065411ecad9fffff3cffe6a8'
        }
        res = self.run.run_main(url,form,None,'post')
        self.assertEqual(res.json()["code"], "00000")
        self.assertEqual(res.json()["msg"],"成功上传1个花型")



    def test_pattern_info_update(self):
        """
        修改花型：传入ticket和info_code
        :return:
        """


        url = "http://one.heartdub.cn:8082/pattern_info_update"
        form = {
            "ticket":self.ticket,
            "info_code": self.info_code,
        }
        res = self.run.run_main(url,form,None,'post')
        self.assertEqual(res.json()["code"], "00000")

    def test_pattern_info_update2(self):
        """
        修改花型：ticket、info_code、info_name、remark
        :return:
        """


        url = "http://one.heartdub.cn:8082/pattern_info_update"
        form = {
            "ticket":self.ticket,
            "info_code": self.info_code,
            "info_name":'["002.png"]',
            "remark":"备注花型"
        }
        res = self.run.run_main(url,form,None,'post')
        self.assertEqual(res.json()["code"], "00000")

    def test_pattern_info_delete(self):
        """
        删除花型：必传参数
        :return:
        """


        url = "http://one.heartdub.cn:8082/pattern_info_delete"
        form = {
            "ticket":self.ticket,
            "info_code": self.info_code,
        }
        res = self.run.run_main(url, form, None, 'post')
        self.assertEqual(res.json()["code"], "00000")