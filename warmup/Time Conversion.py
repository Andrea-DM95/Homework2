#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    time= s[:-2].split(":")
    AM_PM=s[-2:]
    if AM_PM == "AM":
        if time[0]=="12":
            time[0]="00"
    else:
        if time[0]!="12":
            time[0]= str(int(time[0])+12)
    return ':'.join(time)


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
