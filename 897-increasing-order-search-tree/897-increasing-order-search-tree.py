# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.dummyNode = TreeNode(None)
        
    def increasingBST(self, root: TreeNode) -> TreeNode:
        result = self.dummyNode
        self.rearrange(root)
        return result.right
        
    def rearrange(self, node):
        if not node:
            return
        
        self.rearrange(node.left)
        
        node.left = None
        self.dummyNode.right = node
        self.dummyNode = self.dummyNode.right
        
        self.rearrange(node.right)
        
        