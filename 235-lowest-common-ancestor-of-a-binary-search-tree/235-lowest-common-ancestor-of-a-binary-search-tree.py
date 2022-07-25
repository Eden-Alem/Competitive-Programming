# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        maxi = max(p.val, q.val)
        mini = min(p.val, q.val)
        
        if (maxi >= root.val and mini <= root.val):
            return root
        
        if (maxi < root.val and mini < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        
        if (maxi > root.val and mini > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        