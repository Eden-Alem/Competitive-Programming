from typing import Collection

class Solution:
    def topKFrequent(self, nums, k):        
#         if k == len(nums):
#             return nums
        
#         frequency_list = Counter(nums)
#         return heapq.nlargest(k, frequency_list.keys(), key=frequency_list.get) 
        frequency_dict = Collection.Counter(nums)
        result = []
        
        unique = list(set(nums))
        
        unique.sort(key=lambda x: frequency_dict[x])
        return unique[-k:]    
        