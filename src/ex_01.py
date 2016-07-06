# -*- coding: utf-8 -*-
'''
Created on 2016年7月5日

@author: frank_yen
'''

num = 1000
print int(1000)/2

nums = [1,1,1,2,2,3,4,5]
print nums
nums = list(set(nums))
print nums

nums = (10,5,7,1,6,2)
print nums
nums = list(nums)
nums.sort()
print tuple(nums)

nums = (10,5,7,1,6,2)
print nums
nums = sorted(nums)
nums = tuple(nums)
print nums

num = input('請輸入任一整數:')
if isinstance(num, int):
    print '此數值為整數'
else:
    print '此數值不為整數'    
print num

user_input = input("Enter something:")
if type(user_input) == int:
    print("Is a number")
else:
    print("Not a number")
print user_input

userInput = 0
while True:
  try:
     userInput = int(input("Enter something: "))
     print("Yes an integer!")
     break    
  except ValueError:
     print("Not an integer!")
