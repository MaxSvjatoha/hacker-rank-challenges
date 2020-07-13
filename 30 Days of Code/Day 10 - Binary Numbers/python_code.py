import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    l = bin(n).split("b")
    l2 = str(l[1])
    consec = 0
    bestconsec = 0
    for num in l2:
        if num == "1":
            consec += 1
            if consec > bestconsec:
                bestconsec = consec
        else:
            if consec > bestconsec:
                bestconsec = consec
            consec = 0
    print(bestconsec)
