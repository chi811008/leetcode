class WordNode:
    def __init__(self) -> None:
        self.children = {}
        self.end_of_word = False


class WordDictionary:

    def __init__(self):
        self.root = WordNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = WordNode()
            curr = curr.children[c]
        curr.end_of_word = True

    def search(self, word: str) -> bool:

        def dfs(j, root):
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for value in curr.children.values():
                        if dfs(i + 1, value):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.end_of_word
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

class TrieNode:
    
    def __init__(self):
        self.children = dict()
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end_of_word = True
            
    def search(self, word: str) -> bool:
        curr = self.root
        def dfs(curr_node, i):
            for j in range(i, len(word)):

                # word[i] == "."
                if word[j] == ".":
                    for value in curr_node.children.values():
                        if dfs(value, j + 1):
                            return True
                    return False
                # normal condition
                else:
                    if word[j] not in curr_node.children:
                        return False
                    curr_node = curr_node.children[word[j]]
            return curr_node.end_of_word 
        
        return dfs(curr, 0)



# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
words = ["bad","dad","mad"]
s = ["pad","bad",".ad","b.."]

for word in words:
    obj.addWord(word)

for _ in s:
    param_2 = obj.search(_)
    print(param_2)