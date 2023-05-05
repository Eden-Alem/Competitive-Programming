class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True
        
    def search(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children and letter >= 'A' and letter <= 'Z':
                return False
            elif letter in current.children:
                current = current.children[letter]
        return current.is_word

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        result = []
        trie = Trie()
        trie.insert(pattern)
        for query in queries:
            result.append(trie.search(query))
        return result


       