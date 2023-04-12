# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        
        nodes = set()
        child_nodes = set()
        
        graph = defaultdict(set)
        for p, c, isLeft in descriptions:
            nodes.add(p)
            nodes.add(c)
            
            child_nodes.add(c)
            
            graph[p].add((c, isLeft))
        
        root_val = (nodes - child_nodes)
        
        result = root_node = TreeNode(list(root_val)[0])
        
        queue = deque([root_node])
        
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                
                for (child, isLeft) in graph[node.val]:
                    if isLeft:
                        node.left = TreeNode(child)
                        queue.append(node.left)
                        
                    else:
                        node.right = TreeNode(child)
                        queue.append(node.right)
                        
        return result

        
        
        
        
        
        
        
        
        
        
            
            
        
        