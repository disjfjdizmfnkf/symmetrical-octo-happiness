/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function (nums, k) {
    let l = 0,
      r = nums.length - 1;
    // 整个反转
    _reverse(l, r);
    // 反装前k个
    k = k % nums.length;
    l = 0; r = k - 1;  // k个的索引是k-1
    _reverse(l, r);
    l = k; r = nums.length - 1;
    _reverse(l, r);
  
    // reverse nums
    function _reverse(l, r) {
      while (l < r) {
        [nums[l], nums[r]] = [nums[r], nums[l]];
        l++;
        r--;
      }
    }
  };
  