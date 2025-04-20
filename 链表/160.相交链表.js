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
  if (headA === null || headB === null) return null;
  let a = headA,
    b = headB;
  while (a !== b) {
    a = a === null ? headB : a.next;
    b = b === null ? headA : b.next;
  }
  return a;
};

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
