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

var permute = function (nums) {
  const res = [];
  const used = new Array(nums.length).fill(false);
  function backtrack(combine) {
    if (combine.length === nums.length) {
      res.push(combine);
      return;
    }
    for (let i = 0; i < nums.length; i++) {
      if (used[i]) continue;
      used[i] = true;
      backtrack([...combine, nums[i]]);
      used[i] = false;
    }
  }
  backtrack([]);
  return res;
};
