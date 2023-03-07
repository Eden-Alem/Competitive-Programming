class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        scores = self.compute(nums, True)
        return scores[0] >= scores[1]
        
    def compute(self, nums, turn):
        if (len(nums) == 0):
            return (0,0)

        if (len(nums) == 1):
            if (turn): return (nums[0], 0)
            return (0, nums[0])

        if (turn):
            x = nums[0]
            (t1, t2) = self.compute(nums[1:], not turn)

            y = nums[-1]
            (p1, p2) = self.compute(nums[:-1], not turn)

            if (t1 + x > p1 + y):
                return (t1 + x, t2)
            return (p1 + y,p2)

        else:
            x = nums[0]
            (t1, t2) = self.compute(nums[1:], not turn)

            y = nums[-1]
            (p1, p2) = self.compute(nums[:-1], not turn)        

            if (t2 + x > p2 + y):
                return (t1, t2 + x)
            return (p1, p2 + y)



    
        