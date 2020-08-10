import math
import os
import random
import re
import sys



#
# Complete the 'kSub' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY nums
#

k = int(input())
a = []
n = int(input())
for i in range(0,n):
    a.append(int(input()))
bucket = []
for i in range(k):
    bucket.append([])
currSum  = 0
for i,num in enumerate(a):
    currSum += num
    bucket[currSum%k].append(i)
total = 0
for i  in range(len(bucket)):
    if i == 0:
        total+= (len(bucket[0]) * (len(bucket[i]) +1))/2
    else:
        total += (len(bucket[i]) * (len(bucket[i]) -1) )/ 2
print (int(total))