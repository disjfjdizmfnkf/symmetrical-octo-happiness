/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
//NOTE: 
// * 1. 从后向前找到第一个升序对（nums[p-1] < nums[p]）。
// * 2. 如果找不到，说明整个序列是降序的，直接反转为升序。
// * 3. 否则，从后向前找到第一个大于nums[p-1]的数，交换两者。
// * 4. 最后将p及其后面的部分反转，使其变为最小的升序排列。

var nextPermutation = function (nums) {
  // NOTE: 如果是递减就不存在这样的数
  const len = nums.length;
  let p = len - 1;
  while (p > 0 && nums[p] <= nums[p - 1]) p--;
  // 此时p是递增的最后一个数
  // NOTE: 如果整体都是逆序的, 直接反转
  if (p === 0) {
    reverseParten(nums, 0, len - 1);
  } else {
    // NOTE: 从后往前找第一个大于nums[p - 1]的数(利用之后的数列都是降序的)
    while (nums[i] <= nums[p - 1]) i--;
    [nums[i], nums[p - 1]] = [nums[p - 1], nums[i]];
    reverseParten(nums, p, len - 1);
  }
};

function reverseParten(arr, l, r) {
  while (l < r) {
    [arr[l], arr[r]] = [arr[r], arr[l]];
    l++;
    r--;
  }
};

