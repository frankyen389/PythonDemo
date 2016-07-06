# -*- coding: utf-8 -*-
'''
Created on 2016年7月1日

@author: frank_yen
'''

import random

random_num = random.randint(1,20)
guess = 3
sum = 1
while guess != random_num:
    guess = random.randint(1,20)
    print "您猜",guess,",猜錯了,答案=",random_num
    sum += 1
print "恭喜您猜對了, 答案=",random_num
print "您總共猜",sum,"次"
