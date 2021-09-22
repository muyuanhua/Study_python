import hashlib
import json
from datetime import *
import requests


#获取cookies值
user_name = "13668418734"
user_pass = hashlib.md5(b"myh123").hexdigest()
url = "http://one.heartdub.cn:8080/login"
from_data = {
        "user_addr":user_name,
        "user_pass":user_pass,
}
login_response = requests.post(url, data=from_data)
assert login_response.text == "success"
c = login_response.cookies


def make_order():  #提交订单并获取订单id
    global c
    url = "http://www.xxx.com/ajax/create_order"
    from_data={"restaurant_id":11196,
               "menu_item_total":"12.00",
               "menu_items_data":"[{'id': '1653196','p':'2','q':'6'}]",
               "delivery_fee":"3.00"
                }
    make_response=requests.post(url,data=from_data,cookies=c)
    res=make_response.text
    id=json.load(res)["order_id"]
    assert id !=""
    return id

def place_order(id):
    global c
    global user_name
    time=datetime.now()+timedelta(hours=1)
    url="http://www.xxx.com/ajax/place_order/"
    from_data={
        "order_id":id,
        "customer_name":"xxxx",
        "mobile_number":user_name,
        "delivery_address":"xxxxx",
        "preorder":"yes",
        "preorder_time":time,
        "pay_type":"cash"
    }
    place_response=requests.post(url,data=from_data,cookies=c)
    res=place_response.text
    assert res == "success"
    print("订餐成功")


def sms():
    result = ask_sms()
    if result == "{'status':'ok','need_sms':'False'}":
        return
    else:
        request_sms()
        code = get_sms()
        validate_sms(code)

def ask_sms():
    global c
    global user_name
    url ="http://www.xxx.com/ajax/is_order_need"
    from_data = {"mobile":user_name}
    ask_response=requests.post(url,data=from_data,cookies=c)
    res = ask_response.text
    return res

def request_sms():
    global c
    global user_name
    url="http://www.xxx.com/ajax/common_sms_code/"
    form_data={
        "mobile":user_name
    }
    sms_response=requests.post(url,data=form_data,cookies=c)
    res = sms_response.text
    assert res == "True"

def get_sms():
    global user_name
    url = "http://www.xxx.com/manager/login.action"
    from_data = {"user":"admin","pwd":123456}
    login_response = requests.post(url,data=from_data)
    cookie = login_response.cookies
    url2 = "http://www.xxx.com/manager/smsmanager"
    form_data2 = {
        "phone":user_name
    }
    code_response = requests.post(url2,data=form_data2,cookies=cookie)
    code = code_response.text
    assert code != ""
    return code

def validate_sms(code):
    global c
    global user_name
    url="http://www.xxx.com/ajax/calidate_sms_code/"
    form_data={
        "mobile":user_name,
        "sms_code":code
    }
    validate_response=requests.post(url,data=form_data,cookies=c)
    res=validate_response.text
    assert code == "True"


if __name__ == '__main__':
    make_order()
    sms()
    id=validate_sms(id)