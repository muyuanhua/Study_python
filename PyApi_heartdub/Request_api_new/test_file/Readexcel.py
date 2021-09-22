import os
from readPath import path
import xlrd



class Readexcel():
    def get_excel(self,excelname,excelsheet)->list:
        cls=[]
        excel_path = os.path.join(path, "test_case", excelname)
        file=xlrd.open_workbook(excel_path)
        sheet=file.sheet_by_name(excelsheet)
        rows=sheet.nrows
        for i in range(0,rows):
            if sheet.row_values(0) !="用例编号":
                cls.append(sheet.row_values(i))
        return cls



if __name__ == '__main__':
    print(Readexcel().get_excel("testcase1.xls","fabric"))
    print(Readexcel().get_excel("testcase1.xls","fabric")[2][1])