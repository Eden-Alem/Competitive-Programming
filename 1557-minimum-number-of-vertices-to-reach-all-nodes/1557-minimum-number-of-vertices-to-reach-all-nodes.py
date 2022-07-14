class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        inwards = {}
        for e1, e2 in edges:
            inwards[e2] = inwards.get(e2,0)+1
            
        result = []
        for node in range(n):
            if node not in inwards:
                result.append(node)
                
        return result
        