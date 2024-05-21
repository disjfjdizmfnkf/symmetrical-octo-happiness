class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:

    def __init__(self):
        self.root = TrieNode()  # 加上括号调用构造函数，创建的是实例对象，否者初始化为类本身了

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char in cur.children:
                cur = cur.children[char]
            else:
                return False
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char in cur.children:
                cur = cur.children[char]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)