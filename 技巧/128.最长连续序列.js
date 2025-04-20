/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  let res = 0;
  nums = new Set(nums);
  for (const i of nums) {
    if (!nums.has(i - 1)) {
      j = i;
      while (nums.has(j)) j++;
      res = Math.max(res, j - i);
    }
  }
  return res;
};
