class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])


        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols: return
            if board[i][j] != "O": return
            board[i][j] = "S"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)


        for j in range(cols):
            if board[0][j]=="O": dfs(0,j)
            if board[rows-1][j]=="O": dfs(rows-1,j)
        for i in range(rows):
            if board[i][0]=="O": dfs(i, 0)           
            if board[i][cols-1]=="O": dfs(i, cols - 1)   

        for i in range(rows):
            for j in range(cols):
                if board[i][j]=="O": board[i][j]="X"

        
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=="S": board[i][j]="O"
            