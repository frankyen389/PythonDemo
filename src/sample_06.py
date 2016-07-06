# -*- coding: utf-8 -*-
'''
Created on 2016年7月6日

@author: frank_yen
'''

x = "global"

def showScope():
    x = "local"
    return x

def takeInt():
    try:
        num = int(input("請輸入整數:"))
    except ValueError:
        print "這不是整數"
    else:
        return num    
            

if __name__ == '__main__':
    print x
    print showScope()
    print x
    num = takeInt()
    print num
    


