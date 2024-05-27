def canJump(nums):
    #排除[0]的因素
    if len(nums)==1:return True
    
    i=0   
    while i+nums[i]<len(nums)-1:         
        if nums[i]==0:return False
        #每次都選最大的步
        max_step=0
        Next_step=1
        for j in range(nums[i],0,-1):
            if max_step<nums[i+j]:
                max_step=nums[i+j]
                Next_step=j
        i+=Next_step        
    return True
        
    
    
    


nums=[2,3,1,1,4]
print(canJump(nums))
nums=[3,2,1,0,4]
print(canJump(nums))
nums=[2,5,0,0]
print(canJump(nums))
nums=[1,1,2,2,0,1,1]
print(canJump(nums))
nums=[1,0,2]
print(canJump(nums))

nums=[5,9,3,2,1,0,2,3,3,1,0,0]
print(canJump(nums))

nums=[4,2,0,0,1,1,4,4,4,0,4,0]
print(canJump(nums))