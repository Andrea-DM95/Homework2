#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    #print(day)
    notification=0
    i=0
    lim=(len(expenditure)-1)-d
    while i<=lim:
        his=expenditure[i:i+d]
        transaction=expenditure[i+d]
        his.sort()
        median=0
        if d%2==0:
            median=(his[(d//2)]+his[(d//2)-1])/2
        else:
            median=his[int(d/2)]
        if transaction>= (2*(median)):
            notification+=1
        i+=1
    return notification

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
