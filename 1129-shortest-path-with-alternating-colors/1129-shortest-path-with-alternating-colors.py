class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        self.red = defaultdict(list)
        self.blue = defaultdict(list)
        
        for s, d in redEdges:
            self.red[s].append(d)
            
        for s, d in blueEdges:
            self.blue[s].append(d)
            
        result = [float("inf")] * n
        
        self.resultR = [float("inf")] * n
        self.resultB = [float("inf")] * n
        
        self.shortestPath(0, "red", 0)
        self.shortestPath(0, "blue", 0)
        
        for i in range(n):
            result[i] = min(self.resultR[i], self.resultB[i])
            
        return list(map(lambda x:x if x!=float("inf") else -1, result))
            
        
        
    def shortestPath(self, node, color, level):
        neigh = []
        if color == "red":
            self.resultR[node] = level
            neigh = self.red[node]
        else:
            self.resultB[node] = level
            neigh = self.blue[node]
            
        newColor = "red" if color == "blue" else "blue"
        
        result = []
        result = self.resultR if newColor == "red" else self.resultB
        
        for n in neigh:
            if level < result[n]:
                self.shortestPath(n, newColor, level+1)
        