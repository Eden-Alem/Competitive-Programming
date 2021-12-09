# Accepting inputs
m, n = map(int,  input().split())
value = 0
 
if (m % 2 == 0):
    value = (m // 2) * n
else:
    value = ((m // 2) * n) + (n // 2)
 
print(value)