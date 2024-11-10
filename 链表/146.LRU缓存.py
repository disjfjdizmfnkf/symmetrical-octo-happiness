# 双向列表的节点
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.cap = capacity
        self.left.next, self.right.prev = self.right, self.left
        self.cache = {}  # key -> node

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # 添加到链表的最后
    def append(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.append(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        #  做这个操作也要更新
        if key in self.cache:
            self.remove(self.cache[key])
        newNode = Node(key, value)
        self.append(newNode)
        # 记得添加或者删除缓存字典中的key和value
        self.cache[key] = newNode
        if len(self.cache) > self.cap:
            re_node = self.left.next
            self.remove(re_node)
            del self.cache[re_node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)