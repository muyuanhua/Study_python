import os

PROJECT_ROOT=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
LOG_PATH=os.path.join(PROJECT_ROOT,"NEW_testApi","log","api_test.log")
case_root = os.path.join(PROJECT_ROOT, "NEW_testApi",'database')  # 测试用例
results_root = os.path.join(PROJECT_ROOT,"NEW_testApi", 'results', 'results.xlsx')#测试结果
REPORT_PATG = os.path.join(PROJECT_ROOT,  "NEW_testApi",'report', 'index.html')  # 报告路径
TEST_JSON = os.path.join(PROJECT_ROOT, "NEW_testApi",'database', 'test_data.txt')  #存放接口返回数据
print(PROJECT_ROOT)
# print(LOG_PATH)
# print(case_root)
# print(results_root)
# print(REPORT_PATG)
# print(TEST_JSON)