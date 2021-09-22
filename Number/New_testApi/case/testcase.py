import unittest
import ddt
from data.data_driven import data_processing
from lib.sendrequest import send_request
from lib.utlis import *
import json
# import paramunittest


@ddt.ddt
class TestCase(unittest.TestCase):

    @ddt.data(*case_data("testcase"))
    def test_run_case(self, data):
        """
        执行测试脚本
        :param data: 参数化后测试用例|dict类型
        :return:
        """
        self.response = send_request(data)  # 返回response
        print('________')
        logging.info("页面返回信息：%s" % self.response.json())
        self.result = self.response.json()
        code = data['code']  # 获取表内code
        status = data['status']  # 获取表内状态码
        msg = data['msg']  # 获取响应状态
        # 判断前置条件是否为1 ---新增
        # if data['precondition'] == 1:
        #     # 为1：将内容写进test_data文件用来替换下个接口的参数
        #     with codecs.open(setting.TEST_JSON, 'w', encoding='utf-8') as f:
        #         json.dump(self.result, f)


        if code == self.result['code'] and status == self.response.status_code \
                and msg == self.result['msg']:  # 判断返回数据是否和表内数据相同
            self.msg_data = "PASS"
        else:
            self.msg_data = "FAIl"
        Excel('w', 'D:\\PyApi_heartdub\\Number\\New_testApi\\results\\results.xlsx') .write(write_result(value7=str(self.result), value8=self.msg_data))
        self.assertEqual(self.result['code'], code)
        self.assertEqual(self.response.status_code, status)
        self.assertEqual(self.result['msg'], msg)


