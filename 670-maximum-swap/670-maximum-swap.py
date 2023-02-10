class Solution:
    def maximumSwap(self, num: int) -> int:
        
        nums = list(str(num))
        
        for i in range(len(nums)):
            max_index = i
            for j in range(i+1, len(nums)):
                if nums[j] >= nums[max_index]:
                    max_index = j
                    
            if (i != max_index and nums[i] != nums[max_index]):
                nums[i], nums[max_index] = nums[max_index], nums[i]
                break
                
        return int("".join(nums))
                
        
        