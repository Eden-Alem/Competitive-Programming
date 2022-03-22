from collections import deque
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

def minSteps(thirties, target):

    if thirties == target:
        return 0

    queue = deque()
    time = {}
    time[thirties] = 0
    queue.append(thirties)
    while queue:
        curr = queue.popleft()

        if curr + 4 == target:
            return time[curr] + 1
        if curr - 1 == target:
            return time[curr] + 1

        temp = curr + 4
        if temp not in time:
            time[temp] = time[curr] + 1
            queue.append(temp)

        temp = curr - 1
        if temp not in time:
            time[temp] = time[curr] + 1
            queue.append(temp)       


def solve(num):    
    if minSteps(31, num) <= minSteps(32, num):
        return str(31)
    else:
        return str(32)






    
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

 
 
