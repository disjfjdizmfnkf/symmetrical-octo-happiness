/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function (target, nums) {
  let l = 0, res = target + 1, total = 0;
  for (let r = 0; r < nums.length; r++) {
    total += nums[r];
    while (total >= target) {  //! 等于的时候也需要调整
      res = Math.min(res, r - l + 1);
      total -= nums[l];
      l++;
    }
  }
  return res > target ? 0 : res;
};
