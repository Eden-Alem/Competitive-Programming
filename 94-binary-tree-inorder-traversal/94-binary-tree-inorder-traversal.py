# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        self.checker(root, result)
        return result
    
    def checker(self, root, result):
        if root:
            self.checker(root.left, result)
            result.append(root.val)
            self.checker(root.right, result)
            
            