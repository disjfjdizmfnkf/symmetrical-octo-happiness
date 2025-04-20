/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSlidingWindow = function (nums, k) {
  //! q存放的是索引
  const q = [], res = [];
  for (let i = 0; i < nums.length; i++) {
    //* 维护窗口大小限制
    while (q.length && q[0] < i - k + 1) q.shift();
    //* 维护单调性
    while (q.length && nums[i] > nums[q[q.length - 1]]) q.pop();
    q.push(i);
    //* 将结果加入数组
    if (i + 1 >= k) res.push(nums[q[0]]);
  }
  return res;
};
