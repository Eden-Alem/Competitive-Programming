class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        freq = Counter(arr)
        
        unique = list(set(arr))
        unique.sort(key=lambda x: freq[x])
        
        remove = 0
        count = 0
        
        for num in reversed(unique):
            remove += freq[num]
            count += 1
            
            if remove >= n//2:
                return count
            
        