class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        adjList = defaultdict(list)
        wordList.append(beginWord)
        
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "." + word[i+1:]
                adjList[pattern].append(word)
                
        queue = deque([beginWord])
        visit = set([beginWord])
        result = 1
        
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                for i in range(len(word)):
                    if word == endWord:
                        return result
                    
                    pattern = word[:i] + "." + word[i+1:]
                    for neigh in adjList[pattern]:
                        if neigh not in visit:
                            visit.add(neigh)
                            queue.append(neigh)
                            
            result += 1
        
        return 0