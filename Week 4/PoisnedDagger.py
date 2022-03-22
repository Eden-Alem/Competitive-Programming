import sys
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

def counter(array, k, dies):
    count = 0
    for a in range(len(array)-1):
        count += min(array[a+1] - array[a], k)

    return count + k >= dies


def solve(dies, times):

    left = 1
    right = dies
    while (left <= right):
        mid = (left + right) // 2
        if (counter(times, mid, dies)):
            right = mid - 1
        else:
            left = mid + 1


    return str(left)


    
output = ""
n = inp()

while n > 0:
    m, dies = invr()
    times = inlt()
    if n-1 != 0:
        output += solve(dies, times) + "\n"
    else:
        output += solve(dies, times)
    n -= 1

    
print(output)
