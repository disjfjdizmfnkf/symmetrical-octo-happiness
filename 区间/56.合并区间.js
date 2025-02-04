/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    if (intervals.length <= 1) {
        return intervals;
    }
    
    intervals.sort((a, b) => a[0] - b[0]); // a - b 递增 
    const merged = [intervals[0]]
    for (let i = 1; i < intervals.length; i++) {
        const interval = intervals[i];
        if (merged[merged.length - 1][1] >= interval[0]) {
            merged[merged.length - 1][1] = Math.max(merged[merged.length - 1][1], interval[1]);
        } else {
            merged.push(interval);
        }
    }

    return merged;
};