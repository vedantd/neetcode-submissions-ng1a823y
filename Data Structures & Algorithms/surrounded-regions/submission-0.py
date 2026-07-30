class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLUMNS = len(board), len(board[-1])

        def dfs(r,c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLUMNS or board[r][c] != "O":
                return
            
            board[r][c] = "T"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        for r in range(ROWS):
            for c in range(COLUMNS):
                if (r in [0,ROWS-1] or c in [0, COLUMNS-1] ):
                    dfs(r,c)


        for r in range(ROWS):
            for c in range(COLUMNS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        


        for r in range(ROWS):
            for c in range(COLUMNS):
                if board[r][c] == "T":
                    board[r][c] = "O"
        