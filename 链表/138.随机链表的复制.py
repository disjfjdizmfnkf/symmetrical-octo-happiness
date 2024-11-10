class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# 使用hashMap存储原节点到新节点的映射
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_to_new = {}
        current = head

        # First pass: create all new nodes and store the mapping from old nodes to new nodes
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next

        current = head

        # Second pass: assign next and random pointers to the new nodes
        while current:

            # if current.next:
            #     old_to_new[current].next = old_to_new[current.next]
            # if current.random:
            #     old_to_new[current].random = old_to_new[current.random]

            # 使用get()方法不用判空
            old_to_new[current].next = old_to_new.get(current.next)  # 运用原节点寻找相同的新节点
            old_to_new[current].random = old_to_new.get(current.random)

            current = current.next

        return old_to_new[head]