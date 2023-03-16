class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        
        def backtrack(i, path):
            if i == len(graph)-1:
                result.append(path.copy())
                return 
            
            for neigh in graph[i]:
                path.append(neigh)
                backtrack(neigh, path)
                path.pop()
                
        backtrack(0, [0])
        return result
            
        