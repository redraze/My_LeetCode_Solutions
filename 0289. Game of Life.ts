var prev: number[][];
function clone(matrix: number[][]): number[][] {
    const copy = [];

    matrix.map((row, i) => {
        copy.push([]);

        row.map((cell, j) => {
            copy[i].push(cell);
        });
    });

    return copy;
}

var m: number;
var n: number;
function compare(cell: number, i: number, j: number): number {
    let c = 0;

    // check neighbor cells
    [-1, 0 ,1].map(y => {
        [-1, 0, 1].map(x => {
            // skip current cell
            if (x == 0 && y == 0) return;

            // check bounds
            if (
                i + y >= 0
                && i + y < m
                && j + x >= 0
                && j + x < n
            ) {
                c = c + prev[i + y][j + x];
            }
        });
    });

    if (cell == 1 && (c == 2 || c == 3)) return 1;
    if (cell == 0 && c == 3) return 1;
    return 0;
};

function gameOfLife(board: number[][]): void {
    prev = clone(board);
    m = board.length;
    n = board[0].length;

    board.map((row, i) => {
        row.map((cell, j) => {
            board[i][j] = compare(cell, i, j);
        });
    });

    return;
};
