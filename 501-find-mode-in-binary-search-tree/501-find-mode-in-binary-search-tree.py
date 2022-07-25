# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.freq = defaultdict(int)
        
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.find(root)
        result = sorted(self.freq.items(), key=lambda kv: kv[1])
        res = result[-1][1]
        
        answer = []
        for k,v in self.freq.items():
            if res == v:
                answer.append(k)
                
        return answer

        
    def find(self, node):
        if not node:
            return 
        
        self.freq[node.val] += 1
        self.find(node.left)
        self.find(node.right)
        
       
        