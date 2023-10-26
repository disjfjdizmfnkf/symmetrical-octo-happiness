class TrieNode:  # 一开始的根并没有值，但是之后的每个node都会有值，因为他们都是children
    def __init__(self):
        self.children = {} # 毫无疑问使用hash表而不是26个长度的列表
        self.isEnd = False


class Trie:

    def __init__(self):
        self.root = TrieNode

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()  #  每个都是TrieNode
            cur = cur.children[char]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char in cur.children:
                cur = cur.children
            else:
                return False
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur =  self.root
        for char in prefix:
            if char in cur.children:
                cur = cur.children
            else:
                return False
        return True