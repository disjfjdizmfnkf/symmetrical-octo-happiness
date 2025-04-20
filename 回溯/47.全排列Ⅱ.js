var permuteUnique = function (nums) {
  const res = [];
  nums.sort((a, b) => a - b); // 排序
  const used = new Array(nums.length).fill(false);

  function backtrack(combine) {
    if (combine.length === nums.length) {
      res.push([...combine]);
      return;
    }
    for (let i = 0; i < nums.length; i++) {
      if (used[i]) continue;
      //! 剪枝的条件: 如果和前一个节点相同,且前一个节点未使用(已经回溯结束恢复状态了|用过了),为了避免重复不能使用当前这个数
      if (i > 0 && nums[i] === nums[i - 1] && !used[i - 1]) continue; // 剪枝条件
      used[i] = true;
      backtrack([...combine, nums[i]]);
      used[i] = false;
    }
  }
  backtrack([]);
  return res;
};
