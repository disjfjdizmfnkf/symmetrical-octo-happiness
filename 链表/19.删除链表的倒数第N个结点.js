/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function (head, n) {
  const dummy = new ListNode(0, head);
  let pre = dummy;  // cur和pre都从dummy开始保证中间相差n个节点
  while (n) {
    pre = pre.next;
    n--;
  }

  let before = new ListNode(0, dummy);
  let after = dummy.next;
  while (pre) {
    pre = pre.next;
    before = before.next;
    after = after.next;
  }
  before.next = after;
  return dummy.next;
};


//? 剑指offer 22 获取倒数第k个节点
var _removeNthFromEnd = function (head, n) {
  const dummy = new ListNode(0, head);
  let cur = dummy, p = dummy;
  while (n) {
    p = p.next;
    n--;
  }
  while (p) {
    cur = cur.next;
    p = p.next;
  }
  return cur.val;
};
