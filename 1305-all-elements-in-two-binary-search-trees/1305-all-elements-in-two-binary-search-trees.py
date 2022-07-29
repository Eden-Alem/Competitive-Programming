# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.allElements = []
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.inorder(root1)
        self.inorder(root2)
        return sorted(self.allElements)
        
    def inorder(self, node):
        if not node:
            return
        
        self.inorder(node.left)
        self.allElements.append(node.val)
        self.inorder(node.right)
        
        