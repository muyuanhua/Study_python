import requests

class Send_request():

    def send_post(self,url,data,header=None):
        re=requests.post(url=url,data=data,headers=header)
        return re
    def send_get(self,url,data,header=None):
        re=requests.get(url=url,params=data,headers=header)
        return re

    def run_request(self,method,url,data,header):
        result=None
        if method=="post":
            result=Send_request().send_post(url,data,header)
        else:
            result=Send_request().send_get(url,data,header)
        return result


if __name__ == '__main__':
    a= Send_request().run_request("post", "http://one.heartdub.cn:8082/fabric_type_select", {"ticket":"9b00995a3349f3f4b9a1b44318f84820ba831af76fa58ea0a2658b5c23e87676"})
    print(a.json())