class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        n = len(arr)
        
        visited = {}
        for i in range(n):
            if arr[i] not in visited:
                visited[arr[i]] = i
            
            if ((2 * arr[i] in visited) and (visited[2 * arr[i]] != i)) or ((arr[i]/2 in visited) and (visited[arr[i]/2] != i)):
                return True
            
        return False
            
        