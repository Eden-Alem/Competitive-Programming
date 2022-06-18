class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = 0

class WordFilter:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        
        for index, word in enumerate(words):
            long = word + "#" + word
            for i in range(len(word)):
                self.insert(long[i:], index)
            
            
    def insert(self, word, i):
        current = self.root
        current.isWord = i
        for w in word:
            if w not in current.children:
                current.children[w] = TrieNode()
                
            current = current.children[w]
            
            current.isWord = i
        
    def isPrefix(self, prefix):
        current = self.root
        
        for p in prefix:
            if p not in current.children:
                return -1
            
            current = current.children[p]
            
        return current.isWord

    def f(self, prefix: str, suffix: str) -> int:
        return self.isPrefix(suffix + "#" + prefix)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)