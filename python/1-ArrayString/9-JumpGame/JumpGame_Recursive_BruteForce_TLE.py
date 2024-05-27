def canJump(nums):
    r=len(nums)-1
    def Rec(l):
        if l>=r: return True
        if nums[l]==0: return False
        for i in range(nums[l],0,-1):
            predict=l+i
            if Rec(predict): return True
        return False

    return Rec(0)



nums=[2,3,1,1,4]
print(canJump(nums))
nums=[3,2,1,0,4]
print(canJump(nums))