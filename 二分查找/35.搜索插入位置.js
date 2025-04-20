/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */

//* 大于等于target的位置为1， 求1第一个出现的位置
var searchInsert = function(nums, target) {
    let l = 0, r = nums.length - 1, m;
    while (r - l > 3) {
        m = (l + r) >> 1;
        if (nums[m] >= target) r = m;
        else l = m + 1;
    }
    for(let i = l; i <= r; i++) {
        if (nums[i] >= target) return i;
    }
    // 如果没有找到
    return nums.length;
};

var searchInsert = function(nums, target) {
    let l = 0, r = nums.length - 1, m;
    while (l <= r) {
        m = (l + r) >> 1;
        if (nums[m] > target) {
            r = m - 1;
        }
        if (nums[m] < target) {
            l = m + 1;
        } else {
            return m;
        }
    }
    return l;
};
