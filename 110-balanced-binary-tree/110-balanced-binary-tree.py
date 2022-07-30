# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.check_balanced(root)[0]
        
    def check_balanced(self, node):
        if not node:
            return (True, -1)
        
        left = self.check_balanced(node.left)
        right = self.check_balanced(node.right)
        
        is_balanced = left[0] and right[0] and abs(left[1]-right[1]) <= 1
        length = max(left[1], right[1]) + 1
        
        return (is_balanced, length)
        
        
        
        