class TrieNode:
    def __init__(self):
        self.childrens = {}
        self.isEndOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.childrens:
                curr.childrens[c] = TrieNode()
            
            curr = curr.childrens[c]
        
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.childrens:
                return False
            curr = curr.childrens[c]
        
        return curr.isEndOfWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.childrens:
                return False
            curr = curr.childrens[c]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)