class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        scores = self.game(nums, True)
        return scores[0] >= scores[1]
        
    def game(self, nums, turn):
        if len(nums) == 0:
            return (0, 0)
        
        if len(nums) == 1:
            if turn:
                return (nums[0], 0)
            return (0, nums[0])
        
        if turn:
            first = nums[0]
            pf1, pf2 = self.game(nums[1:], not turn)
            
            
            last = nums[-1]
            pl1, pl2 = self.game(nums[:-1], not turn)
            
            if (first + pf1 > last + pl1):
                return (first+pf1, pf2)
            
            return (last+pl1, pl2)
            
        else:
            first = nums[0]
            pf1, pf2 = self.game(nums[1:], not turn)
            
            last = nums[-1]
            pl1, pl2 = self.game(nums[:-1], not turn)
            
            if (first + pf2 > last + pl2):
                return (pf1, pf2 + first)
            
            return (pl1, pl2 + last)
                
            
                
                
                