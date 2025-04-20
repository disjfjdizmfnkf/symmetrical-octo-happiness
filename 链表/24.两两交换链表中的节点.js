/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs = function (head) {
  const dummy = new ListNode(0, head);
  let cur = dummy;
  let temp;
  // 后面两个节点都存在
  while (cur.next && cur.next.next) {
    const node1 = cur.next;
    const node2 = cur.next.next;

    temp = node2.next;
    cur.next = node2;
    node2.next = node1;
    node1.next = temp;

    cur = node1;
  }
  return dummy.next;
};