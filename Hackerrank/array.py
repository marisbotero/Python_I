#!/bin/python3

import math
import os
import random
import re
import sys


def inverse (arr):
    arr.reverse()
    
    for num in arr:
        a =  str(num)+ " "
      
        print(a, sep=' ', end='', flush=True)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    inverse(arr)