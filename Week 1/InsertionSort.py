def insertionSort(array):
    for i in range(1, len(array)):
        value = array[i]
        j = i - 1

        while (j >= 0 and value < array[j]):
            array[j+1] = array[j]
            j-=1

        array[j+1] = value

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    for i in range(1, n):
        val = arr[i]
        
        j = i - 1
        while (j >= 0 and val < arr[j]):
            arr[j+1] = arr[j]
            j -= 1            
        arr[j+1] = val
        
        print(' '.join(map(str,arr)))
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)


        