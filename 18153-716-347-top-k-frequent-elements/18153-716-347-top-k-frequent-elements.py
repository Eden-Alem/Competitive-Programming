from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        freq = [[] for i in range(len(nums)+1)]
        for num, count in counts.items():
            freq[count].append(num)
        
        result = []
        for numbers in reversed(freq):
            for num in numbers:
                result.append(num)
                if len(result) == k:
                    return result