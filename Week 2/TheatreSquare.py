import math
n, m, a = map(int,  input().split())

height = math.ceil(n/a)
width = math.ceil(m/a)

result = height * width

print(result)
