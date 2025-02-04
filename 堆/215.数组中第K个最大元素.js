/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function(nums, k) {
    const pivot = nums[Math.floor(Math.random() * nums.length)];
    const big = [], equal = [], small = [];
    // 按照pivot排序
    for (const n of nums) {
        if (n > pivot) {
            big.push(n);
        } else if (n < pivot) {
            small.push(n);
        } else {
            equal.push(n);
        }
    }
    if (k <= big.length) {
        return findKthLargest(big, k);
    } else if (k > big.length + equal.length) {
        return findKthLargest(small, k - big.length - equal.length);
    } else {
        return pivot;
    }
};