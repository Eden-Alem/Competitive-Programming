# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        
        result = []
        while queue:
            maxTemp = float("-inf")
            for i in range(len(queue)):
                val = queue.popleft()
                maxTemp = max(maxTemp, val.val)
                if val.left:
                    queue.append(val.left)
                if val.right:
                    queue.append(val.right)
                    
            result.append(maxTemp)
            
        return result