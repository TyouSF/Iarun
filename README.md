# Iarun

'Iarun'，由 'interface auto run' 缩写而来。

# 简要说明

本项目原本是想基于 python 实现一个接口自动化测试框架。目前只是前期的一些简单思考，为了验证并亲自实践一下，遂先行写一个单一的接口测试示例。

当前仅仅支持请求数据以及返回数据均为 json 的 POST 类型接口。

其用途如下：

- 通过文档对接口测试用例进行编写和维护

  - 支持 .csv 文件类型

- 读取并执行测试用例

# 关于 CSV 文件编辑器

以下是推荐的 CSV 文件编辑器

> Win: [Ron's Editor](https://www.ronsplace.eu/)

> Mac: [Table Tool](https://github.com/jakob/TableTool)

# Python项目结构规范

[项目目录结构规范](docs/project-structure.md)

# 安装说明

1. Pytho主环境：

  - 本项目是基于**Python-3.5**进行的编写，请确保您所使用的python版本不低于3

2. 在使用前，请确保下列相关模块已经安装：

  - requests

# 如何演示

1. 进入到本项目 example 目录下，在终端执行 `python3 testserver.py` 启动测试服务
2. 新建一个终端窗口，在项目 iarun 目录下，执行 `python3 iarun.py -f sample.csv -c default.ini`
3. 查看终端输出打印的测试结果

本项目主程序文件为：[iarun.py](iarun/iarun.py)

**命令说明：**

- `-f`指定测试用例的文件，后接测试用例文件名
- `-c`指定配置文件，后接配置文件名

# 配置说明

1. 测试文件：存储在项目的`testcase`目录下
2. 配置文件：存储在项目的`conf`目录下

## 配置文件编写规范

1. 配置文件应当为`ini`格式文件
2. 配置参数说明：

  - `API` 配置测试接口的域名
  - `Headers` 配置接口请求的header数据

## 用例编写说明

[如何来编写测试用例](docs/testcase.md)
