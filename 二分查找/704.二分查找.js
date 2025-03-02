/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
  let l = 0;
  let r = nums.length - 1;
  let m;
  while (l <= r) {
    m = Math.floor((l + r) / 2);
    if (nums[m] > target) r = m - 1;
    else if (nums[m] < target) l = m + 1;
    else return m;
  }
  return -1;
};