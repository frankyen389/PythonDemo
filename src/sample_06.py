# -*- coding: utf-8 -*-
'''
Created on 2016年7月6日

@author: frank_yen
'''

x = "global"

def showScope():
    x = "local"
    return x

if __name__ == '__main__':
    print x
    print showScope()
    print x


