/**
 * @param {number[]} nums
 * @return {number}
 */
var findPeakElement = function (nums) {
  let l = 0,
    r = nums.length - 1;
  while (l + 1 < r) {
    let m = l + Math.floor((r - l) / 2);
    if (nums[m] < nums[m + 1]) {
      l = m;
    } else {
      r = m;
    }
  }

  return nums[l] > nums[r] ? l : r;
};
