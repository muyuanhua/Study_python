import requests
import unittest
import HTMLTestRunner
from datetime import datetime


user_code_list = []
info_code_list = []
list = []
relation_id_list=[]
relation_list=[]
#登录获取ticket
url_login="http://api.heartdub.cn:8080/login"
form={
    "user_addr":"muyuanhua666@163.com",
    "user_pass":"myh123",
    "auth_code":"150be7d0a3d711eb81d2d1264cd620fb"
}
res = requests.post(url_login,data= form)
user_code1 = res.json()["result"]["user_code"]
ticket1 = res.json()["result"]["ticket"]
list.append(ticket1)
user_code_list.append(user_code1)

ticket=list[0]
#查询面料列表
url_infoCode="http://one.heartdub.cn:8082/fabric_info_select"
form={
    "user_code":202108111002491543221
}
res=requests.post(url_infoCode,data=form)
r=res.json()["result"][0]["info_code"]
info_code_list.append(r)


#获取relation_id
# url = "http://one.heartdub.cn:8082/relation_b_select"
# form = {
#     "ticket": ticket,
# }
# res = requests.post(url, data=form)
# # relation_id_duber = res.json()["result"][0]["id"]
# # relation_id_list.append(relation_id_duber)

#获取relation_id
ticket1 = list[0]
url = "http://one.heartdub.cn:8082/relation_a_select"
form = {
    "ticket": ticket1,
}
res = requests.post(url, data=form)
relation_id=res.json()["result"][0]["id"]
relation_list.append(relation_id)


