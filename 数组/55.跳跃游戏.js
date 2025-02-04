/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    let n = nums.length;
    let dis = nums[0];
    for (let i = 0; i < n; i++) {
        if (i <= dis) {
            dis = Math.max(dis, i + nums[i]);
        } else {
            break;
        }
    }
    // dis是索引
    return dis >= n - 1;
};