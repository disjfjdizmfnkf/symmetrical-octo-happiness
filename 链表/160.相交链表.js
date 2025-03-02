/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
var getIntersectionNode = function (headA, headB) {
  const memo = new Set();
  while (headA) {
    memo.add(headA);
    headA = headA.next;
  }
  while (headB) {
    if (memo.has(headB)) return headB;
    headB = headB.next;
  }
  return null;
};