class Test_Fabric_message(unittest.TestCase):

    def setUp(self):
        print("测试面料接口开始")
        # self.url="http://one.heartdub.cn:8082"
    # def test_login(self):
        """
        登录，获取ticket
        :return:
        """


    def tearDown(self):
        print("测试接口：面料接口参数{}".format(form))

    def test_fabric_type_select(self):
        """
        查询面料类别：只传ticket，查询所有类别
        :return:
        """
        global list
        ticket=list[0]
        url = "http://one.heartdub.cn:8082/fabric_type_select"
        form={"ticket":ticket,}
        res=requests.post(url,data=form)
        self.assertEqual(res.json()["code"],"00000")


    def test_fabric_type_select2(self):
        """
        传parent_code参数，查询对应类别
        :return:
        """
        global list
        ticket = list[0]
        url = "http://one.heartdub.cn:8082/fabric_type_select"
        form = { "ticket": ticket,"parent_code":"ft01"}
        res = requests.post(url, data=form)
        self.assertEqual(res.json()["code"], "00000")


    def test_fabric_type_select3(self):
        """
        传type_name参数，模糊查询包含平布的面料
        :return:
        """
        global list
        ticket = list[0]
        url = "http://one.heartdub.cn:8082/fabric_type_select"
        form = {"ticket": ticket,"type_name":"平布"}
        res = requests.post(url, data=form)
        self.assertEqual(res.json()["code"], "00000")


    def test_fabric_type_select4(self):
        """
        传parent_code和type_name参数，查询包含名称的面料
        :return:
        """
        global list
        ticket = list[0]
        url = "http://one.heartdub.cn:8082/fabric_type_select"
        form = {"ticket": ticket,"parent_code":"ft01","type_name":"平布"}
        res = requests.post(url, data=form)
        self.assertEqual(res.json()["code"], "00000")

    def test_fabric_type_select5(self):
        """
        传parent_code和type_name参数，查询面料库中没有的面料
        :return:
        """
        global list
        ticket = list[0]
        url = "http://one.heartdub.cn:8082/fabric_type_select"
        form = {"ticket": ticket,"parent_code":"db","type_name":"抹布"}
        res = requests.post(url, data=form)
        self.assertEqual(res.json()["code"], "00000")



    def test_fabric_info_select(self):
        """
        只传入必传值user_code,查询面料列表
        :return:
        """
        global user_code_list,info_code_list
        user_code = user_code_list[0]
        url = "http://one.heartdub.cn:8082/fabric_info_select"
        form = {"user_code": user_code,}
        res = requests.post(url, data=form)
        r = res.json()["result"][0]["info_code"]
        self.assertEqual(res.json()["code"], "00000")
        info_code_list.append(r)
        return info_code_list

    def test_fabric_info_select1(self):
        """
        参数组合，传入错误参数值product_code、product_gram、
        :return:
        """
        global user_code_list
        user_code1 = user_code_list[0]
        url = "http://one.heartdub.cn:8082/fabric_info_select"
        form = {"user_code": user_code1,"product_code":1,"product_weave":"钉钉",}
        res = requests.post(url, data=form)
        self.assertEqual(res.json()["code"], "00000")
        self.assertNotEqual(res.json()["msg"],"execute failure")

    def test_fabric_info_select2(self):
        """
        查询克重单位为：g 幅宽为：145 价格类型:rmb
        :return:
        """
        global user_code_list
        user_code1 = user_code_list[0]
        url = "http://one.heartdub.cn:8082/fabric_info_select"
        form = {"user_code": user_code1,"product_gram_unit":"g", "product_price_type":"rmb", "product_width":145}
        res = requests.post(url, data=form)
        self.assertEqual(res.json()["code"], "00000")

    def test_fabric_info_select3(self):
        """
        品号：GTGH20102702 成分：100%棉 库存:10
        :return:
        """
        global user_code_list
        user_code1 = user_code_list[0]
        url = "http://one.heartdub.cn:8082/fabric_info_select"
        form = {"user_code": user_code1,"product_code":"GTGH20102702","product_stock_ratio":"100%棉","product_stock":10}
        res = requests.post(url, data=form)
        self.assertEqual(res.json()["code"], "00000")

    def test_fabric_info_insert(self):
        """
        新建面料:传必传值
        :return:
        """
        global user_code_list, list
        info_code = info_code_list[0]
        ticket1 = list[0]
        headers = {"content-type": "application/x-www-form-urlencoded"}
        url = "http://one.heartdub.cn:8082/fabric_info_insert"
        form= {"ticket": ticket1,"refer": "1624869742216_c16a6080d7ec11eb8736a183c91b4699","info_name": "面料面料1",}
        res= requests.post(url, data=form,headers=headers)
        self.assertEqual(res.json()["code"], "00000")

    def test_fabric_info_insert1(self):
        """
        新建面料:面料名称：面料面料 供应商品号：GTGH20102702 计量单位：g 货币类型：rmb  成分：10%棉 卖点：婴儿
        :return:
        """
        global info_code_list
        info_code=info_code_list[0]
        ticket1=list[0]
        url = "http://one.heartdub.cn:8082/fabric_info_insert"
        headers={"content-type":"application/x-www-form-urlencoded"}
        form = {"ticket": ticket1,"refer": "1624869742216_c16a6080d7ec11eb8736a183c91b4699","info_name": "面料面料","product_code": "GTGH20102702","product_unit": "g","product_price_type": "rmb","product_stock_ratio": "10%棉","product_selling_point": "婴儿",}
        res = requests.post(url, data=form,headers=headers)
        self.assertEqual(res.json()["code"], "00000")
        self.assertNotEqual(res.json()["msg"], "execute failure")


    def test_fabric_info_insert2(self):
        """
        新建面料:参数组合
        :return:
        """
        global info_code_list
        info_code=info_code_list[0]
        ticket1=list[0]
        url = "http://one.heartdub.cn:8082/fabric_info_insert"
        headers={"content-type":"application/x-www-form-urlencoded"}
        form = {
            "ticket": ticket1,
            "refer": "1624869742216_c16a6080d7ec11eb8736a183c91b4699",
            "info_name": "面料面料",
            "product_code": "GTGH20102702",
            "product_unit": "g",
            # "product_price": "10",
            "product_price_type": "rmb",
            "product_stock": "10",
            "product_stock_ratio": "100%棉",
            "product_width": 145,
            "product_technics": "人工纺织",
            "product_selling_point": "婴儿",
        }
        res = requests.post(url, data=form,headers=headers)
        self.assertEqual(res.json()["code"], "00000")
        self.assertNotEqual(res.json()["msg"], "execute failure")

    def test_fabric_info_update(self):
        """
        修改面料：修改info_code参数
        :return:
        """
        global list,info_code_list
        info_code = info_code_list[0]
        ticket1 = list[0]
        url = "http://one.heartdub.cn:8082/fabric_info_update"
        form = {
            "ticket": ticket1,
            "info_code": info_code,
        }
        res = requests.post(url, data=form)
        self.assertEqual(res.json()["code"], "00000")
        self.assertEqual(res.json()["msg"], "修改行数:1")

    def test_fabric_info_update1(self):
        """
            修改面料：修改名称、标签、类别编码、备注、供应商品号、计量单位、价格、货币类型、库存、成分、幅宽、工艺、卖点
        :return:
        """
        global list,info_code_list
        info_code = info_code_list[0]
        ticket1 = list[0]
        url = "http://one.heartdub.cn:8082/fabric_info_update"
        form = {
            "ticket": ticket1,
            "info_code": info_code,
            "info_name":"新建面",
            "type_code":"ft0101",
            "remark":"备注信息",
            "product_code":"GTGH20102702",
            "product_unit":"g",
            "product_price":"100",
            "product_price_type":"rmb",
            "product_stock":"100",
            "product_stock_ratio":"涤纶",
            "product_width":"10",
        }
        res = requests.post(url, data=form)
        self.assertEqual(res.json()["code"], "00000")
        self.assertEqual(res.json()["msg"], "修改行数:1")

    def test_fabric_info_delete(self):
        """
        删除面料：必传参数
        :return:
        """
        global list,info_code_list
        info_code = info_code_list[0]
        ticket1 = list[0]
        url = "http://one.heartdub.cn:8082/fabric_info_delete"
        form = {
            "ticket": ticket1,
            "info_code": info_code,
        }
        res = requests.post(url, data=form)
        self.assertEqual(res.json()["code"], "00000")
        self.assertEqual(res.json()["msg"], "删除行数:1")


    def test_fabric_info_delete1(self):
        """
        删除面料：不传ticket，只传info_code,
        :return:
        """
        global list,info_code_list
        info_code = info_code_list[0]
        ticket1 = list[0]
        url = "http://one.heartdub.cn:8082/fabric_info_delete"
        form = {
            "info_code": info_code,
        }
        res = requests.post(url, data=form)
        self.assertEqual(res.json()["code"], "00000")

    def test_fabric_info_display_order(self):
        """
        设置试衣间展示顺序：必传参数
        :return:
        """
        global list,info_code_list
        info_code = info_code_list[0]
        ticket1 = list[0]
        url = "http://one.heartdub.cn:8082/fabric_info_display_order"
        form = {
            "ticket": ticket1,
            "info_code": info_code,
        }
        res = requests.post(url, data=form)
        self.assertEqual(res.json()["code"], "00000")
        self.assertEqual(res.json()["msg"], "成功设置行数:1")


