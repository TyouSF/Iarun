from getrunargs import args
from loadcase import TestCase
from conf import read_conf
import requests

cfg = read_conf(args.configfilename)

api_host = cfg['API']['Host']  # 获取配置文件中接口域名
headers = dict(cfg['Headers'])  # 获取配置文件中接口所需传递的 headers

testcases = TestCase(args.filename).cases()  # 加载测试用例为列表


def run_case(testcases):
    if testcases:
        for case in testcases:
            response_data = requests.request(method=case['Method'],
                                             url=api_host + case['API'],
                                             json=case['RequestData'],
                                             headers=headers)
            expected = eval(case['Expected'])
            print('<-- 开始执行第 {} 条测试用例 -->'.format(case['No']))
            result = response_data.json()
            result_compare = result.copy()
            result_compare.update(expected)
            if result_compare == result:
                print('--> 测试结果： Passed')
            else:
                print('--> 测试结果： Failed')


if __name__ == '__main__':
    run_case(testcases)
