class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digitSums = defaultdict(list)
        
        for n in nums:
            sum_ = self.sumOfDigits(n)
            digitSums[sum_].append(n)
            
        max_val = -1
        for s in digitSums:
            numbers = digitSums[s]
            if len(numbers) >= 2:
                numbers.sort()
                max_val = max(max_val, numbers[-1] + numbers[-2])
                
        return max_val    
            
    def sumOfDigits(self, n):
        s = str(n)
        sum_ = 0
        for i in range(len(s)):
            sum_ += int(s[i])
            
        return sum_
            
            