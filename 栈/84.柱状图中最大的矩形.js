/**
 * @param {number[]} heights
 * @return {number}
 */
var largestRectangleArea = function (heights) {
  let res = 0;
  const st = []; // 存放索引
  heights.push(0); // NOTE: 添加哨兵元素确保特殊情况下触发计算case
  heights.unshift(0);
  for (let i = 0; i < heights.length; i++) {
    // NOTE: 栈中元素是单调递增的, 遇到小的元素时pop 触发计算逻辑(means this is the right border of the box)
    while (st.length && heights[i] < heights[st[st.length - 1]]) {
      /** NOTE: 单调栈中关注三个元素
       * cur : 以当前元素为高计算面积
       * left: 左边界—— 左边第一个比当前元素矮的元素
       * right: 右边界—— 右边第一个比当前元素矮的元素
       * */
      const cur = st.pop();
      // WARN: 小于的元素作为边界并不包含
      const left = st[st.length - 1] + 1;
      const right = i - 1;
      res = Math.max(res, (right - left + 1) * heights[cur]);
    }
    st.push(i);
  }
  return res;
};
