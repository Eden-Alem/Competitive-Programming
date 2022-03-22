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

def solve(num, comfy, students):  
    if num <= comfy[0]:
        return "NO"

    left = 0
    right = students - 1
    while (left <= right):
        mid = (left + right) // 2
        if (comfy[mid] < num):
            left = mid + 1
        else:
            right = mid - 1
    # print(left)
    if (students // 2 < (students - left)) and (left != 0):
        return "YES"
    else:
        return "NO"




    
output = ""
questions, students = invr()
comfy = inlt()
comfy.sort()

while questions > 0:
    num = inp()
    if questions-1 != 0:
        output += solve(num, comfy, students) + "\n"
    else:
        output += solve(num, comfy, students)
    questions -= 1
    
print(output)
