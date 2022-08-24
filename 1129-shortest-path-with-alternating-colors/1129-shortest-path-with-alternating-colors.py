class Solution:
    def __init__(self):
        self.visited = set()
        
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        self.redPath = defaultdict(list)
        self.bluePath = defaultdict(list)
        
        for a, b in redEdges:
            self.redPath[a].append(b)
        
        for a, b in blueEdges:
            self.bluePath[a].append(b)
            
        self.ansB = [0] + [float("inf")] * (n-1)
        self.ansR = [0] + [float("inf")] * (n-1)
        self.shortestPath(0, 'red', 0)
        self.shortestPath(0, 'blue', 0)
        
        ans = [0] + [float("inf")] * (n-1)
        
        for a in range(len(ans)):
            ans[a] = min(self.ansB[a], self.ansR[a])
        

        return list(map(lambda x: x if x!=float('inf') else -1, ans))
        
    def shortestPath(self, node, color, level):
        neigh = []
        ans = []
        
        if color == 'red':
            self.ansR[node] = level
            neigh = self.redPath[node]
        else:
            self.ansB[node] = level
            neigh = self.bluePath[node]
        
        newColor = 'red' if color == 'blue' else 'blue'
        
        if newColor == 'red':
            ans = self.ansR
        else:
            ans = self.ansB
            
        for n in neigh: 
            if level < ans[n]:
                self.shortestPath(n, newColor, level+1)
                