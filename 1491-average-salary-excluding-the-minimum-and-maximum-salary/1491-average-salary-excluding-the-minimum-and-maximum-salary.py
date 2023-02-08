class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        n = len(salary)
        
        s = 0
        for i in range(1, n-1):
            s += salary[i]
            
        avg = s / (n-2)
        
        return avg