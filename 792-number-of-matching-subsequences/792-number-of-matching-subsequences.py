class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        sequence = defaultdict(list)
        for i, string in enumerate(s):
            sequence[string].append(i)
        
        count = 0
        for w in words:
            correctSequence = True
            previous = -1
            for val in w:
                temp = self.binarySearch(sequence[val], previous)
                if temp == len(sequence[val]):
                    correctSequence = False
                    break
                else:
                    previous = sequence[val][temp]
                    
            if correctSequence:
                count += 1
                
        return count
                
                
        
    def binarySearch(self, array, val):
        l, r = 0, len(array)
        while l<r:
            mid = (l+r)//2
            if val < array[mid]:
                r = mid
            else:
                l = mid + 1
        return l