/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const memo = new Map();
    const len = nums.length;
    for (let i = 0; i < len; i++) {
        if (memo.has(target - nums[i])) {
            return [i, memo.get(target - nums[i])]
        }
        memo.set(nums[i], i);
    }
};