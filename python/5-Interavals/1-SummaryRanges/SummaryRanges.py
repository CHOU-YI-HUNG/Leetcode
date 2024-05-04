

def summaryRanges(nums):
    if len(nums)==0: return []
    start=end=nums[0]
    result=[]
    result.append(str(start))
    for i in range(len(nums)-1):
        if nums[i]+1==nums[i+1]:
            end=nums[i+1]
            if i==len(nums)-2:
                result[len(result)-1]=result[len(result)-1]+"->"+str(end)
        else:
            
            if start!=end:
                result[len(result)-1]=result[len(result)-1]+"->"+str(end)
            start=end=nums[i+1]
            result.append(str(start))
    return result
    

nums=[0,1,2,4,5,7]
print(summaryRanges(nums))
nums=[0,2,3,4,6,8,9]
print(summaryRanges(nums))


