class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        indegree = defaultdict(int)
        result = []
        visit = set()
        
        for u, v in adjacentPairs:
            adjList[u].append(v)
            adjList[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        
        q = deque() 
        for i in indegree:
            if indegree[i] == 1:
                q.append(i)
                break
        
        while q:
            val = q.popleft()
            
            if val not in visit:
                result.append(val) 
                visit.add(val)
            
                for neigh in adjList[val]:
                    q.append(neigh)
        
        return result