import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    arr_2 = []
    for num in arr:
        arr_2.append(0)

    for num in range(len(arr)):
        arr_2[len(arr) - num - 1] = arr[num]
    for num in range(len(arr_2)):
        print(arr_2[num], end = " ")
