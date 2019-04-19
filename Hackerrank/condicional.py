import math
import os
import random
import re
import sys


def condictional(N):
    if N % 2 != 0:
        print("Weird")
    else:
        if N <= 5:
            print("Not Weird")
        elif N <= 20:
            print("Weird")
        else:
            print("Not Weird")


if __name__ == '__main__':
    N = int(input())
    condictional(N)
