class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set)
        indegree = [0] * numCourses
        
        for course, pre in prerequisites:
            graph[pre].add(course)
            indegree[course] += 1
            
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
              
        count = 0
        while queue:
            course = queue.popleft()
            count += 1
            
            for neigh in graph[course]:
                indegree[neigh] -= 1
                
                if indegree[neigh] == 0:
                    queue.append(neigh)
                    
        return count == numCourses
        
        