#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr.sort()
    result=[]
    min_dif=abs(arr[1]-arr[0])
    for i in range(len(arr)-1):
        if min_dif>abs(arr[i+1]-arr[i]):
            min_dif=abs(arr[i+1]-arr[i])
            result.clear()
            result.append(arr[i])
            result.append(arr[i+1])
        elif min_dif==abs(arr[i+1]-arr[i]):
            result.append(arr[i])
            result.append(arr[i+1])
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
