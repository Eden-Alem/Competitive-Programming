class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        directional = [[0,1],[0,-1],[1,0],[-1,0]]
        
        visited = []
        stack = []
        stack.append([sr,sc])
        startPoint = image[sr][sc]
        image[sr][sc] = newColor
        while stack:
            val = stack.pop()   
            if val not in visited:
                visited.append(val)
                for direction in directional:
                    row = direction[0] +  val[0]
                    column = direction[1] + val[1]

                    if row < 0 or row >= len(image) or column < 0 or column >= len(image[0]):
                        continue

                    if image[row][column] == startPoint:
                        image[row][column] = newColor
                        stack.append([row,column])
                    
                    
        
        return image
        