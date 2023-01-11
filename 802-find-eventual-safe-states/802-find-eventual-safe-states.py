class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        
        colors = [0] * n
        
        def has_cycle(node):
            if colors[node] == 1:
                return True
            
            if colors[node] == 2:
                return False
            
            colors[node] = 1
            for neigh in graph[node]:
                if has_cycle(neigh):
                    return True
                
            colors[node] = 2
            return False
        
        result = []
        
        for node in range(n):
            if not has_cycle(node):
                result.append(node)
                
        return result
    