import requests

class Runmain:

    def send_post(self,url,data):
        response=requests.post(url=url,data=data).json()
        return response

    def send_get(self,url,data):
        response=requests.get(url=url,data=data).json()
        return response

    def run_main(self,url,data,params,method):
        respose=None
        if method=='get':
            respose=self.send_get(url,params)
        else:
            respose=self.send_post(url,data)
        return respose