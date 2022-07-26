# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.i = 0
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        lower = 0
        upper = 1001
        
        return self.order(lower, upper, preorder)
        
    def order(self, lower, upper, preorder):
        if self.i == len(preorder):
            return
        
        val = preorder[self.i]
        if val < lower or val > upper:
            return
        
        self.i += 1
        root = TreeNode(val)
        root.left = self.order(lower, val, preorder)
        root.right = self.order(val, upper, preorder)
        
        return root
        
            
        