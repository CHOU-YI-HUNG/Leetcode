class Solution(object):
    def solve(self, board):
        A = board
        def capture(row,col):
            if row < 0 or col < 0 or row >= len(A) or col >= len(A[0]) or A[row][col] !='O':
                return
                
            A[row][col] = 'V'
            capture(row+1,col)
            capture(row-1,col)
            capture(row,col+1)
            capture(row,col-1)
        
        ROW,COL = len(A),len(A[0])
        #convert border, taking approach as capture everything except unsurrounded regions
        for row in range(ROW):
            if A[row][0] == 'O':
                capture(row,0)
            if A[row][COL-1] == 'O':  
                capture(row,COL-1)
        
        for col in range(COL):   
            if A[0][col] == 'O':
                capture(0,col)
            if A[ROW-1][col] == 'O':  
                capture(ROW-1,col)   
                
        #convert everything surrounded
        for row in range(ROW):
            for col in range(COL):
                if A[row][col] == 'O':
                    A[row][col] = 'X'
                elif A[row][col] =='V':
                    A[row][col] = 'O'        
        
         
        