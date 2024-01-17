class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for l in word:
            if l not in curr.children:
                curr.children[l] = TrieNode()

            curr = curr.children[l]

        curr.isEnd = True
        print()
            

    def search(self, word: str) -> bool:

        def find(idx: int, curr: TrieNode) -> bool:
            if idx >= len(word):
                return curr.isEnd

            l = word[idx]
            if l == '.':
                opts = curr.children
            else:
                if l not in curr.children:
                    return False
                opts = [l]
            
            if not opts:
                return False
            
            for o in opts:
                if find(idx+1, curr.children[o]):
                    return True
            
            return False

        return find(0, self.root)


sol = WordDictionary()
sol.addWord("world")
sol.addWord("ala")
sol.search(".la")