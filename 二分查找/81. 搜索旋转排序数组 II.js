/**
 * @param {number[]} nums
 * @param {number} target
 * @return {boolean}
 */
var search = function(nums, target) {
  let head = 0, tail = nums.length - 1;
  if (nums[head] === target || nums[tail] === target) return true;
  //* 去除两头相同的元素
  while(head <= nums.length - 1 && nums[head] === nums[0]) head++;
  while(tail >= 0 && nums[tail] === nums[0]) tail--;    
  let l = head, r = tail, m;
  while (l <= r) {
    m = (l + r) >> 1;
    if (nums[m] === target) return true;
    if (nums[m] <= nums[tail]) {
        if (target > nums[m] && target <= nums[tail]) l = m + 1;
        else r = m - 1; 
    } else {
        if (target < nums[m] && target >= nums[head]) r = m - 1;
        else l = m + 1;
    }
  }
  return false;
};