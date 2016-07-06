# -*- coding: utf-8 -*-
'''
Created on 2016年7月6日

@author: frank_yen
'''

students = {"Tom":[100,90,88,95,55], "John":[70,78,60,89], "Amy":[50,66,20,88,30], "Bob":[99,64,80,72,90], "Tony":[100,83,92] }
names = ["",""]
scores = [0,100]
for name,grades in students.items():
    score = sum(grades)/len(grades)
    if score > scores[0]:
        scores[0] = score
        names[0] = name
    if score < scores[1]:
        scores[1] = score
        names[1] = name
data = list(zip(names,scores))
print('The highest:%s,%f'%(data[0][0],data[0][1]) )
print('The lowest:%s,%f'%(data[1][0],data[1][1]) )