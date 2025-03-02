/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    // f(n): 前n个房间可以偷取到的最大金额
    // f(n) = max(f(n - 2) + nums[n], f(n - 1));
    // f(0) = 0; f(1) = nums[1]; f(2) = max(f0, f1)
    const dp = new Array(nums.length + 1).fill(0);
    dp[0] = 0;
    dp[1] = nums[0];
    for (let i = 2; i <= nums.length; i++) {
        //! i在dp中是个数,在原数组中应该作为索引使用
        dp[i] = Math.max(dp[i - 2] + nums[i - 1], dp[i - 1]); 
    }
    return dp[len];
};

var rob = function(nums) {
    let a = 0, b = 0, c;
    for (const num of nums) {
        c = Math.max(a + num, b);
        a = b;
        b = c;
    }
    return c;
}