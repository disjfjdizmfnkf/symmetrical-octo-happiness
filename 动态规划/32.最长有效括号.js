/**
 * @param {number[]} heights
 * @return {number}
 */
var largestRectangleArea = function (heights) {
  const res = 0;
  const st = [];
  st.push(0);
  st.unshift(0);
  for (let i = 0; i < heights.length; i++) {
    while (heights[i] < heights[st[st.length - 1]]) {
      let cur = st.pop();
      let left = st[st.length - 1] + 1;
      let right = i - 1;
      res = Math.max(res, (right - left + 1) * heights[cur]);
    }
    st.push(i);
  }
  return res;
};
