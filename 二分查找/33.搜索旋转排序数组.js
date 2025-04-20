/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let l = 0, r = nums.length - 1, m;
    while (l <= r) {
        m = (l + r) >> 1;
        if (nums[m] === target) return m;
        if (nums[m] <= nums[r]) {
            if (target > nums[m] && target <= nums[r]) l = m + 1;
            else r = m - 1;
        } else {
            if (target < nums[m] && target >= nums[l]) r = m - 1;
            else l = m + 1;
        }
    }
    return -1;
};