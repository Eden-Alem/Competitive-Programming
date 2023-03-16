# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.array = []
        
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.inorderConstruct(root)
        return self.constructTree(self.array)        
    
    def constructTree(self, arr):
        if not len(arr):
            return
        
        mid = len(arr) // 2
        rootNode = TreeNode(arr[mid])
        rootNode.left = self.constructTree(arr[:mid])
        rootNode.right = self.constructTree(arr[mid+1:])
        
        return rootNode
        
        
    def inorderConstruct(self, node):
        if not node:
            return
        
        self.inorderConstruct(node.left)
        self.array.append(node.val)
        self.inorderConstruct(node.right)
    
        