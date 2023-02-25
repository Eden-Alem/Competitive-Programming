class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        
        for i, (u,v) in enumerate(equations):
            graph[u].append((v, values[i]))
            graph[v].append((u, 1 / values[i]))
            
        result = []
        for src, dest in queries:
            if src not in graph:
                result.append(float(-1))
                continue
                
            queue = deque([(src, 1)])
            visited = set([src])
            validAnswer = False
            
            while queue:
                node, value =  queue.popleft()
                if node == dest:
                    result.append(value)
                    validAnswer = True
                    
                for neigh, val in graph[node]:
                    if neigh not in visited:
                        visited.add(neigh)
                        queue.append((neigh, value * val))
                        
            if not validAnswer:
                result.append(float(-1))
                
        return result