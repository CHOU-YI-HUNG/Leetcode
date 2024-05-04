

def findMinArrowShots(points):
    points=sorted(points,key=lambda x:x[0])
    result=0    
    i=0
    j=1
    while i< len(points):
        start,end=points[i]        
        result+=1        
        while i+j<len(points):
            startj,endj=points[i+j]
            start=max(start,startj)
            end=min(end,endj)            
            if end>=start: # happen overlay                
                j+=1
                continue
            else:                
                break
        i+=j
        j=1
    
    return result
        
       


points=[[10,16],[2,8],[1,6],[7,12]]
print(findMinArrowShots(points))    

points=[[1,2],[3,4],[5,6],[7,8]]
print(findMinArrowShots(points))    

points=[[1,2],[2,3],[3,4],[4,5]]
print(findMinArrowShots(points))    

points=[[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
print(findMinArrowShots(points))    

points=[[4,12],[7,8],[7,9],[7,9],[2,8],[6,7],[5,14],[4,13]]
print(findMinArrowShots(points))    

points=[[0,9],[1,8],[7,8],[1,6],[9,16],[7,13],[7,10],[6,11],[6,9],[9,13]]
print(findMinArrowShots(points))    
