class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        graph = defaultdict(list)
        
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
            
            
        leafNodes = []
        
        for node in graph:
            if len(graph[node]) == 1:
                leafNodes.append(node)
            
        while n > 2:
            n -= len(leafNodes)
            
            leaves = []
            for leaf in leafNodes:
                val = graph[leaf].pop()
                graph[val].remove(leaf)
                
                if (len(graph[val]) == 1):
                    leaves.append(val)
            leafNodes = leaves
                    
        return leafNodes