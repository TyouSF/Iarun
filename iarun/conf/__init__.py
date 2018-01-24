import os
from configparser import ConfigParser


def read_conf(confile):
    '''
    读取配置文件，返回配置文件内容对象 cfg
    '''

    filename = os.path.join(__name__, confile)
    cfg = ConfigParser()
    cfg.read(filename)
    return cfg
