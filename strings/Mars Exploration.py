#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    mes='SOS'*int(len(s)/3)
    err=0
    for i in range(len(s)):
        if s[i]!=mes[i]:
            err+=1
    return err

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
