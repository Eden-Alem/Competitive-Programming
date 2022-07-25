# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.minimum = float("inf")
        self.previous = float("-inf")
        
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        
        self.getMinimumDifference(root.left)
        
        val = root.val        
        self.minimum = min(self.minimum, val - self.previous)
        self.previous = val
        
        self.getMinimumDifference(root.right)
        
        return self.minimum
            
        
            
        
        