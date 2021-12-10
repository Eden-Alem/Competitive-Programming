#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    frequencyArray = [0] * 100
    
    # [2,3,2]
    # [0 0 2 1 0 0 0 0 0]
    # [0 1 2 3]
    for i in range(len(arr)):
        frequencyArray[arr[i]] += 1
    
    # print(frequencyArray)
    return frequencyArray

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
