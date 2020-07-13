
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    
    if N%2 != 0:
        p = 1
    elif N > 20:
        p = 0
    elif N in range(2,5):
        p = 0
    else:
        p = 1

    if p == 1:
        print("Weird")
    elif p == 0:
        print("Not Weird")
    else:
        print("Error")
