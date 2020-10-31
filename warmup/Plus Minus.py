#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive=0
    negative=0
    zeros=0
    n=len(arr)
    for i in arr:
        if i>0:
            positive+=1
        if i<0:
            negative+=1
        if i==0:
            zeros+=1
    print('{:f}\n{:f}\n{:f}'.format((positive/n),(negative/n),(zeros/n)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
