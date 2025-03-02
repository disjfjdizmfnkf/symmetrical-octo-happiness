/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
//! dp[i][j]  nums1以i结尾 和 nums2以j结尾时的最长重复子数组
//! 子数组是连续的
var findLength = function (nums1, nums2) {
  let res = 0;
  const m = nums1.length,
    n = nums2.length;
  const dp = new Array(m + 1).fill(0).map(() => new Array(n + 1).fill(0));
  for (let i = 1; i <= m; i++) {
    const n1 = nums1[i - 1];
    for (let j = 1; j <= n; j++) {
      const n2 = nums2[j - 1];
      if (n1 === n2) {
        dp[i][j] = dp[i - 1][j - 1] + 1;
        res = Math.max(res, dp[i][j]);
      } else {
        // 如果当前元素不相等，以它们结尾的最长重复子数组长度为 0
        dp[i][j] = 0;
      }
    }
  }
  return res;
};