class Test_Pattern_message(unittest.TestCase):

    def setUp(self):
        print("花型接口")

    def tearDown(self):
        print("测试接口：花型参数{}".format(form))

    def test_pattern_info_select(self):
        """
        查询我的花型列表：必传参数
        :return:
        """
        global user_code_list
        user_code1 = user_code_list[0]
        url = "http://one.heartdub.cn:8082/pattern_info_select"
        form = {"user_code":user_code1}
        res = requests.post(url, data=form)
        self.assertEqual(res.json()["code"],"00000")


    def test_pattern_info_select2(self):
        """
        查询我的花型列表：参数组合,按时间倒序
        :return:
        """
        global user_code_list
        user_code1 = user_code_list[0]
        url = "http://one.heartdub.cn:8082/pattern_info_select"
        form = {
            "user_code": user_code1,
            "order_by":"time_des"
        }
        res = requests.post(url, data=form)
        self.assertEqual(res.json()["code"], "00000")

    def test_pattern_info_select3(self):
        """
        查询我的花型列表：参数组合，按热度倒序
        :return:
        """
        global user_code_list
        user_code1 = user_code_list[0]
        url = "http://one.heartdub.cn:8082/pattern_info_select"
        form = {
            "user_code": user_code1,
            "order_by": "hot_des"
        }
        res = requests.post(url, data=form)
        self.assertEqual(res.json()["code"], "00000")


    def test_pattern_info_insert(self):
        """
        新建花型：传入refer和fabric_code
        :return:
        """
        global info_code_list,list
        info_code=info_code_list[0]
        ticket1=list[0]
        url = "http://one.heartdub.cn:8082/pattern_info_insert"

        form = {
            "ticket":ticket1,
            "refer": "1624869733661_bc50fcd0d7ec11eb8736a183c91b4699",
            # "info_name": '["001.png"]',
            "fabric_code":'1629972256535_f8f33270065411ecad9fffff3cffe6a8'
        }
        res = requests.post(url, data=form)
        self.assertEqual(res.json()["code"], "00000")


    def test_pattern_info_insert1(self):
        """
        新建花型：传入ticket、refer。info_name、fabric_code
        :return:
        """
        global info_code_list,list
        info_code=info_code_list[0]
        ticket1=list[0]
        url = "http://one.heartdub.cn:8082/pattern_info_insert"

        form = {
            "ticket":ticket1,
            "refer": "1624869733661_bc50fcd0d7ec11eb8736a183c91b4699",
            "info_name": '["001.png"]',
            "fabric_code":'1629972256535_f8f33270065411ecad9fffff3cffe6a8'
        }
        res = requests.post(url, data=form)
        self.assertEqual(res.json()["code"], "00000")
        self.assertEqual(res.json()["msg"],"成功上传1个花型")



    def test_pattern_info_update(self):
        """
        修改花型：传入ticket和info_code
        :return:
        """
        global info_code_list,list
        info_code=info_code_list[0]
        ticket1=list[0]
        url = "http://one.heartdub.cn:8082/pattern_info_update"
        form = {
            "ticket":ticket1,
            "info_code": info_code,
        }
        res = requests.post(url, data=form)
        self.assertEqual(res.json()["code"], "00000")

    def test_pattern_info_update2(self):
        """
        修改花型：ticket、info_code、info_name、remark
        :return:
        """
        global info_code_list,list
        info_code=info_code_list[0]
        ticket1=list[0]
        url = "http://one.heartdub.cn:8082/pattern_info_update"
        form = {
            "ticket":ticket1,
            "info_code": info_code,
            "info_name":'["002.png"]',
            "remark":"备注花型"
        }
        res = requests.post(url, data=form)
        self.assertEqual(res.json()["code"], "00000")

    def test_pattern_info_delete(self):
        """
        删除花型：必传参数
        :return:
        """
        global info_code_list,list
        info_code=info_code_list[0]
        ticket1=list[0]
        url = "http://one.heartdub.cn:8082/pattern_info_delete"
        form = {
            "ticket":ticket1,
            "info_code": info_code,
        }
        res = requests.post(url, data=form)
        self.assertEqual(res.json()["code"], "00000")

