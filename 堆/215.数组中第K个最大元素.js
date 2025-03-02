/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function(nums, k) {
    const pivot = nums[Math.floor(Math.random() * nums.length)];
    const greater = [], equal = [], less = [];
    // 按照pivot排序
    for (const n of nums) {
        if (n > pivot) {
            greater.push(n);
        } else if (n < pivot) {
            less.push(n);
        } else {
            equal.push(n);
        }
    }
    if (k <= greater.length) {  //! rightBorder is contained 长度对应的就是个数
        return findKthLargest(greater, k);
    } else if (k > greater.length + equal.length) {
        return findKthLargest(less, k - greater.length - equal.length);
    } else {
        return pivot;
    }
};