/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    // 检查矩阵是否为空或者是否没有元素
    if (matrix.length === 0 || matrix[0].length === 0) return false;
    let row = 0;
    let col = matrix[0].length - 1;

    while (row < matrix.length && col >= 0) {
        const cur = matrix[row][col];
        if (cur === target) return true;
        cur < target ? row++ : col--;
    }
    return false;
};