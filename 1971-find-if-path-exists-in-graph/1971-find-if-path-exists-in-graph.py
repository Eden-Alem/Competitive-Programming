class DisjointSet:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        self.n = n
        
    def find(self, node):
        if self.root[node] == node:
            return node
        
        self.root[node] = self.find(self.root[node])
        return self.root[node]
    
    def union(self, n1, n2):
        n1Root = self.find(n1)
        n2Root = self.find(n2)
        
        if n1Root != n2Root:
            if self.rank[n1Root] > self.rank[n2Root]:
                self.root[n2Root] = n1Root
                
            elif self.rank[n1Root] < self.rank[n2Root]:
                self.root[n1Root] = n2Root
                
            else:
                self.root[n1Root] = n2Root
                self.rank[n2Root] += 1
                
            self.n -= 1
            
    def isConnected(self, n1, n2):
        return self.find(n1) == self.find(n2)
                 
                
        
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        disjoint = DisjointSet(n)
        for edge in edges:
            disjoint.union(edge[0], edge[1])
            
        return disjoint.isConnected(source, destination)
        
        
        