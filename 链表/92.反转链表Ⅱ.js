/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} left
 * @param {number} right
 * @return {ListNode}
 */
//* 判断left和right与节点移动次数之间的关系
var reverseBetween = function (head, left, right) {
  const dummy = new ListNode(0, head);
  let groupPrev = dummy;
  let cur = head;
  for (let i = 0; i < left - 1; i++) {
    groupPrev = groupPrev.next;
    cur = cur.next;
  }
  let prev = null;
  for (let i = 0; i < right - left + 1; i++) {
    const temp = cur.next;
    cur.next = prev;
    prev = cur;
    cur = temp;
  }
  groupPrev.next.next = cur;
  groupPrev.next = prev;
  return dummy.next;
};
