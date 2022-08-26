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


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)