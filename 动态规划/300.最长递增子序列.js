/**
 * @param {number[]} nums
 * @return {number}
 */
// WARN: 记住dp数组中索引的含义和nums数组中索引的含义不同, 作为原数组索引需要变换
var lengthOfLIS = function (nums) {
  // dp[i]: 以第i个元素结尾的最长递增子序列的长度
  // dp[i] = (nums[i] > nums[j] 如果是递增的) dp[i] 之前的所有最长递增子序列中最长的
  const dp = new Array(nums.length).fill(1);
  let res = 1;
  for (let i = 0; i < nums.length; i++) {
    for (let j = 0; j < i; j++) {
      //! dp[i]的含义决定了只计算以i结尾的递增的情况
      if (nums[i] > nums[j]) {
        dp[i] = Math.max(dp[i], dp[j] + 1);
      }
      // FIX: dp[i] = Math.max(dp[i], dp[j] + (nums[i - 1] > nums[j - 1] ? 1 : 0));
      // nums[i - 1] <= nums[j - 1] 时不需要使用dp[j] 来更新dp[i]
    }
    res = Math.max(res, dp[i]);
  }
  return res;
};

//! 返回子序列 

