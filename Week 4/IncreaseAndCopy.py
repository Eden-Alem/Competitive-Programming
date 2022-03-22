import sys
import math
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

def solve(num):    
    sqrtNum = int(math.floor(math.sqrt(num)))

    if (sqrtNum - 5) <= 0:
        sqrtNum += 5
    
    minimum = float("inf")
    for i in range(sqrtNum - 5, sqrtNum + 6):
        val = i + ((num - i - 1) // i)
        minimum = min(minimum, val)

    return str(int(minimum))



    
output = ""
n = inp()

while n > 0:
    num = inp()
    if n-1 != 0:
        output += solve(num) + "\n"
    else:
        output += solve(num)
    n -= 1
    
print(output)
