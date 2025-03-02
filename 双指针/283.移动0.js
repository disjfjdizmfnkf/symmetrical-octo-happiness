/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function (nums) {
  let p = 0;
  for (let num of nums) {
    if (num) {
      nums[p] = num;
      p++;
    }
  }
  while (p < nums.length) {
    nums[p] = 0;
    p++;
  }
};
