class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        frequency = Counter(candyType)
        canEat = len(candyType)//2
        
        return min(canEat, len(frequency))
        
        
        