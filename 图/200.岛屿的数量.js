/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    const rows = grid.length, cols = grid[0].length;
    let res = 0;
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (grid[r][c] === '1') {
                res++;
                bfs(r, c);
            }
        }
    }
    return res;

    function bfs(row, col) {
        if (row < 0 || row >= rows || col < 0 || col >= cols || grid[row][col] !== '1') {
            return ;
        }
        grid[row][col] = '0';
        bfs(row + 1, col);
        bfs(row, col + 1);
        bfs(row - 1, col);
        bfs(row, col - 1);
    }
};