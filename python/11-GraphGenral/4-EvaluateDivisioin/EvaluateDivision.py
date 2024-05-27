
class Node(object):
    def __init__(self, src = 0, dst=0, weight=0):
        self.src = src
        self.dst = dst
        self.weight = weight
        
class Graph(object):
    def __init__(self,GraphSize=0,Nodes=[] ):
        self.GraphSize=GraphSize
        self.Nodes=Nodes
    
    def addNode(self,node):
        self.GraphSize+=1
        self.Nodes.append(node)
        
def calcEquation(equations, values, queries):
    """
    :type equations: List[List[str]]
    :type values: List[float]
    :type queries: List[List[str]]
    :rtype: List[float]
    """
    def dfs(s,d,seen):
        if s not in G    
    
    G=Graph(0,[])
    for (x, y), v in zip(equations, values):
        G.addNode(Node(x,y,v))
        G.addNode(Node(y,x,1/v))
        
    
    

print(calcEquation([["a","b"],["b","c"]],[2.0,3.0],[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))

# def BuildTree(equations,values):    
#     Trees=[]
#     TreesSize=-1
#     for e1,e2, value in equations,values:                
#         if Trees:
#             Trees.append(Node(e1,e1))
#             TreesSize+=1            
#         Trees[TreesSize].neighbors.append([Node(e2,e1),value])
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