class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges) 
        colors = [0] * n
        self.maxLen = -1
        def has_cycle(node, count):
            if colors[node] == -1:
                return False
            
            if colors[node] > 0:
                self.maxLen = max(self.maxLen, count - colors[node] + 1)
                return True
            
            count += 1
            colors[node] = count
            if edges[node] != -1:
                has_cycle(edges[node], count)
            
            colors[node] = -1
            return False
        
        for node in range(n):
            has_cycle(node, 0)
                
        return self.maxLen
                    
            
        