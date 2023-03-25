# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = (10 ** 9) + 7
        sums = []
        
        def dfs(node):
            if not node:
                return 0
            
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            
            cur_sum = left_sum + right_sum + node.val           
            sums.append(cur_sum)
            
            return cur_sum
        
        total = dfs(root)
        
        max_product = 0
        
        for s in sums:
            max_product = max(max_product, (total - s) * s)
            
        return max_product % MOD
        