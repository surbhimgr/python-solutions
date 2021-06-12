#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n, k, arr):
    # Write your code herefor
    pn=0
    cur=0
    cnt=0
    for i in arr:
        pg=math.ceil(i/k)
        cur=pn+1
        pn+=pg
        t=0
        #print(i,pre,pn)
        for j in range(cur,pn+1):
            s=t+1
            if j==pn:
                t=i
            else:
                t+=k
            if j>=s and j<=t:
                cnt+=1
            #print(s,t,j,cnt)
    return cnt
            
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
