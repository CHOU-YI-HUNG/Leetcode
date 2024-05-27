
def solve(board):
    """
    :type board: List[List[str]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    def dfs(row, col,histroy):
        if row < 0 or col < 0 or row >= rows or col >= cols:return False            
        if board[row][col] == 'X':return True        
        
        if (row,col) not in history:history.append((row,col))
            
        board[row][col] = 'X'
        T=dfs(row-1, col,histroy)
        D=dfs(row+1, col,histroy)
        L=dfs(row, col-1,histroy)
        R=dfs(row, col+1,histroy)                
                                    
        return L and T and D and R
    
    if not board:return 0    
    rows = len(board)
    cols = len(board[0])
    
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 'O':
                history=[]
                ans=dfs(row, col,history)
                if not ans:
                    for row_h, col_h in history:
                        board[row_h][col_h]="O"
                
                        
                    
                    
board=[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
solve(board)
print(board)

