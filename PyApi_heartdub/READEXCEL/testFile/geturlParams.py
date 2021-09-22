from testFile.readConfig import ReadConfig
from readExcel import readExcel
import re

readconfig=ReadConfig()

class geturlParams():
    def get_url(self):
        url_path=readExcel().get_xls("heartdub_api.xls","Sheet1")
        # print(url_path)
        url_list=[]
        i=1
        for i in range(len(url_path)):
            new_url=readconfig.get_http('scheme') + "://" + readconfig.get_http('baseurl')+":" +readconfig.get_http('port') + url_path[i][1]
            # print(new_url)
            i=i+1
            url_list.append(new_url)
        return url_list


if __name__ == '__main__':
    # print(geturlParams().get_url())
    print(geturlParams().get_url())