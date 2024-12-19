class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:
    # 双向链表，删除节点对象无须知道节点位置
    def __init__(self, capacity: int):
        self.cap = capacity
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        self.cache = {}  # key -> value   值 -> 节点对象

    # 保证传入的节点一定存在时调用
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    # 添加节点到最后
    def append(self, node):
        pre = self.right.prev
        pre.next, node.prev = node, pre
        self.right.prev, node.next = node, self.right 

    # 返回访问节点, 并且移动这个节点到最新位置
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)  # 移除节点
            self.append(node)  # 添加到最后
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        newNode = Node(key, value)
        self.cache[key] = newNode
        self.append(newNode)

        if len(self.cache) > self.cap:
            # 删除最左边的节点
            rm_node = self.left.next
            self.remove(rm_node)
            del self.cache[rm_node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)