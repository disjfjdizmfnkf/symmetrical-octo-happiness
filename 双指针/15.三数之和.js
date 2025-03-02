/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    const res = [];
    nums.sort((a, b) => a - b);  //！ 升序排列
    for (let i = 0; i < nums.length - 2; i++) { //! 最后空两个
        if(i > 0 && nums[i] === nums[i - 1]) continue;  //！和前一个比较
        
        let j = i + 1, k = nums.length - 1;
        while (j < k) {
            const sum = nums[i] + nums[j] + nums[k];
            if (sum > 0) {
                k--;
            } else if (sum < 0) {
                j++;
            } else {
                res.push([nums[i], nums[j], nums[k]]);

                while (j < k && nums[j] === nums[j + 1]) j++;
                while (j < k && nums[k] === nums[k - 1]) k--;
                //! 添加了一个不相等的组合之后还要继续寻找
                j++;
                k--;
            }
        }
    }
    return res;
};  