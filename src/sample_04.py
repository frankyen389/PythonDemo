# -*- coding: utf-8 -*-
'''
Created on 2016年7月4日

@author: frank_yen
'''

class MyClass:
    var1 = "hello world"
    
    def showMsg(self):
        print "This is a function"

myObject = MyClass()
print myObject.var1 
myObject.showMsg()
