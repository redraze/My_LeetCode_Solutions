class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # O(mn) time compelxity
        # O(n) space complexity

        neighbors = [
            (-1, -1), # up left
            (0, -1),  # up
            (1, -1),  # up right
            (-1, 0),  # left
            (1, 0),   # right
            (-1, 1),  # down left
            (0, 1),   # down
            (1, 1),   # down right
        ]

        m, n = len(board), len(board[0])

        # counts the number of live neighbors of a given cell.
        # returns 0 or 1 based on certain conditions
        def nextState(prevState: int, r: int, c: int) -> int:
            counter = 0
            for (x, y) in neighbors:
                if (
                    0 <= r + y < m 
                    and 0 <= c + x < n
                ):
                    neighbor = board[r + y][c + x]
                    if type(neighbor) == tuple:
                        counter += neighbor[0]
                    else:
                        counter += neighbor
            
            # 1. live cell under-population
            # if prevState == 1 and counter < 2:
            #     return 0

            # 2. live cell lives on to next generation
            if prevState == 1 and 2 <= counter <= 3:
                return 1

            # 3. live cell over-population
            # if prevState == 1 and counter > 3:
            #     return 0 

            # 4. dead cell reproduction
            if prevState == 0 and counter == 3:
                return 1

            return 0

        # set each cell to a tuple containing (prevState, currentState)
        for i, row in enumerate(board):
            for j, num in enumerate(row):
                board[i][j] = (num, nextState(num, i, j))

        # simplify each cell's state tuple to current state
        for i, row in enumerate(board):
            for j, state in enumerate(row):
                board[i][j] = state[1]

        return board
