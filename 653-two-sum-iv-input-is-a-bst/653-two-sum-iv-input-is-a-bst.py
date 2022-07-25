# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.uniq = set()
        
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        
        left = self.findTarget(root.left, k)
        if (k - root.val) not in self.uniq:
            self.uniq.add(root.val)
            
        else:
            return True
        
        right = self.findTarget(root.right, k)
        
        return right or left
        