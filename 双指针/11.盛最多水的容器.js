/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let best = 0;
    let l = 0, r = height.length - 1;
    while (l < r) {
        best = Math.max(best, (r - l) * Math.min(height[l], height[r]))
        if (height[l] < height[r]) {
            l++;
        } else {
            r--;
        }
    }
    return best;
};