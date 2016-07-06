# -*- coding: utf-8 -*-
'''
Created on 2016年7月4日

@author: frank_yen
'''

myList = [1,2,3,4]
myList.append(5)
myList += [6]
print myList
for i in myList:
    print i

myTuple = (1,2,3,4)
print myTuple
for i in myTuple:
    print i

myNewList = list(myTuple)
myNewList.append(5)
print myNewList

myNewTuple = tuple(myList)
print myNewTuple



myDictionaries = {'item1':'a', 'item2':'b'}
print myDictionaries['item1']

myDictionaries['item3'] = 'c'
print myDictionaries['item3']

for i in myDictionaries:
    print i, myDictionaries[i]
