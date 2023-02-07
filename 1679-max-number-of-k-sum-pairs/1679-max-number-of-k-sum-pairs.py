class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        freq = Counter(nums)
        
        count = 0
        for num in freq:
            while ((num == k-num) and freq[num] >= 2):
                freq[num] -= 2
                count += 1
                
            while ((num != k-num) and freq[num] and freq[k-num]):
                freq[num] -= 1
                freq[k-num] -= 1
                count += 1
                
        return count