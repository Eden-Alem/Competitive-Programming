class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice = 0
        for a in aliceSizes:
            alice += a
            
        bob = 0
        for b in bobSizes:
            bob += b
            
        aliceSizes.sort()
        bobSizes.sort()
        
        answer = [0] * 2
        for i in range(len(aliceSizes)):
            answer[0] = aliceSizes[i]
            bob_size = ((aliceSizes[i] + bob) - (alice - aliceSizes[i])) // 2
            if bob_size in set(bobSizes):
                answer[1] = bob_size
                return answer
        