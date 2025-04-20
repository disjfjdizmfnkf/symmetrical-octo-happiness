/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function (nums) {
  const res = [];
  const combine = [];
  function backtrack(start) {
    res.push([...combine]);
    for (let i = start; i < nums.length; i++) {
      combine.push(nums[i]);
      backtrack(i + 1);
      combine.pop();
    }
  }
  backtrack(0);
  return res;
};
