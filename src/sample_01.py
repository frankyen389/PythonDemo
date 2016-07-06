# -*- coding: utf-8 -*-
'''
Created on 2016年7月1日

@author: frank_yen
'''

def loopMsg(i,j,k):
    for i in range(j,k):
        print "num=",i
        if i <=5:
            print "Smaller or equal then 5.\n"
        else:
            print "Larger then 5.\n"
    return "finished loop"        

print loopMsg(1,1,10)

print "this is a text plus a number",1
print "this is a text plus a number" + str(1)



oslist = ["Windows", "Linux", "MacOS"]
#get the first element
print oslist[0]
#get the last element
print oslist[-1]
# Sublist - first and second element
print oslist[0:2]
oslist.append("Android")
for i in oslist:
    print i
# remove duplicates from the list
oslist = ["Windows", "Windows", "Linux"]
oslist = list(set(oslist))
for i in oslist:
    print i



even_numbers = [2,4,6,8,10]
odd_numbers = [1,3,5,7,9]
all_numbers = even_numbers + odd_numbers
print even_numbers
print odd_numbers
print all_numbers

for i in even_numbers:
    print i
else:
    print "error"

#if break statement is executed inside for loop then the "else" part is skipped
for k in even_numbers:
    print k
    if k==6:
        break
else:
    print "error"

#note that "else" part is executed even if there is a continue statement
for j in even_numbers:
    if j == 6:
        continue
    print j
else:
    print "error"
