#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    to_place=arr[n-1]
    for i in range(n-2,-1,-1):
        if arr[i]<to_place:
            arr[i+1]=to_place
            print(*arr)
            return
        if arr[i]>to_place:
            arr[i+1]=arr[i]
            print(*arr)
    arr[0]=to_place
    print(*arr)
    return

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
