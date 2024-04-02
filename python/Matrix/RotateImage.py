
def rotate(matrix:list):
    n = len(matrix)
    #把矩陣轉至 
    for r in range(n):
        for c in range(r, n):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    #把矩陣的element以中間為軸後，左右互換
    for r in range(n):
        for c in range(n // 2):
            matrix[r][c], matrix[r][n - 1 - c] = matrix[r][n - 1 - c], matrix[r][c]
            
        
        
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# rotate(matrix)
# print(matrix)

# matrix=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# rotate(matrix)
# print(matrix)
        