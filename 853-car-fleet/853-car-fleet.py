class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mappedDict = {}
        for i in range(len(position)):
            mappedDict[position[i]] = speed[i]
        
        sMappedDict = dict(sorted(mappedDict.items()))
        
        times = []
        monoStack = []
        
        for s in sMappedDict.keys():
            temp = (target - s) / sMappedDict[s]
            times.append(temp)
            
        for i in range(len(times)):
            while(len(monoStack) and times[i] >= monoStack[-1]):
                monoStack.pop()
            monoStack.append(times[i])
        
        return len(monoStack)
        
        