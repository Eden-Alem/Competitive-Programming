class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
                
            cur = cur.children[w]
            
        cur.endOfWord = True
        
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for word in strs:
            self.insert(word)
            
        cur = self.root
        result = ""
        
        while len(cur.children) == 1 and cur.endOfWord == False:
            char = list(cur.children.keys())[0]
            
            result += char
            cur = cur.children[char]
                
        return result