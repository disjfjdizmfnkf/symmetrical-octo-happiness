/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
    let end = 0;
    let dis = 0;
    let count = 0;
    // 题目是返回到达 nums[n - 1] 的最小跳跃次数
    for (let i = 0; i < nums.length - 1; i++) {
        dis = Math.max(dis, i + nums[i]);
        if (i === end) {
            count++;
            end = dis;
        }
    }
    return count - 1;
};