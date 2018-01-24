import argparse


parser = argparse.ArgumentParser(
    description="assign to testfile, only support .csv files")

# 指定测试case的来源文件
parser.add_argument('-f', '--file', metavar='filename',
                    required=True, dest='filename',
                    help='TestCase will come from this file')

# 指定测试case的配置文件
parser.add_argument('-c', '--conf', metavar='configfilename',
                    required=True, dest='configfilename',
                    help='To assign the used configuration file')


args = parser.parse_args()
