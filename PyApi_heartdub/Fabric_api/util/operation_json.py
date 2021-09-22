import json

class OperationJson:

    def __init__(self,file_path=None):
        self.file_path=file_path
        self.data=self.read_data()

    #读取json文件
    def read_data(self):
        with open(self.file_path) as fp:
            data= json.load(fp)
            return data

    # 根据关键字获取数据
    '''
    dict['key']只能获取存在的值，如果不存在则触发KeyError
    dict.get(key, default=None)，返回指定键的值，如果值不在字典中返回默认值None
    excel文件中请求数据有可能为空，所以用get方法获取
    '''
    def get_data(self,key):
        return self.data.get(key)

    #将cookies 数据填写入json文件
    def write_data(self,data):
        with open(r"D:\PyApi_heartdub\Fabric_api\dataconfig\cookie.json",'w')as fp:
            fp.write(json.dumps(data))


if __name__ == '__main__':
    opjson=OperationJson()
    print(opjson.get_data('ticket'))
    print(type(opjson.read_data()))