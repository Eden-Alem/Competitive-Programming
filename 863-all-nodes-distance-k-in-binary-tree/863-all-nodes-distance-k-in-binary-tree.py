# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]
        
        graph = defaultdict(list)
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                queue.append(node.left)
                
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                queue.append(node.right)
                
        queue = deque([target])
        result = []
        visited = set([target])
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                
                for neigh in graph[node]:
                    if neigh not in visited:
                        visited.add(neigh)
                        queue.append(neigh)
                        
            k -= 1
            
            if k == 0:
                for n in queue:
                    result.append(n.val)
                break
                
        return result
                
                
                
                
                
                
                
                
        