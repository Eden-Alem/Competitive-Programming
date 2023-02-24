class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        tuples = sorted(tuple(zip(timestamp, username, website)))
        
        visited = defaultdict(list)
        for time, user, website in tuples:
            visited[user].append(website)
            
        pattern = []
        for user in visited:
            combs = set(itertools.combinations(visited[user], 3))
            for comb in combs:
                pattern.append(tuple(comb))
                
        patternCount = sorted(Counter(pattern).items(), key=lambda x:(-x[1],x[0]))
        
        return (patternCount[0][0])
                
        
            
        
        
        