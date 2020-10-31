#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the isValid function below.
def isValid(s):
    c=Counter(s)
    freq=c.values()
    times_freq=Counter(freq)
    
    if len(times_freq)==1:
        return "YES"
    if len(times_freq)==2:
        k1,k2=times_freq.keys()
        v1,v2=times_freq.values()
        if abs(k1-k2)==0 or (abs(k1-k2)==1 and (v1==1 or v2==1)):
            return 'YES'
        elif ((k1==1 and v1==1) or (k2==1 and v2==1)):
            return 'YES'
        else:
            return 'NO'
    else:
        return 'NO'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
