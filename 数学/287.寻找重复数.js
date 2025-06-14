/**
 * @param {number[]} nums
 * @return {number}
 * Floyd 判圈法（快慢指针），不修改原数组，O(n) 时间 O(1) 空间
 */
var findDuplicate = function (nums) {
  let slow = nums[0]
  let fast = nums[0];
  // 第一阶段：快慢指针相遇
  do {
    slow = nums[slow];
    fast = nums[nums[fast]];
  } while (slow !== fast);
  // 第二阶段：找到入口点
  slow = nums[0];
  while (slow !== fast) {
    slow = nums[slow];
    fast = nums[fast];
  }
  return slow;
};
