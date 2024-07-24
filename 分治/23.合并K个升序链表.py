class Solution:
    # approach1: heap
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not any(lists):  # any(array) 当数组中有一个值为True时返回True
            return

        heap = [(l.val, i, l) for i, l in enumerate(lists) if l]  # 将所有非空列表的 值,列表索引,列表头节点 加入heap
        heapq.heapify(heap)

        dummy = curr = ListNode(0)  # 新建一个dummy Node和一个指针
        while heap:  # 在最后两次遍历之前， heap中项目的个数都为k个？ 就像heap在过滤k条链表
            _, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next