#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the separateNumbers function below.
def separateNumbers(s):
    sub=[]
    for i in range(1,int(len(s)/2)+1):
        sub.append(s[:i])
    for i in range(len(sub)):
        to_check=sub[i]
        j=1
        while len(to_check) < len(s):
            to_check += str(int(sub[i])+j)
            j+=1
        if to_check==s:
            print ("YES "+sub[i])
            break
    else:
        print("NO")


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
