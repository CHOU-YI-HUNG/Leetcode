

def merge(intervals):
    result=[]
    intervals_sorted=sorted(intervals,key=lambda x:x[0])
    i=0
    j=1
    while i<len(intervals):
        start1,end1=intervals_sorted[i]        
        while i+j<len(intervals):  
            start2,end2=intervals_sorted[i+j]                      
            if start2<=end1:
                end1=max(end1,end2)
            else:                               
                break
            j+=1
        result.append([start1,end1])
        i+=j
        j=1
    return result
        
    
    




intervals=[[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))
intervals=[[1,4],[4,5]]
print(merge(intervals))



