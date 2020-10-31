#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    diagonal_1=[]
    diagonal_2=[]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                diagonal_1.append(arr[i][j])
            if (i+j)==(len(arr)-1):
                diagonal_2.append(arr[i][j])
    return (abs(sum(diagonal_1)-sum(diagonal_2)))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
