class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        pairs = [(scores[i], ages[i]) for i in range(n)]
        pairs.sort()
        
        dp = [pairs[i][0] for i in range(n)]
        
        for i in range(n):
            cur_score, cur_age = pairs[i]
            for j in range(i):
                score, age = pairs[j]
                if cur_age >= age:
                    dp[i] = max(dp[i], cur_score + dp[j])
                    
        return max(dp)
        