import logging
import requests


def send_request(apidata):
    """
    分析测试用例自带参数、发送请求
    :param apidata: 测试用例
    :return:
    """
    try:
        method = apidata["get_type"]
        url = apidata['url']
        if apidata["header"] == "":
            #返回None
            header = None
        else:
            header=apidata["header"]
        #判断字典内测试数据是否为空
        if apidata['data'] == "":
            body_data = None
        else:
            #将值处理后用作请求参数
            body_data=apidata['data']
        s = requests.Session()
        re = s.request(method=method, url="http://one.heartdub.cn:8082"+url, data=body_data,headers=header)
        return re
    #     if method == "post":
    #         # re=None
    #         re = requests.post(url="http://one.heartdub.cn:8082"+url, headers=header, data=body_data)
    #         # return re
    #     else:
    #         # re=None
    #         re = requests.get(url="http://one.heartdub.cn:8082"+url, headers=header, params=body_data)
    #         # return re
    #     return re
    except Exception as error:
        logging.error("错误信息",error)


if __name__ == '__main__':
    case_dict = {"id": "1.0",
                 "get_type": "post",
                 "url": "/fabric_info_insert",
                 "interface": "查询面料",
                 "title": "新建面料:传必传值",
                 "expected": {"code":"00000"},
                 "header": {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"},
                 "data": {"ticket": "0bc580058515fa66b3d04390cec4276f2432bcc18175c55d47854baa8186054e",
                 "refer": "1624869742216_c16a6080d7ec11eb8736a183c91b4699",
                 "info_name": "面料面料1"}
                 }
    re = send_request(case_dict)
    # print(re.url)
    print(re.json())
    print(re.headers)












