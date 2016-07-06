# -*- coding: utf-8 -*-
'''
Created on 2016年7月6日

@author: frank_yen
'''

students = {"Tom":[100,90,88,95,55], "John":[70,78,60,89], "Amy":[50,66,20,88,30], "Bob":[99,64,80,72,90], "Tony":[100,83,92] }
students_average = {}
for i in students:
    print i, students[i]
    personal_score = students[i]
    sum = 0.0
    for j in personal_score:
        sum += j
    average_score = sum/len(personal_score)
    print i, ", 平均分數: ", average_score
    students_average[i] = average_score
print students_average

max_student = max(students_average)
min_student = min(students_average)
print "最高分, 學生: ", max_student, ", 分數: ", students_average[max_student]
print "最低分, 學生: ", min_student, ", 分數: ", students_average[min_student]
