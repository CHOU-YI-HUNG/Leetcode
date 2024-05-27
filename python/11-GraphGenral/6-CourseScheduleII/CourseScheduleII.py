
def findOrder(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """
    if not prerequisites: return [i for i in range(numCourses)] 
    G=[[] for i in range(numCourses)]        
    
    # Build Graph: Linked List
    for x,y in prerequisites:
        if x==y: return []              
        G[x].append(y)
    # Traversal Graph                                 
    def dfs(e):
        if e in vis: return True         
        if e in seen: return False 
        seen.add(e)
        for i in G[e]:                             
            if not dfs(i): 
                return False        
        seen.remove(e)
        CourseOrder.append(e)          
        vis.add(e)
        return True        
    CourseOrder=[]     
    seen,vis=set(),set()
    for i in range(numCourses):
        if i not in vis:
            if not dfs(i): return []
    return CourseOrder


print(findOrder(4,[[1,0],[2,0],[3,1],[3,2]]))
print(findOrder(2,[[1,0],[0,1]]))
print(findOrder(2,[[1,0]]))
print(findOrder(2,[[0,1]]))