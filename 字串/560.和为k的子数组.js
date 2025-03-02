/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function(nums, k) {
    let prefixSum = 0;
    // 记录此时之前的前缀和的出现次数
    let countPrefix = {0: 1};  //! 0是一个隐藏的前缀和
    let res = 0;
    for (let num of nums) {
        prefixSum += num;
        // 先计算之前满足要求的子数组，否则会出错 eg. nums:[] k:1
        if ((prefixSum - k) in countPrefix) {
            res += countPrefix[prefixSum - k];
        }
        // 之后再将这个加入count计数
        countPrefix[prefixSum] = (countPrefix[prefixSum] || 0) + 1;
    }
    return res;
};