# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.mem = { 0: [], 1: [TreeNode()] }
        
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        return self.binaryTree(n)
        
    def binaryTree(self, n):
        
        if n in self.mem:
            return self.mem[n]
        
        result = []
        
        for left in range(n):
            right = n - left - 1
            
            leftSubTree = self.binaryTree(left)
            rightSubTree = self.binaryTree(right)
            
            for n1 in leftSubTree:
                for n2 in rightSubTree:
                    result.append(TreeNode(0, n1, n2))
                    
        self.mem[n] = result
        
        return result
            
        



