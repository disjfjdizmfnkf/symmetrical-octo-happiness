/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
// NOTE: 滑动窗口问题 - 累计型问题
var minSubArrayLen = function (target, nums) {
  let l = 0, res = target + 1, total = 0;
  for (let r = 0; r < nums.length; r++) {
    total += nums[r]; //! r = 0 时窗口内应该存在一个值
    while (total >= target) {
      //! 等于的时候也需要调整
      res = Math.min(res, r - l + 1);
      total -= nums[l];
      l++;
    }
  }
  return res > target ? 0 : res;
};
