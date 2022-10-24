class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {}
        dictT = {}
        
        for sL in s:
            dictS[sL] = dictS.get(sL, 0) + 1
            
        for tL in t:
            dictT[tL] = dictT.get(tL, 0) + 1
            
        if len(dictT.keys()) != len(dictS.keys()):
            return False
        
        for ele in dictS.keys():
            if ((ele not in dictT.keys()) or (dictT[ele] != dictS[ele])):
                return False 
            
        return True