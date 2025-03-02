/**
 * @param {number[]} nums
 * @return {number}
 */
var findPeakElement = function (nums) {
  let l = 0, r = nums.length - 1;

  while (l < r) { //! 不是<= 如果是<=就会越界
    const m = (l + r) >> 1;  //* 正整数右移向下取整
    if (nums[m] < nums[m + 1]) {
      l = m + 1;
    } else {
      r = m;  // 如果前面在减小, 峰值可能是m也可能是m-1
    }
  }
  return l;
};
