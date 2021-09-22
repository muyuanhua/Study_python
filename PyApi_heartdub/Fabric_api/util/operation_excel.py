import xlrd
from xlutils.copy import copy

class OperationExcel:
    def __init__(self,file_name=None,sheel_id=None):
        if file_name:
            self.film_name=file_name
            self.sheel_id=sheel_id
        else:
            self.film_name='D:\PyApi_heartdub\Fabric_api\case\interface.xls'
            self.sheel_id=0
        self.data=self.get_data()

    #获取sheets的内容
    def get_data(self):
        data=xlrd.open_workbook(self.film_name)
        tables=data.sheets()[self.sheel_id]
        return tables

    #获取单元格的行数
    def get_lines(self):
        tables=self.data
        return tables.nrows

    #获取某一个单元格的内容
    def get_cell_value(self,row,col):
        tables=self.data
        cell=tables.cell_value(row,col)
        return cell
    #写入数据
    def write_value(self,row,col,value):
        """
        写入到excel数据
        :param row:
        :param col:
        :param value:
        :return:
        """
        read_data=xlrd.open_workbook(self.film_name)
        write_data=copy(read_data)
        sheet_data=write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.film_name)

    #根据对应case_id找到对应行的内容
    def get_rows_data(self,case_id):
        num=0
        coldata=self.get_cell_value()
        for data in coldata:
            if case_id in data:
                return num
            num+=1
        return num

    #根据对应的case_id找到对应的行号
    def get_row_num(self,case_id):
        num=0
        coldata=self.get_col_values()
        for data in coldata:
            if case_id in data:
                return num
            num+=1
        return num
    #根据行号，找到该行的数据
    def get_row_value(self,row):
        tables=self.data
        row_data=tables.row_values(row)
        return row_data

    #根据列号，找到该列的数据
    def get_col_values(self,col=None):
        if col != None:
            col_data=self.data.col_values(col)
        else:
            col_data=self.data.col_values(0)
        return col_data

if __name__ == '__main__':
    a=OperationExcel()
    print(a.get_lines())
    print(a.get_cell_value(15,9))
