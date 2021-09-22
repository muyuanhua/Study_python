# __* coding:utf-8 _*_
from Send_request import Send_request
from test_file.read_data import excel_dict
from Readexcel import Readexcel

# file = 'D:\\PyApi_heartdub\\Request_api_new\\test_case\\testcase1.xls'
# e = Readexcel().get_excel(file, "fabric")
# date=read_data.excel_dict(e)
# print(date)
# method=date[0]['get_type']
# print(method)


def set_data(date):


    method=date["get_type"]
    url=date["url"]
    # request_data=data[i]["data"]
    if date['header'] == "":
        date['header']=None
    else:
        header=eval(date['header'])

    if date['data'] == "":
        date['data']=None
    else:
        data = eval(date['data'])
    result=Send_request().run_request(method=method,url="http://one.heartdub.cn:8082" + url,data=data,header=header)
    return result


if __name__ == '__main__':
    dat={'id': '1.0',
        'get_type': 'post',
        'title': '查询面料类别：只传ticket，查询所有类别',
        'header': "{'content-type':'application/x-www-form-urlencoded'}",
        "url": "/fabric_type_select",
        "data": "{'ticket':'6cf20e91a1ea8a03bcd7c4720f110d04914e535390d7f081a7ab4df291c1d678'}"}
    a=set_data(dat)
    print(a.json())
    # print(a.headers)




