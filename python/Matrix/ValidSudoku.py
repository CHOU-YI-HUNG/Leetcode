
def classify(x:int):
    if x < 3:
        return 0
    elif x < 6:
        return 1
    elif x <= 8:
        return 2
    else:
        return None  

def isValidSudoku(board:list):
    t2tch=[[] for _ in range(3)]
    colCheck=[[] for _ in range(9)]
    for c in range(9):
        
        if c%3==0: # reset t2tch
            t2tch=[[] for _ in range(3)]
        rowCheck='' # reset rowCheck
        for r in range(9):
            if board[c][r]!='.':
                if board[c][r] not in rowCheck:
                    rowCheck+=board[c][r] 
                else:
                    return False                    
                if board[c][r] not in colCheck[r]:
                    colCheck[r].append(board[c][r])
                else:
                    return False
                if board[c][r] not in t2tch[classify(r)]:
                    t2tch[classify(r)].append(board[c][r])
                else:
                    return False
    return True            
                    

board=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))
board=[["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board))


              
    
    
    
    
    
    
    



