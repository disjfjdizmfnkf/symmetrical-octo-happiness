/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  for (let i = 1; i < nums.length; i++) {
    nums[i] += nums[i - 1];
  }
  let res = nums[0];
  let minPrefix = 0;
  for (const prefix of nums) {
    res = Math.max(res, prefix - minPrefix);
    minPrefix = Math.min(minPrefix, prefix);
  };
  return res;
};

// 一遍循环
var maxSubArray = function (nums) {
  //* NOTE: 实事求是的想: 第一个位置之前的最小前缀和是0，此时最大前缀和(only one)就是第一个数
  let prefix = 0;
  let res = nums[0];  //! 初始化为第一个数
  let minPrefix = 0;
  for (const num of nums) {
    prefix += num;  //! 开始时计算
    res = Math.max(res, prefix - minPrefix);
    minPrefix = Math.min(minPrefix, prefix);  //! 第一次最小前缀和为0,不应该先更新
  }
  return res;
};
