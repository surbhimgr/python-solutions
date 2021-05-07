#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):

    cnt = 0
    for i in range(max(a),min(b)+1) :
        for j in a :
            if i%j!=0 :
                break
        else :
            for k in b :
                if k%i!=0 :
                    break
            else :
                cnt+=1
    return cnt
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
