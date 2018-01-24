import os
import csv


# 测试用例类
class TestCase:
    '''
    获取测试用例数据，并提供headers
    实例化类：传入测试文件名
    '''

    def __init__(self, test_file):
        base_path = os.path.split(os.path.abspath(__name__))[0]
        self.test_file = os.path.join(base_path, 'testcase/' + test_file)

    def cases(self):
        '''
        读取测试用例文件，加载测试用例，返回 testcases 对象
        '''

        testcases = []  # 加载测试用例的列表集
        with open(self.test_file, 'r', encoding='utf-8') as f:
            reader = list(csv.DictReader(f))
            for r in reader:
                d = {}
                d['No'] = r['No']
                d['API'] = r['API']
                d['Method'] = r['Method']
                d['RequestData'] = eval(r['RequestData'])
                d['Expected'] = r['Expected']
                testcases.append(d)

        return testcases
