/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function (nums, target) {
  const left = binarySearch(nums, target, true);
  const right = binarySearch(nums, target, false);
  return [left, right];
};

function binarySearch(nums, target, leftBias) {
  let l = 0,
    r = nums.length - 1,
    mid;
  let targetIndex = -1; //! trick
  while (l <= r) {
    mid = Math.floor((l + r) / 2);
    if (target > nums[mid]) l = mid + 1;
    else if (target < nums[mid]) r = mid - 1;
    else {
      //! 在局部(连续、相同)的数组中寻找边界
      targetIndex = mid;
      if (leftBias) {
        r = mid - 1;
      } else {
        l = mid + 1;
      }
    }
  }
  return targetIndex;
}
