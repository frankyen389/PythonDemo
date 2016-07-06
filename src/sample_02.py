# -*- coding: utf-8 -*-
'''
Created on 2016年7月1日

@author: frank_yen
'''

num = int(input("Please input a number:"))
if num%2 == 0:
    print num,"是偶數"
else:
    print num,"是奇數"    



num = int(input("Please input a number:"))
sum = 0
for i in range(1,num+1):
    sum = sum + i
print "總和=",sum



num = int(input("Please input a number:"))
sum=0
i=1
while i <= num:
    sum += i
    i+=1
print "總和=",sum     



num = int(input("Please input a number:"))
for i in range(1,num+1):
    for j in range(1, num+1):
        print i,"*",j,"=",i*j



num = int(input("Please input a number:"))
i=1
j=1
while i <= num:
    while j <= num:
        print i,"*",j,"=",i*j
        j+=1
    j=1    
    i+=1
