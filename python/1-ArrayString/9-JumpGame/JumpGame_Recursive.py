def canJump(nums):        
    def Rec(r,preIndex):        
        if r==0:return True        
        if preIndex>r: return False
        predict=nums[r-preIndex]+(r-preIndex)
        if  predict>=r:
            r-=preIndex                       
            return Rec(r,1)        
        else:
            preIndex+=1
            return Rec(r,preIndex)                
    return Rec(len(nums)-1,1)


print(canJump([2,5,0,0]))
print(canJump([0,2,3]))

print(canJump([2,0,0]))

print(canJump([2,3,1,1,4]))
print(canJump([3,2,1,0,4]))
print(canJump([1,2]))
print(canJump([0]))