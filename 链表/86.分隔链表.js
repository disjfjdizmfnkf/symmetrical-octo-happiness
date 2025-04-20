/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} x
 * @return {ListNode}
 */
 //! 当移动数组中的节点时断开与原数组的连接
 var partition = function (head, x) {
    const leftDummy = new ListNode();
    const rightDummy = new ListNode();
    let left = leftDummy, right = rightDummy, cur = head;
  
    while (cur) {
      // <x在左边, >=x在右边
      if (cur.val < x) {
        left.next = cur;
        left = left.next;
      } else {
        right.next = cur;
        right = right.next;
      }
      const nextNode = cur.next; // 保存下一个节点
      cur.next = null; // 断开当前节点的原链表连接，防止形成环
      cur = nextNode; // 移动到下一个节点
    }
    left.next = rightDummy.next;
    return leftDummy.next;
  };
  