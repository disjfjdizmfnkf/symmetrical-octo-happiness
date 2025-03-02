/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    if (intervals.length < 2) return intervals;
    // 按照每个元素的第一项排序
    intervals.sort((a, b) => a[0] - b[0]);  // a - b递增
    //* 在原数组上合并比较复杂，可以创建新数组
    const merged = [intervals[0]];
    for (let i = 1; i < intervals.length; i++) {
        const mergedLastIndex = merged.length - 1;
        //! 处理 合并/不合并 两种情况
        if (intervals[i][0] <= merged[mergedLastIndex][1]) {
            merged[mergedLastIndex][1] = Math.max(intervals[i][1], merged[mergedLastIndex][1]);
        } else {
            merged.push(intervals[i]);
        }
    }
    return merged;
};