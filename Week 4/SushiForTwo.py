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


def solve(sushi):
    result = []
    point = 0
    s = 0
    while s < len(sushi)-1:
        if sushi[s] == sushi[s+1]:
            point += 1
        else:
            result.append((sushi[s], point + 1))
            point = 0
        s += 1
    result.append((sushi[s], point + 1))


    response = 0
    for a in range(len(result) - 1):
        val = min(result[a][1], result[a+1][1])
        response = max(val, response)

    return response * 2



n = inp()
sushi = inlt()
output = solve(sushi)
    
print(int(output))
