#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    if n==0:
        return 1
    else:
        f=n*extraLongFactorials(n-1)
        return f
if __name__ == '__main__':
    n = int(input())

    print(extraLongFactorials(n))
    
