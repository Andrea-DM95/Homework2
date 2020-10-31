#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    #criterias
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    #number of changes
    answer=0
    if any(l in lower_case for l in password)== False:
        answer+=1
    if any(l in upper_case for l in password)==False:
        answer+=1
    if any(l in special_characters for l in password)==False:
        answer+=1
    if any(l in numbers for l in password)==False:
        answer+=1
    return max(answer,6-n)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
