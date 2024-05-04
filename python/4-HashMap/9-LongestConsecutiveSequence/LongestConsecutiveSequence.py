def longestConsecutive(nums:list):
    if len(nums)==0: return 0
    nums.sort()
    categories=0
    max_value=0
    history={}
    history[categories]=1
    for i in range(len(nums)-1):
        if nums[i]==nums[i+1]: continue        
        if nums[i]+1==nums[i+1] :
            history[categories]+=1
        else:
            if history[categories]>max_value:
                max_value=history[categories]
                history[categories]=1
            else:    
                categories+=1
                history[categories]=1
    if max_value==0:
        return history[categories]   
    return max_value
    
    
    
nums=[100,4,200,1,3,2]    
print(longestConsecutive(nums))  
nums=[0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums))  


 