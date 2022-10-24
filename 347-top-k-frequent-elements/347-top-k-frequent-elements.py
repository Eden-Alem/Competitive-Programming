class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        
        keys = list(set(nums))
        
        keys.sort(key=lambda x: frequency[x], reverse=True)
        
        return keys[:k]