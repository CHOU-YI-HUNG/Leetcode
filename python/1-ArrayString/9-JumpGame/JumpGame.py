def canJump(nums):
    i=len(nums)-1
    preindex=1
    while i>0:      
        if i-preindex<0:
            return False   
        #找前面有可能到達終點的index                        
        if (i-preindex)+nums[i-preindex]>=i:
            preindex=1
            i-=preindex
        else: preindex+=1
            
    return True
        
nums=[0] 
print(canJump(nums)) 
    
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