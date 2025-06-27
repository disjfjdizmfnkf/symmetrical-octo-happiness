/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  // NOTE: 统计每个数字出现的次数
  const count = new Map();
  for (const num of nums) {
    count.set(num, (count.get(num) ?? 0) + 1);
  }
  const maxCnt = Math.max(...count.values());

  // NOTE: 桶排序, 按照频率分组
  const bucket = Array.from({ length: maxCnt + 1 }, () => []);
  for (const [num, freq] of count.entries()) {
    bucket[freq].push(num);
  }

  // NOTE: 从后往前遍历收集前k个数字, 无视顺序
  const ans = [];
  for (let i = maxCnt; i >= 0 && ans.length < k; i--) {
    ans.push(...bucket[i]);
  }
  return ans;
};

