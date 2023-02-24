class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        rounds = 0
        
        all_tasks = Counter(tasks)
        
        for task, count in all_tasks.items():
            if count == 1:
                return -1
            
            if (count % 3 == 0):
                rounds += (count // 3)
                
            else:
                rounds += ((count // 3) + 1)
                
        return rounds

                
                
                
            