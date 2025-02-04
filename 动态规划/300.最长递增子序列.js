/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function(nums) {
    // dp[i]表示长度为i的最长递增子序列的长度
    // dp[i] = (nums[i] > nums[j] 如果是递增的) dp[i] 之前的所有最长递增子序列中最长的 
    const dp = new Array(nums.length).fill(1);
    let res = 1;
    for (let i = 0; i < nums.length; i++) {
        for (let j = 0; j < i; j++) {
            if (nums[i] > nums[j]) {
                dp[i] = Math.max(dp[i], dp[j] + 1); 
            }
        }
        res = Math.max(res, dp[i]);
    }
    return res;
};