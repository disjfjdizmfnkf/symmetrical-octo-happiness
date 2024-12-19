# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 
        # key: 旧节点对象  val: 新节点对象
        mapOldToNew = {}
        cur = head

        # 遍历旧链表，将旧链表中的节点使用哈希表保存起来
        while cur:
            mapOldToNew[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        # 再次遍历旧链表，修改新节点的next和random
        while cur:
            # 错误示例，这是将新节点连接到了旧节点
            # mapOldToNew[cur].next = cur.next
            # mapOldToNew[cur].random = cur.random
            # 另外使用get防止遇到null节点报错
            mapOldToNew[cur].next = mapOldToNew.get(cur.next)
            mapOldToNew[cur].random = mapOldToNew.get(cur.random)
            cur = cur.next
        return mapOldToNew[head]
