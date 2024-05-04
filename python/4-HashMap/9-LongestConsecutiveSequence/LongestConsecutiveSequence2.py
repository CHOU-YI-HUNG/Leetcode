def longestConsecutive(nums:list):
    if len(nums)==0: return 0
    nums.sort()    
    max_value=1
    history=1
    for i in range(len(nums)-1):
        if nums[i]==nums[i+1]: continue        
        if nums[i]+1==nums[i+1] :
            history+=1
        else:
            history=1            
        if history>max_value:
            max_value=history

    return max_value
    
    
    
nums=[100,4,200,1,3,2]    
print(longestConsecutive(nums))  
nums=[0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums))  
nums=[9,1,4,7,3,-1,0,5,8,-1,6]
print(longestConsecutive(nums))  

 