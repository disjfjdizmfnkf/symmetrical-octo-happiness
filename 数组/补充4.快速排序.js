/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArray = function (nums) {
  (function quickSort(left, right) {
    if (left >= right) return;

    const pivotIndex = Math.floor(Math.random() * (right - left + 1)) + left;
    const pivot = nums[pivotIndex];
    [nums[left], nums[pivotIndex]] = [nums[pivotIndex], nums[left]];

    let lt = left; // 小于pivot的最后一个数，初始化为边界之外
    let gt = right + 1;
    let i = left + 1;

    // NOTE: i < gt 也就是在i没有到gt的范围循环
    while (i < gt) {
      if (nums[i] < pivot) {
        lt++;
        [nums[lt], nums[i]] = [nums[i], nums[lt]];
        i++;
      } else if (nums[i] > pivot) {
        gt--;
        [nums[gt], nums[i]] = [nums[i], nums[gt]];
      } else {
        i++;
      }
    }

    [nums[left], nums[lt]] = [nums[lt], nums[left]];

    quickSort(left, lt - 1);
    quickSort(gt, right);
  })(0, nums.length - 1);

  return nums;
};
