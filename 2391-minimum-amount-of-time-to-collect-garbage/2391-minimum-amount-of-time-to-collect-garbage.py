class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        prefix = [0]
        for t in travel:
            prefix.append((prefix[-1] + t))
            
        G, M, P = 0, 0, 0
        houses = 0
        for i, g in enumerate(garbage):
            houses += len(g)
            
            if "G" in g:
                G = i
                
            if "P" in g:
                P = i
                
            if "M" in g:
                M = i
                
        result = houses + prefix[P] + prefix[G] + prefix[M]
        return result
                
                
            
            
        