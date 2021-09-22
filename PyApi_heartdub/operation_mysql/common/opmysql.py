# -*- coding：utf-8 -*-
import logging
import os
import pymysql
from public import config

class OperationDBInterface(object):
    #初始化数据库连接
    def __init__(self,host_db='localhost',user_db="root",passwd_db="123456",name_db='test_interface',port_db=3306,link_type=0):
        """
        :param host_db: 数据库服务主机
        :param user_db: 数据库用户名
        :param passwd_db: 数据库密码
        :param name_db: 数据库名称
        :param port_db: 端口号、整型数据
        :param link_type: 连接类型，用于设置输出数据是元组还是字典，默认是字典，link_type=0
        :return:游标
        """
        try:
            if link_type==0:
                self.coon=pymysql.connect(host=host_db,user=user_db,passwd=passwd_db,db=name_db,port=port_db,charset="utf8",cursorclass=pymysql.cursors.DictCursor)
            else:
                self.coon=pymysql.connect(host=host_db,user=user_db,passwd=passwd_db,db=name_db,port=port_db,charset="utf8")
            self.cur=self.coon.cursor()
        except pymysql.Error as e:
            print("创建连接数据库失败|MySQL Error %d：%s"%(e.args[0],e.args[1]))
            logging.basicConfig(filename=config.src_path+'\log\syserror.log',level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s %(message)s')
            logger=logging.getLogger(__name__)
            logger.exception(e)

    #定义单挑数据操作，包含删除，更新
    def op_sql(self,condition):
        """

        :param condition:SQL语句，该通用方法可用来替代updataone，
        :return:字典形式
        """
        try:
            self.cur.execute(condition) #执行SQL语句
            self.coon.commit()
            result = {"code": "0000","message": "执行通用操作成功","data": "%s"}
        except pymysql.Error as e:
            self.coon.rollback()
            result = {"code":"9999","message": "执行通用操作失败","data":[]}
            print("数据库错误|op_sql %d: %s" %(e.args[0],e.args[1]))
            logging.basicConfig(filename=config.src_path + '\log\syserror.log', level=logging.DEBUG, format='%(asctime)s%(filename)s[line:%(lineno)d]%(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)
        return result

    # 查询表中单条数据
    def select_one(self,condition):
        try:
            rows_affect=self.cur.execute(condition)
            if rows_affect > 0:
                results=self.cur.fetchone()
                result={"code":"00000","message":"执行单条语句成功","data":results}
            else:
                result = {"code": "00000", "message": "执行单条语句成功", "data": []}
        except pymysql.Error as e:
            self.coon.rollback()
            result={"code":"-1001","message":"执行单条语句异常","data":[]}
            print("数据库错误|select_one %d: %s"%(e.args[0],e.args[1]))
            logging.basicConfig(filename=config.src_path + "log/syserror.log",level=logging.DEBUG,format='%(asctime)s %(filmename)s[line:%(lineno)d]%（levelname)s %(message)s')
            logger=logging.getLogger(__name__)
            logger.exception(e)
        return result
    # 查询表中多条数据
    def select_all(self,condition):
        try:
            rows_affect=self.cur.execute(condition)
            if rows_affect>0:
                self.cur.scroll(0,mode='absolute')
                results=self.cur.fetchall()
                result={"code":"0000","message":"执行批量查询成功","data":results}
            else:
                result={"code":"0000","message":"执行批量查询成功","data":[]}
        except pymysql.Error as e:
            self.coon.rollback()
            result={"code":"-1001","message":"执行批量查询异常","data":[]}
            print("数据库错误|select_all %d: %s"%(e.args[0],e.args[1]))
            logging.basicConfig(filename=config.src_path +"log/syserror.log",level=logging.DEBUG,format="%(asctime)s %(filename)s [line:%(lineno)d]% (levelname)s %(message)s")
            logger=logging.getLogger(__name__)
            logger.exception(e)
        return result




    # 定义表中插入数据操作
    def insert_data(self,condition,params):
        try:
            results=self.cur.executemany(condition,params)
            self.coon.commit()
            result={"code":"0000","message":"执行批量查询操作成功","data":results}
        except pymysql.Error as e:
            self.coon.rollback()
            result={"code":"-1001","message":"执行批量插入异常","data":[]}
            print("数据库错误|insert_data %d: %s"%(e.args[0],e.args[1]))
            logging.basicConfig(filename=config.src_path+"log/syserror.log",level=logging.DEBUG,format="%(asctime)s %(filename)s [line:%(lineno)d]% (levelname)s %(message)s")
            logger=logging.getLogger(__name__)
            logger.exception(e)
        return result

    # 关闭数据库
    # def __del__(self):
        # if self.cur != None:
        #     self.cur.close()
        # if self.coon !=None:
        #     self.coon.close()



if __name__ == '__main__':
    # path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    sql=OperationDBInterface()
    result_select_all=sql.select_all("select * from config_total")
    result_select_one=sql.select_one("select * from config_total where id=1")
    result_op_sql = sql.op_sql("update config_total set  value_config='mytest12' where id=16")
    result_insert_data = sql.insert_data("insert into config_total (key_config,value_config,description,status) values (%s,%s,%s,%s)",
                                         [('测试进行','mytest00','文档测试0','0'),('mytest222','mytest122',"我的测试212",'1212')])
    print(result_select_all["data"],result_select_all["message"])
    print(result_select_one["data"],result_select_one["message"])
    print(result_op_sql["data"],result_op_sql["message"])
    print(result_insert_data["data"],result_insert_data["message"])



