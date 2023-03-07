class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n = len(nums)
        monoStack = [(nums[-1], 0)]
        steps = 0
        
        for i in range(n-2, -1, -1):
            cur_step = 0
            while monoStack and monoStack[-1][0] < nums[i]:
                cur_step = max(cur_step+1, monoStack[-1][1])
                monoStack.pop()
                
            steps = max(steps, cur_step)
            monoStack.append((nums[i], cur_step))
            
        return steps
        
        
        