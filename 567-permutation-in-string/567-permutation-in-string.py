class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        ns1, ns2 = len(s1), len(s2)
        
        if (ns1 > ns2):
            return False
        
        s1Count = defaultdict(int)
        s2Count = defaultdict(int)
        
        for i in range(ns1):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1
            
        checks = 0
        for n in range(26):
            if (s1Count[n] == s2Count[n]):
                checks += 1
                
        l = 0
        
        for r in range(ns1, ns2):
            if (checks == 26):
                return True
            
            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if (s1Count[index] == s2Count[index]):
                checks += 1                
            elif (s1Count[index] + 1 == s2Count[index]):
                checks -= 1
                
            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if (s1Count[index] == s2Count[index]):
                checks += 1
            elif (s1Count[index] - 1 == s2Count[index]):
                checks -= 1
                
            l += 1
            
            
        return checks == 26
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            