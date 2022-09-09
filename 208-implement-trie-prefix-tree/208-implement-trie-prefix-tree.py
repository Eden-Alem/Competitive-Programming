class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

    def insert(self, word: str) -> None:
        root = self
        for w in word:
            if not root.children[ord(w)-ord("a")]:
                root.children[ord(w)-ord("a")] = Trie()
                
            root = root.children[ord(w)-ord("a")]
                
        root.endOfWord = True
        

    def search(self, word: str) -> bool:
        root = self
        for w in word:
            if not root.children[ord(w)-ord("a")]:
                return False
            root = root.children[ord(w)-ord("a")]
            
        return root.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        root = self
        for w in prefix:
            if not root.children[ord(w)-ord("a")]:
                return False
            root = root.children[ord(w)-ord("a")]
            
        return True
    
    def delete(self, word):
        root = self
        prev = []
        
        for w in word:
            if not root.children[ord(w)-ord("a")]:
                pass
            
            prev.append((root, ord(w)-ord("a")))
            root = root.children[ord(w)-ord("a")]
        
        root.endOfWord = False
        
        while prev:
            child = prev.pop()
            parent, childIndex = prev[-1]            
            
            count = 0
            for i in range(26):
                if child.children[i]:
                    count+=1
                if count>=2:
                    break
                    
            if count == 0:
                parent.children[childIndex] = None
                
            


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)