class Test_relation_api(unittest.TestCase):
    def setUp(self):
        print("关系部分接口测试")

    def tearDown(self):
        print("测试接口：关系接口参数{}".format(form))

    def test_relation_a_insert(self):
        """
        company创建邀请:传入必传值ticket
        :return:
        """
        ticket1=list[0]
        url="http://one.heartdub.cn:8082/relation_a_insert"
        form={
            "ticket":ticket1,
        }
        res=requests.post(url,data=form)
        self.assertEqual(res.json()["code"],"00000")

    def test_relation_a_insert2(self):
        """
        company创建邀请:参数组合
        :return:
        """
        ticket1 = list[0]
        url = "http://one.heartdub.cn:8082/relation_a_insert"
        form = {
            "ticket": ticket1,
            "remark_a_to_b":"小明"
        }
        res = requests.post(url, data=form)
        self.assertEqual(res.json()["code"], "00000")

    def test_relation_a_select(self):
        """
        company查询关系列表:传入必传值ticket
        :return:
        """
        ticket1 = list[0]
        url = "http://one.heartdub.cn:8082/relation_a_select"
        form = {
            "ticket": ticket1,

        }
        res = requests.post(url, data=form)
        relation_id=res.json()["result"][0]["id"]
        self.assertEqual(res.json()["code"], "00000")
        return relation_id


    def test_relation_a_select2(self):
        """
        company查询关系列表:参数组合
        :return:
        """
        ticket1 = list[0]
        url = "http://one.heartdub.cn:8082/relation_a_select"
        form = {
            "ticket": ticket1,
            "remark_a_to_b":""
        }
        res = requests.post(url, data=form)
        self.assertEqual(res.json()["code"], "00000")

    def test_relation_a_delete(self):
        """
        company删除一个关系:传入必传值
        :return:
        """
        relation_id=relation_list[0]
        ticket1 = list[0]
        url = "http://one.heartdub.cn:8082/relation_a_select"
        form = {
            "ticket": ticket1,
            "relation_id":relation_id
        }
        res = requests.post(url, data=form)
        self.assertEqual(res.json()["code"], "00000")


    def test_relation_a_order(self):
        """
        company将一个邀请的顺序调整到最高
        :return:
        """
        ticket1 = list[0]
        relation_id = relation_list[0]
        url = "http://one.heartdub.cn:8082/relation_a_order"
        form = {
            "ticket": ticket1,
            "relation_id":relation_id,
        }
        res = requests.post(url, data=form)
        self.assertEqual(res.json()["code"], "00000")
        self.assertEqual(res.json()["msg"],"调整成功")

    def test_relation_b_select(self):
        """
        duber查询关系列表:传入必传值ticket值
        :return:
        """
        ticket1 = list[0]
        url = "http://one.heartdub.cn:8082/relation_b_select"
        form = {
            "ticket": ticket1,
        }
        res = requests.post(url, data=form)

        self.assertEqual(res.json()["code"], "00000")




    def test_relation_b_select2(self):
        """
        duber查询关系列表:传入必传值ticket值
        :return:
        """
        ticket1 = list[0]
        url = "http://one.heartdub.cn:8082/relation_b_select"
        form = {
            "ticket": ticket1,
            "remark_b_to_a":""
        }
        res = requests.post(url, data=form)
        self.assertEqual(res.json()["code"], "00000")

    def test_relation_b_delete(self):
        """
        duber删除一个关系
        :return:
        """
        relation_id = relation_list[0]
        ticket1 = list[0]
        url = "http://one.heartdub.cn:8082/relation_b_delete"
        form = {
            "ticket": ticket1,
            "relation_id":relation_id
        }
        res = requests.post(url, data=form)
        self.assertEqual(res.json()["code"], "00000")

    def test_relation_b_order(self):
        """
        duber将一个邀请的顺序调整到最高:传必传值
        :return:
        """
        relation_id_duber=relation_id[0]
        ticket1 = list[0]
        url = "http://one.heartdub.cn:8082/relation_b_order"
        form = {
            "ticket": ticket1,
            "relation_id":relation_id_duber
        }
        res = requests.post(url, data=form)
        self.assertEqual(res.json()["code"], "00000")



    def test_product_account(self):
        """
        查询用户在本产品中的服务信息，例如：
                服务期限，存储额度，展示额度，等等
        :return:
        """
        ticket1 = list[0]
        url = "http://one.heartdub.cn:8082/product_account"
        form = {
            "ticket": ticket1,
        }
        res = requests.post(url, data=form)
        self.assertEqual(res.json()["code"], "00000")


def suite():
    unittest.TestSuite()
    FabricTestCase = unittest.makeSuite(Test_Fabric_message, "test")
    PatternTestCase = unittest.makeSuite(Test_Pattern_message, "test")
    relationTestCase=unittest.makeSuite(Test_relation_api,"test")

    allTest = unittest.TestSuite((FabricTestCase, PatternTestCase,relationTestCase))
    return allTest



if __name__ == '__main__':
    now = datetime.today()
    path = "D:\\PyApi_heartdub\\210830.html"
    fp = open(path, "w", encoding="utf-8")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="Fabric V1.0测试报告", description="测试详情")
    runner.run(suite())
    fp.close()

    # unittest.main()