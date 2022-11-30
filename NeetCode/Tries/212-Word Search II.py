class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode
            curr = curr.children[c]
        curr.end_of_word = False

    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.end_of_word

        
class Solution:
    def __init__(self):
        self.trie = Trie()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for word in words:
            self.trie.insert(word)
        n = len(board)
        m = len(board[0])

        def dfs(i, j, root):
            tmp = ""
            curr = root
            c = board[i][j]
            if c not in curr.children:
                return False
            curr = curr.children[c]
            # move right
            if j + 1 < m:
                dfs(i, j + 1, curr)
            # move down
            if i + 1 < n:
                dfs(i + 1, j, curr)

