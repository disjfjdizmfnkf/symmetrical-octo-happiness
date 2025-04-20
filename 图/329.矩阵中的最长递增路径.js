/**
 * @param {number[][]} matrix
 * @return {number}
 */
var longestIncreasingPath = function(matrix) {
    const DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    const memo = new Map();
    const rows = matrix.length, cols = matrix[0].length;
    let res = 0;

    //* 返回从r,c 开始的最长递增路径的长度
    function dfs(r, c) {
        const key = `${r},${c}`;
        if (memo.has(key)) {
            return memo.get(key);
        }
        let best = 1;
        for (const dir of DIRS) {
            const newR = r + dir[0];
            const newC = c + dir[1];
            if (newR >= 0 && newR < rows && newC >= 0 && newC < cols && matrix[newR][newC] > matrix[r][c]) {
                best = Math.max(best, dfs(newR, newC) + 1);
            }
        }
        memo.set(key, best);
        return best;
    }

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            res = Math.max(res, dfs(i, j));
        }
    }
    return res;
};