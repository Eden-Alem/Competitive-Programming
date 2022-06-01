class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = deque([0])
        N = len(nums)
        for num in range(N):
            sums.append(sums[-1] + nums[num])
            
        sums.popleft()
        return sums