import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def check():
    stack = []
    s = input()
    for c in s:
        #print(c)
        if c == '(':
            stack.append(0);
        elif c == ')':
            if len(stack) > 0 and stack[-1] == 0:
                stack.pop()
            else:
                return -1
        elif c == '[':
            stack.append(2)
        elif c == ']':
            if len(stack) > 0 and stack[-1] == 2:
                stack.pop()
            else:
                return -1
        if c == '{':
            stack.append(4)
        elif c == '}':
            if len(stack) > 0 and stack[-1] == 4:
                stack.pop()
            else:
                return -1
    
    if len(stack) == 0:
        return 0
    else:
        return -1

def solve():
    t = int(input())
    for i in range(0,t):
        if check() == 0:
            print("YES")
        else:
            print("NO")
solve()            
