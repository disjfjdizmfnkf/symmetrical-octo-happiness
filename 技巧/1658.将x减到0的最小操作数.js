/**
 * @param {number[]} nums
 * @param {number} x
 * @return {number}
 */
//* 滑动窗口 + 对偶问题
var minOperations = function (nums, x) {
    const total = nums.reduce((a, b) => a + b, 0);
    const target = total - x;  //! 转换为求中间数组的目标和
    if (target < 0) return -1;
    if (target === 0) return nums.length;

    let currentSum = 0;
    let maxLen = -1;
    let left = 0;
    for (let right = 0; right < nums.length; right++) {
        currentSum += nums[right];
        while(currentSum > target && right > left) {
            currentSum -= nums[left];
            left++;
        }
        if (currentSum === target) maxLen = Math.max(maxLen, right - left + 1);
    }
    return maxLen === -1 ? -1 : nums.length - maxLen;
};

//* 递归
var minOperations = function (nums, x) {
  function helper(left, right, target, steps) {
    if (target === 0) return steps;
    // 如果当前剩余值小于 0 或者左右指针交叉，不可行返回一个极大值
    if (target < 0 || left > right) return Infinity;
    const leftResult = helper(left + 1, right, target - nums[left], steps + 1);
    const rightResult = helper(left, right - 1, target - nums[right], steps + 1);
    return Math.min(leftResult, rightResult);
  }

  const result = helper(0, nums.length - 1, x, 0);
  return result === Infinity ? -1 : result;
};
