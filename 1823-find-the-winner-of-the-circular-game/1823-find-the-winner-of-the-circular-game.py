class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [x+1 for x in range(n)]
        
        i = 0
        while len(friends) > 1:
            i = (i + k - 1) % len(friends)
            friends.remove(friends[i])
            
        return friends[0]