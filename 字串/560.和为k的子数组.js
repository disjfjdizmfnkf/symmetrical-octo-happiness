/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function (nums, k) {
  const countPrefix = { 0: 1 }; //! 初始存在的前缀和
  let prefixSum = 0;
  let res = 0;
  for (const num of nums) {
    prefixSum += num;
    //! 加上所有满足条件的前缀
    if (prefixSum - k in countPrefix) {
      res += countPrefix[prefixSum - k];
    }
    //! 数字有正有负, 前缀和可以有相同的
    countPrefix[prefixSum] = (countPrefix[prefixSum] || 0) + 1; //* 如果不存在自动初始化
  }
  return res;
};
