
def Rule(x,itself):    
    if x<2 or x>3:
        return 0
    if x==3:
        return 1
    if x==2:
        return itself
    
    

def gameOfLife(board):
    n=len(board[0])
    m=len(board)
    xtable=[[] for _ in range(m)]
    
    x=0
    for j in range(m):
        for i in range(n):            
            if i-1>=0:
                x+=board[j][i-1] 
                if j+1<m:
                    x+=board[j+1][i-1] 
                if j-1>=0:
                    x+=board[j-1][i-1]                                             
            if i+1<n:
                x+=board[j][i+1]       
                if j+1<m:
                    x+=board[j+1][i+1]     
                if j-1>=0:
                    x+=board[j-1][i+1]     
                          
            if j-1>=0:
                x+=board[j-1][i]           
            if j+1<m:
                x+=board[j+1][i]           
            xtable[j].append(x)
            x=0

    for i in range(n):
        for j in range(m):            
            board[j][i]=Rule(xtable[j][i],board[j][i])
            
            
            
            

board=[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
gameOfLife(board)
print(board)

board=[[1,1],[1,0]]
gameOfLife(board)
print(board)   
    
    
    
    
    
    




