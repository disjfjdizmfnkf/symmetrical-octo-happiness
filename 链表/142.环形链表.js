/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var detectCycle = function (head) {
  if (!head) return null; // 边界检查
  let slow = head, fast = head;
  while (true) {
    if (!fast || !fast.next) return null; // 无环时返回 null
    fast = fast.next.next;
    slow = slow.next;
    if (fast === slow) break; // 快慢指针相遇，说明有环
  }
  fast = head; // 快指针从头开始
  while (fast !== slow) {
    fast = fast.next;
    slow = slow.next;
  }
  return fast; // 返回环的起点
};
