# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#       6, 24     
#         4        
#  3, 9          2, 11   
#   8              5
#  2, 1           1, 6
#  0   1            6
# 1,0 1, 1        1, 6
# 0,0
# /1

# time complexity O(n)
# space complexity O(n-1)

# count = 3

# Base case: 1, n.val/1
# Return values: No, Sum
# States: node


class Solution:
    def __init__(self):
        self.count = 0
        
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.calculateAverage(root)
        return self.count
        
    def calculateAverage(self, node):
        if not node:
            return (0, 0)
        
        leftResult = self.calculateAverage(node.left)
        rightResult = self.calculateAverage(node.right)
        
        nodeNo = leftResult[0] + rightResult[0] + 1
        Sum = leftResult[1] + rightResult[1] + node.val
        
        sumAverage = Sum // nodeNo
        if sumAverage == node.val:
            self.count += 1
        
        return (nodeNo, Sum)
        
        