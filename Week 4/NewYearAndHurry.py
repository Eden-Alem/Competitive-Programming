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

def binarySearch(array, target):
    left = 0
    right = len(array) - 1

    while (left <= right):
        mid = (left + right) // 2
        if (array[mid] <= target):
            left = mid + 1
        else:
            right = mid - 1
    
    return left

def solve(probs, mins):
    prefixSums = [5]
    for i in range(2, 10):
        prefixSums.append((i * 5) + prefixSums[-1])
    
    target = 240 - mins
    
    val = binarySearch(prefixSums, target)

    if val > probs:
        return str(probs)

    return str(val)


    
output = ""

probs, mins = invr()

output += solve(probs, mins)
    
print(output)
