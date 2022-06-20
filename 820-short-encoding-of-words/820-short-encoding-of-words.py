class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.length = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        current = self.root
        for w in reversed(word):
            if w not in current.children:
                current.children[w] = TrieNode()
            current = current.children[w]
        current.length = len(word)
        return current

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        nodes = []
        node = Trie()
        for word in set(words):
            nodes.append(node.insert(word))
            
        result = 0
        for val in nodes:
            if not val.children:
                result += (val.length + 1)
        
        return result
            