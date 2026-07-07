class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]
        curr.isEnd = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        def dfs(node, i) -> bool:
            if i == len(word):
                return node.isEnd
            
            c = word[i]
            if c == ".":
                for child in node.children.values():
                    if dfs(child,i+1):
                        return True
                return False
            if c not in node.children:
                return False
            
            return dfs(node.children[c],i+1)
        return dfs(curr,0)

            




        
