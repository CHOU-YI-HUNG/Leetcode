def searchZero(matrix:list[list]):
    n=len(matrix[0])
    m=len(matrix)
    recordcol=[]
    recordrow=[]
    
    for i in range(n):
        for j in range(m):
            if matrix[j][i]==0:
                if i not in recordcol: recordcol.append(i)                          
                if j not in recordrow: recordrow.append(j)          
    return [recordcol,recordrow]


def setZereos(matrix:list[list]):
    rows,cols=searchZero(matrix)
    n=len(matrix[0])
    m=len(matrix)
    for e in rows:
        for i in range(m):
            matrix[i][e]=0
    for e in cols:
        for i in range(n):
            matrix[e][i]=0



    
    
    
    
    

matrix=[[1,1,1],[1,0,1],[1,1,1]]
setZereos(matrix)
print(matrix)

matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
setZereos(matrix)
print(matrix)

    