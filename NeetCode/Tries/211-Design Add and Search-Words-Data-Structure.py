class TrieNode:

    def __init__(self):
        self.children = {} # {"a": TrieNode(), ... "z": TrieNode()}
        self.isWord = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True
        
    def search(self, word: str) -> bool:
        def dfs(i, node):
            curr = node 
            for j in range(i, len(word)):
                c = word[j]
                if c == ".":
                    for node in curr.children.values():
                        if dfs(j+1,node):
                            return True
                    return False
                if c not in curr.children:
                    return False
                curr = curr.children[c]
            return curr.isWord

        return dfs(0, self.root)

def runTest():
    # ["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]
    # [[],["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]
    word_dict = WordDictionary()

    # Test adding words
    word_dict.addWord("at")
    word_dict.addWord("and")
    word_dict.addWord("an")
    word_dict.addWord("add")
    word_dict.addWord("bat")

    # Test searching words
    assert word_dict.search("a") == False
    assert word_dict.search(".at") == True
    assert word_dict.search("bat") == True
    assert word_dict.search("an.") == True
    assert word_dict.search("a.d.") == False
    assert word_dict.search("b.") == False
    assert word_dict.search("a.d") == True
    assert word_dict.search(".") == False

if __name__ == "__main__":
    runTest()