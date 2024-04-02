

def spiralOrder(matrix:list[list]):
    ans=[matrix[0][0]]
    count=0
    i=0
    j=0    
    LTR=len(matrix[0])-1
    TTD=len(matrix)-1
    RTL=0
    DTT=1
    status=0
    if LTR==0:
        status=1
    # left to right is 0
    # top to down is 1
    # right to left is 2
    # down to top is 3
    while count<len(matrix)*len(matrix[0])-1:                
        if status==0:
            j+=1
            if j== LTR:
                status+=1
                LTR-=1
        elif status==1:        
            i+=1
            if i== TTD:
                status+=1
                TTD-=1
        elif status==2:
            j-=1
            if j==RTL:
                status+=1
                RTL+=1
        else:
            i-=1
            if i==DTT:
                status=0
                DTT+=1    
        ans.append(matrix[i][j])
        count+=1
        
    return ans



matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix))

matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(matrix))

matrix=[[3],[2]]
print(spiralOrder(matrix))
































