/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function (nums) {
  const res = [];
  function backtrack(combine, nums) {
    const len = nums.length;
    if (!len) {
      res.push(combine);
    }
    for (let i = 0; i < len; i++) {
      //! concat连接性能更好，splice是修改原数组，slice返回新数组
      backtrack(
        combine.concat(nums[i]),
        nums.slice(0, i).concat(nums.slice(i + 1))
      );
    }
  }
  //! 不要忘记调用
  backtrack([], nums);
  return res;
};
