import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    current_sum = 0
    best_sum = 0
    first = True

    for i in range(len(arr)-2):
        for j in range(len(arr[0])-2):
            current_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if first:
                best_sum = current_sum
                first = False
            elif current_sum > best_sum:
                best_sum = current_sum
    print(best_sum)
