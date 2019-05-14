#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Configuration
'''

__author__ = 'Kepler Wang'

import config_default

class Dict(dict):
    '''
    Simple dict but support access as x.y style.
    '''
    def __init__(self, names=(), values=(), **kw):
        super(Dict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

# 结合config_default.py, config_override.py关于DB配置的dict，结合成一个Dict类
def merge(defaults, override):
    r = {}
    for k, v in defaults.items():
        if k in override:
            if isinstance(v, dict):
                r[k] = merge(v, override[k])
            else:
                r[k] = override[k]
        else:
            r[k] = v
    return r

# 转换为dict方法
def toDict(d):
    D = Dict()
    for k, v in d.items():
        D[k] = toDict(v) if isinstance(v, dict) else v
    return D

configs = config_default.configs

# 读取config_default.py, config_override.py内的连接DB配置
# 两个配置信息结合成一个dict
try:
    import config_override
    configs = merge(configs, config_override.configs)
except ImportError:
    pass

configs = toDict(configs)
