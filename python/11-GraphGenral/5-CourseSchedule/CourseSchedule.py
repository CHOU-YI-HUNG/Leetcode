        
def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """    
    if not prerequisites: return True    
    G=[[] for i in range(numCourses)]        
    # Build Graph: Linked List
    for x,y in prerequisites:
        if x==y: return False                    
        G[y].append(x)
    # Traversal Graph                                 
    def dfs(e,seen):                
        if not G[e]: return True                        
        if e in seen: return False                                                        
        for i in G[e]:                                        
            if vis[i]==0 and dfs(i,seen+[e])==False: 
                return False
        vis[e]=1
        return True        
    
    vis = [0] * numCourses
    for i in range(numCourses):
        if G[i] and vis[i]==0:
            if not dfs(i,[]): return False                
    return True

print(canFinish(2,[[1,0]]))
print(canFinish(2,[[1,0],[0,1]]))
print(canFinish(3,[[0,2],[1,2],[2,0]]))
print(canFinish(5,[[1,0],[2,1],[3,4],[4,3]]))
print(canFinish(4,[[2,1],[3,2],[1,3]]))
print(canFinish(5,[[1,4],[2,4],[3,1],[3,2]]))