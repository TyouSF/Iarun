# 项目结构规范

参见[Python 指南--结构化你的工程](http://pythonguidecn.readthedocs.io/zh/latest/writing/structure.html)

```
Iarun
├── README.md                   // 项目整体说明和索引文档
├── docs                        // 项目文档目录
│   ├── install.md              // 安装文档
│   ├── project-structure.md    // 项目结构文档
│   └── testcase.md             // 测试用例说明文档
└── iarun                       // 项目代码目录
    ├── conf                    // 项目配置目录    
    │   ├── __init__.py         // 载入配置文件
    │   └── default.ini         // 配置文件
    ├── example                  // 项目服务
    │   └── testserver.py       // 示例展示的服务
    ├── testcase                 // 项目测试用例存放
    │   └── sample.csv          // 测试用例示例
    ├── getrunargs.py           // 命令行定义
    ├── iarun.py                // 主运行程序
    └── loadcase.py             // 载入测试用例
```
