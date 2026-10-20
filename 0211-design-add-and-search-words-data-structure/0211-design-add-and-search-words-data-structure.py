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

    def dfs(self,index,word,node):
        if index == len(word):
            return node.isEnd
        
        ch = word[index]
        if ch == ".":
            for child in node.dict.values():
                if self.dfs(index + 1,word, child):
                    return True
            
            return False
        
        if ch not in node.dict:
            return False
        
        return self.dfs(index + 1,word, node.dict[ch])

    def search(self, word: str) -> bool:

        return self.dfs(0, word, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)