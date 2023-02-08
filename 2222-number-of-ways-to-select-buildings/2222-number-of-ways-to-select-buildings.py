class Solution:
    def numberOfWays(self, s: str) -> int:
        
        ones = [0]
        zeros = [0]
        for st in s:
            if st == '0':
                zeros.append(1 + zeros[-1])
                ones.append(ones[-1])
                
            elif st == '1':
                ones.append(1 + ones[-1])
                zeros.append(zeros[-1])
           
        ways = 0
        for i in range(1, len(s)-1):
            if s[i] == "0":
                left = ones[i]
                right = ones[-1] - ones[i+1]
                ways += (left * right)
                
            else:
                left = zeros[i]
                right = zeros[-1] - zeros[i+1]
                ways += (left * right)
                
        return ways
            
            
            
        
#         memo = {}
#         def ways(i, st, prev):            
#             if st == 3:
#                 return 1           
            
#             if i >= len(s):
#                 return 0
            
#             if (i, st, prev) in memo:
#                 return memo[(i, st, prev)]
            
#             take = 0
#             if prev != s[i]:
#                 take = ways(i+1, st+1, s[i])
                
#             not_take = ways(i+1, st, prev)
            
#             memo[(i, st, prev)] = take + not_take
            
#             return memo[(i, st, prev)]
        
#         return ways(0, 0, "2")
    
    
        
        
        
#         3 length - base case
#         0 -> 1
#         1 -> 0
#         i, string - state
#         answer - 101  010
        
#         recursive function(i, s, p):
#             len(s) == 3: 
#                 1
                
#             take = 0
#             if p != s[i]: take = function(i+1, s+s[i], s[i])
                
#             not_take = function(i+1, s, p)
            
#             return take + not_take

        
        
        
        
            
        
        
        
        
        