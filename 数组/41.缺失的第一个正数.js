/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function (nums) {
  let n = nums.length;

  // 将每个数放到正确的位置上
  for (let i = 0; i < n; i++) {
    let num = nums[i];
    //* 需要在正确的位置 && 数字num 对应索引num - 1
    while (1 <= num && num <= n && nums[num - 1] !== num) {
      //! num[i] 要后修改, nums[num - 1]使用到了 num[i]
      [nums[num - 1], num] = [num, nums[num - 1]];
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
