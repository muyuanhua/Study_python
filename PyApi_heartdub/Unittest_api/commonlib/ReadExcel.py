import xlrd

class ReadExcel():
    def readexcel(self):
        book=xlrd.open_workbook("D:\\PyApi_heartdub\\Unittest_api\\test\\test_case.xls")
        sheet=book.sheet_by_name("Sheet1")
        row_num=sheet.nrows
        col_num=sheet.ncols
        s=[]
        key=sheet.row_values(0)
        if row_num<0:
            print("无数据")
        else:
            for i in range(row_num):
                if sheet.row_values(0)=="id":

                    s.append(sheet.row_values(i))
            return s
        # for i in range(0,6):




if __name__ == '__main__':

    r=ReadExcel()
    b=r.readexcel()
    print(b)
    print(b[0])
