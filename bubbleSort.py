#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#
def countSwaps(a):
    c  = 0
    for x in range(len(a)):
        for y in range(len(a)-1):
            if(a[y] > a[y+1]):
                c = c + 1
                temp = a[y]
                a[y] = a[y + 1]
                a[y + 1] = temp
                
    print(f'Array is sorted in {c} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
