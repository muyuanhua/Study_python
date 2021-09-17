import requests
import json

class RunMain():
    def send_post(self,url,data):
        result=requests.post(url=url,data=data)
        res=result.text
        return res

    def send_get(self,url,data):
        result=requests.get(url=url,params=data)
        res=result.text
        return res

    def run_main(self,method,url=None,data=None):
        result=None
        if method=="post":
            result=self.send_post(url,data)
        elif method=="get":
            result=self.send_get(url,data)
        else:
            print("method错误")
        return result

if __name__ == '__main__':  # 通过写死参数，来验证我们写的请求是否正确
    result1 = RunMain().run_main('post', 'http://api.heartdub.cn:8080/login', {'user_addr': '1127535539@qq.com','user_pass':'myh123',"auth_code":"150be7d0a3d711eb81d2d1264cd620fb"})
    result2 = RunMain().run_main('get', 'http://api.heartdub.cn:8080/login', 'name=xiaoming&pwd=111')
    print(result1)
    print(result2)

