class TrieNode:
    def __init__(self):
        self.dict = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
      self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.dict:
                curr.dict[c] = TrieNode()
            
            curr = curr.dict[c]
        
        curr.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(index,node):
            if index == len(word):
                return node.isEnd
            

            ch = word[index]
            if ch == ".":
                for child in node.dict.values():
                    if dfs(index + 1, child):
                        return True
                
                return False
            
            if ch not in node.dict:
                return False
            
            return dfs(index + 1, node.dict[ch])

        return dfs(0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)