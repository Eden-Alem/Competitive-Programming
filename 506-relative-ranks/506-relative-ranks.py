class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        
        score_sorted = sorted(score)
        score_rank = {}
        
        rank = 0
        for i in range(n-1,-1,-1):
            rank += 1
            if rank == 1:
                score_rank[score_sorted[i]] = "Gold Medal"
            elif rank == 2:
                score_rank[score_sorted[i]] = "Silver Medal"
            elif rank == 3:
                score_rank[score_sorted[i]] = "Bronze Medal"
            else:
                score_rank[score_sorted[i]] = str(rank)
                
        answer = []
        for i in range(n):
            answer.append(score_rank[score[i]])
            
        return answer
        
                
            
        
        