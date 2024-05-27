import collections

def calcEquation(equations, values, queries):
    """
    :type equations: List[List[str]]
    :type values: List[float]
    :type queries: List[List[str]]
    :rtype: List[float]
    """    
    #Build Tree    
    G = collections.defaultdict(dict)
    for (x, y), v in zip(equations, values):
        G[x][y] = v
        G[y][x] = 1/v  
    ans=[]    
    #Travesal Tree    
    def dfs(src,dst,v,seen):                
        if src not in G or dst not in G or src in seen : return                
        seen.append(src)
        # PreOrder
        if src==dst: ans.append(v)                        
        # PreOrder             
        for d in G[src]:            
            dfs(d,dst,v*G[src][d],seen)                    
                
    for src,dst in queries:
        seen=[]    
        dfs(src,dst,1,seen)
        if dst not in seen:ans.append(-1)            
            
    return ans
    
                
# print(calcEquation([["a","b"],["b","c"]],[2.0,3.0],[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))
print(calcEquation([["a","b"],["b","c"],["a","c"]],[2.0,3.0,6.0],[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))

# Arrays=set()
#     for pair in equations:
#         for e in pair:Arrays.add(e)
#     ArraysSize=len(Arrays)
                
#     matrix=[[0 for i in range(ArraysSize)] for i in range(ArraysSize)]
#     for i in range(ArraysSize):
#         for j in range(ArraysSize):
#             if i==j:matrix[i][j]=1                
#             elif i+1==j:matrix[i][j]=values[j-1]
#             elif i==j+1:matrix[i][j]=1/values[i-1]
#             else:matrix[i][j]=None
#     def Find(path):
                        
#     print(matrix)