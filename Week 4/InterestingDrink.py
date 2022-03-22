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

def solve(shops, days, numberOfCoins):
    
    if (numberOfCoins < shops[0]):
        return "0"


    # Inside every shop:
    #     if coins less than shop:
    #         increase count

    left = 0
    right = len(shops) - 1
    while (left <= right):
        mid = (left + right) // 2
        if (shops[mid] <= numberOfCoins):
            left = mid + 1
        else:
            right = mid - 1


    return str(left)


    
output = ""
n = inp()
shops = inlt()

days = inp()

numberOfCoins = []
for i in range(days):
    numberOfCoins.append(inp())

shops.sort()

i = 0
while days!=0:
    if days-1 != 0:
        output += solve(shops, days, numberOfCoins[i]) + "\n"
    else:
        output += solve(shops, days, numberOfCoins[i])
    days-=1
    i += 1
    
print(output)
