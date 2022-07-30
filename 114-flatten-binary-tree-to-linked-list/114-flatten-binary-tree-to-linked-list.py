# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# p l r
#   7
#       1     9
#         2   
#           3    
#             4 - returned 
#               5
              


# 2 - 1 - 5
# if root.left:
#     temp = root.right       4                       5
#     root.right = root.left   2 - 3               1 - 2 - 3 - 4
#     root.left = null
#     returnedNode.right = temp
# return returnedNode
# Till null while:
#     root.right.right = temp   2 - 3 - 4  o(m) 
# 1 2 5

# m < n

# O(E) + O(n*m)

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        
        if not root.right and not root.left:
            return root
        
        leftTail = self.flatten(root.left)
        rightTail = self.flatten(root.right)
        
        if root.left:
            temp = root.right
            root.right = root.left
            root.left = None
            leftTail.right = temp
            
        return rightTail if rightTail else leftTail
        
        
        