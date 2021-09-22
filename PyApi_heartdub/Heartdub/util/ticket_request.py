import requests

def ticket():
    url_login = "http://api.heartdub.cn:8080/login"
    form = {
        "user_addr": "muyuanhua666@163.com",
        "user_pass": "myh123",
        "auth_code": "150be7d0a3d711eb81d2d1264cd620fb"
    }
    res = requests.post(url_login, data=form)
    user_code = res.json()["result"]["user_code"]
    ticket = res.json()["result"]["ticket"]


    url_infoCode = "http://one.heartdub.cn:8082/fabric_info_select"
    form = {
        "user_code": 202108111002491543221
    }
    res = requests.post(url_infoCode, data=form)
    info_code = res.json()["result"][0]["info_code"]
    return ticket
def user_code():
    url_login = "http://api.heartdub.cn:8080/login"
    form = {
        "user_addr": "muyuanhua666@163.com",
        "user_pass": "myh123",
        "auth_code": "150be7d0a3d711eb81d2d1264cd620fb"
    }
    res = requests.post(url_login, data=form)
    user_code = res.json()["result"]["user_code"]
    return user_code

def info_code():
    url_infoCode = "http://one.heartdub.cn:8082/fabric_info_select"
    form = {
        "user_code": 202108111002491543221
    }
    res = requests.post(url_infoCode, data=form)
    info_code = res.json()["result"][0]["info_code"]
    return info_code