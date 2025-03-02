/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    let len = height.length, res = 0;
    let l = 0, r = len - 1;
    let lHeigh = 0, rHeigh = 0;
    while (l < r) {
        if (height[l] < height[r]) {
            if (lHeigh < height[l]) {
                lHeigh = height[l];
            } else {
                res += lHeigh - height[l];
            }
            l++;
        } else {
            if (rHeigh < height[r]) {
                rHeigh = height[r];
            } else {
                res += rHeigh - height[r];
            }
            r--;
        }
    }
    return res;
};