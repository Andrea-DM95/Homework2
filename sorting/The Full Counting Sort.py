#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def dashify(arr):
    for i in range(int(len(arr)/2)):
        arr[i][1]='-'
        
def countSort(arr):
    dashify(arr)
    arr=sorted(arr, key= lambda arr:int(arr[0]))
    for i in range (len(arr)):
        print(arr[i][1], end=' ')

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
