class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = {}
        n = len(hand)
        
        if n % groupSize != 0:
            return False
        
        for h in hand:
            freq[h] = 1 + freq.get(h, 0)
       
        minHeap = list(freq.keys())
        heapify(minHeap)
        
        while minHeap:
            minimum = minHeap[0]  
            for i in range(minimum, minimum + groupSize):
                if i not in freq:
                    return False
                freq[i] -= 1
                
                if freq[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heappop(minHeap)
            
        return True
        
        

            
        