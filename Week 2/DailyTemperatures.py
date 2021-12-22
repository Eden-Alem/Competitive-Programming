class Solution:
    def dailyTemperatures(self, temperatures):
        remDict = {}
        monoStack = []       
        
        for i in range(len(temperatures)):
            while(len(monoStack) and (temperatures[i] > temperatures[monoStack[-1]])):
                remDict[monoStack.pop()] = i - monoStack[-1]                   
                
            monoStack.append(i)
        
        for a in monoStack:
            remDict[a] = 0
        
        resultStack = []
        for temp in range(len(temperatures)):
            resultStack.append(remDict[temp])
        
        return resultStack       
        
                                                                