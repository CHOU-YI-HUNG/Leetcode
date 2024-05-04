def jump(nums):
    ans=0
    i=len(nums)-1
    preindex=1
    while i>0:      
        # if i-preindex<0:
        #     return False   
        #找前面有可能到達終點的index                        
        if (i-preindex)+nums[i-preindex]>=i:
            preindex+=1            
        else:
            i-=(preindex-1)
            preindex=1
            ans+=1
            
    return ans






nums=[2,3,1,1,4] 
print(jump(nums))

nums=[2,3,0,1,4] 
print(jump(nums))



