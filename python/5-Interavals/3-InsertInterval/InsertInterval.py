

def insert(intervals,newInterval):
    if len(intervals)==0: return [newInterval]
    start, end=newInterval
    result=[]        
    j=1
    #start insert 
    for i in range(len(intervals)):
        starti,endi=intervals[i]
        if end<starti:
            result.append([start,end])
            result.append([starti,endi])   
            break         
        elif start<=endi:
            starti=min(start,starti)
            endi=max(end,endi)
            while i+j<len(intervals):
                starti2,endi2=intervals[i+j]
                if end<starti2:                    
                    break
                endi=max(endi2,endi)
                j+=1
            result.append([starti,endi])
            break
        elif i==len(intervals)-1:
            result.append([starti,endi])
            result.append([start,end])
        else:    
            result.append([starti,endi])
        
        
    for x in range((i+j),len(intervals)):
        starti,endi=intervals[x]
        result.append([starti,endi])
    
    return result
    

intervals=[[1,3],[6,9]]
newInterval=[2,5]
print(insert(intervals,newInterval))    

intervals=[[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval=[4,8]
print(insert(intervals,newInterval))    

intervals=[[1,5]]
newInterval=[6,8]
print(insert(intervals,newInterval))    
    
intervals=[[1,5]]
newInterval=[0,3]
print(insert(intervals,newInterval))    

intervals=[[1,5]]
newInterval=[0,0]
print(insert(intervals,newInterval))     
intervals=[[2,5],[6,7],[8,9]]
newInterval=[0,1]
print(insert(intervals,newInterval))     