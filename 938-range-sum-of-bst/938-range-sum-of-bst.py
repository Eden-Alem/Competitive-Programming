# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.Sum = 0
        
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.inRange(root, low, high)       
            
        return self.Sum
        
    def inRange(self, node, low, high):
        if not node:
            return  0
        
        if (node.val >= low and node.val <= high):
            self.Sum += node.val
        
        leftVal = self.inRange(node.left, low, high)
        rightVal = self.inRange(node.right, low, high)
            
        return node.val
        
        