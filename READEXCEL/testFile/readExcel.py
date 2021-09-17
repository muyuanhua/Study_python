import os
import getPathInfo
from xlrd import open_workbook

path=getPathInfo.get_path()

class readExcel():
    def get_xls(self,xls_name,sheet_name):
        cls = []
        xlspath = os.path.join(path,"testCase",xls_name)
        file = open_workbook(xlspath)
        sheet = file.sheet_by_name(sheet_name)
        nrows = sheet.nrows
        for i in range(nrows):
            if sheet.row_values(i)[0] !=u"case_name":
                cls.append(sheet.row_values(i))
        return cls

if __name__ == '__main__':
    print(readExcel().get_xls("heartdub_api.xls","Sheet1"))
    print(readExcel().get_xls("heartdub_api.xls","Sheet1")[2][1])
    print(readExcel().get_xls("heartdub_api.xls","Sheet1")[1][2])

