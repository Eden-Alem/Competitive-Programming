class DisjointSet:
    def __init__(self, n):
        self.n = n
        self.rank = [1] * n
        self.root = [i for i in range(n)]
        
    def find(self, parent):
        if self.root[parent] == parent:
            return parent
        
        self.root[parent] = self.find(self.root[parent])
        return self.root[parent]
    
    def union(self, node1, node2):
        n1Root = self.find(node1)
        n2Root = self.find(node2)
        
        if n1Root != n2Root:
            if self.rank[n1Root] > self.rank[n2Root]:
                self.root[n2Root] = n1Root
                
            elif self.rank[n1Root] < self.rank[n2Root]:
                self.root[n1Root] = n2Root
                
            else:
                self.root[n1Root] = n2Root
                self.rank[n1Root] += 1
                
            self.n -= 1
            
        
    def getGroups(self):
        return self.n

        
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        disjoint = DisjointSet(n)
        for n1 in range(n):
            for n2 in range(n):
                if isConnected[n1][n2] == 1:
                    disjoint.union(n1, n2)
                    
        return disjoint.getGroups()
        
        