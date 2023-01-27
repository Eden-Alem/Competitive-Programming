class DisjointSet:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        self.n = n
        
    def find(self, node):
        if node == self.root[node]:
            return node
        
        self.root[node] = self.find(self.root[node])
        return self.root[node]
    
    def union(self, n1, n2):
        n1Root = self.find(n1)
        n2Root = self.find(n2)
        
        if (n1Root != n2Root):
            if self.rank[n1Root] > self.rank[n2Root]:
                self.root[n2Root] = n1Root
                
            elif self.rank[n2Root] > self.rank[n1Root]:
                self.root[n1Root] = n2Root
                
            else:
                self.root[n1Root] = n2Root
                self.rank[n2Root] += 1
                
            self.n -= 1
            
    def isConnected(self, n1, n2):
        return self.find(n1) == self.find(n2)
    
    
    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        disjoint = DisjointSet(len(edges))
        
        for edge in edges:
            node1 = edge[0]-1
            node2 = edge[1]-1
            if disjoint.isConnected(node1, node2):
                return edge
            
            disjoint.union(node1, node2)
        
        
        
        