from Readexcel import Readexcel
import readPath

def excel_dict(data):
    """
    1.将excel头部替换成英文的
    2.处理成dict格式
    """
    header = {
        '用例编号': 'id',
        '用例请求类型': 'get_type',
        '测试url': 'url',
        '测试接口': 'interface',
        '用例标题': 'title',
        '测试数据': 'data',
        '预期结果': 'expected',
        '请求头': 'header',
        '响应数据状态/json返回数据的code': 'code',
        '状态码': 'status',
        '响应状态': 'msg'
    }
    head = []
    list_dict_data = []
    for d in data[0]:
        # 获取到英文的头部内容如果为中文，则替换成英文 进行改成一个k
        # 传入两个参数的作用是 查到则返回查到的数据查不到则返回传入的原数据
        d = header.get(d)
        # 将去除的头部英文装进list中
        head.append(d)
    # 获取到数据进行切片处理，0坐标为标题，1坐标是头部
    for b in data[1:]:
        # 头部和内容拼接为json串
        dict_data = {}
        for i in range(len(head)):
            # 之所以判断类型，如果不进行判断会出现str的错误，strip去除空格也有转str的用法
            if isinstance(b[i], str):
                dict_data[head[i]] = b[i].strip()
            else:
                dict_data[head[i]] = b[i]
        # list里面是字典格式
        list_dict_data.append(dict_data)
    return list_dict_data


if __name__ == '__main__':
    file = 'D:\\PyApi_heartdub\\Request_api_new\\test_case\\testcase1.xls'
    e = Readexcel().get_excel(file, "fabric")
    n=excel_dict(e)
    print(n)
    print(n[0]["get_type"])  # 获取列表内第一个字典的get_type的值


