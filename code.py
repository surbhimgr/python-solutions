#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    def kp(num):
        s = str(num**2)
        right = s[len(s)//2:]
        left = '0' if s[:len(s)//2] == '' else s[:len(s)//2]
        return True if int(left) + int(right) == num else False
    ans=[]
    for i in range(p,q+1):
        i=int(i)
        if kp(i):
            ans.append(i)
    if len(ans) == 0:
        print("INVALID RANGE")
    else:
        print(" ".join(str(x) for x in ans))


if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
