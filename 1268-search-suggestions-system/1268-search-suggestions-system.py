class NodeTrie:
    def __init__(self, character):
        self.nodes = {}
        self.isEndOfWord = False
        self.charac = character
        
class Trie:
    def __init__(self):
        self.root = NodeTrie("")
        
    def insert(self, word):
        current = self.root
        
        for w in word:
            if (ord(w) - ord("a")) not in current.nodes:
                current.nodes[ord(w) - ord("a")] = NodeTrie(w) 
            current = current.nodes[ord(w) - ord("a")]
            
        current.isEndOfWord = True
        
        
    def dfs(self, word, node, result):
        if node.isEndOfWord:
            result.append(word + node.charac)
            if len(result) >= 3:
                return result
            
        for child in node.nodes:
            if node.nodes[child]:
                self.dfs(word + node.charac, node.nodes[child], result)
        
        return result
    
        
    def search(self, word):
        current = self.root
        result = []
        
        for w in word:
            if (ord(w) - ord("a")) not in current.nodes:
                return result
            current = current.nodes[ord(w) - ord("a")]
            
        if current.isEndOfWord:
            result.append(word)
            
        for child in current.nodes:
            if current.nodes[child]:
                result.extend(self.dfs(word, current.nodes[child], []))
                if len(result) >= 3:
                    return result[:3]
        
        return result
    

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        result = []
        products.sort()
        for product in products:
            trie.insert(product)
            
        n = len(searchWord)      
        for w in range(1, n+1):
            result.append(trie.search(searchWord[:w]))
            
        return result
            
        