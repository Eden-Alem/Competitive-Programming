class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        monotonic = []
        
        for i, temp in enumerate(temperatures):
            while monotonic and temp > monotonic[-1][1]:
                monoI, monoTemp = monotonic.pop()
                result[monoI] = (i-monoI)
                
            monotonic.append([i, temp])
            
        return result