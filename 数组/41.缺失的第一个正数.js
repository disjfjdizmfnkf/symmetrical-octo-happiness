/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function (nums) {
  let n = nums.length;

  // 将每个数放到正确的位置上
  for (let i = 0; i < n; i++) {
    //* 需要在正确的位置 && 当前位置的数字不在正确位置 
    while (1 <= nums[i] && nums[i] <= n && nums[nums[i] - 1] !== nums[i]) {
      //! num[i] 要后修改, nums[nums[i] - 1]使用到了 num[i]
      [nums[nums[i] - 1], nums[i]] = [nums[i], nums[nums[i] - 1]];
    }
  }

  // 找到第一个位置不正确的数
  for (let i = 0; i < n; i++) {
    if (nums[i] !== i + 1) {
      return i + 1;
    }
  }

  return n + 1;
};
