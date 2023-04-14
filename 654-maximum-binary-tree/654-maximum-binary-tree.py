# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        return self.constructTree(nums, 0, len(nums))
        
    def constructTree(self, nums, l , r):
        if l == r:
            return None
        
        max_index = self.getMaxIndex(nums, l, r)
        root = TreeNode(nums[max_index])
        root.left = self.constructTree(nums, l, max_index)
        root.right = self.constructTree(nums, max_index + 1, r)
        
        return root
        
    def getMaxIndex(self, nums, l, r):
        max_index = l
        
        for i in range(l, r):
            if nums[max_index] < nums[i]:
                max_index = i
                
        return max_index