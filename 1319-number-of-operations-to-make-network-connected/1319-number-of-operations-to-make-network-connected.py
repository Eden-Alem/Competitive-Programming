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
                
            elif self.rank[n1Root] < self.rank[n2Root]:
                self.root[n1Root] = n2Root
                
            else:
                self.root[n1Root] = n2Root
                self.rank[n2Root] += 1
                
            self.n -= 1
            
    def isConnected(self, n1, n2):
        return self.find(n1) == self.find(n2)
            
    def components(self):
        return self.n
    

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        disjoint = DisjointSet(n)
        
        count = 0
        for connection in connections:
            node1 = connection[0]
            node2 = connection[1]
            
            if disjoint.isConnected(node1, node2):
                count += 1
                
            disjoint.union(node1, node2)
            
        components = disjoint.components()
        
        
        return (components - 1) if count >= (components - 1) else -1
            
            
            
        
        
        
        
        