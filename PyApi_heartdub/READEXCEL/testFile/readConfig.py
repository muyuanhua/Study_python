import os
import configparser
import getPathInfo

path=getPathInfo.get_path()
config_path=os.path.join(path+"\\testFile","config.ini")
config=configparser.ConfigParser()
a=config.read(config_path,encoding="utf-8")
print(config_path)

class ReadConfig():
    def get_http(self,name):
        value = config.get("HTTP",name)
        return value

    def get_email(self,name):
        value = config.get("EMAIL",name)
        return value


if __name__ == '__main__':
    print("HTTP中的baseurl值为：",ReadConfig().get_http("baseurl"))
    print('EMAIL中的开关on_off值为：',ReadConfig().get_email("on_off"))